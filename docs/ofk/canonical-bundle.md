# Modelo canonico de bundle

Este documento define o contrato do bundle canonico do fork para a adaptacao ao **OKF 0.1**.

## Objetivo

Todo conhecimento persistido pelo fork deve poder ser lido como um **bundle OKF 0.1** por um consumidor que:

- entende Markdown UTF-8
- consegue parsear frontmatter YAML
- conhece `index.md` e `log.md`
- tolera campos extras desconhecidos

## Contrato base

### 1. Estrutura minima

O bundle canonico deve seguir esta forma minima:

```text
bundle/
|-- index.md
|-- log.md
|-- <diretorios de dominio>/
|   |-- <concept>.md
|   `-- ...
`-- <arquivos auxiliares opcionais>
```

Regras:

- `index.md` e reservado em qualquer nivel.
- `log.md` e reservado em qualquer nivel.
- Todo outro arquivo `.md` e um **concept document**.
- O bundle e salvo em **UTF-8**.

### 2. `index.md` raiz

Neste fork, o `index.md` raiz passa a ser obrigatorio por contrato, mesmo sendo opcional na spec base.

Ele deve:

- declarar `okf_version: "0.1"` no frontmatter raiz
- listar os concepts e subdiretorios por progressive disclosure
- servir como porta de entrada para leitura do bundle

### 3. `log.md` raiz

Neste fork, `log.md` tambem passa a ser obrigatorio por contrato.

Ele deve:

- registrar eventos relevantes do bundle
- permanecer append-only
- funcionar mesmo quando o bundle tambem usar `Logs/YYYY-MM-DD.md` como extensao

Se `Logs/` existir, o `log.md` raiz deve continuar existindo como indice, ponteiro ou resumo operacional. Ele nao some do contrato.

### 4. Concept documents

Cada concept deve ser um Markdown com frontmatter YAML valido.

Obrigatorio:

```yaml
---
type: <string>
---
```

Recomendado:

```yaml
---
type: <string>
title: <string>
description: <string>
resource: <uri>
tags: [<tag>, <tag>]
timestamp: <ISO 8601>
---
```

Campos adicionais sao permitidos e devem ser preservados por round-trip.

## Politica de extensoes

### 1. Campos extras

O fork **nao** vai criar um namespace tecnico novo para extensoes na fase 0. A razao e simples: o OKF ja permite chaves extras no frontmatter.

Portanto, campos como estes continuam validos:

- `ai-first: true`
- `date:`
- `updated:`
- `confidence:`
- `timeline:`
- `related-projects:`
- `related-people:`

Esses campos devem ser tratados como **extensoes documentadas do produtor**, nao como requisitos do core OKF.

### 2. Arquivos auxiliares

Arquivos como:

- `_CLAUDE.md`
- `CRITICAL_FACTS.md`
- `SOUL.md`

podem coexistir no bundle, mas nao sao nomes reservados do formato. Eles sao auxiliares do runtime do fork.

### 3. Preambulo AI-first

O bloco:

```markdown
## For future Claude
```

e uma extensao valida do fork. Ele pode aparecer no body de qualquer concept, mas nunca deve ser tratado como requisito de validade do bundle por consumidores OKF genericos.

## Politica de links

O link canonico do bundle passa a ser **Markdown relativo**.

Exemplo:

```markdown
Veja [orders](../tables/orders.md) para o schema principal.
```

Regra de migracao:

- `[[wikilinks]]` podem continuar existindo durante a transicao
- bundles canonicos e fixtures desta fase devem usar links Markdown relativos
- nenhum concept deve depender exclusivamente de `[[wikilinks]]` para ser navegavel por um consumidor OKF

## Estrutura de pastas

O OKF nao impoe taxonomia fixa de pastas. Este fork tambem nao vai impor `wiki/`, `raw/`, `boards/` como estrutura universal do bundle.

Diretriz:

- o bundle pode ser organizado por dominio, tipo, fonte ou area de negocio
- a organizacao escolhida deve ser refletida no `index.md`
- estruturas mais opinadas, como `raw/`, `wiki/` e `Logs/`, passam a ser convencoes opcionais do fork

## O que continua fora do core

Permanecem fora do contrato base do bundle:

- hooks de escrita
- agentes agendados
- Google Calendar MCP
- canvas e outras representacoes visuais do Obsidian
- regras de interface especificas de CLI

Esses elementos podem continuar existindo no produto, mas nao definem a validade de um bundle OKF.