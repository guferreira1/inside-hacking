# Matriz de cobertura

**Status:** cobertura inicial dos capítulos disponíveis; atualização em 24/09/2026.

[Editorial](README.md) · [Sumário mestre](master-outline.md) · [Estado editorial](publication-status.md)

A matriz relaciona conteúdos efetivamente desenvolvidos, sua profundidade e o que continua em aberto. Uma referência a uma técnica em uma introdução não significa que seu mecanismo completo ou um laboratório já foi entregue. O sumário mestre mantém o planejamento amplo; esta matriz começa pela cobertura concreta dos módulos em produção.

## Campos de acompanhamento

| Campo | Finalidade |
| --- | --- |
| ID | Identificador estável do grupo de cobertura. |
| Tema e categoria | Fundamento, vulnerabilidade, técnica, ferramenta, defesa etc. |
| Pré-requisitos | Conhecimentos necessários, conforme o capítulo. |
| Teoria | Onde o mecanismo é explicado. |
| Aplicação | Onde é demonstrado, exercitado ou reproduzido, quando aplicável. |
| Defesa | Onde prevenção, detecção ou mitigação são discutidas. |
| Profundidade | Introdução, desenvolvimento intermediário ou aprofundamento. |
| Fontes e validação | Referências e registro editorial; não é certificação do leitor. |
| Gap | Pendência ou conteúdo ainda não desenvolvido. |

## Módulo I — Hacking, segurança e método

| ID | Tema / teoria disponível | Aplicação e defesa | Profundidade / fonte e limite |
| --- | --- | --- | --- |
| M01-01 | [Significado de hacking e ferramentas](../book/modulo-1/capitulo-1/README.md) | Exemplos conceituais e perguntas; distinção entre capacidade e permissão. | Introdução. Revisão factual própria ainda aberta no [controle](publication-status.md). Nenhuma prática de ferramentas entregue. |
| M01-02 | [História da cultura hacker](../book/modulo-1/capitulo-2/README.md) | Telefonia histórica, incidentes e resposta coordenada explicados, não reproduzidos. | Introdução; [fontes R1–R14](../book/modulo-1/capitulo-2/referencias.md). Revisão interna encerrada, revisão histórica independente pendente. |
| M01-03 | [Autorização, escopo e evidências](../book/modulo-1/capitulo-3/README.md) | Cenário Aurora, decisões e soluções; limites de coleta e divulgação. | Introdução operacional e jurídica; [fontes](../book/modulo-1/capitulo-3/referencias.md). Revisão jurídica especializada pendente. |
| M01-04 | [Raciocínio investigativo](../book/modulo-1/capitulo-4/README.md) | Comparações fictícias, hipóteses concorrentes, resultado negativo, questões e soluções. | Desenvolvimento conceitual; [fontes S1–S9](../book/modulo-1/capitulo-4/referencias.md). Sem laboratório executável ou medição. |
| M01-05 | [Ativos, ameaças, exploração e risco](../book/modulo-1/capitulo-5/README.md) | Cenários de autorização e exposição; controle de causa, consequências e limites. | Fundamentos; [fontes S1–S12](../book/modulo-1/capitulo-5/referencias.md). Não há cálculo CVSS, medição de probabilidade ou exploração real. |

## Módulo II — Computadores por dentro

Pré-requisito editorial: leitura introdutória e disposição para acompanhar exemplos; não é exigida programação. O capítulo 7 utiliza as representações e unidades construídas no 6.

| ID | Tema / teoria disponível | Aplicação e defesa | Profundidade / fonte e limite |
| --- | --- | --- | --- |
| M02-01 | [Bits, bases e unidades](../book/modulo-2/capitulo-6/README.md) | Contas explicadas e testes de conversões. Distingue capacidade de imprevisibilidade, largura de interpretação. | Fundamentos; [fontes S1–S8](../book/modulo-2/capitulo-6/referencias.md). Revisão interna 1.0. Não ensina circuitos completos ou segurança de chaves. |
| M02-02 | [Texto e interpretação](../book/modulo-2/capitulo-6/6.4-texto-e-interpretacao.md) | ASCII, UTF-8, pontos de código, agrupamentos e cortes; exemplos conferidos. | Introdução a codificações. Não implementa decodificador, normalização completa ou parser seguro. |
| M02-03 | [CPU e componentes](../book/modulo-2/capitulo-7/README.md) | Percurso didático do editor, ciclo de instrução, clock, núcleo, ISA e microarquitetura. | Introdução funcional; [fontes S1–S16](../book/modulo-2/capitulo-7/referencias.md). DRAFT, não benchmark nem projeto de CPU. |
| M02-04 | [Hierarquia de memória](../book/modulo-2/capitulo-7/7.3-memoria-e-cache.md) | RAM, cache, endereço/conteúdo e média hipotética; separa MMU e representação física. | Fundamentos. Memória virtual, processos e permissões ainda exigem aprofundamento no capítulo 9. |
| M02-05 | [Armazenamento e dispositivos](../book/modulo-2/capitulo-7/7.4-armazenamento-e-persistencia.md) | Persistência, interfaces e controles de escrita; [DMA e firmware](../book/modulo-2/capitulo-7/7.5-dispositivos-e-firmware.md). | Introdução. Sem ensaio de energia, driver, configuração de firmware ou exploração de hardware. |

## Cobertura ainda planejada

A matriz continuará a detalhar redes e sistemas, reconhecimento, autenticação, ataques a credenciais, Web, APIs, injeções, autorização, lógica de negócio, infraestrutura, Linux, Windows, Active Directory, cloud, containers, supply chain, exploração de software, pós-exploração, escalada de privilégios, persistência, pivotamento, movimentação lateral, segurança de IA, redes sem fio, mobile, IoT, privacidade, dark web, OSINT, investigação e defesa.

Esses temas pertencem ao planejamento, não são capítulos concluídos por aparecerem nesta lista. Os capítulos 8–10 e demais módulos não recebem linhas de cobertura efetiva antes da produção do texto. A matriz não afirma completude e não substitui os registros específicos de revisão.
