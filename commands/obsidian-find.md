---
description: Smart vault search - returns results with context, not just filenames
category: vault
triggers_en: ["find in vault", "search my notes", "where is", "what did I write about"]
---

Use the obsidian-second-brain skill. Execute `/obsidian-find $ARGUMENTS`:

The argument is the search query.

1. Read `index.md` first if it exists in the bundle root. Treat it as the bundle front door. If `_CLAUDE.md` also exists, read it as an extension file that may refine local conventions, not as part of the core bundle contract.
2. Search the knowledge bundle for the query using the ranked keyword search where it is available: the `obsidian_search` MCP tool, or `vault_ops.search` directly (`integrations/obsidian-mcp-server/`). It applies stopword filtering and length-normalized ranking, so a short concept with the term in its title outranks a long note that merely repeats it. In Claude Code (where no search tool is bound), grep the bundle and read the top matches directly, applying the same judgement: ignore filler words, do not let `raw/` transcripts outrank a canonical concept note, and never treat `index.md` or `log.md` as concept hits.
3. Also try variations if results are sparse (aliases, synonyms, related terms, singular/plural forms).
4. Prefer canonical concept documents over operational artifacts. If both an AI-first note and an exported or generated derivative exist, return the canonical concept first and label the derivative as secondary.
5. Return results with context: note title, relative path inside the bundle, a relevant excerpt, and the note `type` from frontmatter when present.
6. If results are ambiguous, group them by type (`person`, `project`, `task`, `research`, etc.) or by top-level directory.
7. Offer to open, update, or link any of the found notes. For new links, use relative Markdown links as the canonical bundle format. If the existing vault is still Obsidian-native, preserve `[[wikilinks]]` only as a compatibility format.

Do not just return filenames - return enough context for the user to act on the results.

---

**AI-first rule:** Every note created or updated by this command MUST follow `references/ai-first-rules.md` - `## For future Claude` preamble, rich frontmatter (`type`, `date`, `tags`, `ai-first: true`, plus type-specific fields), recency markers per external claim, mandatory internal cross-links for every person/project/concept referenced, sources preserved verbatim with URLs inline, and confidence levels where applicable. The bundle is for future-Claude retrieval - not human reading.

**Anti-fabrication:** Search exhaustively before claiming any note, person, or file is absent - false absence is the most common failure mode - and never invent facts, entities, or dates (mark unknowns as `TBD`). See the anti-fabrication and search-completeness hard rules in `references/ai-first-rules.md`.