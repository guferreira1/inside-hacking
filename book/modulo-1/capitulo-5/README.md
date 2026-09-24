# Capítulo 5 — Ameaças, vulnerabilidades, exploits, risco e superfície de ataque

[← Capítulo 4](../capitulo-4/README.md) · [Índice do livro](../../README.md) · [Página inicial](../../../README.md)

**Módulo I — Hacking, segurança e método**

> **Status:** DRAFT 0.1 — primeira entrega de leitura. Fontes consultadas em 23/09/2026. Exemplos fictícios; nenhuma execução de laboratório alegada. Revisão técnica independente pendente.

Uma biblioteca publica seu catálogo na internet. Qualquer pessoa pode pesquisar um livro, ver se existe um exemplar disponível e consultar o horário de atendimento. Até aqui, a abertura ao público é parte do serviço, não um defeito.

Agora imagine que a mesma biblioteca também permite que qualquer visitante consulte o histórico de empréstimos de qualquer leitor. A aplicação pode continuar rápida, estável e sem mensagens de erro. Mesmo assim, algo importante deixou de ser protegido.

Por que uma informação deveria estar disponível e a outra não? O que exatamente falhou? A existência desse comportamento prova que alguém já o utilizou? E como decidir a urgência da correção?

Essas perguntas parecem pertencer ao mesmo problema, mas pedem respostas diferentes. Precisamos distinguir o que tem valor, o que pode dar errado, qual fraqueza permite isso, como ela pode ser aproveitada e quais consequências importam. Sem essa separação, acabamos chamando qualquer resultado estranho de ameaça, qualquer ferramenta de exploit e qualquer alerta de risco crítico.

Neste capítulo, acompanharemos a biblioteca fictícia Aurora para construir esse vocabulário pelo funcionamento das situações. Não é necessário instalar nada nem conhecer programação. Quando um mecanismo técnico aparecer, ele será explicado no nível necessário à discussão; seu desenvolvimento completo virá nos módulos correspondentes.

## Percurso de leitura

| Seção | Pergunta central |
| --- | --- |
| [5.1 · O que estamos tentando proteger?](5.1-ativos-e-vulnerabilidades.md) | Quando um comportamento passa a ser um problema de segurança? |
| [5.2 · Da possibilidade à exploração](5.2-ameacas-e-exploracao.md) | Como separar ameaça, vulnerabilidade, exploit e impacto? |
| [5.3 · Onde o sistema está exposto e o que fazer primeiro](5.3-superficie-e-risco.md) | Por que uma falha não tem a mesma importância em todos os ambientes? |

As [referências e notas de pesquisa](referencias.md) permitem verificar as definições e seus limites. O cenário Aurora e as comparações ao longo do texto são exemplos autorais, não relatos de incidentes ou resultados experimentais.

**[Começar a seção 5.1 →](5.1-ativos-e-vulnerabilidades.md)**
