# Chapter Template

## Metadados

- Módulo:
- Capítulo (numeração global, sem reinício por módulo):
- Caminho: `book/modulo-M/capitulo-N/`
- Status:
- Última revisão:
- Responsáveis:

Consulte o [guia de estrutura](repository-structure.md) para os índices e caminhos relativos. A inclusão ou movimentação de um capítulo deve atualizar o índice do módulo, o índice geral, o glossário e as referências afetadas no mesmo conjunto de alterações.

## Pergunta central

Qual pergunta o leitor deve conseguir responder ao final?

## Por que este capítulo existe

Qual lacuna ele resolve e por que é necessário na progressão da obra?

## Pré-requisitos

Quais conceitos anteriores serão utilizados?

## Objetivos de aprendizagem

O que o leitor deverá compreender, explicar e, quando aplicável, executar?

## Mapa de subcapítulos

Definir `N.1`, `N.2`, `N.3` etc. por unidade conceitual. Não fragmentar apenas por tamanho.

## Conceitos e mecanismos

Mapa dos conceitos que precisam ser desenvolvidos em prosa.

## Terminologia e glossário

Relacionar os termos e siglas efetivamente utilizados; indicar quais são novos, quais já estão definidos e quais são apenas mencionados. Atualizar [book/glossario.md](../book/glossario.md) junto com a entrega, com definição original e vínculo à ocorrência. Seguir a [política de glossário](glossary-policy.md). Não importar termos de capítulos futuros só para aumentar a lista.

## Narrativa e exemplos

Como o assunto será introduzido e quais exemplos serão usados?

## Prática, demonstração ou exercício

Escolher somente o formato que realmente acrescenta compreensão ao capítulo. **Laboratório não é requisito universal.**

Quando houver laboratório reproduzível, registrar objetivo, ambiente, versões, preparação, observações esperadas, evidências, restauração e limites de autorização.

Quando não houver, usar exemplos, cenários, análise de comportamento, exercícios de raciocínio ou demonstrações conceituais sem alegar execução. Um comportamento esperado fundamentado pode ser explicado como previsão; ele não deve ser apresentado como resultado observado.

## Verificação de compreensão

Perguntas, exercícios e variações que exijam raciocínio, não apenas repetição.

## Defesa e implicações

Mitigações, detecção, limitações e consequências quando aplicável.

## Pesquisa e referências

Fontes primárias, especificações, documentação, pesquisas e materiais complementares usados para verificar o capítulo.

## Validação

- [ ] Pesquisa revisada; fontes e limites de consulta registrados.
- [ ] Afirmações técnicas verificadas ou pendências explicitadas.
- [ ] Siglas e termos explicados antes de serem exigidos.
- [ ] Glossário atualizado nesta entrega ou conferido sem novos termos.
- [ ] Cada verbete novo tem ocorrência e fonte/contexto identificados.
- [ ] Exemplos e soluções revisados, quando existentes.
- [ ] Prática/laboratório reproduzido quando aplicável; caso contrário, N/A ou pendência explícita.
- [ ] Índices, estados, navegação e links relativos conferidos.
- [ ] `python3 scripts/check_docs.py` executado após as alterações.
- [ ] Revisão editorial; revisão técnica e sua independência identificadas.
- [ ] Renderização PDF conferida, somente quando esta entrega incluir PDF.

## Gaps conhecidos

Pendências e pontos que ainda exigem investigação. Uma checklist não executada não é evidência de conclusão.
