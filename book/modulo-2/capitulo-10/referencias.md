# Capítulo 10 · Referências e limites da pesquisa

[← Capítulo](README.md) · [Bibliografia geral](../../bibliografia.md)

**Consulta:** 24/09/2026. **Versão:** DRAFT 0.1.

O formato AUR v1, o registro Livro/3, as situações da Aurora e os programas foram criados para a obra. As fontes verificam mecanismos e convenções; não fornecem um texto a ser recomposto nem endossam o livro. AUR não é um padrão externo. Os comportamentos de arquivos são delimitados ao Linux; as conversões executadas usam Python no ambiente identificado ao final.

<a id="s1"></a>
## S1 · Nomes, metadados e arquivos abertos

Linux man-pages project. *inode(7)*; *open(2)*, DESCRIPTION; *symlink(7)*, introdução; *unlink(2)*, DESCRIPTION.

https://man7.org/linux/man-pages/man7/inode.7.html

https://man7.org/linux/man-pages/man2/open.2.html

https://man7.org/linux/man-pages/man7/symlink.7.html

https://man7.org/linux/man-pages/man2/unlink.2.html

Uso em 10.1: classificação de arquivo, metadados, mtime/ctime, escopo de inode, hard links, links simbólicos e referência de arquivo aberto. O teste usa dois hard links e um descritor próprio em diretório temporário. Não generaliza inode como identidade permanente ou universal; não promete recuperação depois de fechar o arquivo. Não foram adotadas listas históricas de suporte a marcas de tempo como diagnóstico de todos os sistemas atuais.

<a id="s2"></a>
## S2 · Leitura e interfaces de texto

Linux man-pages project. *read(2)*, DESCRIPTION e RETURN VALUE.

https://man7.org/linux/man-pages/man2/read.2.html

Python Software Foundation. *io — Core tools for working with streams*, tipos de E/S e TextIOWrapper.

https://docs.python.org/3/library/io.html

Uso em 10.1: quantidade solicitada versus recebida, posição de leitura, fim de arquivo e transformações de texto. O retorno zero como fim foi delimitado a leitura de tamanho positivo num arquivo regular; não é uma descrição universal de todos os dispositivos. O teste de finais de linha utiliza BytesIO e uma configuração explícita de TextIOWrapper, não supõe que todo editor reescreva arquivos ao abri-los.

<a id="s3"></a>
## S3 · Tipo declarado e validação de arquivos

FIELDING, Roy; NOTTINGHAM, Mark; RESCHKE, Julian. *HTTP Semantics*. RFC 9110, seção 8.3, Content-Type, 2022.

https://www.rfc-editor.org/rfc/rfc9110.html#section-8.3

OWASP Cheat Sheet Series. *File Upload Cheat Sheet*, Content-Type Validation, File Signature Validation e Upload and Download Limits.

https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html

Uso em 10.2 e 10.6: tipo de mídia como metadado, distinção de extensão e assinatura e orçamento depois de descompressão. Não foi testada uma aplicação de upload nem apresentado um bypass. As orientações de defesa são introduções ao mecanismo, não uma implementação completa de armazenamento de arquivos recebidos.

<a id="s4"></a>
## S4 · Assinatura e estrutura de um formato existente

W3C. *Portable Network Graphics (PNG) Specification (Third Edition)*, seções 5.2–5.5 e definições de chunk e CRC.

https://www.w3.org/TR/png-3/

Uso em 10.2 e 10.6: assinatura de oito bytes, organização em chunks e verificação de corrupção. Não foram copiados diagramas ou códigos da especificação, nem implementado um decodificador PNG. O formato didático AUR não contém um campo CRC. Reconhecimento de formato não foi confundido com assinatura digital.

<a id="s5"></a>
## S5 · Empacotamento explícito de campos

Python Software Foundation. *struct — Interpret bytes as packed binary data*, Byte Order, Size, and Alignment e Format Characters.

https://docs.python.org/3/library/struct.html

Uso em 10.2 e no exemplo: formato `>3sBHH`, tamanhos de campos, big-endian e ausência de alinhamento nativo nessa forma. A tabela AUR foi definida antes do código; os bytes esperados são conferidos independentemente do resultado do codificador.

<a id="s6"></a>
## S6 · Validade de UTF-8

YERGEAU, François. *UTF-8, a transformation format of ISO 10646*. RFC 3629, seções 3 e 4, 2003.

https://www.rfc-editor.org/rfc/rfc3629.html

Uso em 10.2 e 10.3: sequências válidas, comprimento em octetos e rejeição de entradas inválidas. Os exemplos reutilizam caracteres específicos já introduzidos; não implementam um decodificador Unicode completo. A substituição tolerante de erro é distinguida da validação estrita.

<a id="s7"></a>
## S7 · Base64 e variantes

JOSEFSSON, Simon. *The Base16, Base32, and Base64 Data Encodings*. RFC 4648, seções 3–5, 2006.

https://www.rfc-editor.org/rfc/rfc4648.html

Python Software Foundation. *base64 — Base16, Base32, Base64, Base85 Data Encodings*, b64encode e b64decode.

https://docs.python.org/3/library/base64.html

Uso em 10.3: agrupamento em seis bits, preenchimento, alfabeto Base64url e validação de entrada. ABC/QUJD e Livro/TGl2cm8= foram recalculados. A fórmula de tamanho assume a forma com padding e sem quebras de linha; não é regra para todo invólucro. Base64 não foi apresentado como criptografia.

<a id="s8"></a>
## S8 · Codificação percentual e suas camadas

BERNERS-LEE, Tim; FIELDING, Roy; MASINTER, Larry. *Uniform Resource Identifier (URI): Generic Syntax*. RFC 3986, seções 2.1–2.4, 2005.

https://www.rfc-editor.org/rfc/rfc3986.html

Uso em 10.3: representação de octetos e dependência do componente interpretado. O exemplo A%2520B utiliza texto constante e nenhuma requisição de rede. O uso de urllib.parse.unquote nos testes confere somente as duas transformações descritas, não conformidade integral de um parser de URI nem técnica de ataque.

<a id="s9"></a>
## S9 · Normalização Unicode

Unicode Consortium. *Unicode Standard Annex #15 — Unicode Normalization Forms*, seções 1.1 e 1.2. Página consultada identificada como revisão 58, Unicode 18.0.0, de 12/08/2026.

https://www.unicode.org/reports/tr15/

Uso em 10.3: equivalência canônica e de compatibilidade, formas NFC/NFD/NFKC/NFKD e limites da transformação. A execução local usa a base Unicode 15.1.0 de seu runtime e apenas o par U+00E9 e U+0065 U+0301, não uma validação da implementação para todo Unicode 18. Não foram copiados os gráficos da publicação.

<a id="s10"></a>
## S10 · Estrutura e interoperabilidade JSON

BRAY, Tim, ed. *The JavaScript Object Notation (JSON) Data Interchange Format*. RFC 8259, seções 2–8, 2017.

https://www.rfc-editor.org/rfc/rfc8259.html

Uso em 10.3 e 10.4: tipos de valores, nomes, escapes e recomendação de unicidade. A restrição do exemplo a objeto com dois campos e a números sem fração ou expoente é um perfil local, não a gramática completa da RFC. Não se afirma uma interpretação única de nomes repetidos em todas as bibliotecas.

<a id="s11"></a>
## S11 · Política concreta do parser Python

Python Software Foundation. *json — JSON encoder and decoder*, object_pairs_hook, parse_constant, Repeated Names Within an Object e Infinite and NaN Number Values.

https://docs.python.org/3/library/json.html

Uso em 10.4 e 10.5: comportamento padrão de nomes repetidos e personalização do perfil. Foram conferidos duplicatas literais e por escape, tipos, campos adicionais, truncamento e valores proibidos. A documentação discute extensões aceitas pela implementação; não adotamos essas extensões como se fossem todas parte do JSON interoperável. A propriedade de booleanos no sistema de tipos Python é tratada por uma checagem explícita, não por coerção silenciosa.

<a id="s12"></a>
## S12 · Campos CSV e dialetos

SHAFRANOVICH, Yakov. *Common Format and MIME Type for Comma-Separated Values (CSV) Files*. RFC 4180, seção 2, 2005. Documento informativo.

https://www.rfc-editor.org/rfc/rfc4180.html

Python Software Foundation. *csv — CSV File Reading and Writing*, reader e dialetos.

https://docs.python.org/3/library/csv.html

Uso em 10.4: delimitadores, aspas, registros e ausência de conversão obrigatória dos campos em números. O exemplo foi conferido com CRLF na entrada do teste; o bloco do manuscrito apresenta as linhas visualmente, sem afirmar que todo Markdown usa os mesmos bytes. Nenhuma fórmula de planilha foi executada.

<a id="s13"></a>
## S13 · Alternativas textuais

W3C. *Extensible Markup Language (XML) 1.0 (Fifth Edition)*, introdução e documentos bem formados.

https://www.w3.org/TR/xml/

YAML Language Development Team. *YAML Ain’t Markup Language, revision 1.2.2*, modelo de informação e seção 10, Recommended Schemas.

https://yaml.org/spec/1.2.2/

Uso introdutório em 10.4: diferenças de organização e de resolução de tipos. Não foram executados parsers XML/YAML, resolvidas entidades externas ou testadas bibliotecas. Os formatos não são apresentados como simples substituições de pontuação de JSON.

<a id="s14"></a>
## S14 · Serialização binária por campos

Protocol Buffers. *Encoding*, Message Structure e Length-Delimited Records.

https://protobuf.dev/programming-guides/encoding/

Uso em 10.4: números de campo, tipos de transporte e papel do esquema para interpretar o conteúdo. Não foi gerado código Protobuf, comparado desempenho ou prometida compatibilidade de qualquer alteração arbitrária de esquema.

<a id="s15"></a>
## S15 · Compressão e reconstrução

DEUTSCH, Peter. *GZIP file format specification version 4.3*. RFC 1952, seção 2.3, 1996.

https://www.rfc-editor.org/rfc/rfc1952.html

Python Software Foundation. *gzip — Support for gzip files*, compress e decompress.

https://docs.python.org/3/library/gzip.html

Uso em 10.6: organização do formato, CRC e diferença entre representação comprimida e reconstruída. O teste utiliza somente 120 bytes conhecidos antes da compressão. Não foi construída bomba de descompressão nem implementado descompressor com orçamento para produção; a limitação deve acompanhar aquisição e processamento numa aplicação real.

<a id="s16"></a>
## S16 · Resumos e representações canônicas

NIST CSRC. *Cryptographic hash function*, glossário.

https://csrc.nist.gov/glossary/term/cryptographic_hash_function

Python Software Foundation. *hashlib — Secure hashes and message digests*.

https://docs.python.org/3/library/hashlib.html

RUNDGREN, Anders; JORDAN, Bret; ERDTMAN, Samuel. *JSON Canonicalization Scheme (JCS)*. RFC 8785, seção 3, 2020.

https://www.rfc-editor.org/rfc/rfc8785.html

Uso em 10.3 e 10.6: distinguir identidade dos bytes de igualdade dos dados reconstruídos, e explicar que canonicalização tem regras além de ordenar chaves. JCS preserva as strings sem normalização Unicode automática. Não foi implementado JCS, pesquisada colisão, criada assinatura ou atribuída autenticidade a um hash vindo de origem não confiável.

<a id="s17"></a>
## S17 · Capacidades de desserialização

Python Software Foundation. *pickle — Python object serialization*, aviso de segurança inicial e Comparison with json.

https://docs.python.org/3/library/pickle.html

CWE Program. *CWE-502 — Deserialization of Untrusted Data*, descrição.

https://cwe.mitre.org/data/definitions/502.html

Uso em 10.6: desserializadores com possibilidade de execução de comportamento. Não foi carregado pickle nem criado conteúdo malicioso. O alerta não é generalizado para afirmar que toda leitura de JSON executa código.

<a id="s18"></a>
## S18 · Validação e contexto posterior

OWASP Cheat Sheet Series. *Input Validation Cheat Sheet*, Input Validation Strategies e relações com prevenção de injeções.

https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html

Uso em 10.5 e 10.6: validação sintática e semântica, limites e distinção de controles necessários no destino. O perfil AUR é didático; não oferece um sanitizador universal, autorização de negócio ou especificação completa de títulos.

## Conferência executada e seus limites

Os [23 testes](../../../scripts/tests/test_chapter10_examples.py) passaram localmente em Linux x86-64, kernel 6.18.44, glibc 2.41 e Python 3.13.5. A base Unicode exposta por unicodedata é 15.1.0. A documentação Python pública consultada estava identificada como 3.14.7; os mecanismos usados foram conferidos no runtime indicado, sem presumir igualdade entre todas as versões.

Quatorze testes verificam o codec AUR e o perfil JSON; oito verificam transformações; um verifica a semântica de nomes e arquivo aberto no Linux. Os testes incluem os bytes fixados independentemente do codificador, ida e volta, fronteiras de tamanho, todas as truncagens do exemplo, entrada excedente, versão, codificação, tipos, nomes repetidos e constantes não aceitas.

Nenhuma rede, arquivo pessoal, permissão administrativa, desserialização executável ou entrada de tamanho abusivo foi utilizada. O teste de arquivo cria e remove apenas seus objetos em diretório temporário. O limite do codec começa em bytes já adquiridos; não limita retroativamente a leitura feita pelo chamador. A checagem do repositório completo é confirmada pelo workflow do commit, separadamente desta execução local. Revisão independente pendente.
