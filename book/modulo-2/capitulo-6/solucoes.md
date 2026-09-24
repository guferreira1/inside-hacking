# Capítulo 6 · Respostas comentadas

[← Perguntas](6.4-texto-e-interpretacao.md#pare-e-explique) · [Índice do capítulo](README.md) · [Capítulo 7 →](../capitulo-7/README.md)

Estas respostas utilizam as convenções declaradas no capítulo. Não é necessário memorizar as frases: explicitar a interpretação é parte da solução.

## 1. Quantidade não é maior valor

Três bits produzem `2^3 = 8` padrões. Ao associá-los aos inteiros não negativos a partir de zero, a faixa é 0–7. Zero ocupa um dos oito valores. Se o campo representar categorias, e não números, nem precisamos usar todos os padrões.

## 2. Três bases, uma quantidade

Em binário, os bits de `10101101` selecionam os pesos 128, 32, 8, 4 e 1. A soma é 173. Os grupos `1010` e `1101` correspondem a A e D. Em hexadecimal, `AD` vale `10 × 16 + 13 = 173`. Converter a escrita não muda a quantidade.

## 3. A regra do sinal

Sem sinal, os oito pesos de `11111111` são positivos e somam 255. Em complemento de dois com oito bits, o primeiro peso é −128, e a soma é −1. Faltam o tipo e a convenção de interpretação. Não é o último bit nem um sinal de menos visível no arquivo que resolve essa distinção.

## 4. A ordem dos bytes

Como inteiro sem sinal de dois bytes em big-endian, `12 34` vale `0x12 × 256 + 0x34 = 4660`. Como little-endian, o mesmo conteúdo vale 13330. Mudar a ordem troca o peso atribuído a cada byte; os oito bits internos de `12` e `34` não são invertidos.

## 5. Unidades explícitas

1 MB contém 1.000.000 de bytes; 1 MiB contém 1.048.576. A conversão entre 100 Mbit/s e 12,5 MB/s divide por oito porque um byte tem oito bits. Ela não é uma medição de transferência de arquivo e não desconta outras utilizações do canal ou limitações dos componentes.

## 6. Valor exibido versus texto armazenado

O byte `0x41` tem valor decimal 65 e corresponde a A em ASCII. O texto `41` contém dois caracteres, `4` e `1`, representados pelos bytes `34 31` em hexadecimal. Nesse texto não há um byte com valor `0x41`. Confundir exibição e conteúdo leva a contar os dados errados.

## 7. Texto não tem largura fixa de um byte

Com as escolhas de pontos de código explicitadas, A utiliza `41`, é utiliza `C3 A9` e o cadeado utiliza `F0 9F 94 92`. São `1 + 2 + 4 = 7` bytes. UTF-8 possui largura variável. Além disso, uma unidade percebida pelo usuário pode combinar vários pontos de código; uma regra geral de contagem precisa declarar qual unidade utiliza.

## 8. Capacidade não garante surpresa

Há 256 padrões de oito bits, mas a regra “sempre zero” determina o valor. Contar os padrões disponíveis não demonstra como foram escolhidos nem o que o observador sabe. Portanto, não é suficiente para afirmar imprevisibilidade ou segurança de uma chave.

[Continuar para o Capítulo 7 →](../capitulo-7/README.md) · [Voltar ao Módulo II](../README.md) · [Consultar o glossário](../../glossario.md)
