# Capítulo 2 — Da curiosidade à segurança ofensiva: uma breve história da cultura hacker

> **Status:** primeira entrega de leitura — draft 0.1

No capítulo anterior, vimos que *hacking* não nasceu como sinônimo de crime digital. Mas essa constatação cria outra pergunta: **como uma cultura de exploração criativa de sistemas se tornou também uma disciplina de segurança, uma profissão e uma atividade associada a ataques?**

A resposta não cabe em uma única data nem em um único grupo.

A história do hacking atravessa universidades, sistemas telefônicos, computadores compartilhados, redes acadêmicas, comunidades underground, incidentes de grande escala, pesquisa de vulnerabilidades e a profissionalização da segurança. Em cada etapa, uma ideia permanece reconhecível: pessoas encontram sistemas complexos, tentam compreendê-los além da interface prevista e descobrem comportamentos que seus projetistas nem sempre imaginaram.

Este capítulo não pretende contar toda a história da computação. Ele procura construir uma linha que nos ajude a entender **de onde vieram a cultura hacker e a segurança ofensiva que estudaremos no restante da obra**.

## 2.1 Quando computadores eram recursos escassos

Hoje carregamos no bolso computadores muito mais acessíveis do que as máquinas que ocupavam laboratórios inteiros nas primeiras décadas da computação.

Essa diferença muda a maneira como precisamos imaginar o ambiente em que a cultura hacker se desenvolveu.

Computadores eram caros, compartilhados e frequentemente controlados por instituições. O acesso podia depender de horários, permissões e da disponibilidade de uma máquina utilizada por várias pessoas. Para estudantes fascinados pela computação, conseguir tempo de máquina significava conseguir experimentar.

No MIT, membros do Tech Model Railroad Club (TMRC) já estavam acostumados a construir e modificar sistemas complexos. O clube, fundado em 1946, possuía uma grande maquete ferroviária com sistemas de controle criados pelos próprios estudantes. O MIT registra que integrantes envolvidos nesses controles estiveram entre os primeiros hackers de computadores da instituição quando máquinas como o TX-0 e o PDP-1 se tornaram disponíveis.

O ponto importante não é transformar um clube universitário em uma “origem oficial” única do hacking. Culturas técnicas semelhantes existiram em outros lugares. O TMRC é importante porque deixou registros de uma comunidade na qual experimentação, improvisação e compreensão profunda de sistemas se encontraram com a computação.

Quando o computador passou a ser o novo sistema a explorar, a curiosidade não mudou de natureza. Mudou de objeto.

## 2.2 O computador como sistema a ser explorado

Imagine receber acesso a uma máquina cuja utilização normal é executar determinados programas.

Uma pessoa pode aprender a usar esses programas.

Outra começa a perguntar:

Como o sistema decide qual programa executar?

Como os usuários compartilham recursos?

O que acontece quando dois programas precisam da mesma memória?

É possível fazer a máquina produzir música?

É possível criar um jogo?

É possível automatizar uma tarefa que ninguém automatizou?

É possível fazer algo que os projetistas não previram?

Essas perguntas não são necessariamente perguntas de segurança. Elas representam uma forma exploratória de aprender tecnologia.

O ambiente hacker inicial valorizava bastante a experimentação direta. Computadores não eram apenas objetos para observar teoricamente; eram sistemas para manipular, programar e compreender pela interação.

Essa postura aparecerá novamente quando começarmos nossos laboratórios. Ler sobre um protocolo nos fornece um modelo. Observar pacotes reais nos permite confrontar esse modelo com o comportamento do sistema.

Mas existe uma tensão histórica importante: **explorar livremente um sistema que você controla é diferente de explorar livremente um sistema que pertence a outra pessoa**.

À medida que computadores e redes passaram a conectar mais usuários e organizações, essa diferença se tornou cada vez mais importante.

## 2.3 Antes da Internet: explorando a rede telefônica

A história hacker também passa pelo telefone.

Entre o fim dos anos 1950 e as décadas seguintes, comunidades que ficaram conhecidas como *phone phreaks* estudaram o funcionamento da rede telefônica. Elas ouviam tons, investigavam sinalização, procuravam documentação técnica e construíam dispositivos capazes de interagir com mecanismos da rede.

Por que isso importa para cybersecurity?

Porque a rede telefônica oferece um exemplo histórico extremamente claro de uma ideia que veremos repetidamente:

> **quando informação de controle e uso normal do sistema compartilham mecanismos que um usuário consegue influenciar, surgem possibilidades inesperadas.**

Sistemas telefônicos antigos utilizavam tons audíveis como parte de sua sinalização. Documentação técnica do Bell System descrevia, entre outros mecanismos, sinalização em frequências que incluíam 2600 Hz. Pessoas que estudavam a rede descobriram maneiras de reproduzir sinais utilizados pelo próprio sistema.

O famoso caso do apito associado ao cereal Cap'n Crunch tornou-se parte da cultura popular porque um brinquedo distribuído com o produto podia produzir aproximadamente um tom utilizado naquele ecossistema de sinalização. John Draper ficou conhecido pelo apelido *Captain Crunch* em associação a essa história.

O detalhe técnico completo da telefonia daquela época não é necessário agora. O que queremos observar é o padrão.

O sistema tinha uma linguagem interna.

Pesquisadores informais descobriram partes dessa linguagem.

Ao conseguir produzir sinais que o sistema interpretava como controle, conseguiram provocar comportamentos que um usuário comum não deveria controlar daquela maneira.

Décadas depois encontraremos o mesmo tipo de pergunta em tecnologias completamente diferentes:

**quais entradas o sistema interpreta como dados e quais interpreta como instruções?**

Essa pergunta aparecerá quando estudarmos injeções, parsers, protocolos e até aplicações de inteligência artificial.

A tecnologia muda. Certas classes de erro de confiança reaparecem.

## 2.4 Comunidades, conhecimento e uma cultura própria

Hacking nunca foi apenas uma relação entre uma pessoa e uma máquina.

Comunidades importaram desde cedo.

Conhecimento circulava entre estudantes, pesquisadores, entusiastas e grupos informais. Pessoas compartilhavam programas, técnicas, descobertas, documentação e histórias. Surgiram vocabulários próprios, publicações e espaços de encontro.

Isso produziu algo maior do que um conjunto de truques técnicos: uma cultura.

Parte dessa cultura valorizava entender sistemas pelo funcionamento interno, compartilhar conhecimento e avaliar habilidade pelo que uma pessoa conseguia construir ou descobrir. Parte também cultivava irreverência diante de regras consideradas arbitrárias.

É importante não romantizar esse passado.

Uma cultura que valoriza acesso irrestrito ao conhecimento pode produzir software, descobertas e aprendizado extraordinários. A mesma atitude aplicada sem consentimento a sistemas de terceiros pode causar danos e violar direitos.

Essa tensão ajuda a explicar por que a história do hacking não pode ser contada apenas como uma história de heróis criativos ou apenas como uma história de criminosos.

Ela contém ambos — e muitas pessoas que não cabem confortavelmente em nenhuma dessas categorias.

## 2.5 Quando computadores começam a conversar

Enquanto comunidades exploravam computadores individualmente, outra transformação estava acontecendo: máquinas começaram a ser conectadas em redes cada vez maiores.

Uma vulnerabilidade em um computador isolado possui um alcance.

Uma vulnerabilidade em um computador conectado a centenas, milhares ou milhões de outros sistemas possui outro.

A conectividade aumenta utilidade e superfície de ataque ao mesmo tempo.

Isso é uma relação que encontraremos durante toda a obra.

Quando conectamos um serviço à rede, criamos uma maneira legítima de alcançá-lo. Essa mesma capacidade pode criar uma nova oportunidade para reconhecimento ou exploração.

Quando permitimos que sistemas confiem uns nos outros, facilitamos operações legítimas. Essa confiança também pode se transformar em caminho de ataque.

Quando automatizamos comunicação entre aplicações, aumentamos capacidade. Também criamos novas interfaces e novos limites que precisam ser protegidos.

A história da segurança ofensiva acompanha, em grande medida, o crescimento dessas interconexões.

## 2.6 1988: um incidente que mudou a percepção da Internet

Em 2 de novembro de 1988, um programa autorreplicante escrito por Robert Tappan Morris começou a se espalhar por sistemas conectados à Internet da época.

Ficou conhecido como **Morris Worm**.

Um *worm* é um tipo de software capaz de se propagar entre sistemas. Mais adiante estudaremos malware com precisão; aqui interessa a consequência histórica.

A Internet daquele período era muito menor do que a atual, mas já conectava universidades, centros de pesquisa e outras instituições. A propagação do worm causou interrupções significativas e evidenciou que um problema distribuído poderia exigir coordenação entre organizações diferentes.

No período posterior ao incidente, a DARPA solicitou ao Software Engineering Institute (SEI), da Carnegie Mellon University, a criação de uma capacidade de resposta. Dessa iniciativa nasceu o **CERT Coordination Center (CERT/CC)** em 1988.

Isso representa uma mudança importante na nossa história.

Segurança deixa de ser apenas um problema que administradores individuais resolvem localmente. Incidentes em redes interconectadas exigem **coordenação, compartilhamento de informações, análise e resposta organizada**.

O Morris Worm não “inventou cybersecurity”. Seria uma simplificação histórica.

Mas ele se tornou um marco porque demonstrou, de maneira difícil de ignorar, como a conectividade transformava a escala dos incidentes e ajudou a catalisar estruturas profissionais de resposta.

## 2.7 Da descoberta informal à pesquisa de vulnerabilidades

À medida que computadores se tornaram infraestrutura de empresas, governos e da vida cotidiana, descobrir uma falha passou a ter consequências cada vez maiores.

Considere uma situação simples.

Você encontra uma maneira de fazer um programa travar.

Isso é apenas um bug?

Talvez.

Mas e se o travamento for causado por uma escrita indevida na memória?

E se essa escrita puder ser controlada?

E se ela permitir alterar o fluxo do programa?

E se o programa estiver executando com privilégios elevados?

Agora um comportamento aparentemente pequeno pode formar uma cadeia:

**bug → condição explorável → vulnerabilidade → técnica de exploração → impacto.**

A pesquisa de segurança se desenvolveu justamente nesse espaço entre observar um comportamento estranho e entender suas consequências.

Isso exige uma mentalidade diferente de simplesmente procurar uma ferramenta que “invada” o software.

O pesquisador precisa reproduzir o comportamento, reduzir variáveis, identificar a causa, determinar quais condições são necessárias, avaliar versões afetadas e descobrir o que realmente pode ser demonstrado.

É ciência experimental aplicada a sistemas imperfeitos.

## 2.8 O nascimento de uma profissão ofensiva

Quando organizações perceberam que poderiam possuir vulnerabilidades antes que adversários as descobrissem, surgiu uma pergunta natural:

**e se pedirmos a alguém para tentar encontrá-las primeiro?**

A ideia de testar segurança simulando ações adversariais é anterior à indústria moderna de pentest. Exercícios de avaliação, equipes que simulavam adversários e análises de segurança já apareciam em contextos governamentais e militares antes da Web.

Com o crescimento das redes corporativas e posteriormente da Internet comercial, esse princípio tornou-se uma atividade profissional mais reconhecível.

Um teste de intrusão moderno não deveria ser simplesmente:

> “tente invadir e veja até onde chega.”

Existe um objetivo, um escopo, regras de engajamento, métodos permitidos, limites de impacto, coleta de evidências e um relatório.

Essa formalização é uma diferença fundamental entre **capacidade ofensiva** e **prestação profissional de um teste ofensivo**.

A técnica pode ser semelhante à utilizada por um adversário.

O contexto não é.

## 2.9 A Web muda novamente a superfície

Quando a Web se tornou parte central da Internet comercial, aplicações passaram a expor funcionalidades complexas para qualquer pessoa com um navegador.

Formulários recebem dados.

Servidores processam entradas.

Aplicações consultam bancos de dados.

Usuários recebem sessões.

Sistemas tomam decisões de autorização.

Arquivos são enviados.

APIs conectam serviços.

Cada uma dessas funcionalidades resolve um problema legítimo — e cada uma introduz suposições que podem falhar.

É nesse ambiente que vulnerabilidades como SQL Injection, Cross-Site Scripting, falhas de autenticação e problemas de controle de acesso ganharam enorme relevância.

Perceba novamente o padrão histórico.

Não surgiu uma “tecnologia de hacking” separada.

**Surgiu uma nova tecnologia útil. Depois, pesquisadores e adversários começaram a explorar as maneiras pelas quais ela podia se comportar fora das expectativas de seus criadores.**

Segurança ofensiva acompanha tecnologia porque vulnerabilidades nascem dentro dos sistemas que construímos.

## 2.10 Divulgação, mercado e Bug Bounty

Descobrir uma vulnerabilidade cria outro problema:

**o que fazer com ela?**

Ao longo da história da segurança, pesquisadores, fornecedores e comunidades discordaram bastante sobre divulgação. Publicar imediatamente pode colocar usuários em risco antes de uma correção. Ocultar indefinidamente uma falha pode deixar usuários vulneráveis sem saber. Comunicar privadamente também não garante que o fornecedor responderá.

Dessas tensões surgiram diferentes práticas de *vulnerability disclosure*, coordenação de vulnerabilidades e, posteriormente, programas estruturados de Bug Bounty.

Em um Bug Bounty, uma organização publica regras que autorizam determinados tipos de pesquisa em determinado escopo e estabelece como vulnerabilidades devem ser reportadas.

Isso altera profundamente a relação entre pesquisador e alvo.

O pesquisador não precisa pressupor autorização.

Ele precisa **ler exatamente a autorização que recebeu**.

Uma empresa pode permitir testes em um domínio e proibi-los em outro. Pode permitir determinados métodos e restringir outros. Pode estabelecer regras específicas para dados pessoais, engenharia social, negação de serviço ou acesso a contas.

Portanto, Bug Bounty não significa “a empresa deixou hackers atacarem”.

Significa que existe **um contrato operacional de pesquisa com limites definidos**.

Voltaremos a isso em profundidade muito mais adiante.

## 2.11 Hacking torna-se especialização — e se fragmenta

Hoje, dizer apenas “trabalho com hacking” descreve muito pouco.

Uma pessoa pode pesquisar aplicações Web.

Outra pode analisar APIs.

Outra trabalha com Windows e Active Directory.

Outra pesquisa segurança de cloud.

Outra estuda dispositivos embarcados.

Outra faz engenharia reversa.

Outra desenvolve exploits.

Outra investiga aplicações de IA.

Outra participa de Red Teams que simulam adversários em ambientes corporativos.

As bases se conectam, mas as especializações podem exigir anos de aprofundamento.

Isso explica a arquitetura deste livro.

Começaremos com fundamentos compartilhados — computadores, sistemas operacionais, redes, programação, identidade e segurança — e então abriremos caminhos progressivamente especializados.

O objetivo não é fingir que todas as áreas são iguais.

É construir uma base suficientemente sólida para que, quando elas se separarem, você entenda **de onde cada uma veio e quais mecanismos ela está explorando**.

## 2.12 A história continua

Cybersecurity possui uma característica desconfortável para quem escreve livros:

ela muda enquanto o livro está sendo escrito.

Novas tecnologias criam novas superfícies.

Sistemas antigos continuam existindo.

Vulnerabilidades conhecidas reaparecem em implementações novas.

Técnicas ofensivas evoluem.

Defesas respondem.

Atacantes adaptam novamente.

Aplicações baseadas em modelos de linguagem são um exemplo contemporâneo. Conceitos como prompt injection parecem novos porque a tecnologia é nova, mas algumas perguntas são familiares: **o que o sistema considera instrução? Em quais dados confia? Que autoridade uma entrada consegue influenciar? Que ações podem resultar dessa influência?**

A história do hacking não é uma sequência de truques que foram substituídos.

É uma história de sistemas, confiança, curiosidade, falhas e adaptação.

Por isso, aprender cybersecurity não pode signific decorar o conjunto de ataques conhecidos em determinado ano.

Precisamos aprender a investigar sistemas que ainda nem existem.

---

## Pare e explique

Sem consultar o capítulo, tente responder:

1. Por que o TMRC é relevante para a história hacker sem precisar ser tratado como a única “origem oficial” do hacking?
2. O que o phone phreaking ensina sobre a relação entre a linguagem interna de um sistema e sua superfície de ataque?
3. Por que a expansão das redes alterou a escala dos problemas de segurança?
4. Qual foi a importância histórica do Morris Worm para a resposta coordenada a incidentes?
5. Explique a sequência: **bug → condição explorável → vulnerabilidade → exploração → impacto**.
6. O que diferencia capacidade ofensiva de um pentest profissional?
7. Por que Bug Bounty não significa autorização irrestrita?
8. Por que a história do hacking ajuda a entender vulnerabilidades modernas em vez de servir apenas como curiosidade?

## Nota de pesquisa

Esta versão foi escrita após consulta a registros e publicações do MIT sobre o Tech Model Railroad Club e a cultura hacker, documentação histórica e técnica sobre phone phreaking e sinalização do Bell System, além de materiais do Software Engineering Institute da Carnegie Mellon University sobre o Morris Worm e a criação do CERT/CC.

Alguns episódios populares possuem versões simplificadas repetidas durante décadas. Sempre que um detalhe histórico não for necessário para compreender o mecanismo, a obra evitará tratá-lo como fato apenas porque se tornou parte do folclore hacker.

As referências serão normalizadas na bibliografia da edição.
