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

A arquitetura inicial possui 16 grandes partes:

1. história, cultura hacker e responsabilidade;
2. funcionamento de computadores;
3. sistemas operacionais;
4. redes e Internet;
5. programação e aplicações;
6. fundamentos de segurança, criptografia e identidade;
7. laboratório e método de investigação;
8. reconhecimento, enumeração e ferramentas;
9. segurança Web e APIs;
10. infraestrutura, Linux, Windows e Active Directory;
11. cloud, containers e cadeia de desenvolvimento;
12. vulnerabilidades de software, exploits e engenharia reversa;
13. outras superfícies de ataque;
14. privacidade, anonimato e dark web;
15. OSINT, fraudes, inteligência e investigação digital;
16. atuação profissional, defesa e pesquisa avançada.

A matriz de cobertura detalhará famílias de vulnerabilidades, técnicas e conhecimentos transversais, incluindo o ciclo ofensivo completo, pós-exploração, escalada de privilégios, credenciais, persistência, pivotamento, movimentação lateral, demonstração de impacto e segurança de sistemas de IA.

## Método editorial

O fluxo preferencial é:

**pesquisar → confrontar fontes → compreender → reproduzir quando aplicável → explicar com voz própria → revisar → publicar.**

Referências servem para fundamentar, verificar e aprofundar. A obra não será construída copiando ou meramente parafraseando artigos e documentações.

Nenhuma afirmação será considerada correta apenas porque foi produzida por IA, escrita por um mantenedor ou aceita em um pull request.

## Evidência e validação

Devem ser distinguidos explicitamente:

- fatos documentados;
- hipóteses;
- exemplos fictícios;
- resultados observados em laboratório;
- interpretações dos resultados.

Uma execução que não ocorreu não receberá saída inventada. Procedimentos dependentes de ambiente ou versão devem registrar essas condições.

## Segurança e autorização

Atividades ofensivas práticas serão destinadas exclusivamente a laboratórios próprios, CTFs, plataformas de treinamento, ambientes explicitamente autorizados e programas de Bug Bounty dentro de seus escopos e regras.

O livro deve ensinar limites, escopo, documentação, proteção de dados e encerramento responsável dos testes junto com as técnicas.

## Arquitetura editorial

As 16 partes organizam a progressão conceitual da obra. O manuscrito será armazenado fisicamente por capítulos em `book/capitulo-N/`.

Capítulos podem ser divididos em subcapítulos numerados (`1.1`, `1.2`, `1.3` etc.) sempre que a divisão melhorar compreensão, navegação, revisão ou manutenção. A granularidade será definida pela unidade conceitual, não por uma quantidade fixa de páginas.

## Open source e evolução

O repositório é a fonte de verdade da obra. O PDF será um artefato versionado gerado a partir do manuscrito.

Novos conceitos, correções, erratas e contribuições poderão evoluir a obra sem alterar retroativamente edições publicadas. Mudanças relevantes deverão ser revisadas técnica e editorialmente antes de integrar uma edição estável.

## Estado deste documento

Este Charter é uma versão inicial. Licenciamento, governança de contribuições, processo de releases e critérios formais de revisão ainda serão definidos.
