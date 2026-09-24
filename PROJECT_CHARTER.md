# Project Charter — Por Dentro do Hacking

**Versão:** 0.1  
**Status:** draft

## Visão

Criar uma obra autoral, técnica, didática, aberta e continuamente atualizável sobre cybersecurity e hacking ético, capaz de conduzir um leitor sem formação técnica prévia dos fundamentos da computação à compreensão e prática avançada de segurança.

## Princípio central

O livro não existe para ensinar comandos a serem reproduzidos mecanicamente. Ele deve explicar sistemas e mecanismos de segurança em profundidade suficiente para que o leitor consiga raciocinar sobre situações que a obra nunca apresentou.

## Público

Leitores que sabem utilizar um computador, mas não precisam conhecer previamente programação, redes, Linux, Windows ou cybersecurity.

## Resultado pretendido

Ao longo da obra, o leitor deve construir fundamentos, aprender a formular hipóteses, observar sistemas, interpretar evidências, reproduzir experimentos em ambientes autorizados, compreender vulnerabilidades e técnicas ofensivas, avaliar impacto e relacionar ataque e defesa.

A leitura, por si só, não será apresentada como garantia de especialização profissional. Competência prática exige experimentação e autonomia.

## Escopo

A arquitetura inicial evoluiu para módulos temáticos, mantidos no sumário mestre como unidades de aprendizagem. O mapa atual possui 21 módulos e permanece revisável:

O escopo detalhado e a relação atual de módulos e capítulos ficam em [`editorial/master-outline.md`](editorial/master-outline.md). Essa separação evita duplicar um índice vivo dentro do Charter.

A matriz de cobertura detalhará famílias de vulnerabilidades, técnicas e conhecimentos transversais, incluindo o ciclo ofensivo completo, pós-exploração, escalada de privilégios, credenciais, persistência, pivotamento, movimentação lateral, demonstração de impacto e segurança de sistemas de IA.

## Método editorial

O fluxo preferencial é:

**pesquisar → confrontar fontes → compreender → reproduzir quando houver algo realmente reproduzível e útil → explicar com voz própria → revisar → publicar.**

Referências servem para fundamentar, verificar e aprofundar. A obra não será construída copiando ou meramente parafraseando artigos e documentações.

Nenhuma afirmação será considerada correta apenas porque foi produzida por IA, escrita por um mantenedor ou aceita em um pull request.

## Evidência e validação

Devem ser distinguidos explicitamente:

- fatos documentados;
- hipóteses;
- exemplos fictícios;
- resultados observados em laboratório;
- interpretações dos resultados.

Uma execução que não ocorreu não receberá saída inventada. Nem todo capítulo precisa de laboratório: fundamentos podem usar explicações, exemplos, cenários e exercícios de raciocínio. Quando houver uma prática reproduzível que realmente acrescente compreensão, ela deve registrar ambiente, versão e condições.

## Segurança e autorização

Atividades ofensivas práticas serão destinadas exclusivamente a laboratórios próprios, CTFs, plataformas de treinamento, ambientes explicitamente autorizados e programas de Bug Bounty dentro de seus escopos e regras.

O livro deve ensinar limites, escopo, documentação, proteção de dados e encerramento responsável dos testes junto com as técnicas.

## Arquitetura editorial

Os módulos organizam a progressão conceitual da obra e também seus diretórios. O manuscrito é armazenado em `book/modulo-M/capitulo-N/`. Cada módulo possui um `README.md` de abertura e índice; o índice geral, o glossário e a bibliografia permanecem diretamente em `book/`.

A numeração de capítulos é global e não reinicia a cada módulo: o Módulo II está planejado para começar pelo capítulo 6. Mover um capítulo entre módulos não altera automaticamente seu número. O [guia de estrutura](editorial/repository-structure.md) detalha as convenções de navegação e manutenção.

Capítulos podem ser divididos em subcapítulos numerados (`1.1`, `1.2`, `1.3` etc.) sempre que a divisão melhorar compreensão, navegação, revisão ou manutenção. A granularidade será definida pela unidade conceitual, não por uma quantidade fixa de páginas.

## Open source e evolução

O repositório é a fonte de verdade da obra. O PDF será um artefato versionado gerado a partir do manuscrito.

Novos conceitos, correções, erratas e contribuições poderão evoluir a obra sem alterar retroativamente edições publicadas. Mudanças relevantes deverão ser revisadas técnica e editorialmente antes de integrar uma edição estável.

## Licenciamento

Conteúdo editorial e ilustrações originais são disponibilizados sob CC BY-SA 4.0. Código, scripts e exemplos de código são disponibilizados sob MIT. O [mapa de licenciamento](LICENSE.md) identifica a aplicação de cada licença e o tratamento de materiais de terceiros. As condições para contribuir estão em [CONTRIBUTING.md](CONTRIBUTING.md).

## Estado deste documento

Este Charter registra a proposta inicial. O licenciamento foi definido em 23 de setembro de 2026. Governança de contribuições, processo de releases e critérios formais de revisão continuam evoluindo nos documentos editoriais.
