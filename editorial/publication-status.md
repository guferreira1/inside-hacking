# Estado editorial e critérios de publicação

**Atualização:** 24 de setembro de 2026.

[← Página inicial](../README.md) · [Índice de leitura](../book/README.md)

## O que os estados significam

| Estado | Significado | O que não significa |
| --- | --- | --- |
| DRAFT | Texto em desenvolvimento, disponível para primeira leitura. | Conteúdo integralmente verificado. |
| REVIEW | Texto aberto a revisão factual, técnica e didática, com pendências registradas. | Certificação, revisão independente concluída ou ausência de erros. |
| VALIDATED | Ciclo de revisão interna concluído para a versão indicada, com critérios aplicáveis de fontes, redação, exercícios e reprodução documentados. | Revisão independente, edição estável do livro ou validade universal em qualquer ambiente ou versão. |
| RELEASED | Conteúdo incluído em uma edição identificada e com artefatos conferidos. | Que a tecnologia não possa mudar depois. |

Uma leitura aprovada confirma uma experiência de leitura; não substitui auditoria factual. Uma revisão feita pela mesma IA que redigiu o texto não é revisão independente. Laboratório não é requisito universal: capítulos conceituais podem ser verificados por fontes, raciocínio e revisão dos exemplos, sem alegar execução.

**Fechamento interno e publicação de uma edição são marcos diferentes.** VALIDATED registra revisão interna documentada. Não transforma a leitura do mantenedor em revisão especializada nem dispensa revisão independente na preparação de uma edição estável. Os limites ficam registrados, em vez de declarar uma validação externa que não ocorreu.

## Situação dos capítulos

| Capítulo | Situação | Pendências e limites |
| --- | --- | --- |
| 1 | REVIEW; primeira leitura recebida | Associar fontes às afirmações; concluir a revisão factual e técnica. Navegação e terminologia foram ajustadas na auditoria anterior, sem encerrar o capítulo. |
| 2 | VALIDATED — versão editorial 1.0; revisão interna concluída | Fontes relacionadas aos trechos, telefonia verificada, redação corrigida e oito respostas comentadas. Revisão histórica independente não realizada; permanece etapa da edição estável. [Registro](reviews/capitulo-2.md). |
| 3 | VALIDATED — versão editorial 1.0; revisão interna concluída | Primeira leitura concluída; fontes e soluções presentes. Revisão jurídica especializada e revisão independente pendentes para edição estável. [Registro](reviews/capitulo-3.md). |
| 4 | VALIDATED — versão editorial 1.0; leitura aprovada em 24/09/2026 | Fontes S1–S9 e seis respostas reconferidas; cenário fictício. Sem execução de laboratório alegada; revisão independente pendente. [Registro](reviews/capitulo-4.md). |
| 5 | VALIDATED — versão editorial 1.0; leitura aprovada em 24/09/2026 | Fontes S1–S12 e relações entre conceitos reconferidas. Exemplos fictícios; nenhuma medição de risco ou exploração alegada. Revisão independente pendente. [Registro](reviews/capitulo-5.md). |
| 6 | VALIDATED — versão editorial 1.0; retorno favorável em 24/09/2026 | Quatro seções e oito respostas reconferidas; fontes S1–S8 e cinco testes de exemplos numéricos. Revisão técnica independente pendente. [Registro](reviews/capitulo-6.md). |
| 7 | VALIDATED — versão editorial 1.0; retorno favorável em 24/09/2026 | Cinco seções e nove respostas relidas; fontes S1–S16 e quatro testes de modelos delimitados. Sem benchmark ou alteração de hardware; revisão independente pendente. [Registro](reviews/capitulo-7.md). |
| 8 | VALIDATED — versão editorial 1.0; retorno favorável em 24/09/2026 | Cinco seções e nove respostas relidas; rastreabilidade S1–S14 e testes próprios preservados. Linux/GCC e Python como contextos delimitados; revisão independente pendente. [Registro](reviews/capitulo-8.md). |
| 9 | DRAFT 0.1 — primeira entrega de leitura | Cinco seções, dez questões e soluções, fontes S1–S18 e sete testes. Seis modelos e um exemplo Linux de mapeamentos; leitura e revisão independente pendentes. [Registro](reviews/capitulo-9.md). |

As aprovações dos capítulos 4 a 8 registram os retornos informados pelo mantenedor. Não foram informados duração das sessões, respostas aos exercícios ou execução de ferramentas pelo leitor; esses resultados não foram presumidos. A validação editorial não é uma classificação de domínio prático do leitor. Testes executados pela equipe para verificar exemplos são registrados separadamente.

As antigas anotações genéricas de “fact-check primário concluído” não constituem auditoria integral. O capítulo 1 mantém suas próprias pendências; a conclusão de outro capítulo não o promove automaticamente.

## Continuidade dos módulos

O capítulo 5 foi produzido antes do 4. A lacuna foi resolvida com a primeira redação do [Capítulo 4](../book/modulo-1/capitulo-4/README.md), não com a recuperação de um texto anterior. Sua leitura e a do 5 foram aprovadas.

O [Módulo I](../book/modulo-1/README.md) possui os cinco textos e leitura inicial aprovada. Seu fechamento interno ainda depende do capítulo 1. Não foi criada uma release ou publicação de encerramento do módulo.

No [Módulo II](../book/modulo-2/README.md), os capítulos [6](../book/modulo-2/capitulo-6/README.md), [7](../book/modulo-2/capitulo-7/README.md) e [8](../book/modulo-2/capitulo-8/README.md) encerraram seus ciclos internos da versão 1.0. O [Capítulo 9](../book/modulo-2/capitulo-9/README.md) está disponível em primeira entrega. Abrir a próxima unidade não apaga pendências anteriores. O capítulo 10 continua planejado, sem manuscrito nesta entrega.

## Organização por módulos

Os capítulos ficam em `book/modulo-M/capitulo-N/`, conforme o [guia de estrutura](repository-structure.md). Cada módulo possui índice e estado próprios. A numeração dos capítulos é global, sem reinício por módulo.

A migração anterior de diretórios não alterou o conteúdo nem o estado editorial dos capítulos. As mudanças de conteúdo e os fechamentos são registrados em suas próprias entregas. Atualizações do glossário acompanham cada novo capítulo, conforme a [política de terminologia](glossary-policy.md).

## Publicação e comunidade

O repositório recebe leitura, feedback público e propostas de alteração por pull request. O licenciamento foi definido: **CC BY-SA 4.0 para conteúdo editorial e ilustrações originais; MIT para código e exemplos de código**, conforme [LICENSE.md](../LICENSE.md). Contribuições passam pelos critérios de revisão e autoria de [CONTRIBUTING.md](../CONTRIBUTING.md).

Os templates de feedback foram preservados. A divulgação deve descrever uma obra em construção, sem prometer o número final de capítulos ou afirmar que laboratórios e PDF já foram entregues. Correções posteriores podem reabrir uma revisão e gerar uma nova versão identificada.

As publicações de continuidade planejadas no LinkedIn usarão o fechamento editorial de módulos como marco, sem periodicidade diária obrigatória. Leitura pessoal, fechamento de capítulo e fechamento de módulo são registros diferentes; esta entrega não cria automação nem publica no LinkedIn.

## Próximas unidades de trabalho

1. Receber a primeira leitura do Capítulo 9, com atenção à distinção entre página, região e objeto.
2. Concluir as pendências factuais do Capítulo 1 antes de fechar o Módulo I e preparar seu post de marco.
3. Prosseguir depois para o Capítulo 10 — Arquivos, formatos, codificação e serialização.
4. Incorporar revisão independente e, onde aplicável, jurídica especializada à preparação da primeira edição estável.
5. Planejar a primeira geração de PDF e conferir sua apresentação antes de anunciar uma release, incluindo os avisos das licenças e os créditos aplicáveis.

Estas são tarefas editoriais, não automações de trabalho futuro.
