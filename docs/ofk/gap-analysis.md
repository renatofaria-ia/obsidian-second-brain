# Gap analysis: upstream vs OKF 0.1

Este documento compara o comportamento atual do upstream `obsidian-second-brain` com a spec **OKF 0.1** e fixa a direcao deste fork.

## Resumo executivo

O upstream ja toca em OKF via `/obsidian-export okf`, mas o formato nativo do sistema ainda e um **vault Obsidian AI-first** com convencoes proprias, como `[[wikilinks]]`, `_CLAUDE.md`, `CRITICAL_FACTS.md`, regras de preambulo obrigatorio e schemas ricos por tipo.

A adaptacao deste fork nao vai fingir que essas convencoes fazem parte do core do OKF. A decisao desta fase e:

- usar **OKF 0.1 como base canonica do bundle**
- preservar o que ja existe como **extensoes documentadas**
- manter a interface publica dos comandos no curto prazo

## Mapa de gaps

| Area | Estado atual no upstream | OKF 0.1 | Gap | Direcao deste fork |
|---|---|---|---|---|
| Unidade de persistencia | Vault Obsidian com pastas opinadas | Bundle hierarquico de Markdown | Parcial | Persistir como bundle OKF 0.1; estrutura de pastas vira decisao do bundle, nao do produto |
| Frontmatter | Schemas ricos, `ai-first: true`, tipos especificos | Apenas `type` e obrigatorio; extras sao permitidos | Parcial | Manter campos extras como extensoes do fork |
| Links internos | `[[wikilinks]]` sao obrigatorios | Links Markdown padrao entre concepts | Conflito | Link canonico do bundle passa a ser Markdown relativo |
| Body do concept | `## For future Claude` e fortemente exigido | Nenhuma secao obrigatoria | Conflito | Preambulo AI-first vira extensao documentada, nao requisito do core |
| Arquivos reservados | `index.md` e `log.md`, mais `_CLAUDE.md`, `SOUL.md`, `CRITICAL_FACTS.md` com papel central | Apenas `index.md` e `log.md` sao reservados | Conflito | Somente `index.md` e `log.md` sao reservados; os demais viram arquivos auxiliares de extensao |
| Tipos | Tipos e schemas bem opinados (`project`, `person`, `task`, etc.) | `type` aberto, sem registro central | Parcial | Manter tipos existentes, mas trata-los como convencoes locais do produtor |
| Navegacao | `index.md` e logica de leitura por vault | `index.md` opcional, progressive disclosure | Alinhado | Tornar `index.md` raiz com `okf_version: "0.1"` obrigatorio neste fork |
| Historico | `log.md` ou `Logs/YYYY-MM-DD.md` | `log.md` opcional | Parcial | Manter `log.md` no bundle; `Logs/` vira extensao opcional |
| Exportacao OKF | Existe, mas como saida derivada de `/obsidian-export okf` | OKF como bundle distribuivel | Parcial | Mudar a meta do fork para OKF nativo, nao apenas exportador |
| Hooks e agentes | Fazem parte da experiencia principal | Fora de escopo da spec | Conflito | Documentar como runtime opcional do fork, nao como parte do bundle |
| Quadros, canvas e UI de vault | Dependem de Obsidian ou plugins | Fora de escopo da spec | Conflito | Permanecem Obsidian-only |

## Implicacoes praticas

### 1. O bundle nao pode depender de `[[wikilinks]]`

O OKF define interoperabilidade por Markdown legivel e parseavel por qualquer consumidor. `[[wikilinks]]` podem continuar existindo como conveniencia de authoring ou backward compatibility, mas o bundle canonico deste fork nao pode depender deles como unico mecanismo de linkagem.

### 2. O OKF nao invalida o modelo AI-first

O OKF e minimo por design. Ele nao proibe:

- preambulo `## For future Claude`
- `ai-first: true`
- `timeline:`
- `confidence:`
- campos extras de dominio

Esses elementos sao validos no fork, desde que documentados como **extensoes** e nao confundidos com o core da spec.

### 3. `_CLAUDE.md` deixa de ser contrato do bundle

`_CLAUDE.md`, `SOUL.md` e `CRITICAL_FACTS.md` podem continuar existindo, mas passam a ser arquivos auxiliares do runtime e da experiencia de agent, nao componentes obrigatorios do formato do conhecimento.

### 4. O `/obsidian-export okf` deixa de ser "ponte"

No upstream, o exportador OKF e uma traducao a partir do vault nativo. Neste fork, o objetivo e que o armazenamento nativo ja obedeca ao contrato OKF, reduzindo a distancia entre persistencia, leitura e distribuicao.

## Decisoes fechadas nesta fase

- Alvo: **OKF 0.1**
- Estrategia: **OKF base + extensoes explicitas**
- Compatibilidade: **preservar os nomes dos comandos na primeira fase**
- Sequencia de implementacao: `/obsidian-save`, `/obsidian-find`, `/obsidian-ingest`, `/obsidian-init`, `/obsidian-export`