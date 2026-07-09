---
description: Create or update a person note from conversation context
category: vault
triggers_en: ["save this person", "add person", "new contact note", "create person note"]
---

Use the obsidian-second-brain skill. Execute `/obsidian-person $ARGUMENTS`:

The argument is a person's name - handle typos and partial matches.

1. Read `index.md` first if it exists in the bundle root. If `_CLAUDE.md` exists, treat it as an extension file that may refine local conventions
2. Search the vault for an existing note matching the name (fuzzy - handle typos and partial names)
3. If found: confirm with user, then update with new info from conversation
4. If not found: create `People/Full Name.md` with full frontmatter schema
5. Fill in everything inferable from the conversation: role, company, context, relationship strength, last interaction date
6. Log the interaction in today's daily note
7. If a People index file exists, add or update the entry there

If the name has a typo or is approximate, search the vault, show what was found, and confirm before proceeding. Never silently create a note with a misspelled name.

---

**AI-first rule:** Every note created or updated by this command MUST follow `references/ai-first-rules.md` - `## For future Claude` preamble, rich frontmatter (`type`, `date`, `tags`, `ai-first: true`, plus type-specific fields), recency markers per external claim, relative Markdown links as the canonical internal link format, and any Obsidian `[[wikilinks]]` preserved only as a compatibility extension when the surrounding bundle still uses them. Sources must remain verbatim with URLs inline, with confidence levels where applicable. The persisted bundle is for future-Claude retrieval, not for human reading first.

**Anti-fabrication:** Search exhaustively before claiming any note, person, or file is absent - false absence is the most common failure mode - and never invent facts, entities, or dates (mark unknowns as `TBD`). See the anti-fabrication and search-completeness hard rules in `references/ai-first-rules.md`.
