# Estrutura do repositório e numeração

[← Editorial](README.md) · [Índice do livro](../book/README.md) · [Sumário mestre](master-outline.md)

## Regra central

**Módulos agrupam; capítulos mantêm numeração global; subcapítulos usam o número do capítulo.**

O caminho do manuscrito é `book/modulo-M/capitulo-N/`, sem acentos e sem zeros à esquerda nos diretórios. O Módulo I reúne os capítulos 1–5 no planejamento atual. O Módulo II começa no capítulo 6, e não em um novo capítulo 1. As faixas completas pertencem ao sumário mestre e não são limites de tamanho da obra.

## Organização

- `book/README.md`: índice geral de leitura.
- `book/glossario.md` e `book/bibliografia.md`: recursos compartilhados pela obra.
- `book/modulo-M/README.md`: abertura, objetivo, capítulos e situação do módulo.
- `book/modulo-M/capitulo-N/README.md`: abertura e índice do capítulo; pode conter o texto integral quando a divisão não acrescentar clareza.
- `book/modulo-M/capitulo-N/N.1-assunto.md`: uma unidade de leitura, quando necessária.
- `referencias.md` e `solucoes.md`: permanecem junto ao capítulo que documentam, quando existentes.
- `editorial/`, `research/`, `labs/` e `assets/`: mantêm suas funções fora de `book/`.

Diretórios de capítulos e módulos futuros são criados com conteúdo, não como uma coleção de pastas vazias. A ausência de um capítulo não renumera os seguintes nem autoriza declarar o módulo concluído.

## Numeração e mudanças

Um capítulo não muda de número só porque passou para outro módulo. Mudanças de numeração ou divisão de capítulos já publicados precisam de decisão editorial explícita e atualização dos índices e referências. A estrutura fina continua flexível; o sumário mestre orienta a ordem de leitura.

Não ordene capítulos por comparação alfabética dos diretórios: `capitulo-10` pode aparecer antes de `capitulo-2` nessa ordenação. Utilize a ordem dos índices e os números dos capítulos ao preparar uma futura geração do livro.

## Navegação relativa

Dentro de um capítulo neste nível de diretório:

| Destino | Caminho relativo |
| --- | --- |
| Índice do próprio capítulo | `README.md` |
| Outra seção do mesmo capítulo | `N.2-assunto.md` |
| Índice do módulo | `../README.md` |
| Índice geral do livro | `../../README.md` |
| Bibliografia geral | `../../bibliografia.md` |
| Página inicial do projeto | `../../../README.md` |
| Registro de revisão do capítulo | `../../../editorial/reviews/capitulo-N.md` |

Um capítulo vizinho no mesmo módulo pode usar `../capitulo-X/README.md`. Entre módulos, o caminho deve incluir o módulo de destino; não presuma que o próximo capítulo esteja no mesmo diretório pai. Preserve também os fragmentos `#s1`, `#r2` e outras âncoras ao atualizar links.

## Migração desta estrutura

Base: commit `76757c2a462ce27ccadb04512875c01afb79e718`.

Os 15 arquivos dos capítulos 1, 2, 3 e 5 foram realocados do nível diretamente abaixo de `book/` para `book/modulo-1/`. Não havia manuscrito do capítulo 4 nessa base. Nenhum capítulo foi renumerado, encerrado, reescrito ou criado para preencher a lacuna.

A migração inclui o índice do Módulo I, a atualização dos índices gerais, referências relativas, bibliografia e documentos editoriais. Glossário, licenças, referências externas e textos dos capítulos mantêm seu conteúdo. A movimentação e os ajustes são publicados juntos, sem um estado intermediário na branch principal.

Links antigos para arquivos movidos precisam usar o novo caminho. O endereço da raiz do repositório permanece igual. Não se presume redirecionamento automático de URLs antigas, e não são mantidas cópias duplicadas do manuscrito nos diretórios anteriores. O histórico continua acessível nos commits anteriores.

Esta é uma alteração de organização e navegação. Ela não constitui revisão técnica do conteúdo, validação de laboratórios, fechamento de módulo ou geração de PDF.
