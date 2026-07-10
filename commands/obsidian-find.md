---
description: Smart vault search - returns results with context, not just filenames
category: vault
triggers_en: ["find in vault", "search my notes", "where is", "what did I write about"]
---

Use the obsidian-second-brain skill. Execute `/obsidian-find $ARGUMENTS`:

The argument is the search query.

1. Read `index.md` first if it exists in the bundle root. Treat it as the bundle front door. If `_CLAUDE.md` also exists, read it as an extension file that may refine local conventions, not as part of the core bundle contract.
2. Search the bundle using the ranked keyword search where it is available: the `obsidian_search` MCP tool, or `vault_ops.search` directly (`integrations/obsidian-mcp-server/`). It already applies stopword filtering, length-normalized ranking, and de-weighting of `raw/` and `log.md`, so a short canonical concept with the term in its title outranks a long operational note that merely repeats it. In Claude Code (where no search tool is bound), grep the bundle and read the top matches directly while applying the same judgement.
3. Also try variations if results are sparse (aliases, synonyms, related terms, singular/plural forms).
4. Apply this precedence when ranking results for the user:
   - canonical concept docs first
   - extension notes second (`Daily/`, `Logs/`, dev logs, boards, `_CLAUDE.md`, `Home.md`, etc.)
   - immutable raw-source notes third (`raw/`)
   - exported or generated derivatives last
   - never return `index.md` or `log.md` as primary concept hits
5. Return each result with enough context to act:
   - title
   - bundle-relative path
   - note `type` when frontmatter provides it
   - a relevant excerpt
   - a short label when the hit is an extension rather than a canonical concept
6. If the top results are ambiguous, group them by `type` (`person`, `project`, `task`, `research`, etc.) or by top-level directory and explain which one looks canonical.
7. Offer the next bundle-safe action:
   - open/read the canonical concept
   - update the concept
   - add a link from another note
   - inspect backlinks before editing a heavily connected concept
8. When proposing new links, use relative Markdown links as the canonical format. Preserve `[[wikilinks]]` only when the existing note is still Obsidian-native and clearly depends on them.

Do not just return filenames - return enough context for the user to act on the results.

---

**AI-first rule:** Every note created or updated by this command MUST follow `references/ai-first-rules.md` - `## For future Claude` preamble, rich frontmatter (`type`, `date`, `tags`, `ai-first: true`, plus type-specific fields), recency markers per external claim, mandatory internal cross-links for every person/project/concept referenced, sources preserved verbatim with URLs inline, and confidence levels where applicable. The bundle is for future-Claude retrieval - not human reading.

**Anti-fabrication:** Search exhaustively before claiming any note, person, or file is absent - false absence is the most common failure mode - and never invent facts, entities, or dates (mark unknowns as `TBD`). See the anti-fabrication and search-completeness hard rules in `references/ai-first-rules.md`.
