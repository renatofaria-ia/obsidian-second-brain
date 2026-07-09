# Alinhamento OKF - fase 0

Este diretorio fecha o contrato inicial de adaptacao do fork `renatofaria-ia/obsidian-second-brain` ao **Open Knowledge Format (OKF) 0.1**.

## Decisoes desta fase

- O formato persistido alvo do fork passa a ser um **bundle OKF 0.1**.
- A interface publica dos comandos permanece a mesma na primeira fase.
- Tudo que excede a spec base do OKF passa a ser tratado como **extensao documentada do fork**.
- A refatoracao dos comandos fica para a fase seguinte, com prioridade em `/obsidian-save`, `/obsidian-find`, `/obsidian-ingest`, `/obsidian-init` e `/obsidian-export`.

## Documentos desta fase

- [`gap-analysis.md`](./gap-analysis.md): diferencas entre o comportamento atual do upstream e a spec OKF 0.1.
- [`canonical-bundle.md`](./canonical-bundle.md): contrato do bundle canonico deste fork.
- [`command-matrix.md`](./command-matrix.md): classificacao dos 44 comandos em `OKF-core`, `OKF + extensao` e `Obsidian-only`.
- [`test-scenarios.md`](./test-scenarios.md): cenarios de validacao para a migracao.
- [`releases/2026-07-ofk-alignment.md`](./releases/2026-07-ofk-alignment.md): log tecnico desta rodada de adaptacao, com escopo, arquivos tocados e validacao executada.

## Fixtures

- [`../../examples/ofk-bundle-minimo/`](../../examples/ofk-bundle-minimo/): bundle minimo em OKF base.
- [`../../examples/ofk-bundle-extensoes/`](../../examples/ofk-bundle-extensoes/): bundle com extensoes AI-first preservadas sobre a base OKF.

## Resultado esperado

Ao final da fase 0, o fork tem um contrato claro para:

- o que e **core OKF**
- o que e **extensao do fork**
- o que permanece **Obsidian-only**
- como validar um bundle minimo e um bundle com round-trip de extensoes