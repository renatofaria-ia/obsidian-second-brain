# NotebookLM import — 2026-07

`/notebooklm-import` é uma extensão OKF que importa um fragmento editorial validado do `notebooklm-to-notes`.

- O fragmento é validado antes da escrita e não pode conter wikilinks ou links internos absolutos.
- A nota final preserva `type` e permanece em UTF-8.
- O comando adiciona uma entrada Markdown relativa ao `index.md` e registra o evento no `log.md` append-only.
- O exportador externo é opt-in e não pode ser usado em CI, automação agendada ou ambiente com cookies compartilhados.

## Validação

- `OBSIDIAN_VAULT_PATH=C:\tmp; uv run pytest tests/test_notebooklm_import.py` — 2 testes aprovados.
- `python -m unittest discover -s tests` em `.tmp/notebooklm-to-notes` — 11 testes aprovados.
