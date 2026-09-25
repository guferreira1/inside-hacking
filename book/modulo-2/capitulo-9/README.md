# Capítulo 9 — Memória, processos e arquitetura de computadores

[← Capítulo 8](../capitulo-8/README.md) · [Índice do módulo](../README.md) · [Glossário](../../glossario.md)

**Módulo II — Computadores por dentro**

> **Status:** DRAFT 0.1 — primeira entrega de leitura. Modelos numéricos e exemplo local conferidos; leitura do mantenedor e revisão independente pendentes. [Registro editorial](../../../editorial/reviews/capitulo-9.md).

Duas execuções do mesmo programa mostram um contador com valor cinco. A primeira altera o contador para nove. A segunda continua mostrando cinco. Até aqui, parece natural: cada execução tem seu próprio trabalho.

Agora você descobre que, nas duas, o contador foi identificado pelo mesmo número de endereço. Como os valores podem ser diferentes se o endereço é igual?

A pergunta esconde uma premissa: a de que um endereço é uma coordenada universal da máquina. Não é essa a visão que um programa normalmente recebe num sistema com memória virtual. Para compreender a diferença, precisamos acrescentar contexto ao número.

No capítulo 8, acompanhamos o caminho do arquivo à execução. Aqui vamos entrar nessa execução: como seu espaço de memória é organizado, o que os threads compartilham, por que uma página pode estar mapeada sem ocupar imediatamente RAM exclusiva e quais limites o hardware consegue — ou não consegue — verificar.

O cenário dos contadores é didático. Usaremos Linux com MMU como implementação de referência e identificaremos as comparações com outros ambientes. Um pequeno exemplo próprio foi executado para observar mapeamentos privados e compartilhados; ele não mede a localização física das páginas nem exige que você o execute para acompanhar o capítulo.

## Percurso de leitura

| Seção | Pergunta central |
| --- | --- |
| [9.1 · Duas execuções, dois contextos](9.1-processos-threads-e-contextos.md) | O que pertence ao processo, o que pertence ao thread e o que acontece quando ele deixa a CPU? |
| [9.2 · O endereço precisa de um mapa](9.2-enderecos-paginas-e-traducao.md) | Como páginas, tabelas e tradução ligam um endereço virtual a um destino? |
| [9.3 · Ter espaço não significa poder usá-lo de qualquer maneira](9.3-regioes-objetos-e-tempo-de-vida.md) | Como código, pilha, heap e tempo de vida estabelecem limites diferentes? |
| [9.4 · Memória prometida, presente e compartilhada](9.4-paginacao-copias-e-medidas.md) | O que page faults, cópia na escrita e medidas de memória realmente mostram? |
| [9.5 · Proteção não é uma única parede](9.5-protecao-concorrencia-e-diagnostico.md) | Como permissões, concorrência e regras da aplicação se complementam? |

As [referências](referencias.md), [respostas comentadas](solucoes.md) e [explicação do exemplo opcional](exemplos/README.md) acompanham o texto. Nenhuma leitura de memória de terceiros, configuração administrativa ou exploração é necessária.

**[Começar a seção 9.1 →](9.1-processos-threads-e-contextos.md)**
