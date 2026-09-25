# Bibliografia e referências

A bibliografia é construída junto com o manuscrito.

As fontes servem para verificar fatos, especificações, contexto histórico e resultados de pesquisas. O texto da obra permanece autoral: referências não substituem compreensão, experimentação nem explicação própria.

**Data desta revisão bibliográfica:** 24 de setembro de 2026.

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

O capítulo permanece DRAFT 0.1, para primeira leitura. O [registro editorial](../editorial/reviews/capitulo-9.md) separa pesquisa, raciocínio, execução e limites da verificação.

## Política de referências

URLs e datas de consulta serão preservadas para recursos Web. Quando houver especificação, norma, RFC, artigo acadêmico ou publicação original disponível, ela deve ser preferida a resumos secundários.

Referências serão revisadas novamente antes de cada release do livro para identificar links quebrados, documentos substituídos e versões mais atuais. As pendências de cada capítulo estão no [controle editorial](../editorial/publication-status.md).
