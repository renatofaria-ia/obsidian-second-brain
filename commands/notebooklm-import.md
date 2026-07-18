---
description: Importa um notebook pessoal do NotebookLM para um concept OKF usando o exportador notebooklm-to-notes em staging.
category: research
triggers_en: ["import notebooklm", "notebooklm import"]
triggers_pt: ["importar notebooklm", "trazer notebook do notebooklm", "importar meu notebook"]
---

Use `/notebooklm-import` somente quando o usuário confirmar o notebook pessoal a importar e o caminho `.md` de destino dentro do bundle.

1. Explique que o fluxo usa a sessão local do NotebookLM e é opt-in; não use em CI, agendamentos ou ambientes compartilhados.
2. Rode o preflight antes de pedir qualquer link público ou tentar importar:

   ```bash
   uv run -m scripts.research.notebooklm_import --preflight
   ```

   Se `status` vier como `missing-exporter`, pare e informe que falta instalar/configurar `notebooklm-to-notes` ou definir `NOTEBOOKLM_TO_NOTES_BIN`. Não trate autenticação do Chrome como suficiente para automação.
3. Confirme que `notebooklm-to-notes` está disponível com suporte ao NotebookLM pessoal e que a autenticação local está ativa (`notebooklm auth check --test --json`).
4. Execute:

   ```bash
   uv run -m scripts.research.notebooklm_import --notebook "<id>" --destination "<pasta>/<arquivo>.md"
   ```

5. O importador cria um fragmento temporário, valida UTF-8, frontmatter `type`, proveniência, briefing, Mermaid e links compatíveis com OKF antes de escrever.
6. Após sucesso, leia a nota importada e aplique o fluxo padrão de `/obsidian-save` apenas para propagar relações reais. Não invente pessoas, tarefas ou links.
7. Informe o caminho salvo, a atualização de `index.md`, o registro em `log.md` e as fontes preservadas.

Não use `/notebooklm-import` para o `/notebooklm` atual: aquele comando continua sendo a síntese do vault via Gemini File Search.
