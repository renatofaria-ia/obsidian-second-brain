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

Validacao desta rodada:

- `python -m pytest tests/test_smoke.py`
- resultado: `29 passed`

## Validacao executada

Validacoes mecanicas:

- `python -m py_compile` nos arquivos Python relevantes
- `git diff --check`
- varreduras locais para garantir ausencia dos padroes antigos mais criticos:
  - `mandatory wikilinks`
  - `Read _CLAUDE.md first`
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
