# Capítulo 6 — Bits, bytes e representação da informação

[← Capítulo 5](../../modulo-1/capitulo-5/README.md) · [Índice do módulo](../README.md) · [Glossário](../../glossario.md)

**Módulo II — Computadores por dentro**

> **Status:** DRAFT 0.1 — primeira entrega de leitura. Referências e exemplos aritméticos conferidos; leitura do mantenedor e revisão técnica independente pendentes. [Registro editorial](../../../editorial/reviews/capitulo-6.md).

Uma ferramenta mostra `41 42 43`. Outra mostra `ABC`. Você olha para o mesmo arquivo e tem a impressão de que uma delas está escondendo alguma coisa.

Talvez nenhuma esteja. Se os valores da primeira tela estão em hexadecimal e a segunda interpreta os bytes como texto ASCII, as duas podem estar apresentando a mesma informação de maneiras diferentes.

Não é preciso entender ainda as palavras hexadecimal e ASCII. Vamos construir essas peças até que a frase anterior deixe de parecer uma explicação em código.

Este capítulo inaugura uma mudança de escala. Nos anteriores, discutimos pessoas, regras, evidências e aplicações. Agora começaremos pela representação mais elementar que usaremos para descrevê-las: sequências de bits. Como dois símbolos conseguem representar números, palavras e instruções? Por que um byte não é necessariamente uma letra? E por que dois programas podem ler os mesmos bytes e chegar a resultados diferentes?

O objetivo não é fazer você decorar longas sequências de zeros e uns. É aprender a atravessar a distância entre **o que uma ferramenta mostra e o que os dados representam**.

## Percurso de leitura

| Seção | Pergunta central |
| --- | --- |
| [6.1 · Antes do zero e do um](6.1-bits-e-estados.md) | Como um estado físico pode representar informação? |
| [6.2 · Contar sem o algarismo dois](6.2-binario-e-hexadecimal.md) | Como ler e construir números binários e hexadecimais? |
| [6.3 · O tamanho muda a pergunta](6.3-bytes-limites-e-unidades.md) | O que um byte comporta e por que largura, sinal e unidade importam? |
| [6.4 · Os mesmos bytes, leituras diferentes](6.4-texto-e-interpretacao.md) | Como representar texto e reconhecer os limites de uma interpretação? |

Nenhuma instalação é necessária. As contas e conversões são exemplos próprios, com [testes de conferência](../../../scripts/tests/test_chapter6_examples.py); não representam uma investigação ofensiva executada. As [referências](referencias.md) sustentam os mecanismos, e as [soluções](solucoes.md) ficam separadas das perguntas opcionais.

**[Começar a seção 6.1 →](6.1-bits-e-estados.md)**
