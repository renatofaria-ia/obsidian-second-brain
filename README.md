# obsidian-second-brain

Fork OKF-first de `obsidian-second-brain` para **Claude Code**, **Codex CLI**, **Gemini CLI**, **OpenCode**, **Hermes** e **Pi**.

Este fork preserva os nomes públicos dos comandos na fase atual, mas muda o contrato de persistência para um bundle governado por **OKF-first**, com base explícita em **Open Knowledge Format (OKF) 0.1**. O objetivo é manter o valor operacional do projeto original enquanto torna o formato persistido mais claro, portátil e verificável.

## Resumo

- `index.md` e `log.md` são nomes reservados na raiz do bundle.
- `index.md` raiz declara `okf_version: "0.1"`.
- O bundle persistido usa Markdown UTF-8 com frontmatter YAML.
- O campo `type` é obrigatório.
- Links Markdown relativos são o formato interno canônico.
- Tudo o que excede a spec base vira **extensão documentada do fork**.

## Documentação canônica

- Contrato e escopo: [docs/ofk/README.md](docs/ofk/README.md)  
  Observação: o diretório docs/ofk/ foi mantido por compatibilidade histórica do fork, mas a sigla da spec é OKF.
- Gap analysis: [docs/ofk/gap-analysis.md](docs/ofk/gap-analysis.md)
- Modelo canônico do bundle: [docs/ofk/canonical-bundle.md](docs/ofk/canonical-bundle.md)
- Matriz de comandos: [docs/ofk/command-matrix.md](docs/ofk/command-matrix.md)
- Cenários de teste: [docs/ofk/test-scenarios.md](docs/ofk/test-scenarios.md)
- Registro técnico desta rodada: [docs/ofk/releases/2026-07-ofk-alignment.md](docs/ofk/releases/2026-07-ofk-alignment.md)

## O problema

Você usa um agente no terminal todos os dias, mas cada sessão tende a começar do zero. Ao mesmo tempo, suas notas em Obsidian acumulam contexto, decisões, pessoas, tarefas e ideias que raramente voltam para melhorar o trabalho seguinte.

O projeto original resolve parte disso ao transformar o vault em uma base viva. Este fork adiciona o que faltava para transformar essa base em um bundle persistido com contrato explícito:

- um contrato persistido explícito;
- separação entre núcleo interoperável e extensão local;
- preservação da interface pública dos comandos enquanto a semântica interna evolui;
- documentação em camadas para humano, agente e modelos.

## Como este fork estende a LLM Wiki

A ideia-base continua próxima do padrão da LLM Wiki do Karpathy: fontes entram, páginas são atualizadas e o conhecimento fica recuperável. A diferença é que o fork passa a explicitar o contrato do bundle.

| Aspecto | LLM Wiki / upstream | Este fork |
|---|---|---|
| Persistência | convenções implícitas do vault | bundle OKF 0.1 com extensões explícitas |
| Novas fontes | append e cross-reference | reescrita de páginas existentes |
| Contradições | resolução manual ou ad hoc | reconciliação explícita via comandos do vault |
| Formato interno | dependente do projeto e do runtime | `index.md`, `log.md`, `type` e links relativos |
| Camada Obsidian | frequentemente implícita | compatibilidade tratada como extensão |
| AI-first | pode ser pressuposto pelo fluxo | extensão documentada, não núcleo da spec |

## O que muda neste fork

### Núcleo do bundle

- `index.md` e `log.md` são arquivos reservados na raiz.
- `index.md` raiz declara `okf_version: "0.1"`.
- O bundle persistido usa Markdown UTF-8 com frontmatter YAML e `type` obrigatório.
- Links Markdown relativos são o formato interno canônico.

### Extensões explícitas do fork

Tudo o que vai além do núcleo OKF continua disponível, mas deixa de ser tratado como parte implícita do padrão:

- `_CLAUDE.md`, `CRITICAL_FACTS.md`, `SOUL.md`, `Bases/` e arquivos auxiliares de runtime;
- regras AI-first, preâmbulo `## For future Claude`, frontmatter enriquecido, recency markers e confidence levels;
- timeline bi-temporal, agentes agendados, hooks de background e convenções específicas de Obsidian;
- `[[wikilinks]]` como compatibilidade para bundles legados ou uso Obsidian-native.

### Compatibilidade pública

- os comandos continuam com os mesmos nomes públicos nesta fase;
- `/obsidian-init` cria o núcleo OKF e pode gerar extensões opcionais;
- `/obsidian-export okf` emite um bundle OKF preservando campos extras suportados;
- bundles Obsidian legados continuam suportados, mas o formato documentado do fork agora é OKF-first.

## O que acontece quando você instala

**Depois de uma reunião:** `/obsidian-save`  
O agente extrai decisões, pessoas, tarefas e ideias da conversa e atualiza as notas corretas no bundle.

**Depois de um áudio:** `/obsidian-ingest meeting.m4a`  
O conteúdo é transcrito, estruturado e distribuído entre entidades, tarefas, projetos e nota diária.

**Depois de uma foto ou screenshot:** `/obsidian-ingest photo.png`  
O agente lê a imagem, extrai texto e estrutura, cria ou atualiza concepts e conecta o material ao restante do bundle.

**Depois de uma fonte externa importante:** `/obsidian-ingest https://youtube.com/...`  
O comando não produz apenas um resumo solto. Ele reescreve páginas existentes, resolve contradições e pode disparar novas sínteses.

**Antes de uma decisão relevante:** `/obsidian-challenge`  
O agente busca falhas parecidas, decisões antigas e reversões já registradas para tensionar a hipótese com o histórico real.

**Quando você quer navegar o mapa geral:** `/obsidian-visualize`  
O comando gera uma visão estrutural do bundle, destacando hubs, órfãos e agrupamentos por tipo.

**No início do dia:** `/obsidian-daily`  
A nota diária é criada ou atualizada com tarefas pendentes, contexto recente e eventos relevantes.

## Antes e depois

| Fluxo | Sem a skill | Com este fork |
|---|---|---|
| Salvar decisões | copiar, colar ou esquecer | atualização do projeto, pessoa ou nota certa |
| Continuidade de sessão | reexplicar tudo | recuperação rápida do contexto do vault |
| Ingestão de conteúdo | ler e esquecer | reescrita de várias páginas do bundle |
| Contradições | ficam escondidas | podem ser reconciliadas explicitamente |
| Exportação | formato difuso | bundle OKF exportável e legível por outros consumidores |
| Contexto para IA futura | implícito | contrato persistido e extensões documentadas |

## Como funciona

O comportamento do fork pode ser visto em quatro camadas:

- **Operações:** captura, ingestão, exportação, manutenção e visualização do vault.
- **Pensamento:** challenge, síntese, distilação, conexão e revisão.
- **Contexto:** pessoas, projetos, mundo e retomada de contexto.
- **Pesquisa:** web, X, YouTube, podcast e fluxos grounded.

São **44 comandos** no total. O comando de calendário (`/obsidian-calendar`) permanece exclusivo do Claude Code, então os builds de Codex, Gemini, OpenCode, Hermes e Pi expõem 43 comandos cross-platform.

## 44 comandos

A classificação técnica dos comandos em `OKF-core`, `OKF + extensão` e `Obsidian-only` está em [docs/ofk/command-matrix.md](docs/ofk/command-matrix.md). Abaixo está a visão funcional para uso diário.

### Operações

| Comando | O que faz |
|---|---|
| `/obsidian-save` | Salva decisões, tarefas, pessoas e ideias extraídas da conversa atual. |
| `/obsidian-ingest` | Incorpora URL, PDF, áudio, imagem ou screenshot e reescreve o vault. |
| `/obsidian-synthesize` | Identifica padrões entre fontes e escreve sínteses úteis. |
| `/obsidian-reconcile` | Encontra e resolve contradições do vault. |
| `/obsidian-export` | Gera snapshot limpo em JSON ou Markdown para outros consumidores. |
| `/obsidian-daily` | Cria ou atualiza a nota diária. |
| `/obsidian-calendar <mode>` | Lê agenda, reconcilia compromissos, transforma evento em nota ou agenda um item. |
| `/obsidian-recurring` | Controla obrigações recorrentes com cadência e próxima data calculada. |
| `/obsidian-log` | Registra uma sessão de trabalho e a conecta ao restante do vault. |
| `/obsidian-task` | Cria ou atualiza tarefa com prioridade, prazo e contexto. |
| `/obsidian-person` | Cria ou atualiza nota de pessoa. |
| `/obsidian-capture` | Faz captura rápida de ideia ou fragmento. |
| `/obsidian-catchup` | Processa capturas despejadas no vault a partir de canais externos. |
| `/obsidian-find` | Faz busca contextual no vault. |
| `/obsidian-recap` | Resume um dia, uma semana ou um mês. |
| `/obsidian-review` | Conduz revisão estruturada semanal ou mensal. |
| `/obsidian-board` | Mostra ou atualiza board de trabalho. |
| `/obsidian-board-hygiene` | Faz triagem de board, destacando itens atrasados ou envelhecidos. |
| `/obsidian-project` | Mantém uma nota de projeto com vínculos para board e diários. |
| `/obsidian-projects` | Consolida visão de portfólio a partir de notas e docs locais. |
| `/obsidian-health` | Audita lacunas, contradições, claims obsoletos e órfãos. |
| `/obsidian-retrieval-eval` | Mede a qualidade da busca no vault e aponta falhas concretas. |
| `/obsidian-decide [--formal]` | Registra decisão; com `--formal`, escreve um ADR completo. |
| `/obsidian-visualize` | Gera um mapa visual do segundo cérebro. |
| `/obsidian-learn` | Revê aprendizados do vault e promove padrões para regras mais estáveis. |
| `/obsidian-init` | Inicializa o núcleo do bundle e extensões opcionais. |
| `/obsidian-architect` | Escaneia um codebase e escreve notas de arquitetura mantidas. |
| `/create-command` | Entrevista guiada que gera um novo comando em `commands/<name>.md`. |

### Pensamento

| Comando | O que faz |
|---|---|
| `/obsidian-challenge` | Usa o próprio histórico para argumentar contra sua ideia. |
| `/obsidian-panel` | Reúne perspectivas distintas sobre uma decisão e sintetiza o resultado. |
| `/obsidian-emerge` | Expõe padrões em notas recentes que ainda não viraram conceito explícito. |
| `/obsidian-connect [A] [B]` | Liga domínios distantes para gerar novas ideias. |
| `/vault-deep-synthesis [topic]` | Cruza notas sobre um tema e aponta acordos, lacunas e contradições. |
| `/obsidian-distill [note or source]` | Condensa nota ou fonte longa em claims-chave com proveniência. |
| `/idea-discovery` | Prioriza direções promissoras a partir de ideias, perguntas e pesquisa órfã. |
| `/obsidian-graduate` | Converte um fragmento de ideia em projeto estruturado. |

### Contexto

| Comando | O que faz |
|---|---|
| `/obsidian-world` | Carrega identidade, estado atual e contexto do vault em camadas de orçamento. |

### Pesquisa

| Comando | O que faz |
|---|---|
| `/x-read [url]` | Lê um post do X, thread, claims e sinais de resposta. |
| `/x-pulse [topic]` | Mapeia tendências, vozes e hooks em torno de um tema. |
| `/research [topic]` | Produz um dossiê web com fatos, timeline, players, contrapontos e fontes. |
| `/research-deep [topic]` | Parte do que já existe no vault e pesquisa só o delta necessário. |
| `/notebooklm [topic]` | Faz síntese grounded a partir de notas relevantes do vault. |
| `/youtube [url]` | Incorpora transcript, metadados e sinais visuais de um vídeo. |
| `/podcast [url]` | Resolve feed, transcript e transforma episódio em nota pesquisável. |

## O bundle está vivo

O objetivo do fork não é arquivar informação e esquecer. O objetivo é fazer o bundle, inclusive quando armazenado em um vault Obsidian, compor ao longo do tempo:

- uma fonte nova atualiza páginas já existentes;
- conhecimento repetido vira estrutura mais estável;
- aprendizados recorrentes sobem de nível;
- mudanças factuais podem preservar histórico via timeline bi-temporal;
- rotinas de manutenção continuam limpando, consolidando e religando o bundle.

## Escolha seu preset

| Preset | Foco |
|---|---|
| `generalist` | captura, síntese e manutenção equilibradas |
| `researcher` | pesquisa, revisão e dossiês |
| `architect` | documentação de codebase e visão estrutural |
| `operator` | acompanhamento operacional mais intenso |

Sem preset, o bootstrap gera uma base genérica e funcional.

## Agente de background e agentes agendados

O projeto continua suportando a ideia de manutenção contínua do vault, mas agora essa camada fica claramente posicionada como extensão do fork, não como definição do formato base.

Exemplos de comportamento:

- continuidade de manutenção após compactação de contexto;
- revisões periódicas de saúde e reconciliação;
- incentivo de save quando há muito contexto sem persistência;
- atualização de notas de rotina sem bloquear a sessão principal.

## Arquitetura do bundle

### Núcleo OKF

O contrato persistido deste fork é OKF-first, sobre a spec base OKF 0.1. O núcleo mínimo do bundle é:

- `index.md` como ponto de entrada canônico;
- `log.md` como arquivo reservado de log;
- frontmatter YAML parseável;
- `type` obrigatório;
- links Markdown relativos como formato interno canônico;
- `okf_version: "0.1"` no `index.md` raiz.

### Extensões explícitas do fork

Este fork pode adicionar, por conveniência operacional:

- `_CLAUDE.md` como camada opcional de orientação;
- regras AI-first;
- timeline bi-temporal;
- agentes agendados;
- convenções específicas de Obsidian;
- compatibilidade com `[[wikilinks]]` para bundles legados.

Bundles legados de Obsidian continuam suportados, mas o formato documentado do fork é OKF-first com extensões explícitas.

## Instalação

### Claude Code

1. Clone este repositório no diretório de skills do seu ambiente.
2. Garanta que `SKILL.md`, `README.md` e `llms.txt` estejam acessíveis ao agente.
3. Rode o processo de instalação ou bootstrap previsto pelo projeto.
4. Valide um bundle mínimo antes de usar em produção.

### Codex CLI, Gemini CLI e OpenCode

O projeto tem um build multiplataforma a partir de uma base comum. Use `scripts/build.sh` para gerar a saída específica do runtime desejado.

Exemplo:

```bash
bash scripts/build.sh --platform codex-cli
bash scripts/build.sh --platform gemini
bash scripts/build.sh --platform opencode
```

### Pi

O build do Pi gera um pacote nativo com templates e skill de descoberta sob `.pi/`.

### Hermes e modelos abertos

A skill continua agnóstica ao modelo. Os builds de OpenCode, Codex e Gemini funcionam como instruções para a CLI hospedeira, então podem rodar com modelos abertos compatíveis.

## Toolkit de pesquisa opcional

Os comandos de pesquisa podem exigir chaves ou conectores, dependendo do fluxo. Mesmo assim, o toolkit continua útil parcialmente sem todas as integrações habilitadas.

Em geral:

- os comandos centrais do vault não dependem de chaves;
- fluxos de pesquisa podem usar fontes livres ou provedores externos;
- integrações específicas precisam ser configuradas conforme o ambiente.

## Busca semântica opcional

A busca semântica continua opcional e desligada por padrão. A busca por palavra-chave funciona imediatamente, e a camada semântica pode ser adicionada depois sem quebrar o fluxo básico.

## Validação do bundle

Um bundle OKF mínimo deve conter:

- `index.md` na raiz;
- pelo menos dois concepts;
- links Markdown válidos;
- frontmatter parseável;
- campo `type` presente.

Também é importante verificar:

- nomes reservados não são usados para concepts;
- campos extras de extensão são preservados em round-trip;
- consumidores que entendem apenas OKF base continuam lendo o bundle;
- a interface pública dos comandos continua estável nesta fase.

## FAQ

### Isto é um plugin do Obsidian?

Não. Isto é uma skill para agentes e CLIs que operam sobre um bundle Markdown, inclusive quando ele está armazenado em um vault Obsidian.

### `_CLAUDE.md` é obrigatório?

Não. Ele é uma extensão do fork, não parte do núcleo OKF.

### `[[wikilinks]]` continuam válidos?

Sim, como compatibilidade para bundles legados ou uso Obsidian-native. O formato canônico interno continua sendo Markdown relativo.

### Os comandos mudaram de nome?

Não nesta fase. A compatibilidade pública foi preservada.

### Funciona com Codex CLI, Gemini CLI e OpenCode?

Sim. O repositório gera builds específicos para cada runtime, preservando a mesma base de comandos.

### Funciona em Hermes ou outros modelos abertos?

Sim. O suporte depende da CLI hospedeira e do build escolhido, não de um único modelo fechado.

### Preciso de API keys para usar isso?

Não para os comandos centrais do bundle. As integrações de pesquisa e conectores podem exigir configuração adicional.

### Como isso se diferencia de Notion AI ou Mem?

Aqui o conteúdo continua no seu vault local, em Markdown simples, com controle explícito sobre o que é persistido e como o bundle é interpretado.

### Posso usar isso no meu vault existente?

Sim. O objetivo é evitar mudanças destrutivas e deixar as notas existentes em paz, enquanto as novas passam a seguir o contrato atualizado.

### Posso ter um vault separado por projeto?

Sim. O fluxo suporta configuração por projeto para cenários multi-repo.

## Filosofia

A maior parte das ferramentas de second brain transforma o usuário em zelador do sistema. Este fork tenta inverter essa relação. Você pensa, trabalha e conversa; o agente cuida da memória operacional, reaproveita o histórico e ajuda a melhorar o raciocínio futuro com contexto persistido.

**Suas notas são o moat.**

## Contribuição

Issues e PRs deste fork são bem-vindos, especialmente para:

- novas ferramentas de escrita, ingestão e síntese;
- ajustes no contrato OKF e nas extensões explícitas;
- melhorias na documentação canônica;
- refinamento do bundle mínimo e dos exemplos;
- correções de compatibilidade entre plataformas.

Se você mantiver uma variação própria, copie [`references/DELTAS.template.md`](references/DELTAS.template.md) para `DELTAS.md` e registre ali suas diferenças locais. Isso ajuda a preservar a rastreabilidade do fork sem transformar arquivos canônicos em acúmulo de desvios implícitos.

## Créditos

Este repositório deriva de [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain).

O trabalho deste fork concentra a adaptação para **OKF-first / OKF 0.1**, a separação entre núcleo e extensões e a atualização dos adapters e documentos para um contrato persistido explícito.

## Licença

Consulte a licença original do projeto e as regras do repositório para uso e redistribuição.
