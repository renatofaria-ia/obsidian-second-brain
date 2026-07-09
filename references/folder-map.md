# Folder Map Resolution

How every command decides **which folder** a note belongs in. Never hardcode a folder name in a command body. Resolve it through this spec so the same command works on an OKF-first bundle, an Obsidian-style vault, or a custom layout.

## The rule

1. **Read the bundle's `index.md` first.** It is the canonical navigation file and the cheapest way to discover top-level structure.
2. **If optional root extension files exist, read them next.** In practice, `_CLAUDE.md` may define a `## Folder Map` or `## Naming Conventions` section that overrides the example placements below.
3. **Inspect the folders and note placements that already exist.** Prefer the folder family the bundle is already using for that note type.
4. **If the bundle is silent and no equivalent folder exists yet, pick one example layout and stay consistent.** For a fresh AI-first bundle, the wiki-style example remains the default. For a clearly human-first Obsidian bundle, use the matching Obsidian-style example.
5. **Never invent a new top-level folder when an equivalent resolved location already exists.** If the note type still cannot be resolved, ask the user rather than guessing.

## Note-type to folder examples

| Note type | Wiki-style example | Obsidian-style example |
|-----------|--------------------|------------------------|
| Person / company / tool (entity) | `wiki/entities/` | `People/` |
| Idea / concept / framework / synthesis | `wiki/concepts/` | `Ideas/` (ideas), `Knowledge/` (reference) |
| Project | `wiki/projects/` | `Projects/` |
| Daily note | `wiki/daily/` | `Daily/` |
| Dev / work log | `wiki/logs/` | `Dev Logs/` |
| Weekly / monthly review | `wiki/reviews/` | `Reviews/` |
| Standalone task | `wiki/tasks/` | `Tasks/` |
| Decision record (ADR) | `wiki/decisions/` | `Knowledge/` (as `ADR-YYYY-MM-DD - Title.md`) |
| Meeting note | `wiki/meetings/` | `Meetings/` |
| Raw source (immutable) | `raw/` (articles, transcripts, pdfs, videos subfolders) | `raw/` |
| Research output | `Research/` (Web, Deep, X-pulse, X-reads, YouTube, NotebookLM subfolders) | `Research/` |
| Kanban board | `boards/` | `Boards/` |

## Notes

- **Examples, not mandates:** the table above shows common placements, not required folder names.
- **Ideas vs concepts:** in a wiki-style bundle there is no separate `Ideas/` folder. Ideas, concepts, frameworks, and synthesis notes all live in `wiki/concepts/`. Only use `Ideas/` if the bundle actually has that folder or documents it explicitly.
- **ADRs:** wiki-style keeps decision records in `wiki/decisions/`; Obsidian-style often keeps them in `Knowledge/` with an `ADR-` filename prefix. Resolve per `index.md`, existing notes, and `_CLAUDE.md` when present.
- **Searching across types:** when a command scans "everywhere" (for example synthesis or find), enumerate the note folders that actually exist in the bundle instead of assuming a fixed top-level layout.
- **Root files:** `index.md` and `log.md` are reserved names, not note-type folders.
