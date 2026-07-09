# `_CLAUDE.md` Template

`_CLAUDE.md` is an optional runtime extension file that lives at the root of a bundle.
Claude should read `index.md` first, then `_CLAUDE.md` when it exists.
Use this file to persist local operating rules across Claude surfaces without confusing them with the core OKF contract.

---

## How to Generate It

When a user asks Claude to create or refresh `_CLAUDE.md`, Claude should:
1. Read `index.md` first.
2. Glob the bundle root (`<vault>/**/*.md`) to map the structure.
3. Read `Home.md` or another dashboard note if one exists.
4. Read 2-3 templates from `Templates/` if that folder exists.
5. Read the current kanban boards if the bundle uses them.
6. Fill in the template below with discovered values.
7. Write the file to `_CLAUDE.md` at the bundle root.

---

## The Template

Copy this, fill in the bracketed values, and save as `_CLAUDE.md` at the bundle root.

```markdown
# Claude Operating Manual - [Your Name]'s Bundle

> Read `index.md` first, then this file.
> This file is the single source of truth for local runtime behavior, not for bundle validity.

---

## Bundle Identity

- **Owner:** [Full Name]
- **Primary purpose:** [e.g. "Life OS - work, personal, side business, finances"]
- **Storage mode:** [e.g. "Obsidian-backed bundle" or "plain Markdown bundle"]
- **Last updated:** [YYYY-MM-DD]

---

## Core Contract Reminder

The persisted contract is OKF-first:
- `index.md` is the canonical entrypoint
- `log.md` is the canonical reserved log file
- persisted notes use UTF-8 Markdown with YAML frontmatter
- `type` is required in concept frontmatter
- relative Markdown links are canonical

This file is an extension layer. It may refine local folder choices, naming conventions, and auto-save rules, but it does not replace `index.md` or `log.md`.

---

## AI-First Extension

Notes written or refreshed under this bundle should follow `references/ai-first-rules.md`.
If this bundle uses exceptions, document them here explicitly.

---

## Folder Map

| Folder | Purpose |
|---|---|
| `[resolved daily area]` | Daily notes if this bundle uses them |
| `[resolved projects area]` | Active and archived projects |
| `[resolved people area]` | One note per person or entity |
| `[resolved tasks area]` | Standalone task notes if used |
| `[resolved boards area]` | Kanban boards if used |
| `[resolved knowledge/concepts area]` | Concepts, references, synthesis notes |
| `[resolved dev-log area]` | Technical or work session logs |
| `[resolved review area]` | Weekly or monthly reviews |
| `[resolved meetings area]` | Meeting notes |
| `Templates/` | Note templates, if present |

State only the folders that actually exist or are intended to exist in this bundle.

---

## Key Files

- **Dashboard or home note:** [path or note link]
- **Primary board:** [path or note link]
- **People index:** [path or note link]
- **Any protected/private area:** [path]

---

## Active Context

- **Current top priority:** [text]
- **Current role or mode:** [text]
- **Key collaborators:** [names and roles]
- **Important constraints:** [text]

---

## Auto-Save Rules

Claude should auto-save the following **without asking**:
- Decisions made in conversation
- New people or entities mentioned when clearly relevant
- Tasks assigned or committed to
- Work logs or execution summaries

Claude should **ask before saving**:
- Financial data
- Health, family, faith, or other sensitive private material
- Anything that deletes, renames, or archives existing notes

---

## Naming Conventions

- Daily notes: `YYYY-MM-DD.md`
- Dev logs: `YYYY-MM-DD - Description.md`
- ADRs: `ADR-YYYY-MM-DD - Title.md`
- People: full name
- Archive prefix: `_archived_`

Override only what this bundle actually uses.

---

## Frontmatter Requirements

Every persisted note should satisfy the bundle contract and any local additions documented here. At minimum:

```yaml
---
date: YYYY-MM-DD
type: [note-type]
tags:
  - [note-type]
---
```

---

## Kanban Convention

If the bundle uses kanban boards, document the actual columns, priority convention, and item format here.
If it does not use kanban, delete this section.

---

## Propagation Rules

| Event | Also update |
|---|---|
| New project | related board + daily note if those exist |
| Task done | task status + project note + daily note |
| Dev session | dev log + project note + daily note |
| Person interaction | daily note + person note |
| Decision made | project note + daily note |

Only list the propagation paths this bundle actually uses.

---

## Do Not Touch

- `Templates/` - do not modify templates during normal operations
- `[private folders]` - [reason]
- `[generated files]` - [reason]

---

*This file is a local runtime extension for the bundle.*
*Regenerate with: "Update my _CLAUDE.md"*
```

---

## Keeping `_CLAUDE.md` Fresh

Refresh `_CLAUDE.md` when:
- a new major project starts
- the folder structure changes
- active priorities shift significantly
- the bundle adopts new extensions or conventions
