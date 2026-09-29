# Primeira entrega editorial — Capítulo 14

**Data:** 29/09/2026. **Estado:** DRAFT 0.1. **Módulo:** III.

[Capítulo](../../book/modulo-3/capitulo-14/README.md) · [Fontes](../../book/modulo-3/capitulo-14/referencias.md) · [Exemplos](../../book/modulo-3/capitulo-14/exemplos/README.md)

## Recorte

Terminal, shell e CLI; argumentos, aspas, expansão, redirecionamentos, pipelines, status, decisões, escopos, contexto de inicialização e fronteira entre dados e código. Bash e PowerShell possuem linguagens e contratos próprios. A ordem dos capítulos não foi modificada; a próxima unidade continua sendo 15 — Usuários, grupos, permissões e privilégios.

Seis seções, doze perguntas e respostas comentadas, quatro scripts pequenos e 26 testes. A narrativa Aurora é fictícia. Os exemplos não examinam alvos, credenciais, históricos ou documentos do leitor.

## Pesquisa e revisão interna

As 49 referências numeradas usam documentação primária GNU, Linux man-pages, Microsoft e Python. Versão documental não é versão executada. Páginas GNU com falha de abertura direta foram consultadas pelo conteúdo oficial indexado; não se afirma disponibilidade HTTP universal.

Foram conferidas as diferenças entre expansão e reinterpretação, globbing e expressão regular, stderr e status, pipe e objeto, set -e e tratamento explícito, execução e dot-sourcing, resultado parcial e resultado validado. O formato fixo de printf e as fronteiras de argumentos são apresentados sem afirmar que impedem toda forma de interpretação no consumidor.

## Execução local

Python 3.13 e Bash 5.2.37(1)-release. A descoberta encontrou 26 testes: **17 casos Bash passaram e 9 casos PowerShell foram SKIP**, porque pwsh não estava disponível no ambiente local. Nenhum desses skips é apresentado como teste bem-sucedido de PowerShell. A regressão do repositório completo e a execução em runners são verificações separadas, registradas após sua realização.

Nenhuma alteração de execution policy, elevação, conta, permissão, serviço ou configuração de host foi necessária. Arquivos de teste são temporários e próprios. Não houve laboratório Windows de UAC, Registro ou SCM: a reprodução de scripts PowerShell não valida retroativamente todos os mecanismos do capítulo 13.

## Estado editorial

O avanço solicitado confirma a aprovação de leitura do capítulo 13. Essa aprovação não é classificação de domínio prático e não registra horas ou laboratórios que o mantenedor não relatou. O capítulo 14 permanece em primeira leitura; revisão técnica independente pendente.
