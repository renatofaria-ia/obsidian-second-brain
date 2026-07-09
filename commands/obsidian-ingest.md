---
description: Ingest a source into the bundle and rewrite affected concepts, index.md, and log.md in an OKF-first flow
category: research
triggers_en: ["ingest this source", "add this article", "import this", "absorb this"]
---

Use the obsidian-second-brain skill. Execute `/obsidian-ingest $ARGUMENTS`:

The argument is a URL, file path, or pasted text. If no argument, ask what to ingest.

1. Read `index.md` first if it exists in the bundle root.
2. If `_CLAUDE.md` exists, treat it as an extension file that may refine note conventions, folder choices, and AI-first defaults.
3. Classify the source type before reading the full content:
   - **Article/blog post**: extract key claims, people, tools, concepts
   - **PDF/document**: extract structure, findings, recommendations
   - **Transcript (meeting/podcast)**: extract speakers, decisions, action items, quotes
   - **YouTube video**: pull metadata, description, and transcript when available
   - **Audio file** (`.m4a`, `.mp3`, `.wav`, `.ogg`, `.webm`): transcribe, identify speakers, extract decisions, tasks, promises
   - **Image/screenshot** (`.png`, `.jpg`, `.jpeg`, `.webp`): read/OCR the image and extract text plus context
   - **Raw text**: classify by content (opinion, technical, narrative) and extract accordingly
4. Read or fetch the full source content using the best available local or runtime capability.
5. Extract and organize:
   - **Entities**: people, companies, tools, projects
   - **Concepts**: ideas, frameworks, methodologies
   - **Claims**: assertions with supporting evidence
   - **Action items**: anything actionable for the user
   - **Quotes**: notable quotes worth preserving
6. Save the raw source to `raw/` as an immutable extension area:
   - create a dated Markdown record in `raw/articles/`, `raw/transcripts/`, `raw/pdfs/`, or `raw/videos/`
   - use valid YAML frontmatter
   - include at minimum `type`, `source_type`, `source_url` when applicable, and provenance metadata
7. Rewrite the bundle, not just append to it:
   - search existing concept docs before creating new ones
   - update matching entity, concept, and project notes in place when the new source changes or deepens them
   - create synthesis pages when the new source reveals a pattern across multiple existing notes
   - when the new source conflicts with an older claim, record the contradiction and prefer the more recent or more authoritative evidence
8. Use the canonical link format when writing bundle content:
   - prefer relative Markdown links in the persisted bundle
   - if the runtime also keeps `[[wikilinks]]` for authoring compatibility, treat them as an extension, not as the canonical persisted format
9. Update structural files after the ingest:
   - rebuild `index.md` sections affected by the ingest so the bundle catalog stays current
   - append an ingest entry to `log.md` at the root as the canonical append-only log
   - if `Logs/YYYY-MM-DD.md` also exists, update it as an extension without skipping the root `log.md`
10. Update the relevant daily or log notes when that extension structure exists in the bundle.
11. Report back with:
   - source title and type
   - new pages created
   - existing pages rewritten and what changed
   - contradictions resolved
   - synthesis pages created

The bundle should become more accurate, more connected, and more navigable after every ingest. If an ingest only creates new files and does not improve any existing concept or index path, it was too shallow.

---

**AI-first rule:** Every note created or updated by this command MUST follow `references/ai-first-rules.md`. The `## For future Claude` preamble, rich frontmatter, recency markers, confidence markers, and additional provenance fields are fork extensions that must be preserved, but they do not replace the core OKF contract (`index.md`, `log.md`, valid YAML, `type`, relative Markdown links).

**Anti-fabrication:** Search exhaustively before claiming any note, person, or file is absent, and never invent facts, entities, or dates (mark unknowns as `TBD`). See the hard rules in `references/ai-first-rules.md`.
