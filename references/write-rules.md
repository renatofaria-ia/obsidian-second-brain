# Write Rules

How Claude writes, links, formats, and updates notes in an OKF-first bundle, including Obsidian-backed bundles.

> **Read `references/ai-first-rules.md` first.** Every AI-first note Claude writes or refreshes must follow that extension contract (preamble, rich frontmatter, recency markers, relative Markdown links as the canonical format, sources verbatim, confidence levels). The rules below are operational details on top of that foundation.

---

## The Propagation Rule

**Never create a note in isolation.** Every write has ripple effects.

When you create or update something, trace forward: what other notes need to know about this?

```text
New project created
  -> Add card to the resolved kanban board, if the bundle uses one
  -> Link from today's daily note, if the bundle uses daily notes
  -> If it has a person involved, link from that person's note

Task completed
  -> Move card in kanban or update the task note status
  -> Update the project note (Recent Activity or Delivered section)
  -> Log in today's daily note when applicable

Person note updated
  -> If interaction happened today, log it in the daily note
  -> If they made a mention or shoutout, update the relevant mentions log if one exists

Dev log created
  -> Link from the project note (Recent Activity section)
  -> Link from today's daily note (Work / Work Log section)

Decision made
  -> Log in the project note (Key Decisions section)
  -> Log in today's daily note
```

Treat the examples above as propagation patterns, not as mandatory files in every bundle.

---

## Internal Linking

Use relative Markdown links as the canonical bundle format. Resolve the relative path from the actual note location in the active bundle.

Always link:
- People mentioned in a note -> `[Jane Smith](../people/jane-smith.md)`
- Projects referenced -> `[My Project Name](../projects/my-project-name.md)`
- Companies -> `[Acme Corp](../companies/acme-corp.md)`
- Related tasks -> `[Task Name](../tasks/task-name.md)`

Compatibility rule:
- If the existing bundle is still Obsidian-native, preserve `[[Note Name]]` only when the surrounding notes already rely on that format.
- New OKF-first fixtures and generated bundle outputs should prefer relative Markdown links.

If the linked note does not exist yet, create it. A stub is fine: frontmatter, `## For future Claude`, title, and one line of context.

---

## Date Formatting

| Context | Format | Example |
|---|---|---|
| Frontmatter `date` field | `YYYY-MM-DD` | `2026-03-24` |
| Frontmatter `due` field | `YYYY-MM-DD` | `2026-03-28` |
| Kanban due date tag | `@{YYYY-MM-DD}` | `@{2026-03-28}` |
| Body text references | Human format | `March 24` or `Mar 24` |
| File names (dated) | `YYYY-MM-DD` | `2026-03-24.md` |

---

## Kanban Board Format

Kanban boards are a bundle extension, not a core OKF requirement. When a bundle uses the Obsidian Kanban plugin, boards may use `kanban-plugin: board` YAML frontmatter.

Columns are H2 headings. Items are task checkboxes with an optional indented description.

**Active item:**
```markdown
- [ ] [high] **Task Title** @{2026-03-28}
  One-line description. [Related Project](../projects/related-project.md) [Person](../people/person.md)
```

**Waiting item:**
```markdown
- [ ] [medium] **Task Title** @{2026-04-07}
  Context for why it is blocked. [Person responsible](../people/person-responsible.md)
```

**Completed item** (move to `## Done` column):
```markdown
- [x] ~~[high] Task Title~~ 2026-03-24
  Brief note on outcome.
```

**Priority convention:**
- `[high]` critical or blocking
- `[medium]` important or this week
- `[low]` nice to have or low urgency

If the existing board uses emoji or another visual convention, preserve the local style.

**Never delete done items**. Move them to the Done column with strikethrough. Done items are the changelog.

---

## Status Values

Use these consistently across all note types:

**Projects:**
`active` | `planning` | `completed` | `archived` | `on-hold`

**Tasks:**
`in-progress` | `done` | `waiting` | `cancelled`

**Deals:**
`prospect` | `negotiating` | `confirmed` | `completed` | `lost`

**Goals:**
`active` | `completed` | `paused` | `abandoned`

**Content:**
`draft` | `scheduled` | `published`

---

## Writing Style Calibration

Before writing a new note in a folder you have not written in before:
1. Read 1-2 existing notes in that folder.
2. Match the heading structure, frontmatter fields present, tone, list style, and section names.
3. Preserve the local visual conventions only after the bundle contract is satisfied.

Do not introduce new patterns when the bundle already has one.

---

## Archiving

**Soft archive** (preferred): add an `_archived_` prefix to the filename.
`Old Project.md` -> `_archived_Old Project.md`

**Update frontmatter**: set `status: archived`

Never delete persisted notes as part of normal maintenance. Archive them. The bundle is a permanent record.

---

## Template Usage

When creating notes from templates, strip all Templater syntax (`<% ... %>`) and replace it with actual values. Never leave template placeholders in saved notes.

---

## Stub Notes

When a link target does not exist yet, create a minimal stub:
```yaml
---
date: 2026-03-24
type: person
tags:
  - person
ai-first: true
---

## For future Claude
Stub note created because another note needed this link target. Expand it when more context is available.

# Person Name
```

Resolve the target folder through `references/folder-map.md` and existing bundle structure. Do not assume a fixed `People/` path.

---

## Section Injection

When updating an existing note instead of creating a new one, use targeted section injection:

1. Read the full file.
2. Find the target section heading.
3. Append content below the last item in that section, before the next `---` or `##` heading.
4. Write back the full file.

For kanban boards: find the correct column heading and insert the new item above the last item in that column, or at the top if it is empty.

---

## Sentinel-safe regeneration

For notes that a command generates and a human may hand-edit (architecture docs, dashboards, or any note meant to be refreshed by re-running a command), use sentinel markers so a refresh never destroys human edits:

```html
<!-- @generated:start -->
...machine-generated content - safe to overwrite on the next run...
<!-- @generated:end -->

<!-- @user:start -->
...human notes - NEVER overwritten by a refresh...
<!-- @user:end -->
```

Rules on refresh:
1. Read the existing note.
2. Replace only the content between `@generated:start` and `@generated:end`.
3. Never touch `@user` blocks, and never touch anything outside the markers.
4. On the first run, if no markers exist yet, wrap the generated content in `@generated` markers so future refreshes stay safe.

This lets a command be idempotent and re-runnable without wiping user additions. Used by `/obsidian-architect`; available to any command that maintains a regenerable note.

---

## Search Before Write

Before creating any note:
```text
search(query="keyword from title")
```

If a match is found:
- Same concept -> update the existing note instead of creating a duplicate.
- Different concept, similar name -> proceed with creation but choose a distinct name.

Duplicate detection is especially important for people, projects, deals, and concepts with multiple aliases.

**Never claim absence from memory.** Before writing "no note exists" or creating a note because you believe none exists, search exhaustively by every plausible name, alias, and folder. List and grep rather than relying on one lucky query. False absence is the most common failure mode. When unsure, over-include and label the uncertainty. See the anti-fabrication and search-completeness hard rules in `references/ai-first-rules.md`.
