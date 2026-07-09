# Testes e cenarios da fase 0

Esta fase nao altera os 44 comandos. Ela fecha o contrato e fornece fixtures para validacao futura.

## Fixtures

- Bundle minimo: [`../../examples/ofk-bundle-minimo/`](../../examples/ofk-bundle-minimo/)
- Bundle com extensoes: [`../../examples/ofk-bundle-extensoes/`](../../examples/ofk-bundle-extensoes/)

## Cenario 1: bundle minimo em OKF base

Objetivo: validar o menor bundle que este fork deve aceitar como canonico.

Checklist:

- existe `index.md` na raiz
- existe `log.md` na raiz
- existem pelo menos 2 concepts
- cada concept tem frontmatter YAML parseavel
- cada concept tem `type`
- os links internos usam Markdown relativo valido
- o `index.md` raiz declara `okf_version: "0.1"`

Fixture de referencia:

- `examples/ofk-bundle-minimo/`

## Cenario 2: round-trip de extensoes

Objetivo: garantir que extras do fork sobrevivem sem quebrar consumidores que so entendem OKF base.

Checklist:

- o concept continua valido para um leitor OKF generico
- campos extras permanecem no frontmatter depois de leitura e reescrita
- o body preserva o preambulo `## For future Claude`
- links Markdown continuam intactos

Campos-alvo desta validacao:

- `ai-first`
- `date`
- `updated`
- `timeline`
- `related-projects`
- `related-people`

Fixture de referencia:

- `examples/ofk-bundle-extensoes/`

## Cenario 3: compatibilidade publica dos comandos

Objetivo: preservar a interface publica enquanto a persistencia muda.

Checklist:

- os nomes atuais dos comandos continuam existindo
- a documentacao dos comandos nao perde discoverability
- os primeiros refatores nao introduzem rename em `/obsidian-save`, `/obsidian-find`, `/obsidian-ingest`, `/obsidian-init` e `/obsidian-export`

Evidencia esperada:

- a matriz em `docs/ofk/command-matrix.md`
- futuras PRs com implementacao mantendo os mesmos nomes de comando

## Cenario 4: nomes reservados

Objetivo: impedir colisao entre concepts e arquivos estruturais.

Checklist:

- nenhum concept usa `index.md` como nome de arquivo
- nenhum concept usa `log.md` como nome de arquivo
- `_CLAUDE.md`, `CRITICAL_FACTS.md` e `SOUL.md` nunca sao tratados como nomes reservados da spec

## Cenario 5: logs estendidos

Objetivo: permitir `Logs/YYYY-MM-DD.md` sem perder compatibilidade do bundle.

Checklist:

- `log.md` raiz continua existindo
- `Logs/` e tratado como extensao opcional
- consumidores que ignoram `Logs/` ainda conseguem navegar pelo bundle

## Cenario 6: bootstrap OKF-first

Objetivo: garantir que o bootstrap inicial ja gere um bundle compativel com o contrato canonico do fork.

Checklist:

- existe `index.md` na raiz com `okf_version: "0.1"`
- existe `log.md` na raiz com a entrada inicial de bootstrap
- `_CLAUDE.md` existe como extensao do fork, nao como requisito do core
- `Home.md`, `Boards/` e `Bases/` continuam disponiveis como extensoes opcionais
- nenhum concept e salvo como `index.md` ou `log.md`

## Saida esperada desta fase

Uma implementacao futura sera considerada aderente a esta fase quando conseguir:

- produzir um bundle minimo igual ou equivalente ao fixture base
- preservar extensoes como no fixture estendido
- manter os nomes publicos dos comandos
- respeitar os nomes reservados do OKF