# Vault Schema Reference

## Canonical OKF-first bundle

This fork persists knowledge as an **OKF 0.1 bundle** first. The canonical bundle contract is minimal:

```text
bundle/
|-- index.md
|-- log.md
|-- <domain directories>/
|   |-- <concept>.md
|   `-- ...
`-- <optional extension files and folders>
```

### Core contract

- `index.md` is the canonical entrypoint and navigation file.
- `index.md` should carry parseable YAML frontmatter with at least `type: index` and `okf_version: "0.1"`.
- `log.md` is the canonical append-only operational log.
- `index.md` and `log.md` are reserved names and are never treated as concept docs.
- Every persisted concept document should have parseable YAML frontmatter.
- `type` is required in concept frontmatter.
- Relative Markdown links are the canonical internal link format.
- Extra frontmatter fields are allowed and must be preserved.

### Optional extension files and folders

These are valid project conventions, but they are **not** part of the core bundle contract:

- `_CLAUDE.md`
- `CRITICAL_FACTS.md`
- `SOUL.md`
- `raw/`
- `boards/` or `Boards/`
- `Bases/`
- `Templates/` or `templates/`
- `Logs/`

Use them when present. Do not require them for bundle validity.

---

## Layout conventions

The OKF contract does not force one directory taxonomy. This fork supports two common example layouts.

### Wiki-style AI-first layout

Optimized for vaults where the agent writes most of the knowledge layer.

```text
Your Bundle/
|-- index.md
|-- log.md
|-- _CLAUDE.md                # optional extension
|-- CRITICAL_FACTS.md         # optional extension
|-- raw/                      # optional immutable sources
|   |-- articles/
|   |-- transcripts/
|   |-- pdfs/
|   `-- videos/
|-- wiki/
|   |-- entities/
|   |-- concepts/
|   |-- projects/
|   |-- daily/
|   |-- logs/
|   |-- reviews/
|   |-- tasks/
|   |-- decisions/
|   `-- meetings/
|-- boards/
|-- templates/
`-- _trash/
```

### Obsidian-style human-first layout

Optimized for vaults that humans browse frequently in Obsidian.

```text
Your Bundle/
|-- index.md
|-- log.md
|-- _CLAUDE.md                # optional extension
|-- Home.md                   # optional extension note
|-- Daily/
|-- Dev Logs/
|-- Tasks/
|-- Projects/
|-- People/
|-- Boards/
|-- Knowledge/
|-- Learning/
|-- Ideas/
|-- Content/
|-- Goals/
|-- Health/
|-- Finances/
|-- Jobs/
|-- Businesses/
|-- Mentions/
|-- Reviews/
|-- Meetings/
|-- Templates/
`-- _trash/
```

---

## Folder mapping examples

| Note type | Wiki-style example | Obsidian-style example |
|---|---|---|
| Person / company / tool (entity) | `wiki/entities/` | `People/` |
| Idea / concept / framework / synthesis | `wiki/concepts/` | `Ideas/` or `Knowledge/` |
| Project | `wiki/projects/` | `Projects/` |
| Daily note | `wiki/daily/` | `Daily/` |
| Dev / work log | `wiki/logs/` | `Dev Logs/` |
| Weekly / monthly review | `wiki/reviews/` | `Reviews/` |
| Standalone task | `wiki/tasks/` | `Tasks/` |
| Decision record (ADR) | `wiki/decisions/` | `Knowledge/` |
| Meeting note | `wiki/meetings/` | `Meetings/` |
| Raw source (immutable) | `raw/` | `raw/` |
| Research output | `Research/` | `Research/` |
| Kanban board | `boards/` | `Boards/` |

These are example placements, not mandatory paths. Use `references/folder-map.md` as the operational resolver when a command needs to decide which existing folder to use.

---

## Frontmatter schemas

These schemas are **fork conventions on top of OKF**, not the base spec itself. They all remain valid because OKF allows extra fields. Relative links below illustrate common placements from the example layouts above; adapt them to the actual resolved paths in the bundle.

### Root `index.md`
Reserved root file. In this fork, it should declare the bundle version explicitly.

```yaml
---
type: index
okf_version: "0.1"
---
```

### Daily note
```yaml
---
date: 2026-03-24
type: daily
tags:
  - daily
ai-first: true
mood: ""
energy: ""
---
```

### Project note
```yaml
---
date: 2026-03-24
updated: 2026-03-24
type: project
tags:
  - project
ai-first: true
status: active
related-people:
  - ../people/jane-smith.md
related-projects: []
timeline:
  - fact: "status: planning"
    from: 2026-03-01
    until: 2026-03-15
    learned: 2026-03-01
  - fact: "status: active"
    from: 2026-03-15
    until: present
    learned: 2026-03-15
---
```

### Task note
```yaml
---
date: 2026-03-24
type: task
tags:
  - task
ai-first: true
status: in-progress
due: 2026-03-28
related-projects:
  - ../projects/project-name.md
related-people:
  - ../people/person-name.md
---
```

### Entity note (person / company / tool)
```yaml
---
date: 2026-03-24
updated: 2026-03-24
type: person
tags:
  - entity
  - person
ai-first: true
role: "Senior Engineer"
company: ../companies/acme-corp.md
last-interaction: 2026-03-24
timeline:
  - fact: "CTO at Acme Corp"
    from: 2024-01-01
    until: 2026-04-07
    learned: 2026-02-23
  - fact: "Architect at Acme Corp"
    from: 2026-04-07
    until: present
    learned: 2026-04-07
    source: ../daily/2026-04-07.md
---
```

### Source note
```yaml
---
date: 2026-03-24
type: source
tags:
  - source
ai-first: true
source-kind: article
resource: "https://example.com/article"
content-hash: ""
---
```

### Concept note
```yaml
---
date: 2026-03-24
type: concept
tags:
  - concept
ai-first: true
status: active
related-projects: []
---
```

### Dev log
```yaml
---
date: 2026-03-24
type: devlog
tags:
  - devlog
ai-first: true
project: ../projects/project-name.md
---
```

### Decision record (ADR)
```yaml
---
date: 2026-03-24
type: adr
tags:
  - adr
  - decision
ai-first: true
status: accepted
related-projects:
  - ../projects/project-name.md
---
```

### Goal
```yaml
---
date: 2026-01-01
type: goal
tags:
  - goal
ai-first: true
category: career
status: active
progress: 35
target-date: 2026-12-31
---
```

For the full writing contract, use `references/ai-first-rules.md`.

---

## Naming conventions

| Type | Pattern | Example |
|---|---|---|
| Daily note | `YYYY-MM-DD.md` | `2026-03-24.md` |
| Dev log | `YYYY-MM-DD - Description.md` | `2026-03-24 - API Gateway Debug.md` |
| Entity | Full name (flat) | `Jane Smith.md`, `Acme Corp.md` |
| Concept | Descriptive title | `LLM-Wiki Pattern.md` |
| Project | Proper name | `My Project Name.md` |
| Source | `YYYY-MM-DD - Source Title.md` | `2026-04-06 - Karpathy LLM Wiki.md` |
| Decision | `ADR-YYYY-MM-DD - Title.md` | `ADR-2026-04-06 - Wiki Style Default.md` |
| Archive prefix | `_archived_` | `_archived_Old Project.md` |

Reserved root names:
- `index.md`
- `log.md`

Every other Markdown filename is available for concept docs or extension notes.
