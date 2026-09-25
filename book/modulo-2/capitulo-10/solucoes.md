# Capítulo 10 · Respostas comentadas

[← Perguntas](10.6-integridade-e-fronteiras.md#pare-e-explique) · [Índice do capítulo](README.md)

As respostas distinguem o contrato didático dos comportamentos documentados de cada plataforma. Os exemplos executados usam conteúdo próprio e pequeno; não são avaliações de arquivos externos.

## 1. Dois nomes não criam duas cópias

Um hard link acrescenta um nome para o mesmo objeto no sistema de arquivos. Alterar seu conteúdo por um nome pode ser percebido pelo outro. Uma cópia cria outro objeto, cujo conteúdo pode começar igual e depois divergir. Um link simbólico tem ainda outro papel: guarda um caminho a resolver. A igualdade inicial dos bytes não permite deduzir qual dessas relações existe.

## 2. A abertura não depende de repetir o nome

No Linux, a abertura mantém uma referência ao objeto. Remover seus nomes não invalida automaticamente essa referência, e a exclusão final depende de não restarem as referências pertinentes. O teste leu somente um arquivo temporário mantido aberto. Não demonstrou recuperação posterior ao fechamento, nem equivalência dessa operação em todos os sistemas de arquivos e plataformas.

## 3. Sinais diferentes de reconhecimento

Extensão é parte do nome; tipo de mídia é identificação declarada num contexto, como o protocolo; assinatura de formato é um padrão nos bytes. Eles podem orientar a escolha de um leitor, mas ainda faltam a estrutura completa, os limites dos campos e as condições de uso. Uma assinatura de formato também não é uma assinatura digital de autoria.

## 4. Oito bytes de cabeçalho e cinco de título

Offsets 0–2 guardam AUR; o byte 3 contém a versão 1. Os bytes 4–5 contêm o comprimento, e 6–7, a quantidade, ambos como inteiros sem sinal de dois bytes em big-endian. O título começa no offset 8. Para Livro, há cinco bytes UTF-8: `8 + 5 = 13`. As barras usadas na explicação não pertencem ao arquivo.

## 5. A unidade é byte, não letra percebida

O é precomposto é representado por `C3 A9` em UTF-8, logo o comprimento é dois. Uma sequência inválida não é apenas um caractere que falta no repertório do leitor: não respeita a estrutura da codificação. Nosso contrato rejeita essa entrada em vez de substituir conteúdo silenciosamente. Outro visualizador pode ter política tolerante, que precisa ser identificada como transformação.

## 6. Base64 muda a representação

Os 24 bits de ABC são divididos em quatro grupos de seis: 16, 20, 9 e 3, associados a Q, U, J e D. É possível recuperar os bytes pela regra pública inversa. Não há uma chave exigida para essa conversão, e a forma estudada expande o tamanho em vez de comprimir os dados. Base64url é uma variante com alfabeto próprio; o protocolo define o tratamento de preenchimento.

## 7. Uma transformação pode revelar outra escrita

Uma decodificação de A%2520B substitui %25 por %, produzindo A%20B. Uma segunda interpreta %20 e produz um espaço. São duas camadas de processamento, não duas maneiras idênticas de executar uma única operação. Precisamos definir qual representação cada componente recebe e quantas transformações fazem parte do acordo.

## 8. O contrato resolve a ambiguidade explicitamente

A RFC recomenda nomes únicos e alerta para diferenças entre receptores quando há repetição. No exemplo, Python em sua configuração padrão conserva a última quantidade, sete. Nosso perfil rejeita o documento, inclusive quando um escape produz o mesmo nome depois do parsing. Isso evita que a importação escolha silenciosamente um de dois valores onde o contrato exige um só.

## 9. Concordar entre duas funções não valida todo o formato

Um codificador e um decodificador podem compartilhar o mesmo erro e ainda preservar um round-trip. Por isso, também verificamos bytes esperados definidos pela tabela e casos de rejeição, como truncamento, sobra e campo fora de faixa. O limite de entrada deve começar durante sua aquisição: rejeitar um objeto bytes enorme depois de lê-lo não recupera o orçamento que a leitura já consumiu.

## 10. Valores equivalentes e identidade binária são comparações diferentes

Ordem de campos e espaços podem mudar sem alterar os valores reconstruídos no exemplo. Os bytes e os hashes calculados sobre eles são diferentes. JCS define um conjunto específico de regras de canonicalização, não apenas ordenação de chaves, e não normaliza automaticamente as strings Unicode. Nosso codificador compacto não declara conformidade com JCS.

## 11. Tamanho de entrada e autenticidade exigem outras evidências

Uma representação comprimida pode reconstruir uma quantidade diferente de dados, além de exigir trabalho e estruturas de processamento. É preciso limitar as etapas relevantes, não somente o arquivo externo. CRC ajuda a detectar certas corrupções, mas pode ser recalculado por quem altera o conteúdo; não estabelece quem o produziu. Mesmo um hash precisa de referência confiável para sustentar uma comparação de integridade.

## 12. O poder do leitor e o uso posterior importam

Alguns desserializadores de objetos podem executar comportamento durante a reconstrução. O alerta de pickle exige que conteúdo não confiável não seja tratado como simples dado inofensivo. JSON reduz esse tipo específico de expectativa ao representar dados, mas não elimina defeitos de biblioteca, consumo de recursos, decisões de autorização ou uso indevido dos valores em outro contexto. A segurança depende do caminho completo.

[Voltar ao capítulo](README.md) · [Índice do módulo](../README.md) · [Glossário](../../glossario.md)
