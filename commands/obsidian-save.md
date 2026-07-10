---
description: Save everything worth keeping from this conversation to the vault
category: vault
triggers_en: ["save this", "save the conversation", "save to vault", "obsidian save"]
---

Use the obsidian-second-brain skill. Execute `/obsidian-save`:

1. Read `index.md` first if it exists in the bundle root. Treat it as the canonical bundle catalog. If `_CLAUDE.md` also exists, treat it as an extension file that may refine local conventions, folder choices, and AI-first defaults.
2. Scan the entire conversation and identify everything worth persisting in the bundle: people, projects, tasks, decisions, ideas, learnings, deals, mentions, and content-worthy research findings.
3. Split the work into **core bundle writes** versus **extension propagation**:
   - **Core bundle writes (mandatory)**: concept docs, `index.md`, `log.md`
   - **Extension propagation (optional)**: daily notes, boards, dev logs, `social-media/`, `Logs/YYYY-MM-DD.md`
4. Resolve candidate concept docs before creating anything:
   - use `obsidian_search` or `vault_ops.search` to find existing notes
   - read the top candidates and prefer updating an existing concept when the conversation deepens the same entity, project, task, or idea
   - use `obsidian_backlinks` when necessary to understand how an existing concept is already connected before editing it
   - only call `obsidian_save_note` when no equivalent concept exists; otherwise use `obsidian_update_note`
5. Persist the **core bundle** in this order:
   - update or create the relevant concept docs first
   - preserve existing extension fields when they already exist (`ai-first`, `timeline`, `related-projects`, `updated`, `confidence`, etc.)
   - keep frontmatter parseable with required `type`
   - use relative Markdown links as the canonical internal link format
   - preserve `[[wikilinks]]` only when the surrounding note is still Obsidian-native and clearly depends on them
6. After concept writes are complete, update the canonical structural files:
   - refresh the affected `index.md` sections so new or renamed concepts are navigable from the bundle front door
   - append a save event to the root `log.md`
   - never treat `index.md` or `log.md` as concept docs and never overwrite log history
7. Only after the core bundle is consistent, apply **extension propagation** when those structures already exist:
   - **Daily note**: add links to what was saved if the bundle uses daily notes
   - **Boards**: update task state or add references only if a board structure already exists
   - **Dev Logs**: if the conversation was a substantial work session, update or create a dated dev-log note in the resolved extension location and link it from the relevant project note
   - **`social-media/`**: if that extension folder exists, route hooks/data points/swipe-file items/research notes there; do not create the folder unprompted
8. Validate the touched notes before finishing:
   - run `obsidian_validate_note` on notes that were newly created or materially rewritten
   - if a change introduced a broken link or missing required frontmatter, fix it before reporting success
9. Report back with a clean bundle-first summary:
   - concepts created
   - concepts updated
   - `index.md` / `log.md` updates
   - optional extension files updated

Search before creating anything - duplicate concepts are bundle rot. Core bundle consistency comes first; extension propagation must never replace the required `index.md` and `log.md` updates.

---

**AI-first rule:** Every note created or updated by this command MUST follow `references/ai-first-rules.md` - `## For future Claude` preamble, rich frontmatter (`type`, `date`, `tags`, `ai-first: true`, plus type-specific fields), recency markers per external claim, mandatory internal cross-links for every person/project/concept referenced, sources preserved verbatim with URLs inline, and confidence levels where applicable. The bundle is for future-Claude retrieval - not human reading.

**Anti-fabrication:** Search exhaustively before claiming any note, person, or file is absent - false absence is the most common failure mode - and never invent facts, entities, or dates (mark unknowns as `TBD`). See the anti-fabrication and search-completeness hard rules in `references/ai-first-rules.md`.
