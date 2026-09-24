# Glossário

[Índice do livro](README.md) · [Módulo I](modulo-1/README.md) · [Módulo II](modulo-2/README.md) · [Bibliografia](bibliografia.md)

Este glossário acompanha os termos presentes na obra. Cada entrada aponta para uma ocorrência; a definição curta não substitui o capítulo. **Uma menção introdutória não significa que o assunto já foi ensinado em profundidade.**

Não importamos todos os assuntos futuros. OSINT é identificado como menção do planejamento, incluída para esclarecer a sigla solicitada na revisão. Os demais verbetes se relacionam ao texto ou às referências dos capítulos disponíveis.

**Consulta:** [A](#a) · [B](#b) · [C](#c) · [D](#d) · [E](#e) · [F](#f) · [G](#g) · [H](#h) · [I](#i) · [K](#k) · [L](#l) · [M](#m) · [N](#n) · [O](#o) · [P](#p) · [R](#r) · [S](#s) · [T](#t) · [U](#u) · [V](#v) · [W](#w) · [X](#x).

## A

### Abstração digital

Modelo que trata sinais como valores discretos, por exemplo 0 e 1, sem representar a cada operação todos os detalhes físicos de sua implementação. Suas garantias dependem das condições de funcionamento do dispositivo. [Conceito: 6.1][c61].

### Active Directory

Tecnologias de diretório da Microsoft. No contexto de domínios citado, Active Directory Domain Services organiza objetos, como usuários e computadores, e participa da administração de identidades e acesso. [Menção: capítulo 2][c2]. [Documentação][ad-doc].

### Ameaça

Circunstância ou evento com potencial de causar consequência adversa de segurança. Não designa necessariamente uma pessoa; também pode envolver condições acidentais. [Conceito: 5.2][c52].

### API

Application Programming Interface, interface de programação de aplicações. Define uma forma de componentes de software interagirem; nem toda API é um serviço Web. [Menção introdutória: capítulo 2][c2].

### ASCII

American Standard Code for Information Interchange. Código de sete bits com 128 posições, incluindo letras, dígitos, pontuação e controles. A letra A tem valor decimal 65, ou hexadecimal 41. O ASCII básico não representa todo o texto Unicode. [Conceito: 6.4][c64].

### Ativo

Algo com valor para pessoas ou organizações, como informação, equipamento, serviço ou capacidade. Não é apenas o computador que guarda os dados. [Conceito: 5.1][c51].

### Autenticação

Verificação de uma identidade ou alegação de identidade. Reconhecer uma conta não determina, sozinho, quais dados ela pode acessar. [Conceito: 5.1][c51].

### Autorização

Decisão sobre a permissão para uma ação ou recurso. A autorização aplicada pelo sistema e a autorização humana para conduzir um teste são distintas. [Controle de acesso: 5.1][c51]. [Permissão de teste: 3.1][c31].

### AWS

Amazon Web Services. Provedor de nuvem citado para distinguir testes em recursos do cliente de testes na infraestrutura do provedor. A menção não autoriza testes. [Contexto: 3.1][c31].

## B

### Banco de dados

Conjunto organizado de dados mantido para consulta e atualização. A aplicação pode utilizá-lo para guardar registros; o sistema que gerencia os dados não deve ser confundido com a informação armazenada. [Menção: capítulo 1][c1]; [exemplo: 5.1][c51].

### Base numérica

Quantidade de algarismos e fator entre pesos de posições em uma representação posicional. O mesmo valor pode ser escrito em bases diferentes; a mudança de escrita não muda a quantidade representada. [Conceito: 6.2][c62].

### Big-endian

Ordem que coloca primeiro o byte de maior peso de um valor com vários bytes. Não significa inverter os bits de cada byte. [Conceito: 6.3][c63].

### Binário

No sistema de numeração apresentado, base dois: usa os algarismos 0 e 1 e pesos que são potências de dois. O termo também aparece em computação com outros sentidos; o contexto deve identificá-los. [Conceito: 6.2][c62].

### Bit

Binary digit, dígito binário. Posição com dois valores possíveis, 0 ou 1. O significado desses valores depende da convenção; a largura de uma sequência não demonstra sozinha imprevisibilidade. [Conceito: 6.1][c61].

### Black hat

Rótulo informal associado a atividade ofensiva maliciosa ou não autorizada. Não substitui a análise de permissão, conduta e impacto. [Contexto: capítulo 1][c1].

### Blue box

Dispositivo histórico empregado para produzir sinais usados em certos sistemas telefônicos. Não era uma chave universal de redes; o exemplo não é apresentado como técnica para telefonia atual. [Contexto: capítulo 2][c2].

### Bug

Defeito no comportamento ou implementação de um programa. Sua relação com segurança depende das condições e consequências; comportamento estranho não é automaticamente vulnerabilidade. [Conceito: 5.1][c51].

### Bug Bounty

Programa que pode recompensar relatos de vulnerabilidades conforme seus critérios. Autorização, escopo, divulgação e elegibilidade para pagamento são questões diferentes. [Contexto: capítulo 2][c2] e [3.1][c31].

### Burp Suite

Conjunto de ferramentas da PortSwigger para segurança Web. O Burp Proxy permite examinar e modificar tráfego que passa por ele; não observa qualquer comunicação apenas por estar aberto. [Menção: capítulo 1][c1]. [Documentação][burp-doc].

### Byte

Unidade de oito bits no escopo desta obra, representada por B nas unidades. Oferece 256 padrões e não equivale necessariamente a um caractere. [Conceito: 6.3][c63].

## C

### Cache

Armazenamento para reutilização. Em HTTP, conserva respostas sob condições do protocolo. Receber novamente uma resposta não comprova novo processamento na origem. [Conceito: 4.2][c42].

### Causalidade

Relação em que uma condição ou ação contribui para produzir um efeito. Observar dois acontecimentos juntos não basta para estabelecê-la. [Conceito: 4.3][c43].

### CERT/CC

CERT Coordination Center, do Software Engineering Institute da Carnegie Mellon University. Aparece na resposta coordenada após o Morris Worm. É uma instituição, não o autor ou nome do programa. [Contexto: capítulo 2][c2].

### CISA

Cybersecurity and Infrastructure Security Agency. Organização dos Estados Unidos responsável pelo get.gov, cuja política aparece como exemplo de delimitação de pesquisa. [Contexto: 3.1][c31].

### Cloud

Computação em nuvem: recursos de computação disponibilizados como serviços por rede. A introdução distingue os recursos do cliente da infraestrutura do provedor e suas condições de teste. [Contexto: 3.1][c31].

### Cluster de grafemas

Agrupamento de pontos de código utilizado na segmentação de texto para aproximar uma unidade percebida pelo usuário. Um agrupamento pode conter vários pontos de código e vários bytes; essas contagens não são equivalentes. [Conceito: 6.4][c64].

### Codificação

Regra para representar informação. No caso do texto, especifica como valores de caracteres são convertidos em uma sequência de unidades, como bytes em UTF-8. Não deve ser confundida com criptografia. [Conceito: 6.4][c64].

### Complemento de dois

Convenção de representação de inteiros com sinal em que o bit de maior peso recebe peso negativo. Com oito bits, representa −128 a 127; a sequência de oito uns representa −1. [Conceito: 6.3][c63].

### Confidencialidade

Preservação das restrições de acesso e divulgação. Não significa tornar tudo secreto: um catálogo público e um histórico privado têm regras diferentes. [Conceito: 5.1][c51].

### Correlação

Associação observada entre acontecimentos ou variáveis. Pode orientar a investigação, mas não demonstra sozinha que um deles causou o outro. [Conceito: 4.3][c43].

### Credencial

Informação ou meio utilizado para comprovar uma identidade, como senha ou chave. Sua posse não comprova autorização para utilizá-la em uma investigação. [Conceito: 5.2][c52]; [exemplo: soluções do capítulo 3][c3-sol].

### CSRC

Computer Security Resource Center, do NIST. Portal de referências e glossários usado nas notas de pesquisa, não uma ferramenta de exploração. [Ocorrência: referências do capítulo 5][c5-ref].

### CTF

Capture the Flag. Formato de desafio de segurança realizado sob as regras de um ambiente preparado. Sua autorização não se estende a sistemas externos. [Menção: capítulo 1][c1].

### CVE

Common Vulnerabilities and Exposures. Identificação e registros de vulnerabilidades publicamente conhecidas. Um número ajuda a comunicar um caso; sua ausência não demonstra ausência de vulnerabilidade. [Conceito: 5.1][c51].

### CVSS

Common Vulnerability Scoring System. Sistema de descrição e pontuação da severidade de vulnerabilidades. O escore Base não é porcentagem de chance de ataque nem avaliação completa de risco. [Conceito: 5.3][c53].

### CWE

Common Weakness Enumeration. Catálogo de tipos de fraquezas de software e hardware. Descreve padrões de problema, função diferente da identificação de casos por CVE. [Conceito: 5.1][c51].

## D

### DARPA

Defense Advanced Research Projects Agency. Agência citada por solicitar ao SEI uma capacidade de resposta após o incidente de 1988. [Contexto: capítulo 2][c2].

### Dados pessoais

No contexto brasileiro discutido, informações relacionadas a pessoa natural identificada ou identificável. Um teste não elimina as obrigações sobre seu tratamento. [Contexto: 3.2][c32].

### Dados sintéticos

Dados construídos para representar situações sem reproduzir registros pessoais reais. Trocar somente um nome em um registro real não o torna automaticamente sintético. [Exemplos: 3.2][c32].

### Decimal

Sistema de numeração de base dez, com algarismos de 0 a 9. Em notação posicional, cada posição à esquerda tem dez vezes o peso da anterior. Aqui o termo descreve a base, não um tipo específico de dados de uma linguagem. [Conceito: 6.2][c62].

### Disponibilidade

Possibilidade de acesso e uso por quem está autorizado quando necessário. Recusar todos os pedidos não é correção suficiente se os usos legítimos também deixam de funcionar. [Conceito: 5.1][c51].

### Divulgação coordenada

Coordenação entre participantes que descobrem, corrigem, utilizam e comunicam informações sobre vulnerabilidades. Não é sinônimo de programa de recompensas. [Contexto: capítulo 2][c2].

### DOI

Digital Object Identifier. Identificador persistente usado para referenciar objetos, como publicações. Não certifica a correção do conteúdo nem substitui sua leitura. [Ocorrência: referências do capítulo 2][c2-ref].

## E

### Encadeamento de vulnerabilidades

Combinação de condições em que o resultado de uma etapa permite avançar para outra. Cada ligação exige evidência; leitura indevida não implica automaticamente controle de todo o ambiente. [Conceito: 5.2][c52].

### Endianness

Ordem dos bytes na representação de um valor com vários bytes. Interpretar a mesma sequência em big-endian ou little-endian pode produzir números distintos. O formato precisa definir a convenção. [Conceito: 6.3][c63].

### Engenharia reversa

Análise de um sistema ou artefato para compreender sua estrutura e funcionamento a partir do que está disponível. É citada como especialização, sem técnica detalhada nesta introdução. [Menção: capítulo 2][c2].

### Enumeração

Levantamento sistemático de informações sobre elementos de um ambiente, como usuários, serviços ou permissões. Não equivale, sozinho, à exploração de uma falha. [Menções: capítulo 1][c1].

### Escalada de privilégios

Obtenção de permissões ou capacidades superiores às do contexto inicial. Executar código e executar com privilégio administrativo são situações distintas. [Menção: capítulo 1][c1].

### Escopo

Delimitação do que será avaliado e das condições da avaliação. Descobrir um sistema conectado não amplia automaticamente a autorização. [Conceito: 3.1][c31].

### Ethical hacking

Hacking ético. Na obra, investigação ofensiva conduzida com autorização, escopo e responsabilidade. Intenção de ajudar não substitui permissão. [Contexto: capítulo 1][c1] e [capítulo 3][c3].

### Evidência

Informação que sustenta ou contraria uma afirmação sob condições identificadas. A procedência e os limites importam; uma tela não comprova automaticamente a explicação atribuída a ela. [Conceito: 4.3][c43].

### Exploit

Método ou artefato que aproveita uma vulnerabilidade. Não é a própria fraqueza; publicar um código não comprova vulnerabilidade de qualquer instalação do produto. [Conceito: 5.2][c52].

### Exposição

Condição de alcance: quem consegue interagir, por qual caminho e sob quais circunstâncias. Uma função exposta não é necessariamente vulnerável. [Conceito: 5.3][c53].

## F

### Falso negativo

Falha em identificar uma condição que o detector deveria reconhecer e que estava presente. Ausência de alerta não permite contar, por si só, problemas não detectados. [Conceito: 4.3][c43].

### Falso positivo

Indicação de uma condição ausente no caso classificado. Um alerta não verificado pode ser inconclusivo, sem ser automaticamente verdadeiro ou falso. [Conceito: 4.3][c43].

### FIRST

Forum of Incident Response and Security Teams. Organização responsável pela documentação CVSS citada no capítulo 5. A referência não representa endosso ao livro. [Contexto: 5.3][c53].

### Fonte de ameaça

Origem de ação ou condição capaz de explorar ou acionar uma fraqueza. Pode envolver intenção adversarial ou circunstâncias acidentais. [Conceito: 5.2][c52].

### Fronteira de confiança

Limite entre contextos com permissões, controle ou suposições de confiança diferentes. Atravessá-lo exige examinar quais decisões e verificações deveriam ocorrer. [Menção: capítulo 1][c1].

## G

### Gray hat

Rótulo informal usado para situações que misturam características atribuídas a white hat e black hat. Não constitui autorização nem categoria jurídica adotada pelo livro. [Contexto: capítulo 1][c1].

## H

### Hack

Termo com diferentes sentidos históricos, como solução engenhosa, modificação criativa ou exploração de um sistema. Seu significado depende do contexto. [Conceito: capítulo 1][c1].

### Hacker

Termo que pode designar quem explora sistemas em profundidade ou, em outros contextos, pessoas associadas a intrusões. A palavra isolada não comprova intenção ou autorização. [Conceito: capítulo 1][c1].

### Hash

Resultado de uma função que transforma uma entrada segundo um algoritmo. No contexto de senhas citado, testar candidatos contra hashes não significa descriptografar a senha. [Menção: capítulo 1][c1].

### Hashcat

Ferramenta de recuperação e auditoria de senhas que testa candidatos contra representações compatíveis, como hashes. Não é uma operação universal para descobrir qualquer senha. [Menção: capítulo 1][c1]. [Documentação][hashcat-doc].

### Hexadecimal

Sistema de base dezesseis, com algarismos 0–9 e A–F. Um algarismo hexadecimal corresponde a quatro bits; um byte pode ser exibido com dois deles. É notação, não criptografia. [Conceito: 6.2][c62].

### Hipótese

Explicação provisória a confrontar com observações e alternativas. É mais útil quando permite prever um resultado e dizer o que a contrariaria. [Conceito: 4.1][c41].

### HTTP

Hypertext Transfer Protocol. Protocolo de requisições e respostas usado na Web. O código de status integra a resposta, mas não comprova sozinho qual conteúdo ou decisão de acesso ocorreu. [Conceito: 4.3][c43].

### HTTPS

HTTP utilizado por conexão protegida com TLS. Proteger o canal não demonstra correção da aplicação, e o número 443 não certifica o protocolo utilizado. [Menção: capítulo 1][c1]. [Semântica do esquema][https-rfc].

## I

### IA

Inteligência artificial. A sigla aparece em aplicações com modelos de linguagem e no apoio editorial. Conteúdo produzido por IA não é, por si só, evidência nem revisão independente. [Contexto: 4.4][c44].

### Identificador

Valor utilizado para distinguir um objeto ou registro. Conhecê-lo não equivale a ter permissão para consultar o objeto. [Conceito: 5.1][c51].

### Impacto

Consequência de uma falha ou ação. Distinguir impacto observado de impacto possível e limitar a afirmação ao que as evidências sustentam. [Conceito: 5.2][c52].

### Inferência

Conclusão construída a partir de observações e premissas. Não equivale ao registro bruto produzido por tela ou ferramenta. [Conceito: 4.1][c41].

### Inteiro com sinal

Representação numérica que admite valores negativos e não negativos. É preciso conhecer a convenção, como complemento de dois, e a largura em bits para interpretar o campo. [Conceito: 6.3][c63].

### Inteiro sem sinal

Representação de inteiros não negativos. Em n bits com todos os padrões utilizados, sua faixa é de zero a `2^n − 1`. [Conceito: 6.3][c63].

### Integridade

Proteção contra alteração ou destruição indevida. Alterar uma data sem permissão é consequência diferente de consultar informação privada. [Conceito: 5.1][c51].

## K

### Kali Linux

Distribuição Linux preparada para tarefas de segurança. O ambiente e suas ferramentas não comprovam habilidade nem autorização de quem os utiliza. [Menção: capítulo 1][c1]. [Documentação][kali-doc].

### kB e KiB

kB, kilobyte, representa 1.000 bytes; KiB, kibibyte, representa 1.024 bytes. Os prefixos decimal e binário não são grafias equivalentes da mesma quantidade. [Conceito: 6.3][c63].

### Kerberos

Protocolo de autenticação em rede baseado em tickets e em uma autoridade de confiança. É mencionado como mecanismo de identidade que terá desenvolvimento próprio. [Menção: capítulo 1][c1]. [Especificação V5][kerberos-rfc].

## L

### LGPD

Lei Geral de Proteção de Dados Pessoais, Lei brasileira nº 13.709/2018. O capítulo 3 introduz sua relação com evidências, sem emitir parecer sobre uma operação real. [Contexto: 3.2][c32].

### Linha de base

Referência de comportamento em condições identificadas. Ajuda a comparar um caso legítimo com o investigado sem confundir falha geral do serviço com decisão correta de autorização. [Conceito: 4.2][c42].

### Little-endian

Ordem que coloca primeiro o byte de menor peso de um valor com vários bytes. A convenção deve ser definida pelo formato ou operação, não adivinhada pela aparência dos dados. [Conceito: 6.3][c63].

### Log

Registro de eventos produzido por um sistema. Seu valor depende dos campos, procedência, cobertura e relação com a operação examinada. [Conceito: 4.3][c43].

## M

### MB e MiB

MB, megabyte, representa 1.000.000 de bytes; MiB, mebibyte, representa 1.048.576. Uma taxa em Mbit/s mede bits por segundo, não bytes armazenados. [Conceito: 6.3][c63].

### Metasploit

Framework de segurança com módulos para tarefas distintas, inclusive exploração. O livro usa sua terminologia para separar exploit e payload, sem afirmar que toda falha segue essa arquitetura. [Conceito: 5.2][c52].

### MF

Multifrequency, sinalização multifrequência. Na telefonia histórica discutida, combinações de tons representavam endereçamento. É diferente do tom único de supervisão de certas ligações. [Contexto: capítulo 2][c2].

### MIT

Massachusetts Institute of Technology, instituição à qual pertence o TMRC. A sigla também nomeia uma licença de software no repositório; são usos distintos. [Contexto histórico][c2]. [Licenciamento](../LICENSE.md).

### Modelo de linguagem

Modelo computacional usado para processar ou gerar linguagem. A introdução menciona aplicações que recebem contexto e instruções; nem todo modelo possui ferramentas externas. [Menção: capítulo 2][c2].

### Morris Worm

Programa autorreplicante associado a Robert Tappan Morris e ao incidente de novembro de 1988. Não é a pessoa do episódio do apito telefônico nem a origem única de cybersecurity. [Contexto: capítulo 2][c2].

### Movimentação lateral

Uso de acesso ou relação de confiança para alcançar outros sistemas ou contextos do ambiente. Pode combinar-se com escalada de privilégios, mas não é a mesma atividade. [Menção: capítulo 1][c1].

## N

### NBS

National Bureau of Standards. Instituição identificada no relatório histórico do workshop de segurança de 1972. A sigla é preservada conforme a fonte histórica. [Contexto: capítulo 2][c2].

### NIST

National Institute of Standards and Technology. Instituição que mantém referências e glossários utilizados no livro. As definições agregadas podem vir de documentos e contextos diferentes. [Contexto: 5.1][c51].

### Nmap

Network Mapper. Ferramenta de exploração e auditoria de redes, incluindo descoberta e investigação de portas e serviços. O resultado exige interpretação, não diagnóstico automático de vulnerabilidade. [Menção: capítulo 1][c1]. [Documentação][nmap-doc].

## O

### Observação

Informação registrada por um meio identificado. Pode ter limites ou erros de medição e não contém automaticamente a explicação da causa do que foi percebido. [Conceito: 4.1][c41].

### Octeto

Grupo de oito bits. O termo aparece em especificações de protocolos e explicita o tamanho que chamamos de byte no escopo da obra. [Conceito: 6.3][c63].

### OSINT

Open Source Intelligence, inteligência de fontes abertas. Conhecimento produzido a partir de informações publicamente ou comercialmente disponíveis para responder a necessidades de inteligência. Não é sinônimo de software open source.

**Menção no planejamento, ainda sem capítulo desenvolvido:** [mapa da obra](../editorial/master-outline.md). A entrada esclarece a sigla solicitada, sem registrar o assunto como já ensinado. [Referência institucional][osint-doc].

### Overflow

Estouro: situação em que um resultado não cabe na faixa da representação numérica adotada. Reação, sinalização de erro e eventual retenção de bits dependem das regras do sistema ou linguagem. [Conceito: 6.3][c63].

### OWASP

Open Worldwide Application Security Project. Fundação e comunidade que mantêm projetos e referências sobre segurança de software. Não é ferramenta única nem vulnerabilidade. [Ocorrência: 4.1][c41] e [5.1][c51]. [Sobre a fundação][owasp-about].

## P

### Payload

No contexto de exploração apresentado, componente que realiza a ação desejada após aproveitar a vulnerabilidade. Nem toda exploração possui payload executável separado. [Conceito: 5.2][c52].

### Pentest

Penetration test, teste de intrusão. Avaliação com objetivos, escopo, métodos permitidos e comunicação de resultados; não se resume à obtenção de acesso. [Contexto: capítulo 2][c2] e [capítulo 3][c3].

### Persistência

Meios de conservar ou recuperar acesso apesar de mudanças, como interrupção de uma sessão. Não é etapa obrigatória nem automaticamente autorizada após exploração. [Menção: capítulo 1][c1].

### Phone phreaking

Investigação e manipulação de mecanismos de redes telefônicas. O capítulo discute episódios históricos, sem generalizar métodos para redes atuais ou autorizá-los. [Contexto: capítulo 2][c2].

### Pivotamento

Uso de um ponto intermediário para alcançar recursos que não eram diretamente acessíveis da origem da investigação. Depende do escopo autorizado. [Menção: capítulo 1][c1].

### Ponto de código

Identificador numérico de uma posição no espaço Unicode, escrito frequentemente como U+ seguido de hexadecimal. Não é sinônimo de byte nem de uma unidade visual de texto. [Conceito: 6.4][c64].

### Porta de rede

Identificador usado por protocolos de transporte para distinguir pontos de comunicação. O número isolado não certifica qual serviço está sendo executado. [Menção: capítulo 1][c1].

### Pós-exploração

Análise e atividades posteriores ao acesso obtido por exploração, como investigar contexto, permissões e alcance. O objetivo determina o que é necessário e autorizado. [Introdução: capítulo 1][c1].

### Previsão

Resultado que uma hipótese leva a esperar em condições especificadas, formulado antes de observar a execução. Não é evidência de que ocorreu. [Conceito: 4.1][c41].

### Privilégio

Permissão ou capacidade associada a uma identidade ou contexto de execução. Saber que código foi executado não informa, sozinho, quais permissões ele possuía. [Menção: capítulo 1][c1].

### Prompt injection

Manipulação de entradas ou conteúdos processados por uma aplicação com modelo de linguagem para influenciar indevidamente seu comportamento. Os efeitos dependem do contexto e das capacidades da aplicação; não é equivalente a SQL injection. [Menções: capítulos 1][c1] e [2][c2]. [Referência][prompt-doc].

### Protocolo

Convenções que permitem a sistemas interpretar uma comunicação. Conhecê-las ajuda a compreender os significados e limites de uma resposta. [Menção: capítulo 1][c1]; [exemplo HTTP: 4.3][c43].

### Prova de conceito (PoC)

Proof of concept. Demonstração de uma possibilidade em condições determinadas. Não comprova automaticamente comprometimento de produção ou ocorrência de ataque anterior. [Conceito: 5.2][c52].

### PTES

Penetration Testing Execution Standard. Referência metodológica para testes de intrusão. O capítulo usa sua distinção entre escopo e regras de engajamento, sem adotar toda recomendação histórica como atual. [Contexto: 3.1][c31].

## R

### Ransomware

Software malicioso usado para restringir acesso a dados ou sistemas e exigir resgate, frequentemente por criptografia de arquivos. A introdução apenas menciona a categoria, sem análise de amostras. [Menção: capítulo 1][c1]. [Referência CISA][ransomware-doc].

### Red Team

Atividade ou equipe que utiliza uma perspectiva adversarial orientada a objetivos para avaliar uma organização e suas defesas. Não é automaticamente sinônimo de pentest. [Menção: capítulo 1][c1].

### Regras de engajamento

Condições sobre como conduzir o teste, incluindo métodos, janela de execução, comunicação e interrupção. Complementam a definição de escopo. [Conceito: 3.1][c31].

### Requisição

Mensagem em que um componente solicita uma operação a outro. Em HTTP, seu significado depende de método, destino e demais elementos, a serem aprofundados no módulo de redes. [Introdução: 4.3][c43].

### Resposta

Mensagem devolvida em relação a uma requisição. Código de status e conteúdo precisam ser interpretados juntos, no contexto da operação. [Introdução: 4.3][c43].

### RFC

Request for Comments. Documento numerado de uma série de especificações e outros materiais técnicos. Nem toda RFC é um padrão; categoria e contexto importam. [Menção: capítulo 1][c1]; [referências do capítulo 4][c4-ref].

### Risco

Relação entre possibilidade de um evento adverso e consequências no contexto analisado. Não é sinônimo de vulnerabilidade ou nota de severidade. [Conceito: 5.3][c53].

### Risco residual

Risco que permanece depois de controles ou respostas. Uma medida pode melhorar o cenário sem eliminar todas as possibilidades relevantes. [Conceito: 5.3][c53].

## S

### Safe harbor

Compromisso de uma organização sobre pesquisa de boa-fé, sob condições declaradas. Não amplia automaticamente o escopo nem equivale a imunidade universal perante terceiros. [Conceito: 3.1][c31].

### Scanner

Ferramenta que automatiza observações ou testes. Descoberta de serviços e detecção de vulnerabilidades são tarefas distintas; alerta não substitui investigação. [Menção: capítulo 1][c1]; [conceito: 4.3][c43].

### security.txt

Arquivo padronizado pela RFC 9116 para indicar contatos e informações de divulgação de vulnerabilidades. Sua presença não concede, sozinha, autorização para testar. [Conceito: 3.1][c31].

### SEI

Software Engineering Institute, da Carnegie Mellon University. Instituição associada à criação do CERT/CC no episódio histórico discutido. [Contexto: capítulo 2][c2].

### Servidor

Programa que atende solicitações; a palavra também pode designar o computador que o executa. Distinguir programa, serviço e equipamento evita conclusões imprecisas. [Conceito: 5.1][c51].

### Sessão

Contexto usado por uma aplicação para associar interações, frequentemente a uma identidade autenticada. Duas abas visíveis não comprovam isolamento entre sessões. [Conceito: 4.2][c42].

### Severidade

Descrição da gravidade de uma vulnerabilidade segundo critérios determinados. Não equivale sozinha ao risco para uma organização específica. [Conceito: 5.3][c53].

### Sinalização em banda

Sinais de controle transmitidos pelo mesmo canal do conteúdo de uso, como voz no exemplo telefônico. Supervisão e endereçamento são funções distintas. [Conceito histórico: capítulo 2][c2].

### SQL

Linguagem de definição, consulta e manipulação de dados em sistemas de banco de dados que a implementam. Aparece na introdução à SQL injection e terá desenvolvimento próprio adiante. [Menção: capítulo 1][c1].

### SQL injection

Falha em que uma entrada influencia indevidamente a estrutura ou significado de uma consulta SQL. Não é qualquer erro de banco de dados. [Menção: capítulo 1][c1]. [Referência técnica][sqli-doc].

### Superfície de ataque

Pontos e caminhos pelos quais um sistema pode ser alcançado ou influenciado, incluindo interfaces, dados e contextos de acesso. É um mapa do que examinar, não lista de falhas confirmadas. [Conceito: 5.3][c53].

## T

### Terminal

Interface de entrada e saída de texto para interagir com programas, inclusive interpretadores de comandos. Não é o mesmo componente que interpreta a linguagem de comandos. [Menção: capítulo 1][c1].

### TMRC

Tech Model Railroad Club, clube de ferromodelismo do MIT presente nos episódios de experimentação. Sua história não estabelece origem única da segurança de computadores. [Contexto: capítulos 1][c1] e [2][c2].

### Truncamento

Corte de uma sequência ou representação para um tamanho menor. Em texto de largura variável, cortar em um byte arbitrário pode interromper uma sequência de caractere; o formato precisa ser respeitado. [Conceito: 6.4][c64].

## U

### Unicode

Padrão para representar caracteres, com pontos de código e formas de codificação. Identificar um ponto de código e escolher seus bytes são etapas distintas; Unicode não significa que toda letra ocupa um ou dois bytes. [Conceito: 6.4][c64].

### UTF-8

Forma de codificação Unicode que utiliza de um a quatro bytes por valor escalar e preserva a representação ASCII. Uma unidade percebida pelo usuário pode reunir vários valores; nem toda sequência arbitrária de bytes é UTF-8 válido. [Conceito: 6.4][c64].

## V

### VDP

Vulnerability Disclosure Policy, política de divulgação de vulnerabilidades. Define canais e condições para comunicar falhas e pode delimitar pesquisa autorizada. Não significa automaticamente pagamento de recompensas. [Conceito: 3.1][c31].

### Vulnerabilidade

Fraqueza em código, configuração, controle, procedimento ou implementação que pode ser explorada ou acionada para produzir consequência adversa. Pode existir sem exploit público. [Conceito: 5.1][c51].

## W

### White hat

Rótulo informal associado a pesquisa ou avaliação autorizada e voltada à proteção. Não comprova por si só a autorização de uma atividade específica. [Contexto: capítulo 1][c1].

### Worm

Programa capaz de se executar independentemente e propagar cópias funcionais para outras máquinas. No caso Morris Worm, o primeiro termo identifica o autor e o segundo o tipo de programa. [Conceito: capítulo 2][c2].

## X

### XSS

Cross-Site Scripting. Classe de falha em que conteúdo controlado por um atacante pode executar código no navegador no contexto de uma aplicação Web. É distinta de SQL injection. [Menção: capítulo 2][c2]. [Referência técnica][xss-doc].

---

As definições metodológicas expressam o vocabulário de trabalho do livro. As fontes dos conceitos estão nos capítulos; documentação complementar aparece em verbetes introdutórios. Uma ocorrência comprova que o termo está na obra, não que já foi aprofundado. [Como manter o glossário](../editorial/glossary-policy.md).

[c1]: modulo-1/capitulo-1/README.md
[c2]: modulo-1/capitulo-2/README.md
[c3]: modulo-1/capitulo-3/README.md
[c31]: modulo-1/capitulo-3/3.1-autorizacao-e-escopo.md
[c32]: modulo-1/capitulo-3/3.2-evidencias-e-responsabilidade.md
[c41]: modulo-1/capitulo-4/4.1-observacao-e-hipoteses.md
[c42]: modulo-1/capitulo-4/4.2-testes-e-comparacoes.md
[c43]: modulo-1/capitulo-4/4.3-resultados-e-evidencias.md
[c44]: modulo-1/capitulo-4/4.4-conclusoes-e-limites.md
[c51]: modulo-1/capitulo-5/5.1-ativos-e-vulnerabilidades.md
[c52]: modulo-1/capitulo-5/5.2-ameacas-e-exploracao.md
[c53]: modulo-1/capitulo-5/5.3-superficie-e-risco.md
[c61]: modulo-2/capitulo-6/6.1-bits-e-estados.md
[c62]: modulo-2/capitulo-6/6.2-binario-e-hexadecimal.md
[c63]: modulo-2/capitulo-6/6.3-bytes-limites-e-unidades.md
[c64]: modulo-2/capitulo-6/6.4-texto-e-interpretacao.md
[c2-ref]: modulo-1/capitulo-2/referencias.md
[c3-sol]: modulo-1/capitulo-3/solucoes.md
[c4-ref]: modulo-1/capitulo-4/referencias.md
[c5-ref]: modulo-1/capitulo-5/referencias.md
[ad-doc]: https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview
[burp-doc]: https://portswigger.net/burp/documentation/desktop/tools/proxy
[hashcat-doc]: https://hashcat.net/wiki/doku.php?id=hashcat
[https-rfc]: https://www.rfc-editor.org/rfc/rfc9110.html#section-4.2.2
[kali-doc]: https://www.kali.org/docs/introduction/what-is-kali-linux/
[kerberos-rfc]: https://www.rfc-editor.org/rfc/rfc4120
[nmap-doc]: https://nmap.org/book/man.html
[osint-doc]: https://archive.dni.gov/files/documents/ICD/ICS-206-01.pdf
[owasp-about]: https://owasp.org/about
[prompt-doc]: https://genai.owasp.org/llmrisk/llm01-prompt-injection/
[ransomware-doc]: https://www.cisa.gov/stopransomware/ransomware-guide
[sqli-doc]: https://portswigger.net/web-security/sql-injection
[xss-doc]: https://portswigger.net/web-security/cross-site-scripting
