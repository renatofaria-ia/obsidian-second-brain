#!/usr/bin/env bash
# =============================================================================
# adapters/hermes/adapter.sh - Nous Research Hermes Agent platform adapter
# =============================================================================
# Hermes Agent ships a native Skills System (agentskills.io-compatible): a skill
# is a directory `skills/<category>/<name>/` with a `SKILL.md` (YAML frontmatter
# + body). Hermes loads skills with progressive disclosure, the user installs a
# set by adding the repo as a "tap" (`hermes skills tap add <owner/repo>`) or
# copying into `~/.hermes/skills/`, and invokes them via `/skills` or implicit
# description match.
#
# We emit one native Hermes skill per command, grouped by category. This is the
# Hermes-runtime counterpart to the Codex native-skills adapter (Phase 2 of the
# Hermes work, Issue #79). The MCP connector (integrations/obsidian-mcp-server)
# is the separate bounded-data path; this adapter is the skill/playbook path.
#
# SKILL.md frontmatter (per Hermes creating-skills spec):
#   required: name, description, version, author, license
#   optional: metadata.hermes.tags (+ more we do not need here)
# =============================================================================

HERMES_PLATFORM="hermes"
HERMES_DIR="hermes"
HERMES_SKILLS_DIR="skills"
HERMES_AUTHOR="Eugeniu Ghelbur"
HERMES_LICENSE="MIT"

adapter_build() {
  local src="$1" dst="$2"

  HERMES_VERSION="$(_hermes_version "$src")"
  _hermes_emit_skills "$src/commands" "$dst/$HERMES_SKILLS_DIR"
  _hermes_copy_references "$src/references" "$dst/references"
  _hermes_copy_scripts "$src/scripts" "$dst/scripts"
  _hermes_emit_install_hint "$dst"
}

# Read the project version from pyproject.toml so SKILL.md `version:` tracks
# releases instead of going stale. Falls back to 0.0.0.
_hermes_version() {
  local src="$1" v
  v="$(grep -m1 '^version' "$src/pyproject.toml" 2>/dev/null | sed 's/.*=[[:space:]]*"//; s/".*//')"
  [[ -n "$v" ]] && echo "$v" || echo "0.0.0"
}

# Emit one native Hermes skill per command:
#   skills/<category>/<name>/SKILL.md
# Frontmatter carries the required fields plus metadata.hermes.tags. The
# command's English triggers are folded into the description (for implicit
# selection) and surfaced as a "## When to use" preamble; the command body
# follows as the procedure, tool-neutralized and path-rewritten.
_hermes_emit_skills() {
  local src="$1" dst="$2"
  [[ -d "$src" ]] || return 0
  local f name desc triggers category out trig_clean
  for f in "$src"/*.md; do
    [[ -f "$f" ]] || continue
    should_include "$f" "$HERMES_PLATFORM" || continue

    name="$(basename "$f" .md)"
    desc="$(parse_frontmatter "$f" description)"
    triggers="$(parse_frontmatter "$f" triggers_en)"
    category="$(parse_frontmatter "$f" category)"
    [[ -z "$category" ]] && category="misc"
    [[ -z "$desc" ]] && desc="Run the $name command of the obsidian-second-brain skill."

    trig_clean=""
    if [[ -n "$triggers" ]]; then
      trig_clean="$(echo "$triggers" | tr -d '[]"' | sed 's/,/, /g; s/  */ /g; s/^ *//; s/ *$//')"
      [[ -n "$trig_clean" ]] && desc="$desc Triggers: $trig_clean."
    fi

    mkdir -p "$dst/$category/$name"
    out="$dst/$category/$name/SKILL.md"
    {
      echo "---"
      echo "name: $name"
      printf 'description: "%s"\n' "${desc//\"/\\\"}"
      echo "version: $HERMES_VERSION"
      printf 'author: "%s"\n' "$HERMES_AUTHOR"
      echo "license: $HERMES_LICENSE"
      echo "metadata:"
      echo "  hermes:"
      echo "    tags: [obsidian-second-brain, $category]"
      echo "---"
      echo
      if [[ -n "$trig_clean" ]]; then
        echo "## When to use"
        echo
        echo "When the user's request matches any of: $trig_clean."
        echo
      fi
      echo "## Procedure"
      echo
      command_body "$f"
    } > "$out"

    rewrite_tool_neutral "$out"
    rewrite_platform_paths "$out" "$HERMES_DIR"
  done
}

_hermes_copy_references() {
  local src="$1" dst="$2"
  [[ -d "$src" ]] || return 0
  mkdir -p "$dst"
  cp -R "$src/." "$dst/"
  find "$dst" -type f -name '*.md' -print0 | while IFS= read -r -d '' f; do
    rewrite_platform_paths "$f" "$HERMES_DIR"
  done
}

_hermes_copy_scripts() {
  local src="$1" dst="$2"
  [[ -d "$src" ]] || return 0
  mkdir -p "$dst"
  cp -R "$src/." "$dst/"
}

_hermes_emit_install_hint() {
  local dst="$1"
  cat > "$dst/INSTALL.md" <<'EOF'
# Install on Hermes Agent

The obsidian-second-brain commands are emitted here as native Hermes skills
under `skills/<category>/<name>/SKILL.md` (agentskills.io-compatible).

## Option A - install from this built tree

```bash
# From the repo root, after `bash scripts/build.sh --platform hermes`:
mkdir -p ~/.hermes/skills/obsidian-second-brain
cp -R dist/hermes/skills/. ~/.hermes/skills/obsidian-second-brain/
# Shared specs + Python helpers the skills reference:
cp -R dist/hermes/references ~/.hermes/skills/obsidian-second-brain/references
cp -R dist/hermes/scripts    ~/.hermes/skills/obsidian-second-brain/scripts
```

## Option B - add as a tap (when published to a skills repo)

```bash
hermes skills tap add <owner>/<repo>
```

Then in Hermes:

- Browse with `hermes skills browse` / the `/skills` command, or just describe
  the task and let Hermes select a skill from its description.
- Skills run in your Hermes session. The AI-first vault rule lives in
  `references/ai-first-rules.md` - it is non-negotiable for every note a skill
  writes (`## For future Claude` preamble, rich frontmatter, `[[wikilinks]]`,
  recency markers, sources verbatim, confidence levels).
- Python helpers under `scripts/` run via `uv run -m scripts.research.<name>`
  from the vault root.

Point Hermes at your vault as the working directory, or pair these skills with
the MCP connector (`integrations/obsidian-mcp-server/`) for bounded vault data
access. Scheduled-agent and lifecycle pieces are tracked in Issue #79.
EOF
}
