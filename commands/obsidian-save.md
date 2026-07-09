---
description: Save everything worth keeping from this conversation to the vault
category: vault
triggers_en: ["save this", "save the conversation", "save to vault", "obsidian save"]
---

Use the obsidian-second-brain skill. Execute `/obsidian-save`:

1. Read `index.md` first if it exists in the bundle root. If `_CLAUDE.md` also exists, treat it as an extension file that may refine local conventions.
2. Scan the entire conversation and identify all vault-worthy items: decisions, tasks, people mentioned, projects started, ideas, learnings, deals, mentions/shoutouts, AND content-worthy items (hooks, data points, swipe-file material, research findings)
3. Group items by type: people, projects, tasks, decisions, ideas, deals, content
4. Spawn parallel subagents - one per group - so all note types are handled simultaneously:
   - **People agent**: search for each person, create or update concept docs, log interactions, and preserve any existing extension fields such as `ai-first`, `timeline`, `related-projects`, and `updated`.
   - **Projects agent**: search for each project, create or update concept docs. If the conversation was a substantial dev/work session (code written, problems solved, decisions made on a project), also write a dev-log note for it - the same artifact `/obsidian-log` produces - to the logs folder (resolved per `references/folder-map.md`: wiki-style `wiki/logs/`, Obsidian-style `Dev Logs/`), named `YYYY-MM-DD - Project Name.md`, and link it from the project's Recent Activity and today's daily note when the bundle uses that convention. This is why `/obsidian-save` absorbs `/obsidian-log`: a full save already captures the work, so you do not need to run both. If a dev-log for this project and date already exists, update it rather than creating a second.
   - **Tasks agent**: parse tasks, add to the right kanban columns
   - **Decisions agent**: find relevant project notes, append to Key Decisions sections
   - **Ideas agent**: search Ideas/ for related notes, create or append
   - **Content agent** (if a `social-media/` folder exists in the vault): scan for content-worthy items and route them:
     - **Hooks, angles, contrarian takes** -> append to `social-media/ideas.md` (dated bullet)
     - **Specific numbers, stats, reusable data points** -> append to `social-media/data-points.md` (with source)
     - **External posts that hit + why** -> append to `social-media/swipe-file.md` (link + reason)
     - **Research findings, frameworks, methodologies** -> create `social-media/research/YYYY-MM-DD - topic.md`
5. Every created or updated concept doc must remain valid as an OKF-compatible markdown concept: frontmatter YAML parseable, `type` present, and `index.md` / `log.md` never treated as concept files. Use relative Markdown links as the canonical internal link format. If the bundle is still Obsidian-native, preserve `[[wikilinks]]` only when the surrounding notes already rely on them.
6. After all agents complete: update today's daily note with links to everything saved if the bundle uses daily notes as an extension. Always append an operational entry to `log.md` or the bundle's extended log structure.
7. Report back: a clean list of what was saved and where

Search before creating anything - duplicate notes are vault rot. Propagate every write to boards, daily note, and linked notes. Never create an orphaned note.

The content agent only runs if `social-media/` exists in the vault. If it doesn't exist, skip silently - don't create the folder unprompted.

---

**AI-first rule:** Every note created or updated by this command MUST follow `references/ai-first-rules.md` - `## For future Claude` preamble, rich frontmatter (`type`, `date`, `tags`, `ai-first: true`, plus type-specific fields), recency markers per external claim, mandatory internal cross-links for every person/project/concept referenced, sources preserved verbatim with URLs inline, and confidence levels where applicable. The bundle is for future-Claude retrieval - not human reading.

**Anti-fabrication:** Search exhaustively before claiming any note, person, or file is absent - false absence is the most common failure mode - and never invent facts, entities, or dates (mark unknowns as `TBD`). See the anti-fabrication and search-completeness hard rules in `references/ai-first-rules.md`.