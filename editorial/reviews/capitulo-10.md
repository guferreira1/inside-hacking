# Primeira entrega editorial — Capítulo 10

**Data:** 24/09/2026. **Estado:** DRAFT 0.1. **Módulo:** II.  
**Base:** `23435ad3789828f06cb7d87921115e194e9c9c41`.

[Manuscrito](../../book/modulo-2/capitulo-10/README.md) · [Referências](../../book/modulo-2/capitulo-10/referencias.md) · [Exemplos](../../book/modulo-2/capitulo-10/exemplos/README.md)

## Objetivo e percurso

Seis seções acompanham um registro que sai da aplicação para um arquivo e precisa ser interpretado por outro componente. Nomes e objetos, metadados, tipos de mídia, estrutura binária, codificações, serialização, parsing, integridade e uso posterior são separados por mecanismos e exemplos. Doze perguntas opcionais possuem respostas comentadas.

O formato AUR v1 foi criado para o livro. Seu cabeçalho de oito bytes e o registro Livro/3 permitem verificar comprimentos, ordem e significado sem depender de infraestrutura. O codec Python é opcional, utiliza biblioteca padrão e não lê entradas externas quando executado diretamente. Nenhum laboratório ofensivo foi exigido.

## Pesquisa e decisões

As fontes S1–S18 delimitam consultas a Linux man-pages, RFCs, documentação W3C, Unicode, YAML, Protobuf, Python, OWASP e CWE. A prosa é original. PNG/XML/YAML/Protobuf são comparações introdutórias, não leitores implementados. JCS não é confundido com mera ordenação de chaves nem com normalização Unicode de strings.

O texto diferencia extensão, tipo declarado e assinatura de formato; texto e bytes; capacidades do campo e limites do domínio; duplicatas JSON e política do receptor; round-trip e conformidade; CRC, hash e autenticidade; validação e autorização. AUR rejeita versões desconhecidas e dados excedentes por contrato explícito, não como regra imposta a todo formato.

O perfil JSON é restrito: dois campos exatos, UTF-8, nomes únicos, quantidade inteira sem fração/expoente e limites próprios. Não é implementação de JSON Schema ou JCS. Booleanos, NaN/Infinity e substituição silenciosa de UTF-8 inválido não são aceitos. O título não recebe filtro universal nem garantia de adequação a toda saída.

## Execução documentada

Os [23 testes](../../scripts/tests/test_chapter10_examples.py) passaram localmente em Linux x86-64, kernel 6.18.44, glibc 2.41, Python 3.13.5. unicodedata informou Unicode 15.1.0. Quatorze testes conferem formato e perfil JSON; oito conferem transformações; um confere a semântica Linux de dois nomes e uma abertura após unlink.

Os bytes do registro foram comparados a uma expectativa literal independente do codificador. Foram verificados ida e volta, limites, todos os prefixos truncados, sobra, assinatura, versão, UTF-8, campos, tipos e duplicatas inclusive por escape. As transformações incluem Base64, decodificação percentual em duas camadas, o par canônico de é, finais de linha, CSV, hashes e compressão de 120 bytes.

O teste de arquivo cria e remove somente objetos temporários próprios. Não foram processados arquivos pessoais, acessadas redes, executado pickle ou produzidas entradas abusivas. A função recebe bytes já adquiridos; o limite interno não substitui limitar a aquisição. O requisito de sintaxe Python 3.10+ não é afirmação de teste em todas essas versões. O teste de arquivos é explicitamente restrito ao Linux.

A documentação Unicode consultada e a base do runtime são distintas e isso foi preservado nas notas. Nenhuma verificação do par de caracteres foi generalizada para toda a versão Unicode da fonte.

## Documentação e checagem de conjunto

README principal, índice geral, índice do módulo, passagem entre capítulos 9 e 10, bibliografia, glossário, matriz de cobertura e estado editorial acompanham o manuscrito. As entradas novas do glossário apontam para ocorrências no capítulo; conceitos apenas mencionados permanecem identificados como introdutórios.

O repositório completo é conferido pelo workflow associado ao commit; o clone local não foi concluído por resolução de rede. A aprovação local dos 23 testes não é descrita como auditoria local do restante do repositório. O workflow executa também as suítes anteriores e verifica destinos e âncoras internos; URLs externas são inventariadas, não confirmadas como acessíveis por esse passo.

O capítulo 9 tem fechamento interno separado. O capítulo 10 permanece em primeira leitura e sem revisão técnica independente. Os cinco textos do Módulo II agora existem, mas seu fechamento depende da leitura do 10 e revisão de conjunto. Não houve publicação no LinkedIn ou geração de PDF.

**Próxima revisão:** observar a clareza das passagens entre nome, bytes, formato, transformação e autorização. Próximo capítulo planejado: **11 — O papel de um sistema operacional**, início do Módulo III.
