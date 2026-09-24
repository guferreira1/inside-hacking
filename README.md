<h1 align="center">Por Dentro do Hacking</h1>
<p align="center"><strong>Dos fundamentos da computação à segurança ofensiva.</strong></p>
<p align="center">Entender os sistemas. Investigar suas falhas. Aprender com evidências.</p>
<p align="center"><a href="book/modulo-1/capitulo-1/README.md"><strong>Comece a leitura</strong></a> · <a href="book/README.md">Módulos e capítulos</a> · <a href="editorial/master-outline.md">Mapa da obra</a> · <a href="CONTRIBUTING.md">Enviar feedback</a></p>

---

## Um livro para entender o que acontece por dentro

Aprender uma ferramenta é diferente de compreender o mecanismo que ela observa. **Por Dentro do Hacking** nasce dessa diferença: um livro em português que constrói os fundamentos antes de avançar para vulnerabilidades, técnicas de investigação, exploração e defesa.

A proposta é permitir que quem está começando entenda computadores, sistemas operacionais, redes e aplicações e, progressivamente, consiga analisar sua segurança. Não é necessário conhecer os autores, participar de um curso ou acompanhar conversas externas para ler a obra.

**O livro está sendo escrito em público.** Os primeiros capítulos já podem ser lidos; o restante é planejamento, não conteúdo concluído. Correções e dúvidas são bem-vindas, inclusive quando o leitor ainda não sabe propor uma solução.

## Comece por aqui

**[Módulo I — Hacking, segurança e método](book/modulo-1/README.md)**

| Leitura | O que você encontrará | Estado |
| --- | --- | --- |
| [1 · O que é hacking?](book/modulo-1/capitulo-1/README.md) | Conceitos iniciais, investigação, ferramentas e responsabilidade. | Em revisão |
| [2 · Da curiosidade à segurança ofensiva](book/modulo-1/capitulo-2/README.md) | Uma introdução à história da cultura hacker e da segurança. | Revisão interna concluída — v1.0 |
| [3 · Ética, legalidade, autorização e escopo](book/modulo-1/capitulo-3/README.md) | Permissões, limites, dados e um estudo de caso com respostas comentadas. | Revisão interna concluída — v1.0 |
| [4 · Como pensar como investigador de segurança](book/modulo-1/capitulo-4/README.md) | Uma investigação explicada: observação, hipóteses, comparações e conclusões. | Rascunho para leitura — v0.1 |
| [5 · Ameaças, vulnerabilidades, exploits, risco e superfície de ataque](book/modulo-1/capitulo-5/README.md) | Uma narrativa para distinguir fraquezas, exploração, exposição e consequências. | Rascunho para leitura — v0.1 |

**[Abrir o índice de leitura →](book/README.md)**

Os cinco capítulos do Módulo I estão disponíveis para leitura. O módulo continua em produção: disponibilidade do texto não equivale a revisão editorial concluída.

Os estados indicam o andamento editorial, não certificação ou revisão independente concluída. O fechamento interno de um capítulo não equivale à publicação de uma edição estável do livro. Consulte o [estado editorial e suas pendências](editorial/publication-status.md).

## O caminho planejado

A obra parte de computação, sistemas operacionais, redes, programação, criptografia e identidade. Depois, avança para reconhecimento, Web e APIs, credenciais, pós-exploração, escalada de privilégios, Active Directory, cloud e containers.

Pesquisa de vulnerabilidades, engenharia reversa, wireless, mobile, IoT, segurança de IA, privacidade, dark web, investigação de fraudes, Red Team, defesa e atuação profissional também fazem parte do escopo planejado.

O [sumário mestre](editorial/master-outline.md) é um mapa vivo organizado em módulos, capítulos e subcapítulos. Capítulos podem ser reorganizados, unidos ou ampliados conforme a escrita revelar necessidades. O número de títulos não mede o progresso da obra.

Os arquivos seguem `book/modulo-M/capitulo-N/`. A numeração dos capítulos é global e não reinicia a cada módulo. Cada módulo possui seu próprio índice de leitura.

## Como estudar

Leia um capítulo ou uma seção de cada vez. Depois, feche o texto e tente explicar o mecanismo com suas palavras. Use as perguntas propostas e, quando existirem, os exercícios e laboratórios. As soluções comentadas ficam separadas da tentativa. Laboratórios entram quando acrescentam compreensão e possuem um ambiente documentado; não são requisito para todo capítulo.

Uma dúvida pode revelar tanto um conceito a rever quanto uma explicação que o livro precisa melhorar. Abra um [feedback didático](https://github.com/guferreira1/inside-hacking/issues/new?template=didactic-feedback.md) indicando onde sua compreensão parou.

O [glossário](book/glossario.md) ajuda na consulta; a [bibliografia](book/bibliografia.md) permite examinar as fontes. Nenhum deles substitui as explicações dos capítulos.

## Como o livro é construído

O texto é desenvolvido com uma sequência didática própria. Referências sustentam fatos e mecanismos; não são um pretexto para copiar ou apenas rearranjar conteúdo de terceiros.

Há apoio de IA na pesquisa, organização e redação. Respostas de IA não são consideradas fontes nem revisão técnica independente. Fontes consultadas, resultados reproduzidos e pendências de validação devem ser distinguidos. A aprovação de leitura, por si só, não comprova correção técnica.

O manuscrito no Git é a fonte editorial. **O PDF será gerado em uma etapa posterior; ainda não há uma edição em PDF publicada nem pipeline de geração implementado.** Os laboratórios executáveis também serão adicionados progressivamente, quando pertinentes.

## Participe da revisão

Você pode apontar um [possível erro técnico](https://github.com/guferreira1/inside-hacking/issues/new?template=technical-error.md), sugerir [conteúdo ou aprofundamento](https://github.com/guferreira1/inside-hacking/issues/new?template=content-suggestion.md), relatar [desatualização](https://github.com/guferreira1/inside-hacking/issues/new?template=outdated-content.md) ou dizer que não entendeu um trecho.

Leia o [guia de contribuição](CONTRIBUTING.md). Não inclua tokens, credenciais, dados pessoais ou detalhes de vulnerabilidades privadas em issues ou pull requests. Correções e propostas de melhoria podem ser enviadas por pull request e passam por revisão antes da integração.

<details>
<summary><strong>Para quem quer conhecer a organização do projeto</strong></summary>

| Área | Função |
| --- | --- |
| [`book/`](book/README.md) | Índice geral, glossário, bibliografia e módulos da obra. |
| [`book/modulo-1/`](book/modulo-1/README.md) | Índice e capítulos do primeiro módulo. |
| [`editorial/`](editorial/README.md) | Planejamento, padrão de escrita e controle de revisão. |
| [`research/`](research/README.md) | Notas de pesquisa; não são automaticamente conteúdo publicado. |
| [`labs/`](labs/README.md) | Área reservada aos materiais dos laboratórios. |
| [`assets/`](assets/README.md) | Recursos visuais da obra. |

O [Project Charter](PROJECT_CHARTER.md) registra a proposta e as decisões editoriais. O [guia de estrutura](editorial/repository-structure.md) define diretórios, numeração e navegação. O sumário mestre contém a arquitetura expandida e revisável.

</details>

## Uso responsável

Os exercícios ofensivos destinam-se exclusivamente a laboratórios e ambientes explicitamente autorizados. A presença de um sistema neste livro ou em suas referências **não concede autorização para testá-lo**.

## Licenças

Conteúdo editorial e ilustrações originais sob [CC BY-SA 4.0](LICENSES/CC-BY-SA-4.0.txt). Código, scripts e exemplos de código sob [MIT](LICENSES/MIT.txt). Consulte o [mapa de licenciamento e atribuição](LICENSE.md).

---

**[Comece pelo Capítulo 1 →](book/modulo-1/capitulo-1/README.md)**
