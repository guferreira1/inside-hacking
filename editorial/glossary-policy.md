# Política de glossário e terminologia

[Editorial](README.md) · [Glossário do livro](../book/glossario.md) · [Modelo de capítulo](chapter-template.md)

## Regra de entrega

**Cada capítulo novo ou alterado deve sair com o glossário revisado no mesmo conjunto de alterações.** Se não houver termos novos, registrar que a conferência foi feita e que as entradas existentes continuam adequadas. Não deixar a atualização para o fechamento de um módulo.

O glossário acompanha a leitura. Não é um catálogo antecipado dos 234 capítulos candidatos e não deve apresentar um tópico planejado como conhecimento já desenvolvido.

## O que entra

Termos técnicos, siglas, ferramentas, instituições citadas como referência e expressões de método que possam impedir a compreensão. Deve existir uma ocorrência no manuscrito, nos exemplos ou nas referências do capítulo. Entradas explicativas podem reunir variantes realmente usadas, como pentest e penetration test ou PoC e prova de conceito.

Quando um termo estiver somente no planejamento e uma dúvida exigir explicação, a entrada deve ser excepcional, curta e marcada **menção no planejamento**. OSINT está nessa categoria nesta revisão. Não acrescentar os demais assuntos futuros por associação.

Rótulos internos de exemplo, como H1 e S2, não são termos técnicos: são identificadores de hipóteses ou fontes. Não criar verbetes para cada número. Nomes de autores e todo substantivo do texto também não precisam virar glossário.

## Conteúdo de cada verbete

Usar a grafia correta e, para uma sigla, sua expansão verificada e uma explicação em português. Escrever uma definição original e curta, delimitada ao uso no livro; explicar a diferença de um termo próximo quando a confusão tiver relevância. Vincular o verbete ao capítulo ou subcapítulo onde aparece e, quando necessário, à fonte primária que sustenta a definição.

Uma referência à ocorrência não substitui uma fonte técnica. Não atribuir a um capítulo uma definição que ele não oferece. Nas menções introdutórias, informar que o aprofundamento virá depois.

Preservar ordem alfabética e âncoras estáveis. Ao reorganizar um capítulo, atualizar os links de ida e de retorno. Não duplicar definições contraditórias para uma sigla e sua expressão por extenso.

## Explicar antes de depender do termo

O glossário complementa o capítulo, não corrige silenciosamente seus saltos didáticos. Na primeira utilização relevante, explicar a sigla ou o conceito no próprio texto. Um leitor que segue o capítulo deve conseguir acompanhar sem interromper cada parágrafo para consultar outra página.

Em referências e notas técnicas, a definição pode ficar no glossário, desde que sua consulta seja acessível. Termos apenas citados como exemplo de assunto futuro não precisam receber uma aula completa naquele momento.

## Conferência em duas passagens

Na primeira passagem, levantar os termos do capítulo e relacioná-los às entradas existentes. Na segunda, conferir grafia, definição, fonte, ocorrência e navegação após as alterações. A revisão deve distinguir termo explicado, mencionado ou apenas planejado.

A automação em [scripts/check_docs.py](../scripts/check_docs.py) auxilia com inventário e links. Ela **não determina sozinha a completude ou correção semântica do glossário**. Uma sigla detectada não é uma definição validada; um link funcionando não comprova o fato citado.
