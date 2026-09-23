# Estado editorial e critérios de publicação

**Atualização:** 23 de setembro de 2026.

[← Página inicial](../README.md) · [Índice de leitura](../book/README.md)

## O que os estados significam

| Estado | Significado | O que não significa |
| --- | --- | --- |
| DRAFT | Texto em desenvolvimento, disponível para primeira leitura. | Conteúdo integralmente verificado. |
| REVIEW | Texto aberto a revisão factual, técnica e didática, com pendências registradas. | Certificação, revisão independente concluída ou ausência de erros. |
| VALIDATED | Ciclo de revisão interna concluído para a versão indicada, com critérios aplicáveis de fontes, redação, exercícios e reprodução documentados. | Revisão independente, edição estável do livro ou validade universal em qualquer ambiente ou versão. |
| RELEASED | Conteúdo incluído em uma edição identificada e com artefatos conferidos. | Que a tecnologia não possa mudar depois. |

Uma leitura aprovada confirma uma experiência de leitura; não substitui auditoria factual. Uma revisão feita pela mesma IA que redigiu o texto não é revisão independente. Laboratório não é requisito universal: capítulos conceituais podem ser verificados por fontes, raciocínio e revisão dos exemplos, sem alegar execução.

**Fechamento interno e publicação de uma edição são marcos diferentes.** No Capítulo 2, VALIDATED registra a revisão interna factual/editorial documentada. Não transforma a leitura do mantenedor em revisão especializada nem dispensa revisão histórica independente na preparação de uma edição estável. Os limites ficam registrados, em vez de declarar uma validação externa que não ocorreu.

## Situação dos capítulos

| Capítulo | Situação | Pendências e limites |
| --- | --- | --- |
| 1 | REVIEW; primeira leitura recebida | Associar fontes às afirmações; verificar a redação de conceitos e ferramentas; revisão técnica independente pendente. |
| 2 | VALIDATED — versão editorial 1.0; revisão interna concluída | Fontes relacionadas aos trechos, telefonia verificada, redação corrigida e oito respostas comentadas. Sem laboratório executável aplicável. Revisão histórica independente não realizada; permanece etapa da edição estável. [Registro](reviews/capitulo-2.md). |
| 3 | VALIDATED — versão editorial 1.0; revisão interna concluída | Primeira leitura concluída; feedback de maior densidade registrado; fontes e soluções presentes. Revisão jurídica especializada e revisão independente permanecem pendentes para edição estável. [Registro](reviews/capitulo-3.md). |
| 4 | Manuscrito não localizado na main; leitura informada pelo mantenedor | Conciliar a entrega lida com os arquivos do repositório. Não foi atribuído DRAFT, VALIDATED ou fechamento a um arquivo ausente. |
| 5 | DRAFT 0.1 — primeira entrega de leitura | Três seções conceituais e fontes S1–S12. Exemplos fictícios, sem laboratório exigido ou execução alegada. Primeira leitura e revisão independente pendentes. |

As antigas anotações genéricas de “fact-check primário concluído” não constituem auditoria integral. No Capítulo 2, a anotação foi substituída por referências junto às afirmações e pelo registro desta revisão. O Capítulo 1 mantém suas próprias pendências; a conclusão de outro capítulo não o promove automaticamente.

## Reconciliação de continuidade

Na conferência da branch `main` no commit `eaf066222f8051f80900c22d6d340a5c4828d1d4`, os manuscritos existentes eram os capítulos 1, 2 e 3. A leitura do Capítulo 4 foi informada pelo mantenedor, mas `book/capitulo-4/README.md` não foi localizado e a listagem de branches retornou somente `main`. Isso é uma divergência entre relato de leitura e publicação, não uma conclusão de que a leitura não aconteceu.

A nova entrega atende à solicitação de avançar ao Capítulo 5 sem renumerar os conteúdos ou inventar a publicação do 4. O texto do 5 desenvolve suas definições sem depender de um link inexistente. **O Módulo I continua em produção:** o Capítulo 4 precisa ser disponibilizado/conferido, o 1 mantém pendências e o 5 está em primeira leitura.

## Publicação e comunidade

O repositório recebe leitura, feedback público e propostas de alteração por pull request. O licenciamento foi definido: **CC BY-SA 4.0 para conteúdo editorial e ilustrações originais; MIT para código e exemplos de código**, conforme [LICENSE.md](../LICENSE.md). Contribuições passam pelos critérios de revisão e autoria de [CONTRIBUTING.md](../CONTRIBUTING.md).

Os templates de feedback já existentes foram preservados. A divulgação deve descrever uma obra em construção, sem prometer o número final de capítulos ou afirmar que laboratórios e PDF já foram entregues. Correções posteriores podem reabrir uma revisão e gerar uma nova versão identificada.

As publicações de continuidade planejadas no LinkedIn usarão o fechamento editorial de módulos como marco, sem periodicidade diária obrigatória. Leitura pessoal, fechamento de capítulo e fechamento de módulo são registros diferentes; esta entrega não cria automação nem publica no LinkedIn.

## Próximas unidades de trabalho

1. Receber a leitura do Capítulo 5 e revisar sua clareza e precisão.
2. Resolver a divergência de publicação do Capítulo 4 antes de declarar o Módulo I concluído.
3. Concluir as pendências factuais do Capítulo 1.
4. Incorporar revisão técnica/histórica independente e, onde aplicável, jurídica especializada à preparação da primeira edição estável.
5. Planejar a primeira geração de PDF e conferir sua apresentação antes de anunciar uma release, incluindo os avisos das licenças e os créditos aplicáveis.

Estas são tarefas editoriais, não automações de trabalho futuro.
