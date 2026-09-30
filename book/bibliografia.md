# Bibliografia e referências

A bibliografia é construída junto com o manuscrito.

As fontes servem para verificar fatos, especificações, contexto histórico e resultados de pesquisas. O texto da obra permanece autoral: referências não substituem compreensão, experimentação nem explicação própria.

**Data desta revisão bibliográfica:** 29 de setembro de 2026.

## Capítulo 1 — O que é hacking?

- Tech Model Railroad Club (MIT). *TMRC — Hackers*. https://tmrc.mit.edu/old/hackers-ref.html
- Tech Model Railroad Club (MIT). *A Brief History of the Tech Model Railroad Club*. https://tmrc.mit.edu/old/history/index.html
- Tech Model Railroad Club (MIT). *TMRC @ Building 20*. https://tmrc.mit.edu/old/bldg20.html
- Shirey, R. *Internet Security Glossary, Version 2*. RFC 4949. RFC Editor, 2007. https://www.rfc-editor.org/rfc/rfc4949
- Raymond, Eric S. (ed.). *The New Hacker's Dictionary*. 3rd ed. MIT Press, 1996.
- NIST Computer Security Resource Center. *Hacker — Glossary*. https://csrc.nist.gov/glossary/term/hacker

### Nota editorial

As fontes não adotam uma definição única de *hacker*. A RFC 4949 registra sentidos históricos distintos, enquanto a definição agregada pelo glossário atual do NIST/CNSSI enfatiza acesso não autorizado. Essa divergência é tratada explicitamente no capítulo, e não resolvida artificialmente escolhendo uma definição como universal.

## Capítulo 2 — Da curiosidade à segurança ofensiva

As referências completas e a delimitação dos trechos utilizados estão em [Referências e limites da pesquisa do Capítulo 2](modulo-1/capitulo-2/referencias.md). Os identificadores R1–R14 aparecem junto às afirmações correspondentes no manuscrito.

A revisão reúne o relato do TMRC publicado no MIT e o dicionário do clube; documentação técnica do Bell System sobre sinalização; um relato retrospectivo de Steve Wozniak; a RFC 1135 e o histórico do SEI sobre o Morris Worm e o CERT/CC; o relatório Ware e o registro da NBS TN 827 sobre segurança anterior a 1988; além de referências metodológicas, de divulgação, Web e IA para as conexões introdutórias do capítulo.

A rastreabilidade da seção de telefonia foi concluída nesta rodada: os mecanismos são associados à documentação técnica e o episódio do apito é atribuído a um relato pessoal. Não se apresenta um participante como fundador de cybersecurity nem se generaliza a sinalização histórica para redes atuais.

A consulta das fontes não equivale a revisão histórica independente. O [registro de fechamento interno](../editorial/reviews/capitulo-2.md) documenta a versão editorial 1.0, as correções e os limites da validação. Não houve execução de ataques ou reprodução dos episódios históricos.

## Capítulo 3 — Ética, legalidade, autorização e escopo

As referências desta entrega estão em [Fontes e notas de pesquisa do Capítulo 3](modulo-1/capitulo-3/referencias.md), com identificadores utilizados ao longo do texto, localização dos trechos pertinentes, data de consulta e limites da revisão.

Incluem PTES, política de divulgação do get.gov/CISA, política de pentest da AWS, RFC 9116, documentação de safe harbor da HackerOne, art. 154-A do Código Penal brasileiro e artigos pertinentes da LGPD. São fontes de mecanismos e regras específicos, não endosso institucional à obra.

Os exemplos Aurora são fictícios e não representam execuções reais. A discussão jurídica permanece educacional e pendente de revisão especializada.

## Capítulo 4 — Como pensar como investigador de segurança

As [fontes S1–S9 e seus limites](modulo-1/capitulo-4/referencias.md) sustentam os conceitos de autorização, planejamento experimental, interações entre fatores, associação e causalidade, falsos positivos e negativos, códigos HTTP, cache e registros de eventos.

Foram consultados trechos do NIST/SEMATECH e-Handbook, verbetes do NIST CSRC, as RFCs 9110 e 9111 e páginas da OWASP Cheat Sheet Series. O enredo Aurora, as comparações e as decisões são construções didáticas originais. Não houve laboratório executável, medição ou exploração real.

A leitura foi aprovada e a revisão interna concluída em 24/09/2026, na versão editorial 1.0. O [registro editorial](../editorial/reviews/capitulo-4.md) identifica o que foi reconferido e os limites remanescentes; consulta de fontes e aprovação de leitura não constituem revisão independente.

## Capítulo 5 — Ameaças, vulnerabilidades, exploits, risco e superfície de ataque

As [fontes S1–S12](modulo-1/capitulo-5/referencias.md) identificam verbetes do NIST, documentação OWASP, definição de CWE e terminologia do Metasploit. O guia CVSS v4.0 da FIRST sustenta a distinção entre severidade Base e avaliação de risco. Cada fonte tem seu uso delimitado; consultas a glossários não são apresentadas como leitura integral das publicações que eles citam.

A narrativa usa situações fictícias para conectar definições, condições de exploração, exposição e consequências. Não houve exploração executada, medição de probabilidade, cálculo CVSS ou revisão independente. O [fechamento interno](../editorial/reviews/capitulo-5.md) da versão editorial 1.0 foi registrado após a leitura aprovada em 24/09/2026; o Módulo I mantém a pendência do capítulo 1.

## Capítulo 6 — Bits, bytes e representação da informação

As [fontes S1–S8](modulo-2/capitulo-6/referencias.md) relacionam notas do curso Computation Structures, a página de unidades do NIST, as RFCs 20 e 3629, a documentação de conversões de inteiros do Python e materiais do Unicode Consortium.

As explicações constroem representação binária e hexadecimal, largura e sinal de inteiros, ordem de bytes, unidades e codificação de texto. As contas e sequências usadas como exemplos foram conferidas por [testes editoriais](../scripts/tests/test_chapter6_examples.py). Esses testes verificam os exemplos, não substituem revisão independente nem representam laboratório ofensivo.

O ciclo interno da versão editorial 1.0 foi concluído após retorno favorável do mantenedor e reconferência das quatro seções, fontes e respostas. O [registro da revisão](../editorial/reviews/capitulo-6.md) preserva os limites da verificação e a pendência de revisão independente.

## Capítulo 7 — Hardware: CPU, memória, armazenamento e dispositivos

As [fontes S1–S16](modulo-2/capitulo-7/referencias.md) relacionam o curso Computation Structures, documentação de CPU da Intel, materiais de armazenamento da Kingston, guias do kernel Linux, documentação de segurança da Microsoft, verbetes do NIST e o modelo de programação da NVIDIA.

Seu uso é delimitado: mecanismos de processamento e hierarquia, tradução de endereços, confirmação de escrita, DMA, firmware e estágios de inicialização. Não foram importados benchmarks, recomendações de compra ou garantias de segurança integral. Tentativas sem conteúdo recuperável da especificação UEFI não foram registradas como leitura da especificação.

A narrativa do editor e as contas são originais. Quatro [testes de conferência](../scripts/tests/test_chapter7_examples.py) tratam apenas dos modelos numéricos e de endereço, não de desempenho ou proteção de equipamentos reais. Após o retorno favorável do mantenedor e a reconferência interna de texto, respostas e limites das fontes, o ciclo editorial da versão 1.0 foi encerrado. O [registro editorial](../editorial/reviews/capitulo-7.md) preserva a pendência de revisão independente.

## Capítulo 8 — Como um programa se torna execução

As [fontes S1–S14](modulo-2/capitulo-8/referencias.md) relacionam documentação GCC e GNU, ELF, Linux man-pages, formato PE e convenções binárias da Microsoft, uma interface LSB, materiais da Python Software Foundation e a especificação JVM Java SE 25.

O percurso distingue código-fonte, artefatos, pré-processamento, compilação, montagem, ligação, carregamento e contexto de execução. Interpretadores e runtimes são explicados sem impor uma divisão absoluta entre linguagens compiladas e interpretadas.

Os [três arquivos C](modulo-2/capitulo-8/exemplos/README.md) e os [nove testes editoriais](../scripts/tests/test_chapter8_examples.py) são autorais. A execução realizada em Linux/GCC e Python é delimitada; Windows, JVM, permissões especiais e todos os detalhes de carregamento não foram reproduzidos. Após retorno favorável e releitura interna, a versão editorial 1.0 foi encerrada, conforme seu [registro de revisão](../editorial/reviews/capitulo-8.md). Revisão independente continua pendente.

## Capítulo 9 — Memória, processos e arquitetura de computadores

As [fontes S1–S18](modulo-2/capitulo-9/referencias.md) relacionam documentação de memória e processos do Linux, descrições de proteção da Microsoft, alocação e quadros de chamada GNU, concorrência em CWE/GCC/LLVM, uma reprodução identificada de POSIX e interfaces Python.

As explicações usam modelos próprios de endereços, objetos, residência e intercalamento. Os [sete testes](../scripts/tests/test_chapter9_examples.py) incluem seis conferências de modelos e um [exemplo Linux](modulo-2/capitulo-9/exemplos/README.md) que verifica valores visíveis em mapeamentos privados e compartilhados. Não foram observados quadros físicos nem medidos faults, RSS/PSS, swap ou eficácia de proteções.

Após retorno favorável e releitura interna das cinco seções e respostas, o ciclo editorial da versão 1.0 foi encerrado. O [registro editorial](../editorial/reviews/capitulo-9.md) delimita a reconferência de pontos centrais e mantém os limites da execução e da revisão independente.

## Capítulo 10 — Arquivos, formatos, codificação e serialização

As [fontes S1–S18](modulo-2/capitulo-10/referencias.md) relacionam interfaces Linux, RFCs sobre representações e formatos, materiais W3C e Unicode, especificações YAML e Protobuf, documentação Python e orientações OWASP/CWE.

O registro Livro/3 e o formato AUR v1 são criações didáticas. Seis seções separam nomes, bytes, formatos, transformações, serialização, parsing, validação e integridade. Não foi implementado um parser PNG/XML/YAML/Protobuf nem um canonicalizador JCS; essas referências sustentam comparações introdutórias.

O [codec AUR/JSON](modulo-2/capitulo-10/exemplos/README.md) e os [23 testes](../scripts/tests/test_chapter10_examples.py) verificam casos pequenos e próprios, incluindo entradas inválidas. Após aprovação de leitura, reconferência editorial e auditoria de conjunto do Módulo II, o capítulo encerrou seu ciclo interno como versão editorial 1.0. Seu [registro editorial](../editorial/reviews/capitulo-10.md) preserva ambiente, limites e verificações. Isso não equivale a revisão independente nem a uma edição em PDF.

## Capítulo 11 — O papel de um sistema operacional

As [fontes S1–S14](modulo-3/capitulo-11/referencias.md) relacionam documentação Debian, Linux, Microsoft, seL4, Python, systemd e OWASP. O percurso distingue abstrações, núcleo e espaço de usuário, chamadas de sistema, espera, recursos, contexto de segurança e ciclo de vida de serviços.

As páginas systemd efetivamente consultadas são reproduções identificadas de sua documentação no man7. A comparação de microkernel é introdutória; não houve instalação de seL4, Windows ou configuração de isolamento. O caso Aurora e os modelos de duração e dependência são autorais e fictícios.

O [exemplo opcional](modulo-3/capitulo-11/exemplos/README.md) usa somente arquivos temporários próprios para distinguir leitura, fim de arquivo e erros de operação. Os [seis testes](../scripts/tests/test_chapter11_examples.py) incluem três verificações desse exemplo e três de modelos conceituais. Não demonstram política entre contas nem medem chamadas de sistema ou desempenho. A leitura foi aprovada e o ciclo interno da versão editorial 1.0 foi encerrado em 29/09/2026, conforme seu [registro editorial](../editorial/reviews/capitulo-11.md). Revisão independente permanece pendente.

## Capítulo 12 — Linux por dentro

As [fontes S1–S19](modulo-3/capitulo-12/referencias.md) relacionam documentação do kernel, Linux man-pages, Debian, FHS, systemd, kmod, util-linux e Python. Delimitam composição da instalação, árvore de nomes, montagens, interfaces de estado, dispositivos, módulos e pacotes. O percurso Debian/APT não é generalizado para todas as distribuições; convenções FHS e merged-/usr são identificadas por suas fontes.

O cenário de visibilidade do catálogo é fictício. O [exemplo opcional](modulo-3/capitulo-12/exemplos/README.md) consulta somente um descritor do próprio processo, sobre arquivo temporário próprio. Os [quatro testes](../scripts/tests/test_chapter12_examples.py) conferem plataforma, metadados/leitura, limpeza e saída documentada; não demonstram uma política entre identidades nem compartilhamento de posição entre aberturas.

O capítulo tem leitura aprovada e revisão interna 1.0 concluída, conforme seu [registro editorial](../editorial/reviews/capitulo-12.md). Não houve montagem, instalação, administração de serviços, carga de módulos ou leitura de processos alheios. Revisão técnica independente permanece pendente.

## Capítulo 13 — Windows por dentro

As [44 referências do capítulo](modulo-3/capitulo-13/referencias.md) usam documentação primária da Microsoft para arquitetura, objetos, caminhos, PE/DLL, contas e tokens, Registro, serviços e eventos. A narrativa é fictícia; não houve reprodução de kernel, UAC, Registro ou SCM. Leitura aprovada e ciclo interno da versão 1.0 concluído, com [limites registrados](../editorial/reviews/capitulo-13.md).

## Capítulo 14 — Terminal, shells e automação

As [49 referências numeradas](modulo-3/capitulo-14/referencias.md) usam documentação GNU, Linux man-pages, Microsoft e Python. [Quatro scripts próprios](modulo-3/capitulo-14/exemplos/README.md) e os testes associados examinam argumentos, expansão, fluxos, status, escopos e validação. [O registro editorial](../editorial/reviews/capitulo-14.md) separa documentação consultada, execuções reais e limitações de plataforma. Leitura aprovada e ciclo interno da versão editorial 1.0 concluído; revisão independente pendente.

## Capítulo 15 — Usuários, grupos, permissões e privilégios

As [47 referências numeradas](modulo-3/capitulo-15/referencias.md) relacionam documentação Linux man-pages, Linux ACL, GNU, shadow-utils, util-linux, sudo, kernel, Microsoft, Python e OWASP. Sete seções desenvolvem identidades, operações, criação e ACLs, tokens e direitos Windows, delegação, camadas, revogação e investigação. Os modelos de acesso Linux e Windows são distinguidos.

O [exemplo opcional](modulo-3/capitulo-15/exemplos/README.md) observa somente arquivos temporários do próprio usuário comum em Linux. Os nove testes separam três verificações de modelo/guarda e seis de operações reais e limpeza. Não houve administração de contas, ACLs ou privilégios, nem execução dos controles Windows. O [registro editorial](../editorial/reviews/capitulo-15.md) preserva ambientes, resultados e limites; o capítulo está em VALIDATED 1.0, com leitura aprovada e limites de revisão independente preservados.

## Capítulo 16 — Processos, serviços, logs e persistência de estado

As [44 referências](modulo-3/capitulo-16/referencias.md) relacionam documentação Linux, systemd, procps-ng, Cronie, logrotate, Microsoft, Python, SQLite e OWASP. As reproduções de manuais são identificadas; não se confunde versão documental com ambiente executado.

Os [dois exemplos próprios](modulo-3/capitulo-16/exemplos/README.md) e os [14 testes](../scripts/tests/test_chapter16_examples.py) separam inicialização, término, diagnóstico, efeito confirmado e resposta ausente. O exemplo SQLite usa apenas um banco temporário e interrupções de processo em dois pontos conhecidos, sem simular falha de energia ou sistema distribuído. O capítulo permanece DRAFT 0.1; [registro editorial](../editorial/reviews/capitulo-16.md) e [auditoria](../editorial/audits/2026-09-29-capitulo-16.md) delimitam fontes, execuções e revisão.

## Política de referências

URLs e datas de consulta serão preservadas para recursos Web. Quando houver especificação, norma, RFC, artigo acadêmico ou publicação original disponível, ela deve ser preferida a resumos secundários.

Referências serão revisadas novamente antes de cada release do livro para identificar links quebrados, documentos substituídos e versões mais atuais. As pendências de cada capítulo estão no [controle editorial](../editorial/publication-status.md).
