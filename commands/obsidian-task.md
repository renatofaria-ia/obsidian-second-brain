---
description: Add a task to the right kanban board with inferred priority and due date
category: vault
triggers_en: ["add task", "new todo", "track this", "remind me"]
triggers_pt: ["adicione uma tarefa", "novo a fazer", "acompanhe isto", "me lembre disto"]
---

Use the obsidian-second-brain skill. Execute `/obsidian-task $ARGUMENTS`:

1. Read `index.md` first if it exists in the bundle root. If `_CLAUDE.md` exists, treat it as an extension file that may refine local conventions
2. Parse the task from the argument, or pull from recent conversation context if no argument given
3. Infer: priority (🔴/🟡/🟢), due date, linked project, linked person
4. Search for the right kanban board - use `_CLAUDE.md` board list or search `Boards/`
5. Add the task card to the correct column (`📋 This Week` or `📥 Backlog` depending on due date)
6. Create a task note in `Tasks/` if the task is substantial (more than a one-liner)
7. Link the task from the relevant project note and today's daily note

---

**AI-first rule:** Every note created or updated by this command MUST follow `references/ai-first-rules.md` - `## For future Claude` preamble, rich frontmatter (`type`, `date`, `tags`, `ai-first: true`, plus type-specific fields), recency markers per external claim, relative Markdown links as the canonical internal link format, and any Obsidian `[[wikilinks]]` preserved only as a compatibility extension when the surrounding bundle still uses them. Sources must remain verbatim with URLs inline, with confidence levels where applicable. The persisted bundle is for future-Claude retrieval, not for human reading first.

**Anti-fabrication:** Search exhaustively before claiming any note, person, or file is absent - false absence is the most common failure mode - and never invent facts, entities, or dates (mark unknowns as `TBD`). See the anti-fabrication and search-completeness hard rules in `references/ai-first-rules.md`.
