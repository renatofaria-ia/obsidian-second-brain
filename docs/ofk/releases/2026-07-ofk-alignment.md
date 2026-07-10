# Release Notes - alinhamento OKF

Data: 2026-07-09
Escopo: alinhamento do fork `renatofaria-ia/obsidian-second-brain` ao **OKF 0.1**
Status: concluido

## Objetivo

Registrar, em um unico artefato, as decisoes, mudancas de comportamento, arquivos tocados e evidencias de validacao da migracao do fork para um contrato **OKF-first**.

Este documento existe para:

- dar rastreabilidade tecnica da adaptacao
- separar contrato do bundle de convencoes do fork
- facilitar reabertura futura sem depender do historico do chat

## Decisoes fechadas

- O formato persistido alvo do fork passa a ser um **bundle OKF 0.1**.
- `index.md` e `log.md` passam a ser os nomes reservados do contrato canonico do bundle.
- `index.md` raiz passa a ser obrigatorio neste fork e deve declarar `okf_version: "0.1"`.
- `log.md` raiz passa a ser obrigatorio neste fork como log append-only.
- O formato canonico de links internos passa a ser **Markdown relativo**.
- `[[wikilinks]]` permanecem apenas como formato de compatibilidade para bundles ainda Obsidian-native.
- `_CLAUDE.md`, `CRITICAL_FACTS.md`, `SOUL.md`, `Logs/`, `Bases/`, `Boards/` e outras convencoes semelhantes passam a ser **extensoes explicitas do fork**, nao parte implicita do core da spec.
- Na primeira fase, os nomes publicos dos comandos sao preservados.

## Mudancas implementadas

### 1. Documentacao do contrato

Criados os artefatos-base da fase 0:

- [../README.md](C:/Users/konok/Documents/vibecode/second-brain/docs/ofk/README.md)
- [../gap-analysis.md](C:/Users/konok/Documents/vibecode/second-brain/docs/ofk/gap-analysis.md)
- [../canonical-bundle.md](C:/Users/konok/Documents/vibecode/second-brain/docs/ofk/canonical-bundle.md)
- [../command-matrix.md](C:/Users/konok/Documents/vibecode/second-brain/docs/ofk/command-matrix.md)
- [../test-scenarios.md](C:/Users/konok/Documents/vibecode/second-brain/docs/ofk/test-scenarios.md)

### 2. Fixtures de referencia

Criados bundles de referencia para validacao:

- [../../../examples/ofk-bundle-minimo](C:/Users/konok/Documents/vibecode/second-brain/examples/ofk-bundle-minimo)
- [../../../examples/ofk-bundle-extensoes](C:/Users/konok/Documents/vibecode/second-brain/examples/ofk-bundle-extensoes)

### 3. Bootstrap e export OKF-first

O caminho de inicializacao e serializacao do bundle foi adaptado para o contrato novo:

- [../../../scripts/bootstrap_vault.py](C:/Users/konok/Documents/vibecode/second-brain/scripts/bootstrap_vault.py)
- [../../../scripts/export_okf.py](C:/Users/konok/Documents/vibecode/second-brain/scripts/export_okf.py)

Resultado esperado desse bloco:

- bootstrap gera `index.md` raiz com `okf_version: "0.1"`
- bootstrap gera `log.md` raiz
- export respeita `index.md` e `log.md` como nomes reservados
- export preserva extensoes de frontmatter
- export converte `[[wikilinks]]` para links Markdown relativos no bundle exportado

### 4. Runtime de links internos

O runtime passou a entender o formato canonico de links do fork:

- [../../../scripts/vault_health.py](C:/Users/konok/Documents/vibecode/second-brain/scripts/vault_health.py)
- [../../../scripts/link_graph.py](C:/Users/konok/Documents/vibecode/second-brain/scripts/link_graph.py)
- [../../../integrations/obsidian-mcp-server/vault_ops.py](C:/Users/konok/Documents/vibecode/second-brain/integrations/obsidian-mcp-server/vault_ops.py)

Resultado esperado desse bloco:

- suporte a links Markdown relativos para `.md`
- compatibilidade mantida com `[[wikilinks]]`
- health, graph, backlinks e validacao passam a operar no modelo OKF-first

### 5. Comandos prioritarios

Os comandos mais importantes para persistencia e navegacao foram reancorados no contrato OKF-first:

- [../../../commands/obsidian-save.md](C:/Users/konok/Documents/vibecode/second-brain/commands/obsidian-save.md)
- [../../../commands/obsidian-find.md](C:/Users/konok/Documents/vibecode/second-brain/commands/obsidian-find.md)
- [../../../commands/obsidian-ingest.md](C:/Users/konok/Documents/vibecode/second-brain/commands/obsidian-ingest.md)
- [../../../commands/obsidian-init.md](C:/Users/konok/Documents/vibecode/second-brain/commands/obsidian-init.md)
- [../../../commands/obsidian-export.md](C:/Users/konok/Documents/vibecode/second-brain/commands/obsidian-export.md)

### 6. Normalizacao do repositorio

Os pontos de entrada e referencias principais foram atualizados para refletir a nova arquitetura:

- [../../../README.md](C:/Users/konok/Documents/vibecode/second-brain/README.md)
- [../../../SKILL.md](C:/Users/konok/Documents/vibecode/second-brain/SKILL.md)
- [../../../architecture.md](C:/Users/konok/Documents/vibecode/second-brain/architecture.md)
- [../../../references/ai-first-rules.md](C:/Users/konok/Documents/vibecode/second-brain/references/ai-first-rules.md)
- [../../../references/write-rules.md](C:/Users/konok/Documents/vibecode/second-brain/references/write-rules.md)
- [../../../references/folder-map.md](C:/Users/konok/Documents/vibecode/second-brain/references/folder-map.md)
- [../../../references/vault-schema.md](C:/Users/konok/Documents/vibecode/second-brain/references/vault-schema.md)
- [../../../integrations/obsidian-mcp-server/README.md](C:/Users/konok/Documents/vibecode/second-brain/integrations/obsidian-mcp-server/README.md)
- [../../../integrations/obsidian-mcp-server/server.py](C:/Users/konok/Documents/vibecode/second-brain/integrations/obsidian-mcp-server/server.py)

### 7. Limpeza semantica dos comandos

Foi feita uma passada adicional para remover instrucoes normativas antigas que ainda tratavam `_CLAUDE.md` ou `[[wikilinks]]` como contrato principal.

Arquivos ajustados nessa passada:

- [../../../commands/obsidian-review.md](C:/Users/konok/Documents/vibecode/second-brain/commands/obsidian-review.md)
- [../../../commands/obsidian-recap.md](C:/Users/konok/Documents/vibecode/second-brain/commands/obsidian-recap.md)
- [../../../commands/obsidian-distill.md](C:/Users/konok/Documents/vibecode/second-brain/commands/obsidian-distill.md)
- [../../../commands/obsidian-calendar.md](C:/Users/konok/Documents/vibecode/second-brain/commands/obsidian-calendar.md)
- [../../../commands/obsidian-visualize.md](C:/Users/konok/Documents/vibecode/second-brain/commands/obsidian-visualize.md)
- [../../../commands/obsidian-projects.md](C:/Users/konok/Documents/vibecode/second-brain/commands/obsidian-projects.md)
- [../../../commands/notebooklm.md](C:/Users/konok/Documents/vibecode/second-brain/commands/notebooklm.md)
- [../../../commands/research-deep.md](C:/Users/konok/Documents/vibecode/second-brain/commands/research-deep.md)
- [../../../commands/vault-deep-synthesis.md](C:/Users/konok/Documents/vibecode/second-brain/commands/vault-deep-synthesis.md)
- [../../../commands/idea-discovery.md](C:/Users/konok/Documents/vibecode/second-brain/commands/idea-discovery.md)
- [../../../commands/obsidian-catchup.md](C:/Users/konok/Documents/vibecode/second-brain/commands/obsidian-catchup.md)
- [../../../commands/obsidian-daily.md](C:/Users/konok/Documents/vibecode/second-brain/commands/obsidian-daily.md)
- [../../../commands/obsidian-panel.md](C:/Users/konok/Documents/vibecode/second-brain/commands/obsidian-panel.md)

## Compatibilidade preservada

- Os nomes publicos dos comandos foram mantidos.
- O runtime continua aceitando `[[wikilinks]]` como compatibilidade.
- Estruturas como `_CLAUDE.md`, `Logs/`, `Boards/`, `Bases/` e `raw/` continuam suportadas como extensoes do fork.

### 8. Fechamento documental e editorial

Foi executada uma passada final de consistencia transversal entre os pontos de entrada e referencias canonicas do fork para consolidar a narrativa **OKF-first** e separar com mais rigor o que e contrato persistido versus o que e extensao operacional.

Arquivos ajustados nessa passada:

- [../../../README.md](C:/Users/konok/Documents/vibecode/second-brain/README.md)
- [../../../SKILL.md](C:/Users/konok/Documents/vibecode/second-brain/SKILL.md)
- [../../../references/ai-first-rules.md](C:/Users/konok/Documents/vibecode/second-brain/references/ai-first-rules.md)
- [../../../references/write-rules.md](C:/Users/konok/Documents/vibecode/second-brain/references/write-rules.md)
- [../../../references/folder-map.md](C:/Users/konok/Documents/vibecode/second-brain/references/folder-map.md)
- [../../../references/vault-schema.md](C:/Users/konok/Documents/vibecode/second-brain/references/vault-schema.md)
- [../../../references/claude-md-template.md](C:/Users/konok/Documents/vibecode/second-brain/references/claude-md-template.md)
- [../../../references/claude-md-assistant-template.md](C:/Users/konok/Documents/vibecode/second-brain/references/claude-md-assistant-template.md)
- [../../../references/DELTAS.template.md](C:/Users/konok/Documents/vibecode/second-brain/references/DELTAS.template.md)

Resultado esperado desse bloco:

- consolidacao de `bundle` como termo do contrato persistido
- rebaixamento de `vault` para contexto de armazenamento, operacao em Obsidian ou compatibilidade legada
- reposicionamento de `_CLAUDE.md` como extensao opcional, nunca como ponto de entrada primario do contrato
- consolidacao de links Markdown relativos como formato canonico interno
- alinhamento dos templates auxiliares ao mesmo contrato `bundle-first`
- correcao de inconsistencias editoriais e de codificacao UTF-8 nos documentos principais

## Atualizacao de 2026-07-10 - Fase 1 dos comandos prioritarios

Escopo desta rodada:

- fechamento da semantica **OKF-first real** dos comandos `/obsidian-save`, `/obsidian-ingest`, `/obsidian-find`, `/obsidian-init` e `/obsidian-export`
- alinhamento do guia operacional exposto pelo MCP/runtime ao mesmo contrato desses comandos
- reforco da rastreabilidade: mudancas relevantes agora devem atualizar tambem `docs/ofk/releases/` na mesma rodada

Arquivos ajustados nesta rodada:

- [../../../commands/obsidian-save.md](C:/Users/konok/Documents/vibecode/second-brain/commands/obsidian-save.md)
- [../../../commands/obsidian-ingest.md](C:/Users/konok/Documents/vibecode/second-brain/commands/obsidian-ingest.md)
- [../../../commands/obsidian-find.md](C:/Users/konok/Documents/vibecode/second-brain/commands/obsidian-find.md)
- [../../../commands/obsidian-init.md](C:/Users/konok/Documents/vibecode/second-brain/commands/obsidian-init.md)
- [../../../commands/obsidian-export.md](C:/Users/konok/Documents/vibecode/second-brain/commands/obsidian-export.md)
- [../../../integrations/obsidian-mcp-server/vault_ops.py](C:/Users/konok/Documents/vibecode/second-brain/integrations/obsidian-mcp-server/vault_ops.py)
- [../../../tests/test_smoke.py](C:/Users/konok/Documents/vibecode/second-brain/tests/test_smoke.py)
- [../../../SKILL.md](C:/Users/konok/Documents/vibecode/second-brain/SKILL.md)
- [../../../CONTRIBUTING.md](C:/Users/konok/Documents/vibecode/second-brain/CONTRIBUTING.md)
- [../README.md](C:/Users/konok/Documents/vibecode/second-brain/docs/ofk/README.md)

Resultados consolidados desta rodada:

- `/obsidian-save` passa a declarar ordem canonica de persistencia: ler `index.md`, buscar conceitos existentes, atualizar antes de criar, refletir navegacao no `index.md`, registrar evento em `log.md` e so depois propagar para extensoes opcionais
- `/obsidian-ingest` passa a tratar `raw/` como extensao documentada e fixa o ciclo fonte -> entidades/claims/acoes -> update de conceito -> sintese opcional -> `index.md` -> `log.md`
- `/obsidian-find` passa a explicitar a precedencia de concepts canonicos sobre extensoes, `raw/` e derivados exportados
- `/obsidian-init` consolida `index.md` e `log.md` como core obrigatorio e rebaixa `_CLAUDE.md`, `Bases/`, `Boards/`, `Templates/`, `Logs/` e `.obsidian/` para camada opcional
- `/obsidian-export` passa a descrever `export okf` como serializacao deterministica principal, com JSON e snapshots Markdown como derivados
- o guia exposto por `vault_ops.get_skill()` agora reforca `obsidian_update_note`, `obsidian_validate_note` e `obsidian_backlinks` como primitivas esperadas do fluxo canonico
- a rastreabilidade de futuras mudancas relevantes passa a ser regra operacional do fork, documentada no skill, na contribuicao e na pasta `docs/ofk/`

Complemento desta rodada:

- `CHANGELOG.md` foi sincronizado com um resumo publico das fases OKF-first ja fechadas: contrato persistido, comandos prioritarios, runtime de links/export e regra de rastreabilidade via release tecnico
- `CONTRIBUTING.md` foi ajustado apos a remocao de `SECURITY.md` para eliminar um link de contato que passaria a ficar quebrado na raiz do projeto

Validacao desta rodada:

- `python -m pytest tests/test_smoke.py`
- resultado: `29 passed`

## Atualizacao de 2026-07-10 - polimento editorial final do README

Escopo desta passada:

- homogeneizacao do tom do `README.md` apos a restauracao de conteudo
- preservacao integral do contrato tecnico **OKF-first** sem nova mudanca semantica
- limpeza de trechos metalinguisticos e ajuste de vocabulario para narrativa mais uniforme

Ajustes aplicados no arquivo:

- [../../../README.md](C:/Users/konok/Documents/vibecode/second-brain/README.md)

Resultados desta passada:

- a secao `O que acontece quando voce instala` deixa de falar sobre si mesma e volta a descrever diretamente a experiencia de uso
- a narrativa geral fica mais uniforme entre posicionamento, exemplos praticos, arquitetura e filosofia
- termos como `cross-platform` foram alinhados para `multiplataforma` quando nao eram tecnicamente obrigatorios
- o conteudo restaurado do README foi preservado, sem nova compressao editorial

## Validacao executada

Validacoes mecanicas:

- `python -m py_compile` nos arquivos Python relevantes
- `git diff --check`
- varreduras locais para garantir ausencia dos padroes antigos mais criticos:
  - `mandatory wikilinks`
  - instrucao de leitura primaria de `_CLAUDE.md`
  - instrucoes normativas com `[[wikilink]]`

Smoke checks funcionais executados manualmente:

- bootstrap OKF-first
- export OKF-first
- `vault_health.py` com links Markdown relativos
- `link_graph.py` com links Markdown relativos
- `vault_ops.py` com validacao, backlinks e wanted notes para links Markdown relativos

Observacao:

- `pytest` nao estava instalado no Python local durante a rodada final, entao a cobertura dos cenarios criticos foi reproduzida manualmente.

## Limites conhecidos

- Ainda ha textos historicos no repositorio que mencionam convencoes legadas em contexto explicativo ou historico. Isso nao invalida o contrato atual, mas futuras revisoes podem simplificar essa sobreposicao.
- Os avisos remanescentes de `git diff --check` sao apenas sobre normalizacao `CRLF/LF` em arquivos Python ja existentes.

## Proximos passos sugeridos

1. Transformar este documento em serie de releases tecnicas por fase da adaptacao OKF.
2. Ligar este arquivo a `docs/ofk/README.md`.
3. Se fizer sentido para o repositorio publico, resumir estas mudancas no `CHANGELOG.md`.
4. Em uma proxima fase, adicionar validacao automatica dedicada para os fixtures OKF no CI.

## Relacao com outros artefatos

- Este documento registra **o que mudou** nesta rodada.
- [../canonical-bundle.md](C:/Users/konok/Documents/vibecode/second-brain/docs/ofk/canonical-bundle.md) registra **qual e o contrato**.
- [../test-scenarios.md](C:/Users/konok/Documents/vibecode/second-brain/docs/ofk/test-scenarios.md) registra **como validar**.
- [../command-matrix.md](C:/Users/konok/Documents/vibecode/second-brain/docs/ofk/command-matrix.md) registra **como os 44 comandos foram classificados**.


## Atualizacao de 2026-07-10 - hooks, adapters e superficies residuais

Escopo desta rodada:

- fechamento das superficies secundarias que ainda reintroduziam o contrato antigo em hooks, adapter, exemplos e docs de manutencao
- consolidacao de `index.md` como porta de entrada canonica tambem nos fluxos automatizados
- adicao de testes de regressao semantica para evitar retorno de `_CLAUDE.md` como requisito ou de `[[wikilinks]]` como formato obrigatorio
- rebuild completo dos targets para confirmar propagacao do posicionamento **OKF-first**

Arquivos ajustados nesta rodada:

- [../../../hooks/load_vault_context.py](C:/Users/konok/Documents/vibecode/second-brain/hooks/load_vault_context.py)
- [../../../hooks/obsidian-bg-agent.sh](C:/Users/konok/Documents/vibecode/second-brain/hooks/obsidian-bg-agent.sh)
- [../../../hooks/obsidian-hermes-session-end.sh](C:/Users/konok/Documents/vibecode/second-brain/hooks/obsidian-hermes-session-end.sh)
- [../../../adapters/pi/adapter.sh](C:/Users/konok/Documents/vibecode/second-brain/adapters/pi/adapter.sh)
- [../../../commands/create-command.md](C:/Users/konok/Documents/vibecode/second-brain/commands/create-command.md)
- [../../../commands/podcast.md](C:/Users/konok/Documents/vibecode/second-brain/commands/podcast.md)
- [../../../CLAUDE.md](C:/Users/konok/Documents/vibecode/second-brain/CLAUDE.md)
- [../../../architecture.md](C:/Users/konok/Documents/vibecode/second-brain/architecture.md)
- [../../../examples/README.md](C:/Users/konok/Documents/vibecode/second-brain/examples/README.md)
- [../../../tests/test_smoke.py](C:/Users/konok/Documents/vibecode/second-brain/tests/test_smoke.py)
- [../../../CHANGELOG.md](C:/Users/konok/Documents/vibecode/second-brain/CHANGELOG.md)

Resultados consolidados desta rodada:

- `load_vault_context.py` deixa de depender de `_CLAUDE.md` para funcionar e passa a carregar `index.md` como contexto principal do bundle, usando `_CLAUDE.md` apenas quando presente como extensao opcional
- os prompts headless de `obsidian-bg-agent.sh` e `obsidian-hermes-session-end.sh` passam a ancorar primeiro em `index.md`, eliminando a suposicao de que `_CLAUDE.md` e sempre o ponto de entrada
- o adapter Pi passa a gerar um skill que ensina leitura de `index.md` primeiro, usa links Markdown relativos como formato interno canonico e manda rodar `/obsidian-init` pela ausencia de `index.md`, nao pela ausencia de `_CLAUDE.md`
- `create-command.md` e `podcast.md` deixam de propagar linguagem antiga sobre `wikilinks` obrigatorios e passam a gerar/comunicar comandos com contrato alinhado ao bundle **OKF-first**
- `CLAUDE.md`, `architecture.md` e `examples/README.md` passam a separar com mais rigor o bundle persistido do contexto Obsidian-native e a enquadrar o sample vault como exemplo de compatibilidade legada, nao como layout canonico do fork
- os targets foram rebuildados apos os ajustes nas fontes para confirmar a propagacao do novo posicionamento
- o smoke recebe duas travas novas: o hook de contexto agora e validado com bundle que tem `index.md` e nao tem `_CLAUDE.md`, e o build do Pi agora falha se o skill gerado voltar a exigir `_CLAUDE.md` ou `[[wikilinks]]` obrigatorios

Validacao desta rodada:

- `bash scripts/build.sh`
- `python -m pytest tests/test_smoke.py -q`
- resultado: `30 passed`


## Atualizacao de 2026-07-10 - gatilhos em pt-BR e rebuild dos adapters

Escopo desta rodada:

- adicionar `triggers_pt` primeiro aos comandos prioritarios e depois expandir a cobertura para todos os 45 comandos do repositorio
- habilitar uma camada explicita de invocacao em linguagem natural pt-BR sem mudar os nomes publicos dos comandos
- rebuildar os adapters para propagar a nova lingua aos dispatchers gerados
- registrar a mudanca no release tecnico, mantendo a regra de rastreabilidade do fork

Arquivos ajustados nesta rodada:

- [../../../commands/create-command.md](C:/Users/konok/Documents/vibecode/second-brain/commands/create-command.md)
- [../../../commands/idea-discovery.md](C:/Users/konok/Documents/vibecode/second-brain/commands/idea-discovery.md)
- [../../../commands/notebooklm.md](C:/Users/konok/Documents/vibecode/second-brain/commands/notebooklm.md)
- [../../../commands/obsidian-architect.md](C:/Users/konok/Documents/vibecode/second-brain/commands/obsidian-architect.md)
- [../../../commands/obsidian-board-hygiene.md](C:/Users/konok/Documents/vibecode/second-brain/commands/obsidian-board-hygiene.md)
- [../../../commands/obsidian-board.md](C:/Users/konok/Documents/vibecode/second-brain/commands/obsidian-board.md)
- [../../../commands/obsidian-calendar.md](C:/Users/konok/Documents/vibecode/second-brain/commands/obsidian-calendar.md)
- [../../../commands/obsidian-capture.md](C:/Users/konok/Documents/vibecode/second-brain/commands/obsidian-capture.md)
- [../../../commands/obsidian-catchup.md](C:/Users/konok/Documents/vibecode/second-brain/commands/obsidian-catchup.md)
- [../../../commands/obsidian-challenge.md](C:/Users/konok/Documents/vibecode/second-brain/commands/obsidian-challenge.md)
- [../../../commands/obsidian-connect.md](C:/Users/konok/Documents/vibecode/second-brain/commands/obsidian-connect.md)
- [../../../commands/obsidian-daily.md](C:/Users/konok/Documents/vibecode/second-brain/commands/obsidian-daily.md)
- [../../../commands/obsidian-decide.md](C:/Users/konok/Documents/vibecode/second-brain/commands/obsidian-decide.md)
- [../../../commands/obsidian-distill.md](C:/Users/konok/Documents/vibecode/second-brain/commands/obsidian-distill.md)
- [../../../commands/obsidian-emerge.md](C:/Users/konok/Documents/vibecode/second-brain/commands/obsidian-emerge.md)
- [../../../commands/obsidian-export.md](C:/Users/konok/Documents/vibecode/second-brain/commands/obsidian-export.md)
- [../../../commands/obsidian-find.md](C:/Users/konok/Documents/vibecode/second-brain/commands/obsidian-find.md)
- [../../../commands/obsidian-graduate.md](C:/Users/konok/Documents/vibecode/second-brain/commands/obsidian-graduate.md)
- [../../../commands/obsidian-health.md](C:/Users/konok/Documents/vibecode/second-brain/commands/obsidian-health.md)
- [../../../commands/obsidian-ingest.md](C:/Users/konok/Documents/vibecode/second-brain/commands/obsidian-ingest.md)
- [../../../commands/obsidian-init.md](C:/Users/konok/Documents/vibecode/second-brain/commands/obsidian-init.md)
- [../../../commands/obsidian-learn.md](C:/Users/konok/Documents/vibecode/second-brain/commands/obsidian-learn.md)
- [../../../commands/obsidian-log.md](C:/Users/konok/Documents/vibecode/second-brain/commands/obsidian-log.md)
- [../../../commands/obsidian-panel.md](C:/Users/konok/Documents/vibecode/second-brain/commands/obsidian-panel.md)
- [../../../commands/obsidian-person.md](C:/Users/konok/Documents/vibecode/second-brain/commands/obsidian-person.md)
- [../../../commands/obsidian-project.md](C:/Users/konok/Documents/vibecode/second-brain/commands/obsidian-project.md)
- [../../../commands/obsidian-projects.md](C:/Users/konok/Documents/vibecode/second-brain/commands/obsidian-projects.md)
- [../../../commands/obsidian-recap.md](C:/Users/konok/Documents/vibecode/second-brain/commands/obsidian-recap.md)
- [../../../commands/obsidian-reconcile.md](C:/Users/konok/Documents/vibecode/second-brain/commands/obsidian-reconcile.md)
- [../../../commands/obsidian-recurring.md](C:/Users/konok/Documents/vibecode/second-brain/commands/obsidian-recurring.md)
- [../../../commands/obsidian-retrieval-eval.md](C:/Users/konok/Documents/vibecode/second-brain/commands/obsidian-retrieval-eval.md)
- [../../../commands/obsidian-review.md](C:/Users/konok/Documents/vibecode/second-brain/commands/obsidian-review.md)
- [../../../commands/obsidian-save.md](C:/Users/konok/Documents/vibecode/second-brain/commands/obsidian-save.md)
- [../../../commands/obsidian-synthesize.md](C:/Users/konok/Documents/vibecode/second-brain/commands/obsidian-synthesize.md)
- [../../../commands/obsidian-task.md](C:/Users/konok/Documents/vibecode/second-brain/commands/obsidian-task.md)
- [../../../commands/obsidian-visualize.md](C:/Users/konok/Documents/vibecode/second-brain/commands/obsidian-visualize.md)
- [../../../commands/obsidian-world.md](C:/Users/konok/Documents/vibecode/second-brain/commands/obsidian-world.md)
- [../../../commands/podcast.md](C:/Users/konok/Documents/vibecode/second-brain/commands/podcast.md)
- [../../../commands/research-deep.md](C:/Users/konok/Documents/vibecode/second-brain/commands/research-deep.md)
- [../../../commands/research.md](C:/Users/konok/Documents/vibecode/second-brain/commands/research.md)
- [../../../commands/vault-deep-synthesis.md](C:/Users/konok/Documents/vibecode/second-brain/commands/vault-deep-synthesis.md)
- [../../../commands/x-pulse.md](C:/Users/konok/Documents/vibecode/second-brain/commands/x-pulse.md)
- [../../../commands/x-read.md](C:/Users/konok/Documents/vibecode/second-brain/commands/x-read.md)
- [../../../commands/youtube.md](C:/Users/konok/Documents/vibecode/second-brain/commands/youtube.md)
- [../../../CONTRIBUTING.md](C:/Users/konok/Documents/vibecode/second-brain/CONTRIBUTING.md)
- [../../../tests/test_smoke.py](C:/Users/konok/Documents/vibecode/second-brain/tests/test_smoke.py)
- [../../../CHANGELOG.md](C:/Users/konok/Documents/vibecode/second-brain/CHANGELOG.md)

Resultados consolidados desta rodada:

- todos os comandos agora expoem `triggers_pt` no frontmatter, com frases naturais em pt-BR alinhadas ao comportamento publico ja existente
- os cinco comandos prioritarios passam a aceitar tambem gatilhos explicitos em pt-BR no mesmo modelo usado antes apenas para `triggers_en`
- os dispatchers gerados por adapter passam a poder renderizar uma secao dedicada a `portugues (`pt`)` sem mudanca de arquitetura, apenas pelo preenchimento dos frontmatters
- `create-command.md` passa a ensinar `triggers_pt` tambem no template de comando novo, reduzindo regressao futura para comandos criados no fork
- `CONTRIBUTING.md` passa a tratar `triggers_pt` como implementacao de referencia para idioma nao ingles e documenta que a cobertura portuguesa ja existe em todos os comandos
- o smoke agora trava a presenca dos gatilhos pt-BR no skill gerado do `codex-cli` e rejeita `?` em qualquer linha `triggers_pt:`, evitando regressao de propagacao ou de codificacao

Validacao desta rodada:

- `bash scripts/build.sh`
- `python -m pytest tests/test_smoke.py -q`
- verificacao de cobertura: `45` arquivos de comando com `triggers_pt`


## Atualizacao de 2026-07-10 - restauracao editorial do README

Escopo desta rodada:

- restaurar no `README.md` parte do valor demonstrativo que havia sido comprimido na reescrita OKF-first
- preservar o contrato tecnico do fork, mas recuperar cenarios praticos importantes do README original
- explicitar que pesquisa, automacoes e manutencao continuam existindo como extensoes documentadas do fork

Arquivos ajustados nesta rodada:

- [../../../README.md](C:/Users/konok/Documents/vibecode/second-brain/README.md)
- [../../../docs/ofk/releases/2026-07-ofk-alignment.md](C:/Users/konok/Documents/vibecode/second-brain/docs/ofk/releases/2026-07-ofk-alignment.md)

Resultados consolidados desta rodada:

- a secao `O que acontece quando voce instala` volta a cobrir casos de uso praticos que haviam sumido, incluindo manutencao noturna, `x-read`, `x-pulse`, `research`, `research-deep` e `youtube`
- a tabela `Antes e depois` volta a mostrar com mais clareza o ganho operacional do projeto em pesquisa, leitura social, rotina noturna e ingestao multimodal
- o README continua OKF-first, mas deixa de reduzir o projeto apenas ao contrato persistido e volta a comunicar melhor a experiencia do produto
