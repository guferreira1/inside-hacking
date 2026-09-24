# Capítulo 6 · Referências e limites da pesquisa

[← Capítulo](README.md) · [Bibliografia geral](../../bibliografia.md)

**Consulta e reconferência:** 24/09/2026. **Versão editorial:** VALIDATED 1.0 — revisão interna; revisão independente pendente.

As explicações e contas são autorais. Não foram copiados diagramas ou tabelas de terceiros. Os exemplos de estados de livros, contadores e limites de campos são construções didáticas. As conversões numéricas e de texto possuem testes no repositório; isso não representa teste de um alvo nem revisão independente do capítulo.

<a id="s1"></a>
## S1 · Informação e representação de inteiros

*Computation Structures*. Notas “Information”, especialmente representações de tamanho fixo, números inteiros sem sinal e seção 3.2.1.2, Two's Complement Representation.

https://computationstructures.org/notes/information/notes.html

Uso: bit, representação posicional, grupos de quatro bits e complemento de dois. As contas de 13, 173, 255 e −1 foram desenvolvidas para o livro. A seção de capacidade não atribui entropia ou resistência criptográfica somente à largura de um campo; não foi aplicado um modelo probabilístico.

<a id="s2"></a>
## S2 · Abstração digital

*Computation Structures*. Notas “The Digital Abstraction”, descrição da representação de valores discretos por grandezas físicas e condições de validade.

https://computationstructures.org/notes/digitalabstraction/notes.html

Uso: separar valores lógicos de sua implementação física. Não foram extraídas medições dos gráficos nem construído um circuito. O capítulo não fixa tensões universais nem trata a analogia das placas como descrição literal de memória.

<a id="s3"></a>
## S3 · Bytes e prefixos de unidades

NIST. *Prefixes for binary multiples*, quadro de exemplos e comparações com prefixos SI.

https://physics.nist.gov/cuu/Units/binary.html

Uso: byte de oito bits; distinção entre prefixos decimais e binários. As conversões de unidades foram recalculadas. Comentários históricos sobre fabricantes na página não foram generalizados como descrição atual de todos os produtos.

<a id="s4"></a>
## S4 · UTF-8

YERGEAU, François. *UTF-8, a transformation format of ISO 10646*. RFC 3629, novembro de 2003. Seções 1–4 e 10. DOI: 10.17487/RFC3629.

https://www.rfc-editor.org/rfc/rfc3629

Uso: octetos, preservação de ASCII, sequências de um a quatro bytes e rejeição de sequências inválidas. A apresentação é introdutória, não uma implementação completa de decodificador nem a descrição de todos os ataques de codificação.

<a id="s5"></a>
## S5 · Ordem de bytes e conversão de inteiros

Python Software Foundation. *Built-in Types*, documentação de `int.from_bytes` e `int.to_bytes`.

https://docs.python.org/3/library/stdtypes.html#int.from_bytes

Uso: ordem big-endian/little-endian e interpretação com ou sem sinal dos exemplos de dois bytes. As operações aparecem nos testes editoriais, não como conhecimento de Python exigido do leitor. O exemplo de retenção dos oito bits baixos é uma operação explicitamente definida, não uma generalização do comportamento de overflow em linguagens.

<a id="s6"></a>
## S6 · ASCII

CERF, Vint. *ASCII format for Network Interchange*. RFC 20, outubro de 1969. Seção 2 e tabela de códigos. DOI: 10.17487/RFC0020.

https://www.rfc-editor.org/rfc/rfc20.txt

Uso: código de sete bits, uso em byte de oito bits e correspondências de letras e dígitos. É documentação histórica do código, não recomendação de limitar sistemas modernos a ASCII.

<a id="s7"></a>
## S7 · Unicode e formas de codificação

Unicode Consortium. *FAQ — UTF-8, UTF-16, UTF-32 & BOM*. Perguntas gerais sobre representações Unicode e definição de UTF.

https://www.unicode.org/faq/utf_bom.html

Uso: distinguir ponto de código de sua representação em bytes. Não foram reproduzidas recomendações de desempenho ou estatísticas de uso da FAQ. Os valores dos exemplos de texto foram conferidos por conversão.

<a id="s8"></a>
## S8 · O caractere percebido pelo usuário

Unicode Consortium. *Unicode Standard Annex #29 — Unicode Text Segmentation*, introdução e seção sobre Grapheme Cluster Boundaries.

https://www.unicode.org/reports/tr29/

Uso: distinção entre pontos de código e agrupamentos percebidos como unidades de texto. O capítulo não implementa segmentação nem apresenta uma regra universal de um grafema por ponto de código. A comparação `U+00E9` versus `U+0065 U+0301` é um exemplo limitado, não uma explicação completa de normalização Unicode.

## Conferência dos exemplos

Os testes em [test_chapter6_examples.py](../../../scripts/tests/test_chapter6_examples.py) verificam bases numéricas, sinal, ordem de bytes, conversões de unidades e as sequências de texto usadas nesta versão. Sua execução na entrega inicial está registrada no [workflow do commit d148c59](https://github.com/guferreira1/inside-hacking/actions/runs/36071240309). O workflow de documentação os mantém na suíte das entregas seguintes.

O retorno favorável do mantenedor e a reconferência interna do texto, das fontes e das oito respostas foram registrados na [revisão editorial](../../../editorial/reviews/capitulo-6.md). Os testes verificam exemplos específicos. Não comprovam todas as possíveis interpretações de arquivos, a correção de sistemas de terceiros ou domínio prático do leitor. Revisão técnica independente permanece pendente.
