# Capítulo 2 — Da curiosidade à segurança ofensiva: uma breve história da cultura hacker

[← Capítulo 1](../capitulo-1/README.md) · [Índice do livro](../../README.md) · [Capítulo 3 →](../capitulo-3/README.md)

> **Status:** VALIDATED — versão editorial 1.0; fechamento da revisão interna em 23/09/2026. As fontes e os limites da verificação estão documentados. Revisão histórica independente não realizada; esta versão não é uma release do livro em PDF. [Registro da revisão](../../../editorial/reviews/capitulo-2.md).

No capítulo anterior, vimos que *hacking* não nasceu como sinônimo de crime digital. Mas essa constatação cria outra pergunta: **como uma cultura de exploração criativa de sistemas se tornou também uma disciplina de segurança, uma profissão e uma atividade associada a ataques?**

A resposta não cabe em uma única data nem em um único grupo.

Nosso percurso passa por universidades, sistemas telefônicos, computadores compartilhados, redes, incidentes e pesquisa de vulnerabilidades. Não vamos tratá-los como etapas de uma evolução inevitável, nem procurar uma pessoa que tenha inventado tudo. Vamos observar episódios que ajudam a entender a relação entre a tecnologia e as maneiras de investigá-la.

Este capítulo não pretende contar toda a história da computação. Ele procura construir uma linha que nos ajude a entender **de onde vieram a cultura hacker e a segurança ofensiva que estudaremos no restante da obra**.

## 2.1 Quando computadores eram recursos escassos

Para imaginar os ambientes em que essas comunidades se desenvolveram, precisamos deixar de lado a ideia de que cada estudante tinha um computador pessoal disponível a qualquer momento. Em instituições com equipamentos caros e compartilhados, aproveitar o tempo de máquina era uma questão importante. O relatório de segurança organizado por Willis Ware descreve justamente sistemas que dividiam recursos de computação entre usuários, aumentando o aproveitamento do equipamento e introduzindo problemas de isolamento entre eles. [R8](referencias.md#r8)

No MIT, membros do Tech Model Railroad Club (TMRC) já estavam acostumados a construir e modificar sistemas complexos. O clube, fundado em 1946, possuía uma maquete ferroviária com controles desenvolvidos pelos estudantes. Em um relato publicado pelo MIT em 1996, John Shriver, do próprio clube, relaciona os integrantes que trabalhavam nesses controles aos primeiros hackers de computadores da instituição, quando máquinas como o TX-0 e o PDP-1 se tornaram disponíveis. [R1](referencias.md#r1)

O ponto importante não é transformar um clube universitário em uma “origem oficial” única do hacking. O TMRC é um caso documentado de encontro entre experimentação, construção de sistemas e computação. Seu dicionário, derivado de um texto de Pete Samson de 1959 e ampliado posteriormente, também preserva parte do vocabulário daquela comunidade. [R2](referencias.md#r2)

Para nossa leitura, a conexão é esta: o computador podia se tornar um novo objeto para uma curiosidade técnica que já existia.

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

Essas perguntas não são necessariamente perguntas de segurança. Elas representam uma forma exploratória de aprender tecnologia. São um exemplo didático, não a transcrição de uma conversa histórica.

Podemos estudar o computador como objeto para observar e também como sistema para programar, modificar e compreender pela interação. Essa postura aparecerá novamente nos laboratórios da obra: uma explicação apresenta um modelo; uma observação permite confrontá-lo com o comportamento do sistema.

Mas existe uma distinção importante para nosso método: **explorar um ambiente que você está autorizado a testar é diferente de presumir a mesma liberdade sobre sistemas de terceiros**. Curiosidade será o ponto de partida das nossas perguntas, não uma autorização automática para executar qualquer teste.

## 2.3 Explorando a rede telefônica

A história hacker também passa pelo telefone. Em seu relato pessoal sobre a construção de uma *blue box*, Steve Wozniak descreve a leitura, em 1971, de uma reportagem sobre pessoas que investigavam a rede telefônica, seguida da consulta a documentação técnica e de experimentos com circuitos. Esses exploradores ficaram conhecidos como *phone phreaks*. [R5](referencias.md#r5)

Por que isso importa para cybersecurity?

Porque essa história permite investigar uma pergunta que reaparecerá na obra:

> **O que acontece quando um usuário consegue produzir sinais que o sistema interpreta como comandos de controle?**

Em determinados sistemas telefônicos históricos, sinais de controle viajavam no mesmo canal usado para transmitir a voz. Essa é a ideia de sinalização **em banda**. Um artigo de A. Weaver e N. A. Newell, publicado no *Bell System Technical Journal* em 1954, descreve sistemas de frequência única e o uso de 2600 Hz em determinadas linhas. O próprio artigo discute o risco de outros sons imitarem a sinalização e os mecanismos projetados para reduzir esse problema. [R3](referencias.md#r3)

Um episódio conhecido envolve o apito distribuído com o cereal Cap'n Crunch. Wozniak relata que ele podia produzir um tom de 2600 Hz, relacionado à supervisão de certas ligações. John Draper, conhecido como *Captain Crunch*, aparece nessa história. Aqui estamos identificando o relato de um participante, não atribuindo a Draper a descoberta de todos esses mecanismos ou a criação da segurança de computadores. [R5](referencias.md#r5)

Há uma diferença técnica importante: **produzir um tom não equivale a controlar toda a rede telefônica**. Supervisão da ligação e transmissão do número de destino são funções distintas. A documentação do Bell System de 1960 descreve sinalização multifrequência, ou MF, que representava informações de endereçamento por combinações de tons. Não devemos reduzir todos esses mecanismos a um único apito. [R4](referencias.md#r4)

Também não devemos generalizar o comportamento desses sistemas históricos para qualquer rede telefônica, muito menos para as atuais. O exemplo serve para compreender uma arquitetura e sua exposição; não é uma instrução de teste em serviços de telecomunicações.

O padrão que queremos reconhecer é o seguinte: o sistema tinha convenções internas de controle; quem compreendia essas convenções podia investigar se entradas acessíveis a um usuário seriam interpretadas com uma autoridade indevida.

Décadas depois, faremos uma pergunta parecida diante de tecnologias diferentes:

**quais entradas o sistema interpreta como dados e quais interpreta como instruções?**

Essa comparação é uma ferramenta didática. Ela não significa que sinalização telefônica, SQL injection e prompt injection funcionem da mesma maneira ou aceitem as mesmas defesas.

## 2.4 Comunidades, conhecimento e uma cultura própria

Hacking não precisa ser pensado apenas como a relação entre uma pessoa e uma máquina. O dicionário do TMRC, por exemplo, registra um vocabulário coletivo, comentários bem-humorados e contribuições de diferentes integrantes. É um vestígio de práticas compartilhadas, não apenas de feitos individuais. [R2](referencias.md#r2)

Para interpretar esse material, vale separar cultura de idealização. Podemos valorizar criatividade, troca de conhecimento e habilidade técnica sem presumir que todos os participantes de uma comunidade tenham a mesma conduta ou os mesmos objetivos.

Uma pessoa pode construir algo engenhoso e, em outra situação, tomar uma decisão irresponsável. Um relato autobiográfico também pode apresentar a atuação de seu autor de maneira favorável. Por isso, nossa leitura histórica deve distinguir o que o documento demonstra da interpretação que fazemos dele.

O livro não tratará o passado como uma sequência de heróis criativos nem como uma história composta apenas por criminosos. A pergunta mais útil continua sendo: **qual sistema estava envolvido, o que aconteceu e que evidência sustenta essa explicação?**

## 2.5 Quando computadores começam a conversar

Agora imagine dois cenários fictícios.

No primeiro, um computador executa um programa sem disponibilizá-lo pela rede. No segundo, a mesma função passa a receber solicitações de outras máquinas.

A conectividade acrescenta uma possibilidade legítima de uso. Também pode acrescentar uma forma de alcançar uma falha. Não se segue daí que todo serviço conectado esteja vulnerável, nem que um computador isolado esteja livre de riscos. A diferença é que precisamos incluir os caminhos de comunicação na análise.

Quando permitimos que sistemas confiem uns nos outros, também precisamos perguntar quais operações essa confiança autoriza. Uma relação útil para o funcionamento do ambiente pode se tornar relevante para um ataque, dependendo dos controles presentes.

Essa é a conexão conceitual com o próximo episódio histórico: um problema que se propaga entre máquinas pode exigir uma resposta que não termina na administração de uma única máquina.

## 2.6 1988: um incidente que mudou a percepção da Internet

Em 2 de novembro de 1988, o programa associado a Robert Tappan Morris começou a se espalhar por sistemas conectados à Internet. Ficou conhecido como **Morris Worm**. A RFC 1135, publicada em 1989, descreve a propagação, as interrupções causadas e os esforços para combatê-lo. [R6](referencias.md#r6) [R7](referencias.md#r7)

Um *worm* é um programa capaz de se executar de forma independente e propagar cópias funcionais de si para outras máquinas. Esse sentido não deve ser confundido com o nome de uma pessoa. No episódio estudado, **Morris** é o sobrenome do autor; **worm** descreve o tipo de programa. [R6](referencias.md#r6)

Segundo o histórico institucional do Software Engineering Institute (SEI), da Carnegie Mellon University, a DARPA pediu ao instituto que estabelecesse uma equipe de resposta a emergências computacionais após o incidente. Dessa iniciativa surgiu, em 1988, o **CERT Coordination Center (CERT/CC)**. [R7](referencias.md#r7)

O episódio ajuda a entender a importância de coordenação, análise e comunicação entre organizações. Mas não marca a invenção da segurança de computadores: o National Bureau of Standards e a Association for Computing Machinery já haviam realizado, em dezembro de 1972, um workshop sobre controle de acesso, auditoria, identificação e outros temas de segurança, documentado na NBS Technical Note 827, de 1974. [R9](referencias.md#r9)

**Phone phreaking, Morris Worm e criação do CERT/CC são episódios diferentes.** Não devemos fundi-los na história de uma pessoa que teria criado cybersecurity. O caso da telefonia ajuda a estudar sinalização; o worm ajuda a estudar propagação e impacto; o CERT/CC representa uma resposta institucional ao problema de coordenação.

## 2.7 Da descoberta informal à pesquisa de vulnerabilidades

Vamos usar um exemplo fictício para entender a diferença entre observar uma falha e estabelecer suas consequências.

Você encontra uma maneira de fazer um programa travar.

Isso demonstra que existe um problema de execução, mas ainda não explica sua causa ou todo o seu impacto.

O que ocorreu na memória?

O programa estava processando uma entrada controlável por um usuário?

O comportamento aparece sempre ou depende de alguma condição?

A falha afeta apenas aquela execução ou também um serviço utilizado por outras pessoas?

Há evidência de que seria possível alterar o fluxo do programa?

Um percurso de investigação possível seria:

**comportamento inesperado → investigação da causa → vulnerabilidade, se confirmada → teste de exploração, quando necessário e autorizado → impacto demonstrado.**

Essa sequência é uma organização do trabalho, não uma definição de como toda vulnerabilidade nasce. Uma vulnerabilidade pode existir antes de alguém descobrir um exploit. Da mesma forma, observar um travamento não autoriza concluir que existe execução arbitrária de código.

No exemplo, seria necessário reduzir variáveis, distinguir observação de hipótese e decidir quais testes poderiam sustentar cada conclusão. Uma hipótese que não se confirmou deve ser registrada como tal. Isso não prova, automaticamente, que o sistema inteiro esteja seguro.

Essa é a forma de investigação que queremos exercitar: **a conclusão deve ter o tamanho da evidência, não o tamanho da expectativa do pesquisador**.

## 2.8 O nascimento de uma profissão ofensiva

A ideia de avaliar a segurança com tentativas deliberadas de atravessar seus controles é anterior à Web. O relatório *Security Controls for Computer Systems*, publicado originalmente em 1970 e reeditado em 1979, já discutia testes e tentativas diagnósticas de penetração conduzidos sob a autoridade responsável pelo sistema. Isso demonstra a existência desse pensamento naquele período; não estabelece uma data única de nascimento do pentest. [R8](referencias.md#r8)

A pergunta central é simples:

**e se procurarmos as falhas de forma autorizada antes que um adversário as explore?**

A execução profissional exige mais que habilidade para obter acesso. Objetivos, planejamento, regras de engajamento, tratamento de dados e comunicação dos resultados fazem parte de uma avaliação organizada. A NIST SP 800-115, de 2008, descreve esses elementos e inclui um modelo de regras de engajamento. É uma referência metodológica daquele período, não um manual atualizado de ferramentas. [R10](referencias.md#r10)

Um teste não deveria ser simplesmente:

> “tente invadir e veja até onde chega.”

Para o método adotado neste livro, precisamos definir o que queremos avaliar, como demonstraremos os resultados e quais limites serão respeitados.

Essa é uma diferença fundamental entre **capacidade ofensiva** e **prestação profissional de um teste ofensivo**.

## 2.9 A Web muda novamente a superfície

Pense nas funções de uma aplicação Web: receber formulários, processar entradas, consultar dados, reconhecer usuários, controlar acesso e aceitar arquivos. Não é necessário entender sua implementação agora. Basta perceber que cada função envolve decisões sobre quais dados aceitar e quais ações permitir.

O estudo de segurança dessas aplicações inclui SQL injection, Cross-Site Scripting, falhas de autenticação e problemas de autorização. Esses são temas distintos, documentados, por exemplo, nos materiais da Web Security Academy da PortSwigger. Citá-los aqui não atribui a essa plataforma a descoberta dessas classes de falha. [R13](referencias.md#r13)

Perceba o padrão didático: não precisamos imaginar uma tecnologia de hacking separada dos sistemas úteis. Investigamos justamente o que acontece quando as suposições desses sistemas não se sustentam.

Ao estudar uma funcionalidade, voltaremos a perguntar quem a utiliza, em quais entradas ela confia e quais resultados deveriam ser impossíveis. Os capítulos técnicos construirão cada mecanismo antes de desenvolver seus testes.

## 2.10 Divulgação, mercado e Bug Bounty

Descobrir uma vulnerabilidade cria outra pergunta:

**o que fazer com ela?**

Divulgar informações sobre uma falha pode ajudar a proteger usuários, mas também pode facilitar sua exploração antes que existam medidas de proteção. Manter a informação restrita, por outro lado, não garante que o problema será corrigido. O guia de divulgação coordenada do CERT trata dessa coordenação entre quem encontra, quem corrige, quem utiliza e quem comunica a vulnerabilidade. [R12](referencias.md#r12)

Programas de **Bug Bounty** acrescentam a possibilidade de recompensar relatos que atendam a critérios definidos. Não são sinônimo de toda política de divulgação: um canal para reportar falhas pode existir sem recompensa financeira. O programa da Mozilla é um exemplo que explicita tanto critérios de recompensa quanto regras de pesquisa e limites envolvendo sistemas de terceiros. [R11](referencias.md#r11) [R12](referencias.md#r12)

Para o pesquisador, a existência de um programa não deve ser interpretada como permissão irrestrita. É preciso conferir exatamente quais sistemas e atividades a política contempla. Elegibilidade para recompensa, autorização para testar e regras de divulgação são questões relacionadas, mas distintas. [R11](referencias.md#r11)

No método do livro, isso se traduz em uma regra de trabalho: **não começar pelo que uma ferramenta consegue fazer; começar pelo que foi permitido investigar**.

Voltaremos ao tema no próximo capítulo e, mais adiante, na parte específica de Bug Bounty.

## 2.11 Hacking torna-se especialização — e se fragmenta

Nosso próprio mapa de estudos ajuda a perceber a variedade de problemas reunidos sob a palavra hacking.

Aplicações Web e APIs exigirão compreensão dos fluxos de dados e decisões de acesso. Windows e Active Directory trarão outros mecanismos de identidade e confiança. Dispositivos embarcados, engenharia reversa, cloud e aplicações de IA abrirão problemas diferentes.

Não estamos afirmando que essas áreas sejam equivalentes ou que uma única ferramenta sirva para todas. Estamos planejando uma base compartilhada, seguida de aprofundamentos.

É por isso que a obra começará por computadores, sistemas operacionais, redes, programação, identidade e segurança. Quando os percursos se separarem, queremos que o leitor consiga reconhecer o sistema que está investigando e localizar os conhecimentos que ainda precisa construir.

O objetivo não é decorar o nome de cada especialidade. É compreender **por que problemas diferentes exigem conhecimentos e formas de observação diferentes**.

## 2.12 A história continua

Um livro como este precisa manter separadas duas coisas: os episódios históricos que consegue documentar e a interpretação que propõe para aprender com eles.

Aplicações com modelos de linguagem oferecem uma conexão contemporânea. A OWASP descreve prompt injection como um problema em que entradas podem influenciar indevidamente o comportamento do modelo, inclusive por conteúdo de fontes externas. Os efeitos dependem do contexto da aplicação e das capacidades disponíveis. [R14](referencias.md#r14)

Para nossa investigação, reaparecem perguntas familiares: **o que o sistema considera instrução? Em quais dados confia? Que autoridade uma entrada consegue influenciar? Que ações podem resultar disso?**

Essa aproximação não torna uma aplicação de IA equivalente a uma central telefônica ou a um banco de dados. Usaremos a história para melhorar nossas perguntas, não para aplicar automaticamente uma solução antiga a um mecanismo novo.

Por isso, aprender cybersecurity não pode significar decorar o conjunto de ataques conhecidos em determinado ano.

Precisamos aprender a investigar sistemas que ainda nem existem.

---

## Pare e explique

Sem consultar o capítulo, tente responder:

1. Por que o TMRC é relevante para a história hacker sem precisar ser tratado como a única “origem oficial” do hacking?
2. O que o phone phreaking ensina sobre sinais de controle? Por que um tom de 2600 Hz não deve ser descrito como uma chave universal da rede telefônica?
3. Por que a conectividade pode alterar o alcance de um problema de segurança, sem tornar todo sistema conectado automaticamente vulnerável?
4. O que foi o Morris Worm e qual é sua relação com a criação do CERT/CC? Por que isso não equivale à invenção de cybersecurity?
5. No exemplo do programa que trava, o que foi observado e o que ainda precisa ser investigado? Por que uma vulnerabilidade não depende da existência de um exploit público?
6. O que diferencia capacidade ofensiva de um pentest profissional?
7. Por que Bug Bounty não significa autorização irrestrita? Toda política de divulgação precisa oferecer recompensa?
8. Como a história pode ajudar a investigar sistemas modernos sem levar à suposição de que tecnologias diferentes funcionam da mesma maneira?

Depois da tentativa, consulte as [respostas comentadas](solucoes.md). Elas apresentam o raciocínio esperado, não frases que precisam ser decoradas.

## Fontes e notas de leitura

As marcações R1 a R14 remetem às [referências do capítulo](referencias.md), com autoria, datas, localização dos trechos consultados e limites de uso. Relatos de participantes são identificados como relatos; exemplos fictícios e conexões didáticas são explicações da obra, não novos acontecimentos históricos.

Este capítulo não contém um laboratório executável. A atividade proposta é interpretar os episódios e justificar respostas. O [registro editorial](../../../editorial/reviews/capitulo-2.md) documenta a verificação realizada e distingue o fechamento interno de uma revisão especializada independente.

**[Continuar para o Capítulo 3 — Ética, legalidade, autorização e escopo →](../capitulo-3/README.md)**
