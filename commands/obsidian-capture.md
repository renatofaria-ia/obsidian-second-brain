---
description: Quick idea capture - zero friction, saves to your ideas folder and mentions in daily note
category: vault
triggers_en: ["capture this idea", "save this idea", "quick note", "drop a thought"]
triggers_pt: ["capture esta ideia", "salve esta ideia", "anotação rápida", "registre um pensamento"]
---

Use the obsidian-second-brain skill. Execute `/obsidian-capture $ARGUMENTS`:

The optional argument is the idea text. If not provided, pull the most recent idea or thought from the conversation.

1. Read `index.md` first if it exists in the bundle root. If `_CLAUDE.md` exists, treat it as an extension file that may refine local conventions
2. Take the argument as the idea, or pull from recent conversation context
3. Resolve the idea folder per `references/folder-map.md` (read the vault's `_CLAUDE.md` Folder Map first; wiki-style ideas live in `wiki/concepts/`, Obsidian-style in `Ideas/`). Search it for a related existing note - if found, append to it
4. If new: create `<idea-folder>/Title.md` with minimal frontmatter (`date`, `tags: [idea]`)
5. Write the idea with any supporting context from the conversation
6. Add a brief mention in today's daily note under an Ideas or Captures section

---

**AI-first rule:** Every note created or updated by this command MUST follow `references/ai-first-rules.md` - `## For future Claude` preamble, rich frontmatter (`type`, `date`, `tags`, `ai-first: true`, plus type-specific fields), recency markers per external claim, relative Markdown links as the canonical internal link format, and any Obsidian `[[wikilinks]]` preserved only as a compatibility extension when the surrounding bundle still uses them. Sources must remain verbatim with URLs inline, with confidence levels where applicable. The persisted bundle is for future-Claude retrieval, not for human reading first.

**Anti-fabrication:** Search exhaustively before claiming any note, person, or file is absent - false absence is the most common failure mode - and never invent facts, entities, or dates (mark unknowns as `TBD`). See the anti-fabrication and search-completeness hard rules in `references/ai-first-rules.md`.
