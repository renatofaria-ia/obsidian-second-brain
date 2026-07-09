---
description: Convene a panel of distinct perspectives on a decision - one independent verdict per lens, then a synthesis. A multi-persona complement to /obsidian-challenge
category: thinking
triggers_en: ["convene a panel", "advisor panel", "get multiple perspectives on", "panel review", "what would the experts say about"]
---

Use the obsidian-second-brain skill. Execute `/obsidian-panel [decision or question]`:

Pressure-tests a decision from several independent angles at once. Where `/obsidian-challenge` red-teams from one adversarial stance, this gathers a panel of distinct lenses and makes each argue on its own before you see a synthesis.

1. Resolve the decision/question from the argument. If none, ask what to put to the panel.
2. Choose the panel:
   - If the vault has an `Advisors/` folder, read those persona notes and use each as a panelist (each verdict reflects that advisor's stated lens and priorities).
   - Otherwise, use 4 generic lenses: the skeptic (what breaks this), the user/customer (who is served or hurt), the operator (can this actually be run/maintained), and the long-game (what does this look like in a year).
3. For EACH panelist, write an independent verdict: their position, the strongest reason behind it, and what would change their mind. Keep them genuinely distinct - do not let them converge prematurely.
4. Write a synthesis: where the panel agreed, where it split, and a recommended decision with its main risk. Do not hide the disagreement - the split is the most useful output.
5. Save to `wiki/concepts/YYYY-MM-DD - panel - <slug>.md` (`type: synthesis`, tagged `[thinking, panel]`), linking any advisor notes and related entity/project notes the decision touches. Cross-link from today's daily note.

---

**AI-first rule:** Every note created or updated by this command MUST follow `references/ai-first-rules.md` - `## For future Claude` preamble, rich frontmatter (`type`, `date`, `tags`, `ai-first: true`, plus type-specific fields), recency markers per external claim, relative Markdown links as the canonical internal link format, and any Obsidian `[[wikilinks]]` preserved only as a compatibility extension when the surrounding bundle still uses them. Sources must remain verbatim with URLs inline, with confidence levels where applicable. The persisted bundle is for future-Claude retrieval, not for human reading first.

**Anti-fabrication:** If you use `Advisors/` notes, base each verdict on what that note actually says - do not invent an advisor's position or attribute views to a real person they have not expressed. Never fabricate a consensus; report the real split. See the anti-fabrication and search-completeness hard rules in `references/ai-first-rules.md`.
