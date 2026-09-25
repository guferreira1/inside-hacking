# Capítulo 8 — Como um programa se torna execução

[← Capítulo 7](../capitulo-7/README.md) · [Índice do módulo](../README.md) · [Glossário](../../glossario.md) · [Capítulo 9 →](../capitulo-9/README.md)

**Módulo II — Computadores por dentro**

> **Status:** VALIDATED — versão editorial 1.0; retorno favorável e revisão interna concluída em 24/09/2026. Revisão técnica independente pendente. [Registro editorial](../../../editorial/reviews/capitulo-8.md).

Você altera uma conta no código de um programa. Antes era `2 + 3`; agora é `2 + 7`. Salva o arquivo, executa o programa e continua recebendo cinco.

A primeira suspeita poderia ser um erro na soma. Mas talvez o computador esteja executando exatamente o que recebeu: a versão anterior. **O arquivo que você editou é o mesmo arquivo que o sistema está executando?**

Essa situação será nosso ponto de partida. Nos capítulos anteriores, distinguimos representações e componentes. Agora precisamos entender as transformações que ligam uma descrição escrita por uma pessoa às instruções executadas pelo processador — e por que um programa guardado em disco não é o mesmo que um processo em funcionamento.

Usaremos um programa pequeno, criado para o livro, que apresenta uma quantidade de exemplares. Sua função é tornar o percurso visível, não implementar a biblioteca Aurora inteira. O código necessário será explicado no texto; não é preciso já conhecer C, instalar um compilador ou executar os exemplos para acompanhar a leitura.

## Percurso de leitura

| Seção | Pergunta central |
| --- | --- |
| [8.1 · O arquivo que você editou não é necessariamente o que executou](8.1-codigo-e-construcao.md) | O que distingue código-fonte, construção e execução? |
| [8.2 · Traduzir as peças e encontrar as conexões](8.2-compilacao-e-ligacao.md) | Como pré-processamento, compilação, montagem e ligação cooperam? |
| [8.3 · Um arquivo ganha um contexto de execução](8.3-carregamento-e-processos.md) | Como formato, carregamento, bibliotecas e processo se relacionam? |
| [8.4 · Interpretar também exige execução](8.4-interpretadores-e-runtimes.md) | O que muda em Python, bytecode e máquinas virtuais de linguagem? |
| [8.5 · O programa não trabalha sozinho](8.5-contexto-e-diagnostico.md) | Por que entradas, ambiente e etapa da falha mudam o diagnóstico? |

As [referências](referencias.md) sustentam os mecanismos. Os [arquivos de exemplo](exemplos/README.md) e os testes são uma forma opcional de conferir o texto, não um laboratório ofensivo obrigatório. As [respostas comentadas](solucoes.md) ficam separadas das perguntas.

**[Começar a seção 8.1 →](8.1-codigo-e-construcao.md)**
