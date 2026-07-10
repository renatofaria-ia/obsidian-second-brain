---
description: Create or update today's daily note - pulls calendar events, overdue tasks, and conversation context
category: vault
triggers_en: ["todays note", "create todays daily", "open daily", "today daily note"]
triggers_pt: ["nota de hoje", "crie a nota diária de hoje", "abra a diária", "nota diária de hoje"]
---

Use the obsidian-second-brain skill. Execute `/obsidian-daily`:

1. Read `index.md` first if it exists in the bundle root. If `_CLAUDE.md` exists, treat it as an extension file that may refine local conventions
2. Read `CRITICAL_FACTS.md` for timezone

3. Check if `wiki/daily/YYYY-MM-DD.md` exists for today
   - If not: read `templates/Daily Note.md`, fill in date fields, create the file
   - If yes: update existing note (inject, don't overwrite)

4. Pull calendar events (if a Google Calendar MCP is connected):
   - Find the primary calendar with `mcp__claude_ai_Google_Calendar__list_calendars`, then fetch today's events with `mcp__claude_ai_Google_Calendar__list_events` (these are the tool names exposed by the claude.ai Google Calendar connector; if your calendar MCP namespaces its tools differently, use that server's `list_events` equivalent)
   - Add a ## Calendar section to the daily note with:
     - Time, title, attendees for each event
     - For meetings with known entities: link to their person notes
   - If no calendar MCP is connected, skip silently (don't error)

5. Pull overdue and due-today tasks from kanban boards:
   - Scan `boards/` for items with `@{date}` that match today or are past due
   - Add to the daily note's Focus section with priority markers

6. Scan the current conversation for anything relevant to today:
   - Tasks in progress, people mentioned, decisions made, what's being worked on
   - Pre-fill or update the note's sections with that context

7. Check the operation log for last night's sleeptime consolidation (if `Logs/` exists: read yesterday's `Logs/YYYY-MM-DD.md`; otherwise read `log.md`):
   - If the nightly agent ran, summarize what it did (reconciled, synthesized, healed)
   - Add a brief "Overnight changes" note so the user knows what happened while they slept

8. Return the path of the daily note when done.

---

**AI-first rule:** Every note created or updated by this command MUST follow `references/ai-first-rules.md` - `## For future Claude` preamble, rich frontmatter (`type`, `date`, `tags`, `ai-first: true`, plus type-specific fields), recency markers per external claim, relative Markdown links as the canonical internal link format, and any Obsidian `[[wikilinks]]` preserved only as a compatibility extension when the surrounding bundle still uses them. Sources must remain verbatim with URLs inline, with confidence levels where applicable. The persisted bundle is for future-Claude retrieval, not for human reading first.

**Anti-fabrication:** Search exhaustively before claiming any note, person, or file is absent - false absence is the most common failure mode - and never invent facts, entities, or dates (mark unknowns as `TBD`). See the anti-fabrication and search-completeness hard rules in `references/ai-first-rules.md`.
