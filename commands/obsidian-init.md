---
description: Scan your bundle and generate an OKF-first root index, root log, and optional _CLAUDE.md extension
category: meta
triggers_en: ["init vault", "bootstrap vault", "setup vault", "scan vault"]
---

Use the obsidian-second-brain skill. Execute `/obsidian-init`:

1. Glob the bundle (`<bundle>/**/*.md`) to map the full structure.
2. Read `index.md` first if it already exists. If `_CLAUDE.md` also exists, treat it as an extension file that may refine local conventions.
3. Spawn parallel subagents to discover bundle context simultaneously:
   - **Catalog agent**: inspect root docs and top-level directories
   - **Templates agent**: read files in `Templates/` if that extension folder exists
   - **Boards agent**: read files in `Boards/` if that extension folder exists
   - **Samples agent**: read one existing note per major folder to capture naming conventions and frontmatter patterns
4. Merge all agent results into a complete picture of the bundle.
5. Generate or refresh a complete `_CLAUDE.md` using the template in `references/claude-md-template.md`, filled with real values from the bundle. `_CLAUDE.md` is an extension file, not part of the core OKF contract.
6. Generate `index.md` at the bundle root as the canonical navigation file:
   - add frontmatter with `okf_version: "0.1"`
   - list concept docs and important extension files by progressive disclosure
   - never treat `index.md` or `log.md` as concept files
   - use relative Markdown links as the canonical internal link format
7. Initialize the root operations log:
   - create `log.md` at the bundle root as the canonical append-only log
   - append today's init entry: `## [YYYY-MM-DD] init | Bundle initialized with index.md, log.md, and extension files`
   - if the bundle already uses `Logs/YYYY-MM-DD.md`, keep that extension structure too, but do not omit the root `log.md`
8. Create `Bases/` at the bundle root if it does not exist. Stamp the premade base files from `references/bases/` when the matching folders exist. Treat `Bases/` as an optional Obsidian extension, not as part of the core bundle contract.
9. Write `_CLAUDE.md`, `index.md`, `log.md`, and any new `Bases/*.base` files.
10. Confirm what was written and tell the user to restart the Claude session if they want the new `_CLAUDE.md` rules to take effect automatically.

If `_CLAUDE.md` already exists: show a diff of what would change and ask before overwriting.
If `index.md` already exists: regenerate it because it is the canonical bundle catalog.
If `log.md` already exists: append to it; never replace history.

---

**AI-first rule:** Every note created or updated by this command MUST follow `references/ai-first-rules.md` - `## For future Claude` preamble, rich frontmatter (`type`, `date`, `tags`, `ai-first: true`, plus type-specific fields), recency markers per external claim, mandatory internal cross-links, sources preserved verbatim with URLs inline, and confidence levels where applicable. The bundle is for future-Claude retrieval - not human reading.

**Anti-fabrication:** Search exhaustively before claiming any note, person, or file is absent - false absence is the most common failure mode - and never invent facts, entities, or dates (mark unknowns as `TBD`). See the anti-fabrication and search-completeness hard rules in `references/ai-first-rules.md`.
