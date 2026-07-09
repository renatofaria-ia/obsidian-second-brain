---
description: Export a clean structured snapshot of the vault that any agent or tool can consume - flat JSON, markdown index, or an OKF bundle
category: meta
triggers_en: ["export vault", "snapshot vault", "dump vault", "vault export"]
---

Use the obsidian-second-brain skill. Execute `/obsidian-export $ARGUMENTS`:

The optional argument is the format: `json` (default), `markdown`, or `okf`.

1. Read `index.md` first if it exists in the bundle root. If `_CLAUDE.md` also exists, treat it as an extension file that may refine local conventions.
2. Build a structured export by scanning the knowledge bundle.

   **For each concept document**, extract:
   - `path`: file path relative to bundle root
   - `title`: note title (first heading or filename)
   - `type`: from frontmatter `type` when present
   - `date`: from frontmatter when present
   - `status`: from frontmatter when present
   - `summary`: first paragraph or first 200 characters of body
   - `links_to`: list of outgoing links
   - `linked_from`: list of incoming links (backlinks)
   - `tags`: all frontmatter tags
   - `frontmatter`: full frontmatter as key-value pairs

   Never treat `index.md` or `log.md` as concept documents.

3. Output format:

   **JSON** (default):
   ```json
   {
     "bundle": "Renato's Bundle",
     "exported": "2026-07-09",
     "total_notes": 238,
     "notes": [
       {
         "path": "projects/ofk-adaptation.md",
         "title": "OKF Adaptation",
         "type": "project",
         "summary": "Migration of the fork's persisted format to OKF 0.1...",
         "links_to": ["../people/renato-faria.md"],
         "tags": ["project", "ofk", "migration"]
       }
     ]
   }
   ```
   Save to `_export/vault-snapshot.json`.

   **Markdown**:
   A flat markdown file with every concept listed with its metadata and summary.
   Save to `_export/vault-snapshot.md`.

   **OKF**:
   Do NOT build this by hand. Run the deterministic exporter:
   ```bash
   uv run scripts/export_okf.py --path "<bundle path>"
   ```
   It writes an OKF-compatible bundle to `_export/okf/` with these rules:
   - every concept becomes a markdown concept doc with required `type` and generated `timestamp`
   - `index.md` and `log.md` are treated as reserved names, not concept files
   - internal `[[wikilinks]]` in the body are converted to relative Markdown links
   - extension frontmatter fields are preserved whenever possible (`ai-first`, `updated`, `timeline`, `related-projects`, etc.)
   - a root `index.md` is generated with `okf_version: "0.1"`
   - a root `log.md` is always emitted

4. Append to the operation log: if `Logs/` exists write `**HH:MM** - export | Vault snapshot exported (format, N notes)` to `Logs/YYYY-MM-DD.md`; otherwise append `## [YYYY-MM-DD] export | Vault snapshot exported (format, N notes)` to `log.md`.

This file is the bridge between your bundle and any other AI tool, automation, or agent. They should not need to know your local folder conventions to consume it.

---

**AI-first rule:** Every note created or updated by this command MUST follow `references/ai-first-rules.md` - `## For future Claude` preamble, rich frontmatter (`type`, `date`, `tags`, `ai-first: true`, plus type-specific fields), recency markers per external claim, mandatory internal cross-links, sources preserved verbatim with URLs inline, and confidence levels where applicable.

**Anti-fabrication:** Search exhaustively before claiming any note, person, or file is absent - false absence is the most common failure mode - and never invent facts, entities, or dates (mark unknowns as `TBD`). See the anti-fabrication and search-completeness hard rules in `references/ai-first-rules.md`.