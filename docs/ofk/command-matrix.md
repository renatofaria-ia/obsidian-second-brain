# Matriz de comandos

Esta matriz classifica os 44 comandos atuais segundo o contrato desta fase.

## Criterios

- **OKF-core**: o comando pode operar sobre um bundle OKF sem depender de convencoes especificas do Obsidian ou do runtime AI-first.
- **OKF + extensao**: o comando continua util sobre um bundle OKF, mas depende de tipos, campos, fluxos ou arquivos auxiliares definidos por este fork.
- **Obsidian-only**: o comando depende diretamente de UI, plugin, representacao ou comportamento que nao faz parte do bundle OKF.

## Matriz

| OKF-core | OKF + extensao | Obsidian-only |
|---|---|---|
| `obsidian-export`<br>`obsidian-find`<br>`obsidian-health`<br>`obsidian-log` | `idea-discovery`<br>`notebooklm`<br>`obsidian-architect`<br>`obsidian-capture`<br>`obsidian-catchup`<br>`obsidian-challenge`<br>`obsidian-connect`<br>`obsidian-daily`<br>`obsidian-decide`<br>`obsidian-distill`<br>`obsidian-emerge`<br>`obsidian-graduate`<br>`obsidian-ingest`<br>`obsidian-init`<br>`obsidian-learn`<br>`obsidian-person`<br>`obsidian-project`<br>`obsidian-projects`<br>`obsidian-recap`<br>`obsidian-reconcile`<br>`obsidian-recurring`<br>`obsidian-retrieval-eval`<br>`obsidian-review`<br>`obsidian-save`<br>`obsidian-synthesize`<br>`obsidian-task`<br>`obsidian-world`<br>`podcast`<br>`research`<br>`research-deep`<br>`vault-deep-synthesis`<br>`x-pulse`<br>`x-read`<br>`youtube` | `create-command`<br>`obsidian-board`<br>`obsidian-board-hygiene`<br>`obsidian-calendar`<br>`obsidian-panel`<br>`obsidian-visualize` |

## Notas de interpretacao

### OKF-core

Esses comandos sao os melhores candidatos para virar o primeiro lote de comportamento realmente nativo em OKF:

- `obsidian-export`
- `obsidian-find`
- `obsidian-health`
- `obsidian-log`

### OKF + extensao

Aqui fica a maior parte do valor do produto. Esses comandos nao precisam ser descartados. Eles precisam ser reancorados sobre um bundle OKF e continuar usando extensoes documentadas do fork para:

- tipos locais, como `person`, `project`, `task` e `review`
- campos extras, como `ai-first`, `timeline` e `confidence`
- arquivos auxiliares, como `_CLAUDE.md`
- rotinas de propagacao, reconciliacao e sintese

### Obsidian-only

Esta coluna inclui comandos que hoje dependem de:

- quadros ou visoes especificas do Obsidian
- representacoes visuais do vault
- integracoes de produto que nao fazem parte do bundle
- manutencao interna da propria skill

Esses comandos podem continuar existindo, mas nao definem o contrato de conhecimento interoperavel.

## Ordem sugerida de refatoracao

1. `obsidian-save`
2. `obsidian-find`
3. `obsidian-ingest`
4. `obsidian-init`
5. `obsidian-export`

Essa ordem foi escolhida porque esses comandos definem ingestao, navegacao, inicializacao e serializacao do bundle.