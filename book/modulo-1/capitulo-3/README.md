# Capítulo 3 — Ética, legalidade, autorização e escopo

[← Capítulo 2](../capitulo-2/README.md) · [Índice do livro](../../README.md) · [Página inicial](../../../README.md)

> **Status:** VALIDATED — versão editorial 1.0; fechamento da revisão interna em 23/09/2026. Primeira leitura concluída pelo mantenedor. Revisão jurídica especializada e revisão independente permanecem pendentes para uma edição estável. [Registro da revisão](../../../editorial/reviews/capitulo-3.md).

Você acaba de descobrir algo interessante. Uma aplicação apresenta um comportamento que parece permitir acesso a informações de outra pessoa. Há duas perguntas possíveis. A primeira é técnica: “consigo confirmar a falha?”. A segunda vem antes dela: **“em quais condições posso investigar isso?”**

A diferença entre as duas não está no teclado. Está nas pessoas que controlam o ambiente, nas permissões concedidas, nos dados envolvidos e nas consequências de cada teste.

Nos capítulos anteriores, tratamos hacking como investigação. Agora vamos acrescentar a disciplina que permite conduzir essa investigação sem transformar curiosidade em interferência indevida. Não basta decorar “tenha autorização”. Precisamos aprender a reconhecer uma autorização insuficiente, uma mudança de escopo e uma evidência que expõe mais informação do que o necessário.

O capítulo usa uma biblioteca fictícia, chamada Aurora, para discutir decisões concretas. Não é preciso instalar ferramentas, conhecer protocolos ou acessar um alvo real. A prática desta etapa é **tomar e justificar decisões de teste**.

> **Nota de leitura:** a primeira revisão apontou que este capítulo é mais denso que os anteriores. Parte disso vem da necessidade de distinguir regras operacionais, políticas e referências jurídicas sem simplificá-las indevidamente. Para reduzir essa carga, a versão 1.0 preserva exemplos e decisões concretas como fio condutor e evita transformar a seção jurídica em catálogo de artigos. Essa característica continuará sendo observada nas próximas revisões.

## Percurso de leitura

| Seção | Pergunta que iremos responder |
| --- | --- |
| [3.1 · Autorização e escopo](3.1-autorizacao-e-escopo.md) | Quem pode permitir o teste e o que exatamente foi permitido? |
| [3.2 · Evidências e responsabilidade](3.2-evidencias-e-responsabilidade.md) | Como demonstrar uma falha sem criar outro problema? |
| [3.3 · Estudo de caso](3.3-estudo-de-caso.md) | Como decidir o próximo passo diante de situações ambíguas? |

Depois da sua tentativa, consulte as [soluções comentadas](solucoes.md). As [referências](referencias.md) identificam as fontes e os limites da pesquisa desta entrega.

## Uma distinção antes de começar

Este capítulo combina orientações operacionais propostas pelo livro, exemplos fictícios e uma introdução a referências jurídicas brasileiras. Essas coisas serão identificadas no texto: uma regra conservadora do nosso laboratório não será apresentada como se fosse a redação de uma lei.

A discussão jurídica é educacional, não um parecer sobre um caso concreto. Testes profissionais e dúvidas envolvendo legislação, contratos, dados pessoais ou mais de um país exigem avaliação qualificada das circunstâncias.

**[Começar a seção 3.1 →](3.1-autorizacao-e-escopo.md)**
