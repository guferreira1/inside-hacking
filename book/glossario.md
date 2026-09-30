# Glossário

[Índice do livro](README.md) · [Módulo I](modulo-1/README.md) · [Módulo II](modulo-2/README.md) · [Módulo III](modulo-3/README.md) · [Bibliografia](bibliografia.md)

Este glossário acompanha os termos presentes na obra. Cada entrada aponta para uma ocorrência; a definição curta não substitui o capítulo. **Uma menção introdutória não significa que o assunto já foi ensinado em profundidade.**

Não importamos todos os assuntos futuros. OSINT é identificado como menção do planejamento, incluída para esclarecer a sigla solicitada na revisão. Os demais verbetes se relacionam ao texto ou às referências dos capítulos disponíveis.

**Consulta:** [A](#a) · [B](#b) · [C](#c) · [D](#d) · [E](#e) · [F](#f) · [G](#g) · [H](#h) · [I](#i) · [J](#j) · [K](#k) · [L](#l) · [M](#m) · [N](#n) · [O](#o) · [P](#p) · [Q](#q) · [R](#r) · [S](#s) · [T](#t) · [U](#u) · [V](#v) · [W](#w) · [X](#x) · [Y](#y).

## A

### ABI

Application Binary Interface, interface binária de aplicação. Conjunto de convenções para interação entre componentes binários, como passagem de argumentos, retorno e uso de registradores. Compartilhar uma ISA não garante compartilhar todas essas convenções. [Conceito: 8.3][c83].

### Abstração

Apresentação de operações e garantias que permite trabalhar sem administrar todos os detalhes internos. Não elimina as condições de existência, acesso, custo ou falha do recurso. [Conceito: 11.1][c111].

### Abstração digital

Modelo que trata sinais como valores discretos, por exemplo 0 e 1, sem representar a cada operação todos os detalhes físicos de sua implementação. Suas garantias dependem das condições de funcionamento do dispositivo. [Conceito: 6.1][c61].

### ACE

Access Control Entry. Entrada em uma lista de controle de acesso que relaciona direitos a uma identidade; seu tipo e sua posição importam na interpretação. [Conceito: 13.4](modulo-3/capitulo-13/13.4-contas-tokens-e-controle-de-acesso.md).

### ACL

Access Control List. Lista de controle de acesso. ACLs POSIX Linux e DACLs Windows possuem modelos distintos, que não devem ser reduzidos a uma única regra de avaliação. [Conceito: 15.3](modulo-3/capitulo-15/15.3-criacao-propriedade-e-acls.md).

### ACL padrão

ACL de um diretório que participa da formação da política inicial de novos objetos. Alterá-la não reescreve automaticamente os objetos já existentes. [Conceito: 15.3](modulo-3/capitulo-15/15.3-criacao-propriedade-e-acls.md).

### Active Directory

Tecnologias de diretório da Microsoft. No contexto de domínios citado, Active Directory Domain Services organiza objetos, como usuários e computadores, e participa da administração de identidades e acesso. [Menção: capítulo 2][c2]. [Documentação][ad-doc].

### AdjustTokenPrivileges

API Windows para alterar o estado de privilégios presentes num token. Não acrescenta privilégios que o token não possui. [Conceito: 15.5](modulo-3/capitulo-15/15.5-privilegios-e-delegacao.md).

### Administrador

Conta ou membro de grupo com atribuições administrativas. A associação a um grupo, a elevação de um processo e seu token efetivo não são a mesma informação. [Conceito: 13.4](modulo-3/capitulo-13/13.4-contas-tokens-e-controle-de-acesso.md).

### Administrator protection

Proteção de administrador. Mecanismo documentado pela Microsoft que utiliza uma conta gerenciada pelo sistema e separação de perfil para a execução elevada em ambientes compatíveis. [Conceito: 13.4](modulo-3/capitulo-13/13.4-contas-tokens-e-controle-de-acesso.md).

### Agendador de Tarefas

Task Scheduler. Componente que organiza ações a partir de gatilhos e condições. Não é o escalonador de threads que distribui tempo de CPU. [Conceito: 13.6](modulo-3/capitulo-13/13.6-inicializacao-servicos-e-investigacao.md).

### Alias

Nome alternativo que o shell pode resolver para outro comando ou texto, conforme as regras da linguagem. Não é necessariamente um arquivo executável. [Conceito: 14.1](modulo-3/capitulo-14/14.1-terminal-shell-e-comandos.md).

### Alocação dinâmica

Obtenção de espaço cujo tamanho ou duração pode ser decidido durante a execução. No percurso C, seu contrato é distinto da duração de variáveis automáticas e estáticas. Um pedido ao alocador não equivale necessariamente a uma nova região física exclusiva. [Conceito: 9.3][c93].

### ALU

Arithmetic Logic Unit, unidade aritmética e lógica. Componente que realiza operações como somas e comparações no caminho de execução do processador. Seu papel é distinto do armazenamento de um resultado ou da gravação de um arquivo. [Conceito: 7.2][c72].

### Ambiente virtual Python

Ambiente de interpretador e pacotes organizado, por exemplo, com venv. Seu recorte de dependências não é uma promessa de confinamento de todo o código executado. [Conceito: 17.1](modulo-3/capitulo-17/17.1-virtualizacao-e-fronteiras.md).

### Ameaça

Circunstância ou evento com potencial de causar consequência adversa de segurança. Não designa necessariamente uma pessoa; também pode envolver condições acidentais. [Conceito: 5.2][c52].

### API

Application Programming Interface, interface de programação de aplicações. Define uma forma de componentes de software interagirem; nem toda API é um serviço Web. [Menção introdutória: capítulo 2][c2].

### AppArmor

Mecanismo Linux que aplica controles por perfis associados a programas. É uma camada diferente dos bits tradicionais de modo. [Conceito: 15.6](modulo-3/capitulo-15/15.6-camadas-revogacao-e-menor-privilegio.md).

### APT

Advanced Package Tool. Conjunto de ferramentas que trabalha com fontes e metadados de pacotes, resolução de dependências e operações de instalação. Atualizar índices não equivale a atualizar programas instalados. [Conceito: 12.5][c125].

### Argumento

Valor fornecido a uma função, operação ou programa. No início de um programa, argumentos são uma parte do contexto recebido e não se confundem com variáveis de ambiente. [Conceitos: 8.1][c81] e [8.5][c85].

No contexto do capítulo 14: Valor fornecido a uma chamada. Preservar onde começa e termina cada argumento é diferente de preservar a aparência da linha digitada. [Conceito: 14.2](modulo-3/capitulo-14/14.2-argumentos-aspas-e-expansoes.md).

### Armazenamento persistente

Armazenamento destinado a conservar dados sem depender apenas do estado de trabalho volátil. A confirmação de uma escrita precisa ser interpretada conforme o contrato das camadas envolvidas; persistente não significa indestrutível. [Conceito: 7.4][c74].

### Arquivo de dispositivo

Objeto especial que oferece acesso a uma interface de dispositivo. Seu contrato não é necessariamente o de um arquivo regular que conserva todos os bytes escritos. [Conceito: 12.3][c123].

### Arquivo executável

Artefato preparado para iniciar um programa num ambiente compatível. Não é o processo já em funcionamento; formato, arquitetura, permissões e dependências participam de sua utilização. [Conceitos: 8.1][c81] e [8.3][c83].

### Arquivo objeto

Resultado de tradução que pode participar da ligação com outras peças. No exemplo ELF relocável, contém código e informações para resolver referências e endereços; não é automaticamente um programa completo. [Conceito: 8.2][c82].

### Arquivo regular

Tipo de objeto usado no capítulo para conservar uma sequência de bytes. A classificação no sistema de arquivos é diferente do formato do conteúdo: JSON e PNG podem ser ambos arquivos regulares. [Conceito: 10.1][c101].

### Array

Coleção indexada de valores. Neste capítulo, permite conservar argumentos separados, inclusive os que contêm espaços ou asteriscos literais. [Conceito: 14.6](modulo-3/capitulo-14/14.6-automacao-e-fronteiras-de-confianca.md).

### Artefato

Resultado concreto de uma etapa de construção, como um objeto ou executável. Alterar uma entrada do projeto não modifica automaticamente todos os artefatos já produzidos. [Conceito: 8.1][c81].

### ASCII

American Standard Code for Information Interchange. Código de sete bits com 128 posições, incluindo letras, dígitos, pontuação e controles. A letra A tem valor decimal 65, ou hexadecimal 41. O ASCII básico não representa todo o texto Unicode. [Conceito: 6.4][c64].

### ASLR

Address Space Layout Randomization. Variação da disposição de regiões do espaço de endereços, conforme suporte e configuração. Dificulta certas suposições de localização, mas não corrige por si só uma escrita fora de limites. [Conceito: 9.5][c95].

### Assembly

Representação textual de operações e outros elementos associados a uma arquitetura. A montagem a converte em código objeto; a escrita assembly não é a própria sequência binária de instruções. [Conceito: 8.2][c82].

### Assinatura de formato

Padrão de bytes usado no reconhecimento de um formato; magic bytes. Não é assinatura digital de autoria e não comprova que toda a estrutura posterior seja válida. [Conceito: 10.2][c102].

### Ativo

Algo com valor para pessoas ou organizações, como informação, equipamento, serviço ou capacidade. Não é apenas o computador que guarda os dados. [Conceito: 5.1][c51].

### AUR

Nome do formato binário didático criado no capítulo 10. Sua versão 1 transporta título e quantidade sob regras explícitas de tamanho, ordem dos bytes e validade. Não é padrão externo nem aplicação completa da Aurora. [Contrato: 10.2][c102].

### Autenticação

Verificação de uma identidade ou alegação de identidade. Reconhecer uma conta não determina, sozinho, quais dados ela pode acessar. [Conceito: 5.1][c51].

### Authenticode

Tecnologia de assinatura de código do ecossistema Windows. Sua verificação trata de autenticidade e integridade sob uma política de confiança; não comprova comportamento benigno. [Conceito: 13.3](modulo-3/capitulo-13/13.3-executaveis-bibliotecas-e-carregamento.md).

### Autorização

Decisão sobre a permissão para uma ação ou recurso. A autorização aplicada pelo sistema e a autorização humana para conduzir um teste são distintas. [Controle de acesso: 5.1][c51]. [Permissão de teste: 3.1][c31].

### AWS

Amazon Web Services. Provedor de nuvem citado para distinguir testes em recursos do cliente de testes na infraestrutura do provedor. A menção não autoriza testes. [Contexto: 3.1][c31].

## B

### Backoff

Política de espaçamento entre tentativas. No exemplo, é uma decisão de projeto; um atraso fixo não é automaticamente uma política progressiva. [Conceito: 16.3](modulo-3/capitulo-16/16.3-configuracao-parada-e-reinicio.md).

### Backport

Transporte seletivo de uma correção ou mudança para uma versão mantida anteriormente. Na segurança de pacotes, exige verificar a revisão completa e o aviso da distribuição; o termo não prova sozinho que uma instalação esteja corrigida. [Conceito: 12.5][c125].

### Backup

Cópia acompanhada de estratégia de recuperação compatível com as falhas que se pretende suportar. Pontos de retorno na mesma cadeia e armazenamento não oferecem automaticamente independência da origem. [Conceito: 17.6](modulo-3/capitulo-17/17.6-imagens-snapshots-e-recuperacao.md).

### Banco de dados

Conjunto organizado de dados mantido para consulta e atualização. A aplicação pode utilizá-lo para guardar registros; o sistema que gerencia os dados não deve ser confundido com a informação armazenada. [Menção: capítulo 1][c1]; [exemplo: 5.1][c51].

### Barramento

Caminho de comunicação entre componentes, associado a regras de transporte de dados, endereços ou comandos. A expressão não implica que toda interconexão seja um único fio compartilhado por todos os dispositivos. [Conceito: 7.1][c71].

### Base de confiança

Conjunto de componentes cujo funcionamento correto é necessário para uma garantia específica. O recorte muda conforme se pretende proteger o hospedeiro do convidado ou o convidado de parte da plataforma. [Conceito: 17.1](modulo-3/capitulo-17/17.1-virtualizacao-e-fronteiras.md).

### Base numérica

Quantidade de algarismos e fator entre pesos de posições em uma representação posicional. O mesmo valor pode ser escrito em bases diferentes; a mudança de escrita não muda a quantidade representada. [Conceito: 6.2][c62].

### Base64

Codificação que representa bytes por um alfabeto textual de 64 posições. Na forma com preenchimento estudada, três bytes produzem quatro caracteres; a transformação é reversível sem chave e não equivale a criptografia ou compressão. [Conceito: 10.3][c103].

### Base64url

Variante de Base64 com alterações no alfabeto para determinados contextos de transporte. O protocolo que a utiliza define condições como preenchimento; não se deve misturar variantes por adivinhação. [Introdução: 10.3][c103].

### Bash

Bourne-Again SHell: interpretador de comandos e linguagem do projeto GNU, com regras próprias de expansão, execução e controle. [Conceito: 14.1](modulo-3/capitulo-14/14.1-terminal-shell-e-comandos.md).

### BASH_ENV

Variável que pode indicar um arquivo de inicialização lido pelo Bash em certos contextos não interativos. Sua presença pode influenciar um script. [Conceito: 14.5](modulo-3/capitulo-14/14.5-scripts-contexto-e-repetibilidade.md).

### Biblioteca compartilhada

Objeto de software utilizado por meio de carregamento e ligação dinâmica. Seu código pode participar do contexto do processo que o carrega; estar num arquivo separado não implica isolamento automático. [Conceitos: 8.2][c82] e [8.5][c85].

### Biblioteca de software

Conjunto de código e interfaces reutilizáveis por programas. Conhecer a declaração de uma função não é o mesmo que disponibilizar sua implementação. Bibliotecas podem participar de ligações estáticas ou dinâmicas. [Conceito: 8.2][c82].

### Big-endian

Ordem que coloca primeiro o byte de maior peso de um valor com vários bytes. Não significa inverter os bits de cada byte. [Conceito: 6.3][c63].

### Binário

No sistema de numeração apresentado, base dois: usa os algarismos 0 e 1 e pesos que são potências de dois. O termo também aparece em computação com outros sentidos; o contexto deve identificá-los. [Conceito: 6.2][c62]. No capítulo 8, “um binário” pode designar um artefato de código já traduzido, não apenas a notação de um número. [Contexto: 8.1][c81].

### Bind mount

Montagem que torna uma árvore existente acessível por outro ponto. Não cria, por si só, uma cópia independente dos arquivos nem uma cópia de segurança. [Conceito: 12.2][c122].

Disponibilização de um arquivo ou diretório do hospedeiro do daemon no container, sem criar uma cópia independente por definição. Origem, destino e acesso de escrita precisam ser avaliados. [Conceito: 17.4](modulo-3/capitulo-17/17.4-compartilhamentos-e-autoridade.md).

### Bit

Binary digit, dígito binário. Posição com dois valores possíveis, 0 ou 1. O significado desses valores depende da convenção; a largura de uma sequência não demonstra sozinha imprevisibilidade. [Conceito: 6.1][c61].

### Black hat

Rótulo informal associado a atividade ofensiva maliciosa ou não autorizada. Não substitui a análise de permissão, conduta e impacto. [Contexto: capítulo 1][c1].

### Blue box

Dispositivo histórico empregado para produzir sinais usados em certos sistemas telefônicos. Não era uma chave universal de redes; o exemplo não é apresentado como técnica para telefonia atual. [Contexto: capítulo 2][c2].

### Bootloader

Carregador de inicialização. Software que conduz o carregamento ou a passagem ao próximo estágio de execução necessário ao sistema operacional. Não é sinônimo de todo o firmware da máquina. [Conceito: 7.5][c75].

### Bridge

No modo VirtualBox comparado, conecta o convidado à rede da interface física selecionada. O mesmo nome em outro produto precisa ser interpretado pelo contrato correspondente. [Conceito: 17.5](modulo-3/capitulo-17/17.5-conectividade-e-alcance.md).

### BSS

No ELF discutido, `.bss` é uma seção associada a dados cujo estado inicial zerado não exige ocupar o mesmo espaço em bytes no arquivo. Essa preparação não significa que qualquer alocação posterior, como malloc, também inicialize seus bytes. [Conceito: 9.3][c93].

### Buffer

Área temporária que guarda dados enquanto são produzidos, transferidos ou consumidos. No exemplo de dispositivos, ajuda a intermediar ritmos diferentes de entrada e processamento. [Conceito: 7.5][c75].

### Bug

Defeito no comportamento ou implementação de um programa. Sua relação com segurança depende das condições e consequências; comportamento estranho não é automaticamente vulnerabilidade. [Conceito: 5.1][c51].

### Bug Bounty

Programa que pode recompensar relatos de vulnerabilidades conforme seus critérios. Autorização, escopo, divulgação e elegibilidade para pagamento são questões diferentes. [Contexto: capítulo 2][c2] e [3.1][c31].

### Build

Nome em inglês para a construção de artefatos a partir das entradas de um projeto. Neste livro, construir e executar são atividades distintas, mesmo quando uma ferramenta as aciona no mesmo botão. [Conceito: 8.1][c81].

### Builtin

Comando implementado pelo próprio shell, em vez de depender necessariamente de um executável separado. [Conceito: 14.1](modulo-3/capitulo-14/14.1-terminal-shell-e-comandos.md).

### Burp Suite

Conjunto de ferramentas da PortSwigger para segurança Web. O Burp Proxy permite examinar e modificar tráfego que passa por ele; não observa qualquer comunicação apenas por estar aberto. [Menção: capítulo 1][c1]. [Documentação][burp-doc].

### Byte

Unidade de oito bits no escopo desta obra, representada por B nas unidades. Oferece 256 padrões e não equivale necessariamente a um caractere. [Conceito: 6.3][c63].

### Bytecode

Representação de código destinada a um mecanismo de execução, como uma máquina virtual de linguagem. Não é automaticamente código nativo da CPU nem um formato universal entre versões e implementações. [Conceito: 8.4][c84].

## C

### Cabeçalho

Header. No percurso C do capítulo 8, arquivo que reúne declarações e outras definições compartilhadas por inclusão. Em formatos como ELF, a palavra designa estruturas de metadados do artefato; são contextos diferentes. [Conceito C: 8.2][c82]; [contexto ELF: 8.3][c83]. O cabeçalho AUR reúne os campos necessários para interpretar o registro. [Exemplo: 10.2][c102].

### Cache

Armazenamento para reutilização. Em HTTP, conserva respostas sob condições do protocolo. Receber novamente uma resposta não comprova novo processamento na origem. [Conceito: 4.2][c42]. A cache de CPU conserva blocos usados pelo processamento; ela não é o mesmo componente nem segue as mesmas regras do cache HTTP. [Contexto de hardware: 7.3][c73].

### Cache de páginas

Área de memória utilizada pelo sistema para manter conteúdo associado a operações de arquivos. Pode atender leituras ou intermediar escritas antes da persistência; não é a cache interna da CPU. [Conceito: 7.4][c74].

### Cache hit

Situação em que o bloco procurado é encontrado no nível de cache examinado. Reduz a necessidade de buscá-lo em outro nível, conforme o mecanismo. [Conceito: 7.3][c73].

### Cache miss

Situação em que o bloco procurado não está no nível de cache examinado e precisa ser obtido adiante. Não representa automaticamente defeito ou falha de segurança. [Conceito: 7.3][c73].

### Caminho

Pathname. Expressão usada para localizar um objeto na organização de nomes do sistema. Um caminho relativo exige uma base; nomes diferentes podem alcançar o mesmo objeto e nomes iguais em contextos diferentes podem alcançar objetos distintos. [Conceito: 10.1][c101].

### Canonicalização

Transformação para uma representação definida por regras de um contrato, útil para comparações ou assinaturas. No caso de documentos, pode envolver ordem de campos e escrita de valores; não equivale apenas a normalizar Unicode ou retirar espaços. [Conceito: 10.6][c106].

### CAP_CHOWN

Capability Linux associada à autoridade para mudanças de propriedade. É distinta de permissões rwx e de participação num grupo. [Conceito: 15.5](modulo-3/capitulo-15/15.5-privilegios-e-delegacao.md).

### CAP_DAC_OVERRIDE

Capability Linux associada a ignorar determinadas verificações discricionárias de acesso. Não deve ser tratada como uma permissão inofensiva por ser apenas uma entrada numa lista. [Conceito: 15.5](modulo-3/capitulo-15/15.5-privilegios-e-delegacao.md).

### Capabilities (Linux)

Divisão de parte dos privilégios tradicionalmente associados ao superusuário em capacidades específicas do contexto de execução. Não equivale a todo modelo de segurança baseado em capabilities. [Conceito: 11.4][c114].

### Carregador dinâmico

Componente que encontra e prepara objetos compartilhados necessários à execução. No percurso ELF/Linux, não é o mesmo mecanismo que um interpretador de Python nem o bootloader que inicia o sistema operacional. [Conceito: 8.3][c83].

### Causalidade

Relação em que uma condição ou ação contribui para produzir um efeito. Observar dois acontecimentos juntos não basta para estabelecê-la. [Conceito: 4.3][c43].

### CERT/CC

CERT Coordination Center, do Software Engineering Institute da Carnegie Mellon University. Aparece na resposta coordenada após o Morris Worm. É uma instituição, não o autor ou nome do programa. [Contexto: capítulo 2][c2].

### Cgroup

Control group. Organização hierárquica de processos para administrar recursos no Linux segundo controladores e configurações. Peso relativo de distribuição e teto de consumo não são a mesma garantia. [Conceito: 11.3][c113].

### Chamada de sistema

System call. Interface pela qual um programa solicita serviços do kernel. Chamar uma função de biblioteca não implica realizar exatamente uma chamada de sistema: parte do trabalho pode acontecer no próprio processo. [Conceito: 8.3][c83].

### Chave do Registro

Nó da hierarquia do Registro do Windows. Pode conter subchaves e valores; não é uma chave criptográfica nem um diretório comum do sistema de arquivos. [Conceito: 13.5](modulo-3/capitulo-13/13.5-registro-ambiente-e-configuracao.md).

### Checkpoint

No exemplo da aplicação, registro de progresso usado na retomada. É diferente do campo de progresso de uma transição de serviço Windows. [Conceito: 16.6](modulo-3/capitulo-16/16.6-estado-confirmacao-e-retomada.md).

### Checksum

Nome em inglês para soma de verificação. Valor calculado para conferir alterações segundo um mecanismo específico; não é, por si só, prova de autoria ou autorização. [Conceito: 10.6][c106].

### chmod

Alteração dos bits de modo de arquivos e diretórios. Seu efeito depende do tipo de objeto e pode interagir com a máscara de uma ACL; não muda o proprietário. [Conceito: 15.2](modulo-3/capitulo-15/15.2-permissoes-linux-e-caminhos.md).

### chown

Operação de mudança de proprietário e grupo de um arquivo no Linux, sujeita a requisitos de autoridade. Não é equivalente a alterar os bits de modo. [Conceito: 15.3](modulo-3/capitulo-15/15.3-criacao-propriedade-e-acls.md).

### chroot

Operação Linux que muda a raiz de determinada resolução de caminhos. Não fecha descritores nem constitui sozinha uma barreira completa de segurança. [Conceito: 17.1](modulo-3/capitulo-17/17.1-virtualizacao-e-fronteiras.md).

### Chunk

Bloco estruturado de um formato. No exemplo PNG, os chunks seguem a assinatura inicial e têm organização própria; reconhecer apenas o início do arquivo não valida todos os blocos. [Introdução: 10.2][c102].

### CISA

Cybersecurity and Infrastructure Security Agency. Organização dos Estados Unidos responsável pelo get.gov, cuja política aparece como exemplo de delimitação de pesquisa. [Contexto: 3.1][c31].

### CLI

Command-Line Interface, interface de linha de comando. Forma de interação por comandos e argumentos; uma CLI não precisa implementar a linguagem de um shell. [Conceito: 14.1](modulo-3/capitulo-14/14.1-terminal-shell-e-comandos.md).

### Clock

Sinal de temporização. Sua frequência mede ciclos por segundo, não diretamente instruções concluídas. Trabalho por ciclo e frequência efetiva dependem da implementação e das condições. [Conceito: 7.2][c72].

### Clone completo

No VirtualBox, cópia dos discos necessários para operar independentemente da VM de origem. Essa independência não certifica segurança do conteúdo nem um plano completo de backup. [Conceito: 17.6](modulo-3/capitulo-17/17.6-imagens-snapshots-e-recuperacao.md).

### Clone vinculado

Cópia de uma VM que mantém dependências de imagens anteriores no modelo apresentado do VirtualBox. É diferente de uma cópia independente para recuperação. [Conceito: 17.6](modulo-3/capitulo-17/17.6-imagens-snapshots-e-recuperacao.md).

### Cloud

Computação em nuvem: recursos de computação disponibilizados como serviços por rede. A introdução distingue os recursos do cliente da infraestrutura do provedor e suas condições de teste. [Contexto: 3.1][c31].

### Cluster de grafemas

Agrupamento de pontos de código utilizado na segmentação de texto para aproximar uma unidade percebida pelo usuário. Um agrupamento pode conter vários pontos de código e vários bytes; essas contagens não são equivalentes. [Conceito: 6.4][c64].

### cmd.exe

Processador de comandos do Windows com sintaxe própria; não é outro nome para PowerShell nem para o aplicativo Windows Terminal. [Conceito: 14.1](modulo-3/capitulo-14/14.1-terminal-shell-e-comandos.md).

### Cmdlet

Comando integrado ao modelo de execução do PowerShell, com parâmetros e saída que pode ser composta de objetos. [Conceito: 14.1](modulo-3/capitulo-14/14.1-terminal-shell-e-comandos.md).

### Codec

Componente ou conjunto de operações de codificação e decodificação. No exemplo AUR, transforma um registro em bytes e o reconstrói segundo um contrato explícito. O nome não implica compressão nem criptografia. [Exemplo: 10.5][c105].

### Codificação

Regra para representar informação. No caso do texto, especifica como valores de caracteres são convertidos em uma sequência de unidades, como bytes em UTF-8. Não deve ser confundida com criptografia. [Conceito: 6.4][c64].

### Codificação percentual

Representação de um octeto por % seguido de dois algarismos hexadecimais em URIs. A interpretação depende do componente e da camada; decodificar uma ou duas vezes pode produzir textos diferentes. [Conceito: 10.3][c103].

### Código de máquina

Representação binária de instruções de uma arquitetura. Sua presença em um arquivo não comprova que ele seja um executável completo nem que seja compatível com todo ambiente que use a mesma CPU. [Conceitos: 8.2][c82] e [8.3][c83].

### Código de saída

Valor utilizado pelo programa ao comunicar seu encerramento normal. Não é o texto que escreveu na saída padrão; outros modos de término também participam do estado observado pelo sistema. [Conceito: 8.5][c85].

No contexto do capítulo 14: Resultado numérico de encerramento de um comando ou processo. Seu significado depende do contrato da ferramenta; não é o texto impresso. [Conceito: 14.4](modulo-3/capitulo-14/14.4-status-condicoes-e-controle.md).

### Código-fonte

Descrição escrita segundo uma linguagem de programação. É uma representação armazenada em bytes, distinta do artefato produzido pela construção e da execução que usa esse artefato. [Conceito: 8.1][c81].

### COFF

Common Object File Format. Formato de objetos citado junto à documentação PE da Microsoft. A identificação do formato não garante, sozinha, compatibilidade de arquitetura, ABI ou dependências. [Menção: 8.3][c83]; [fonte S5][c8-ref].

### Commit

Confirmação de uma transação. No exemplo, pode terminar antes de o processo emitir uma resposta a quem o iniciou. [Conceito: 16.6](modulo-3/capitulo-16/16.6-estado-confirmacao-e-retomada.md).

### Compilação

Tradução de uma representação de programa para outra. Pode produzir assembly, código objeto ou representações intermediárias, conforme o percurso. Compilar não é necessariamente executar as operações descritas no fonte. [Conceitos: 8.2][c82] e [8.4][c84].

### Compilador

Programa que realiza uma tradução de código segundo regras da linguagem e do alvo. Não precisa produzir uma instrução por linha nem comprova automaticamente que a aplicação seja segura. [Conceito: 8.1][c81].

### Complemento de dois

Convenção de representação de inteiros com sinal em que o bit de maior peso recebe peso negativo. Com oito bits, representa −128 a 127; a sequência de oito uns representa −1. [Conceito: 6.3][c63].

### Compressão sem perdas

Transformação que produz uma representação da qual o conteúdo original deve ser reconstruído exatamente. Tamanho comprimido e tamanho reconstruído são grandezas distintas, com limites que precisam ser considerados. [Conceito: 10.6][c106].

### Computação confidencial

Mecanismos adicionais, dependentes de hardware, firmware e plataforma, destinados a reduzir parte da confiança necessária no hospedeiro. Menção introdutória, sem configuração executada. [Conceito: 17.1](modulo-3/capitulo-17/17.1-virtualizacao-e-fronteiras.md).

### Concorrência

Organização de atividades cujos períodos de progresso se sobrepõem, mesmo quando usam uma unidade de execução em momentos alternados. Não exige paralelismo físico em todo instante. [Conceito: 9.1][c91].

### Condição de corrida

Situação em que a ordem ou o momento relativo das operações afeta um resultado que deveria obedecer a uma regra. O exemplo do contador examina sincronização inadequada sem executar uma data race real. [Conceito: 9.5][c95].

### Confidencialidade

Preservação das restrições de acesso e divulgação. Não significa tornar tudo secreto: um catálogo público e um histórico privado têm regras diferentes. [Conceito: 5.1][c51].

### Console

Termo dependente do contexto. No Windows, pode designar a infraestrutura de entrada e saída de aplicações de console; não é automaticamente sinônimo de PowerShell. [Conceito: 14.1](modulo-3/capitulo-14/14.1-terminal-shell-e-comandos.md).

### Construção

Processo que produz artefatos a partir das entradas de um projeto; build. Pode coordenar várias ferramentas e etapas. Alterar um arquivo-fonte não obriga uma construção automática a acontecer. [Conceito: 8.1][c81].

### Conta

Identidade administrável associada a uma pessoa ou atividade. Cadastro de conta, autenticação e credenciais de uma execução são estados relacionados, mas distintos. [Conceito: 15.1](modulo-3/capitulo-15/15.1-identidades-contas-e-contextos.md).

### Conta de serviço

Identidade destinada à execução de uma atividade automática. Deve receber os acessos necessários à função, sem depender da conta pessoal de quem a administra. [Conceito: 15.1](modulo-3/capitulo-15/15.1-identidades-contas-e-contextos.md).

### Conta local

Conta administrada no contexto de um computador. A coincidência de nomes entre computadores não demonstra igualdade de identidade. [Conceito: 13.4](modulo-3/capitulo-13/13.4-contas-tokens-e-controle-de-acesso.md).

### Contador de programa

Program counter, PC. Estado do processador que participa da determinação de qual instrução buscar. Seu significado preciso e sua atualização dependem da arquitetura e do fluxo de execução. [Conceito: 7.2][c72].

### Container

Organização de execução e isolamento por uma combinação de mecanismos e configurações. No percurso Linux usual, compartilha o kernel; a separação de uma visão não certifica todos os limites do ambiente. [Conceito: 11.4][c114].

### Content-Type

Campo HTTP que comunica o tipo de mídia da representação. É uma declaração do contexto de comunicação, não uma prova independente de que os bytes obedecem ao formato ou podem ser processados com segurança. [Introdução: 10.2][c102].

### Controlador

Componente que gerencia operações de um dispositivo ou subsistema. Distingue-se do driver, que é software de comunicação e controle utilizado pelo sistema. [Conceito: 7.1][c71].

### Controle de fluxo

Regras que escolhem quais operações executar, repetir ou interromper conforme condições e resultados. [Conceito: 14.4](modulo-3/capitulo-14/14.4-status-condicoes-e-controle.md).

### Convidado

Guest: sistema executado no ambiente virtual. Pode ter seu próprio sistema operacional sem que todos os dados e dispositivos sejam exclusivos. [Conceito: 17.1](modulo-3/capitulo-17/17.1-virtualizacao-e-fronteiras.md).

### Cópia na escrita

Copy-on-write, COW. Estratégia que preserva visões privadas sem copiar antecipadamente todo o conteúdo; uma escrita pode exigir criar uma cópia e ajustar o mapeamento. Não significa que toda escrita necessariamente copie uma página nova. [Conceito: 9.4][c94].

### Correlação

Associação observada entre acontecimentos ou variáveis. Pode orientar a investigação, mas não demonstra sozinha que um deles causou o outro. [Conceito: 4.3][c43].

### CPU

Central Processing Unit, unidade central de processamento. Executa instruções que transformam dados e atualizam o estado da execução. Não corresponde ao computador inteiro nem é o único componente capaz de processar informação. [Conceitos: 7.1][c71] e [7.2][c72].

### CPython

Implementação de Python usada no percurso do capítulo 8. Compila fonte para objetos de código e executa sua representação; detalhes de bytecode dependem da implementação e versão. Não é sinônimo de todas as implementações possíveis da linguagem. [Conceito: 8.4][c84].

### CRC

Cyclic Redundancy Check, verificação de redundância cíclica. Valor utilizado para detectar certas corrupções de conteúdo, como nos formatos PNG e gzip. Não exige um segredo do produtor e não equivale a autenticação criptográfica. [Conceito: 10.6][c106].

### Credencial

Informação ou meio utilizado para comprovar uma identidade, como senha ou chave. Sua posse não comprova autorização para utilizá-la em uma investigação. [Conceito: 5.2][c52]; [exemplo: soluções do capítulo 3][c3-sol].

### Cron

Daemon de agendamento no percurso Cronie documentado. Seu ambiente não é automaticamente o da sessão interativa. [Conceito: 16.4](modulo-3/capitulo-16/16.4-agendamento-e-sobreposicao.md).

### Crontab

Tabela de programação de comandos para cron. Entradas de usuário e de sistema têm diferenças de campos que precisam ser respeitadas. [Conceito: 16.4](modulo-3/capitulo-16/16.4-agendamento-e-sobreposicao.md).

### CSRC

Computer Security Resource Center, do NIST. Portal de referências e glossários usado nas notas de pesquisa, não uma ferramenta de exploração. [Ocorrência: referências do capítulo 5][c5-ref].

### CSV

Comma-Separated Values. Formato textual de registros e campos, com regras de delimitadores e aspas. Uma vírgula dentro de um campo entre aspas pode ser conteúdo; variantes e tipos de valores precisam de um acordo adicional. [Conceito: 10.4][c104].

### CTF

Capture the Flag. Formato de desafio de segurança realizado sob as regras de um ambiente preparado. Sua autorização não se estende a sistemas externos. [Menção: capítulo 1][c1].

### ctime

No Linux, marca de tempo de mudança de estado do inode. Não deve ser lida automaticamente como data de criação do documento. É distinta da data que uma aplicação escreve dentro de um arquivo. [Conceito: 10.1][c101].

### CVE

Common Vulnerabilities and Exposures. Identificação e registros de vulnerabilidades publicamente conhecidas. Um número ajuda a comunicar um caso; sua ausência não demonstra ausência de vulnerabilidade. [Conceito: 5.1][c51].

### CVSS

Common Vulnerability Scoring System. Sistema de descrição e pontuação da severidade de vulnerabilidades. O escore Base não é porcentagem de chance de ataque nem avaliação completa de risco. [Conceito: 5.3][c53].

### CWE

Common Weakness Enumeration. Catálogo de tipos de fraquezas de software e hardware. Descreve padrões de problema, função diferente da identificação de casos por CVE. [Conceito: 5.1][c51].

## D

### DAC

Discretionary Access Control, controle de acesso discricionário. Permite administração de direitos por proprietários e autoridades delegadas, sem excluir a existência de controles adicionais. [Conceito: 15.6](modulo-3/capitulo-15/15.6-camadas-revogacao-e-menor-privilegio.md).

### DACL

Discretionary Access Control List. Lista de entradas usada no controle discricionário de acesso a um objeto protegido. Não representa todos os controles de segurança do Windows. [Conceito: 13.4](modulo-3/capitulo-13/13.4-contas-tokens-e-controle-de-acesso.md).

### DACL nula

Estado Windows que não impõe a restrição discricionária da DACL. Distingue-se de uma lista vazia e não elimina outros controles da plataforma. [Conceito: 15.4](modulo-3/capitulo-15/15.4-tokens-e-acls-no-windows.md).

### DACL vazia

Lista discricionária Windows sem entradas de concessão. Não deve ser confundida com a ausência de restrição discricionária de uma DACL nula. [Conceito: 15.4](modulo-3/capitulo-15/15.4-tokens-e-acls-no-windows.md).

### Dados pessoais

No contexto brasileiro discutido, informações relacionadas a pessoa natural identificada ou identificável. Um teste não elimina as obrigações sobre seu tratamento. [Contexto: 3.2][c32].

### Dados sintéticos

Dados construídos para representar situações sem reproduzir registros pessoais reais. Trocar somente um nome em um registro real não o torna automaticamente sintético. [Exemplos: 3.2][c32].

### Daemon

Processo de serviço em segundo plano no vocabulário Unix apresentado. Serviço lógico, processo e unidade de um gerenciador não precisam ter correspondência de um para um. [Conceito: 11.5][c115].

Processo que presta serviço em segundo plano no vocabulário Unix. O modelo de inicialização supervisionado não exige repetir o destacamento tradicional do terminal. [Conceito: 16.2](modulo-3/capitulo-16/16.2-servicos-e-supervisao.md).

### DARPA

Defense Advanced Research Projects Agency. Agência citada por solicitar ao SEI uma capacidade de resposta após o incidente de 1988. [Contexto: capítulo 2][c2].

### Data race

No contexto de memória compartilhada, conflito entre acessos de threads, ao menos um de escrita, sem a coordenação exigida pelo modelo de memória. Em C/C++, não deve ser reduzida a uma previsão de qual escrita vence: pode envolver comportamento indefinido. É um conceito mais específico que a expressão ampla condição de corrida. [Contexto: 9.5][c95]; [fontes S17][c9-ref].

### Deadlock

Impasse sem progresso sob condições como as do modelo: tarefas mantêm recursos exclusivos e esperam recursos umas das outras sem liberar nem dispor de recuperação. O exemplo do livro é uma dependência desenhada, não um travamento executado. [Conceito: 11.3][c113].

### Decimal

Sistema de numeração de base dez, com algarismos de 0 a 9. Em notação posicional, cada posição à esquerda tem dez vezes o peso da anterior. Aqui o termo descreve a base, não um tipo específico de dados de uma linguagem. [Conceito: 6.2][c62].

### Declaração

No exemplo C, apresenta informações como nome, argumentos e retorno de uma função. A declaração sem corpo permite conhecer sua interface, mas não fornece a implementação necessária à ligação. [Conceito: 8.2][c82].

### Deduplicação

Reconhecimento de operações consideradas equivalentes para evitar repetição indevida. Exige identidade e critério de comparação de conteúdo. [Conceito: 16.6](modulo-3/capitulo-16/16.6-estado-confirmacao-e-retomada.md).

### DEP

Data Execution Prevention, prevenção de execução de dados. Mecanismo que restringe execução a partir de páginas não autorizadas para esse uso. Não valida os limites de cada objeto nem a autorização de negócio da aplicação. [Conceito: 9.5][c95].

### Dependência de software

Relação declarada entre componentes necessários à instalação ou ao funcionamento de software. Resolver dependências não demonstra toda a correção ou segurança da aplicação. [Conceito: 12.5][c125].

### Descritor de arquivo

Identificador de um recurso aberto no contexto de um processo. Apesar do nome, pode se relacionar a recursos que não são documentos em armazenamento persistente. [Conceito: 8.5][c85]. A relação entre abertura, nomes e conteúdo é retomada em [10.1][c101].

### Descritor de segurança

Estrutura que reúne informações de segurança de um objeto, como seu proprietário e informações de controle de acesso. [Conceito: 13.4](modulo-3/capitulo-13/13.4-contas-tokens-e-controle-de-acesso.md).

### Deslocamento

Offset. Posição relativa ao começo de uma unidade, como uma página ou objeto. No modelo de tradução, o deslocamento é combinado ao quadro escolhido pelo mapa; não é um endereço físico universal. [Conceito: 9.2][c92]. Em arquivos e formatos, também indica posição relativa na sequência de bytes. [Aplicação: 10.2][c102].

### Desserialização

Reconstrução de valores ou estruturas a partir de uma representação. As capacidades do mecanismo importam: alguns desserializadores de objetos podem executar comportamento, não apenas ler campos simples. [Conceito: 10.4][c104]; [limites: 10.6][c106].

### Digest

Resumo criptográfico utilizado para identificar conteúdo de uma imagem. Fixa a identidade do artefato, não sua segurança, e exige atualização deliberada quando a base muda. [Conceito: 17.6](modulo-3/capitulo-17/17.6-imagens-snapshots-e-recuperacao.md).

### Diretório de trabalho

Diretório corrente de um processo, usado como base em operações comuns com caminhos relativos. O mesmo nome relativo pode alcançar arquivos diferentes quando essa base muda. [Conceito: 8.5][c85].

No contexto do capítulo 13: Diretório usado como contexto para a interpretação de determinados nomes relativos. Não é necessariamente a pasta onde o executável foi instalado. [Conceito: 13.2](modulo-3/capitulo-13/13.2-volumes-caminhos-e-perfis.md).

### Diretório raiz

Início da árvore usada para resolver caminhos absolutos, representado por /. Não é a conta root nem seu diretório pessoal /root; a raiz e a visão dependem do contexto do processo. [Conceito: 12.2][c122].

### Disparo

Ocorrência que solicita ou habilita o início de uma atividade agendada. Não demonstra sua conclusão. [Conceito: 16.4](modulo-3/capitulo-16/16.4-agendamento-e-sobreposicao.md).

### Disponibilidade

Possibilidade de acesso e uso por quem está autorizado quando necessário. Recusar todos os pedidos não é correção suficiente se os usos legítimos também deixam de funcionar. [Conceito: 5.1][c51].

### Dispositivo de bloco

Tipo de interface de dispositivo que organiza acesso por blocos. É uma classificação da interface, não um formato de documento nem confirmação de que seu sistema de arquivos esteja montado. [Conceito: 12.3][c123].

### Dispositivo de caractere

Tipo de interface de dispositivo distinto do acesso por blocos. O nome não significa que o recurso armazene apenas texto; cada interface mantém suas próprias operações e garantias. [Conceito: 12.3][c123].

### Distribuição Linux

Integração do kernel Linux com ferramentas, bibliotecas, pacotes, configurações e manutenção. Compartilhar o kernel não implica que duas instalações ofereçam as mesmas condições de execução. [Conceito: 11.1][c111].

### Divulgação coordenada

Coordenação entre participantes que descobrem, corrigem, utilizam e comunicam informações sobre vulnerabilidades. Não é sinônimo de programa de recompensas. [Contexto: capítulo 2][c2].

### DLL

Dynamic-Link Library. Biblioteca de ligação dinâmica que pode oferecer funções e dados. No uso comum, é carregada no contexto de um processo que a utiliza. [Conceito: 13.3](modulo-3/capitulo-13/13.3-executaveis-bibliotecas-e-carregamento.md).

### DMA

Direct Memory Access, acesso direto à memória. Permite transferências entre dispositivo e memória sem cópia byte a byte pela CPU principal. Ainda exige preparação, endereços e controle; não significa acesso irrestrito. [Conceito: 7.5][c75].

### DOI

Digital Object Identifier. Identificador persistente usado para referenciar objetos, como publicações. Não certifica a correção do conteúdo nem substitui sua leitura. [Ocorrência: referências do capítulo 2][c2-ref].

### Domínio

No recorte de identidade Windows, contexto de administração de contas que não deve ser confundido com uma conta local de qualquer computador. O funcionamento de Active Directory será aprofundado em outro módulo. [Conceito: 13.4](modulo-3/capitulo-13/13.4-contas-tokens-e-controle-de-acesso.md).

### Dot-sourcing

Execução de um script PowerShell no escopo correspondente do chamador usando o operador ponto, permitindo que definições afetem esse contexto. [Conceito: 14.5](modulo-3/capitulo-14/14.5-scripts-contexto-e-repetibilidade.md).

### dpkg

Ferramenta de administração de pacotes Debian e de seu estado local. Instalação pode envolver arquivos, metadados e scripts de manutenção, não apenas copiar um executável. [Conceito: 12.5][c125].

### dpkg-query

Ferramenta que consulta a base local de pacotes Debian, incluindo versões e caminhos registrados. Não é inventário universal de todos os arquivos criados fora desse mecanismo nem das versões em execução. [Conceito: 12.5][c125].

### DRAM

Dynamic Random Access Memory, memória dinâmica. Tecnologia de memória que exige renovação periódica do estado armazenado, o refresh. A DRAM convencional é volátil. [Conceito: 7.3][c73].

### Driver

Software que participa da comunicação e do controle entre sistema operacional e dispositivo. Não é o próprio circuito controlador nem o dado transferido. [Conceitos: 7.1][c71] e [7.5][c75].

### Drop-in

Arquivo complementar de configuração de uma unidade systemd, sujeito a regras de localização e precedência. [Conceito: 16.3](modulo-3/capitulo-16/16.3-configuracao-parada-e-reinicio.md).

### Durabilidade

Conservação de um resultado confirmado diante das falhas abrangidas pelo contrato. Confirmar uma escrita não implica todas as garantias de armazenamento. [Conceito: 16.6](modulo-3/capitulo-16/16.6-estado-confirmacao-e-retomada.md).

## E

### EACCES

Nome simbólico de erro associado a recusa de acesso nas interfaces discutidas. Não identifica sozinho qual componente do caminho ou política ocasionou a recusa. [Conceito: 11.2][c112].

### EBADF

Nome simbólico de erro que pode indicar descritor inválido ou incompatível com a operação. Uma abertura válida somente para leitura pode produzir esse erro quando usada para escrita. [Conceito: 11.2][c112].

### Elevação

Transição para um contexto administrativo de execução conforme o mecanismo e a política aplicáveis. Não transforma automaticamente um aplicativo em código de kernel. [Conceito: 13.4](modulo-3/capitulo-13/13.4-contas-tokens-e-controle-de-acesso.md).

### ELF

Executable and Linkable Format. Formato que descreve diferentes artefatos, como objetos relocáveis, executáveis e bibliotecas compartilhadas. Tipo, arquitetura e organização precisam ser examinados; a assinatura do formato não demonstra o papel inteiro do arquivo. [Conceito: 8.3][c83].

### Emulação

Reprodução do comportamento de uma máquina ou componente em software. Não oferece automaticamente as mesmas garantias de contenção de uma configuração suportada de virtualização. [Conceito: 17.2](modulo-3/capitulo-17/17.2-maquinas-virtuais-e-hipervisores.md).

### Emulador de terminal

Programa que oferece uma interface de terminal em software. Apresenta a interação com aplicações, mas não define sozinho a linguagem do shell hospedado. [Conceito: 14.1](modulo-3/capitulo-14/14.1-terminal-shell-e-comandos.md).

### Encadeamento de vulnerabilidades

Combinação de condições em que o resultado de uma etapa permite avançar para outra. Cada ligação exige evidência; leitura indevida não implica automaticamente controle de todo o ambiente. [Conceito: 5.2][c52].

### Endereço de memória

Identificador de uma posição dentro de um espaço de endereçamento. O conteúdo da posição pode mudar sem que seu endereço mude; o contexto determina que tipo de endereço está sendo utilizado. [Conceito: 7.3][c73].

### Endereço físico

Endereço relativo à visão física de memória apresentada pela plataforma. Pode ser obtido pela tradução de um endereço virtual; não deve ser confundido automaticamente com o endereço utilizado por um dispositivo em DMA. [Conceitos: 7.3][c73] e [7.5][c75].

### Endereço virtual

Endereço utilizado em um contexto de memória virtual, traduzido para um destino conforme os mapeamentos do sistema. Números iguais em contextos distintos não provam acesso à mesma memória física. [Conceito: 7.3][c73]; [modelo desenvolvido: 9.2][c92].

### Endianness

Ordem dos bytes na representação de um valor com vários bytes. Interpretar a mesma sequência em big-endian ou little-endian pode produzir números distintos. O formato precisa definir a convenção. [Conceito: 6.3][c63].

### Engenharia reversa

Análise de um sistema ou artefato para compreender sua estrutura e funcionamento a partir do que está disponível. É citada como especialização, sem técnica detalhada nesta introdução. [Menção: capítulo 2][c2].

### ENOENT

Nome simbólico de erro associado à ausência de componente necessário à resolução de um caminho. No exemplo, aparece ao tentar abrir um nome não criado, não ao consumir o fim do arquivo existente. [Conceito: 11.2][c112].

### Entrada e saída

E/S; em inglês, Input/Output ou I/O. Operações de comunicação com dispositivos e componentes externos ao processamento considerado, como teclado, tela e armazenamento. Seus caminhos podem envolver drivers, controladores e buffers. [Conceitos: 7.1][c71] e [7.5][c75].

### Entrada padrão

Fluxo convencional pelo qual um programa pode receber dados; em ambientes Unix corresponde ao descritor 0, quando disponível. [Conceito: 14.3](modulo-3/capitulo-14/14.3-fluxos-redirecionamentos-e-pipelines.md).

### Enumeração

Levantamento sistemático de informações sobre elementos de um ambiente, como usuários, serviços ou permissões. Não equivale, sozinho, à exploração de uma falha. [Menções: capítulo 1][c1].

### EOF

End of file, fim de arquivo. No percurso de leitura apresentado, condição de fim da sequência, não um byte obrigatório depois do último caractere. A interpretação do retorno de uma operação depende de seu contrato e do tipo de recurso. [Conceito: 10.1][c101].

### errno

Informação de erro utilizada em interfaces C sob o contrato da função. Deve ser consultada quando a operação indica falha; um valor antigo não comprova erro numa chamada bem-sucedida. Python conserva códigos correspondentes em exceções OSError. [Conceito: 11.2][c112].

### Erro padrão

Fluxo convencional separado da saída de resultado, frequentemente usado para diagnósticos; no modelo Unix corresponde ao descritor 2. [Conceito: 14.3](modulo-3/capitulo-14/14.3-fluxos-redirecionamentos-e-pipelines.md).

### ErrorAction

Parâmetro comum do PowerShell que controla o tratamento de erros não terminantes na chamada correspondente. Stop permite convertê-los em erros terminantes, quando aplicável. [Conceito: 14.4](modulo-3/capitulo-14/14.4-status-condicoes-e-controle.md).

### Escalada de privilégios

Obtenção de permissões ou capacidades superiores às do contexto inicial. Executar código e executar com privilégio administrativo são situações distintas. [Menção: capítulo 1][c1].

### Escalonador

Componente que decide quais fluxos aptos recebem oportunidade de execução, conforme política e recursos. Um fluxo bloqueado por um evento não progride apenas por ter mais tempo de CPU disponível. [Conceito: 9.1][c91].

### Escape

Representação de conteúdo que possui papel especial numa gramática. As regras dependem do contexto, como uma string JSON; aplicar um escape não produz proteção universal para qualquer destino posterior. [Conceito: 10.3][c103].

### Escape de isolamento

Travessia de uma fronteira que deveria impedir a ação, por exemplo devido a defeito na implementação. Usar uma passagem explicitamente concedida não demonstra, por si só, um escape. [Conceito: 17.4](modulo-3/capitulo-17/17.4-compartilhamentos-e-autoridade.md).

### Escopo

Delimitação do que será avaliado e das condições da avaliação. Descobrir um sistema conectado não amplia automaticamente a autorização. [Conceito: 3.1][c31].

### Espaço de endereços

Contexto no qual os endereços de um processo são interpretados. Visões diferentes podem alcançar destinos distintos ou compartilhar regiões sob regras explícitas; separar visões não exige duplicar fisicamente todo conteúdo. [Conceito: 9.1][c91].

### Espaço de usuário

Userspace. Ambiente de execução de aplicações e componentes fora do kernel. Pode incluir serviços com permissões relevantes; não significa que todo programa ali execute sob uma conta sem privilégios. [Conceito: 11.1][c111].

### Esquema

Schema. Descrição da estrutura, tipos, campos e restrições esperados. Pode definir um perfil mais restrito que a gramática geral do formato; aceitar o esquema não substitui a autorização de uma operação. [Conceito: 10.4][c104].

### Estado de processo

Condição da execução descrita pelo sistema, como prontidão, espera ou término. Não é, isoladamente, uma avaliação da saúde da aplicação. [Conceito: 16.1](modulo-3/capitulo-16/16.1-ciclo-de-vida-e-processos.md).

### Ethical hacking

Hacking ético. Na obra, investigação ofensiva conduzida com autorização, escopo e responsabilidade. Intenção de ajudar não substitui permissão. [Contexto: capítulo 1][c1] e [capítulo 3][c3].

### EventID

Identificador de um evento no contexto de seu provedor. Não é uma explicação suficiente quando separado do provedor e dos demais dados do registro. [Conceito: 13.6](modulo-3/capitulo-13/13.6-inicializacao-servicos-e-investigacao.md).

### EventRecordID

Número atribuído a um registro no log de eventos. É diferente do identificador de tipo de evento, EventID. [Conceito: 13.6](modulo-3/capitulo-13/13.6-inicializacao-servicos-e-investigacao.md).

### Evidência

Informação que sustenta ou contraria uma afirmação sob condições identificadas. A procedência e os limites importam; uma tela não comprova automaticamente a explicação atribuída a ela. [Conceito: 4.3][c43].

### Execution policy

Política de execução de scripts do PowerShell. Não constitui, isoladamente, uma fronteira completa de segurança. [Conceito: 14.6](modulo-3/capitulo-14/14.6-automacao-e-fronteiras-de-confianca.md).

### Executive

Conjunto de componentes em modo kernel do Windows com responsabilidades como memória, objetos, processos, entrada e saída e configuração. [Conceito: 13.1](modulo-3/capitulo-13/13.1-arquitetura-processos-e-objetos.md).

### execve

Interface Linux que, quando bem-sucedida, substitui a imagem de programa executada por um processo existente. Seu PID é preservado; outros atributos seguem regras específicas. Não é sinônimo de criar um processo novo. [Conceito: 8.3][c83].

### Expansão

Etapa em que o shell substitui expressões por valores ou nomes segundo o contexto sintático, como uma variável ou padrão de arquivo. [Conceito: 14.2](modulo-3/capitulo-14/14.2-argumentos-aspas-e-expansoes.md).

### Exploit

Método ou artefato que aproveita uma vulnerabilidade. Não é a própria fraqueza; publicar um código não comprova vulnerabilidade de qualquer instalação do produto. [Conceito: 5.2][c52].

### Exposição

Condição de alcance: quem consegue interagir, por qual caminho e sob quais circunstâncias. Uma função exposta não é necessariamente vulnerável. [Conceito: 5.3][c53].

### Extensão de arquivo

Sufixo do nome, como .json ou .txt, utilizado por ferramentas para classificação ou seleção de leitura. Renomeá-lo não converte, por si só, os bytes para outro formato. [Conceito: 10.2][c102].

## F

### Falso negativo

Falha em identificar uma condição que o detector deveria reconhecer e que estava presente. Ausência de alerta não permite contar, por si só, problemas não detectados. [Conceito: 4.3][c43].

### Falso positivo

Indicação de uma condição ausente no caso classificado. Um alerta não verificado pode ser inconclusivo, sem ser automaticamente verdadeiro ou falso. [Conceito: 4.3][c43].

### FHS

Filesystem Hierarchy Standard. Documento de convenções para a organização de diretórios e suas funções. O capítulo usa a versão 3.0 como referência, sem presumir conformidade literal de toda instalação atual. [Conceito: 12.2][c122].

### findmnt

Utilitário do projeto util-linux para consultar informações de sistemas de arquivos montados. A interpretação depende das opções e da origem da consulta; a visão do terminal não é automaticamente a de outro serviço. [Conceito: 12.2][c122].

### Firmware

Software associado à inicialização ou à operação de um equipamento ou componente. Estar armazenado num dispositivo não o transforma no circuito físico. Pode existir fora dos arquivos substituídos ao reinstalar o sistema operacional. [Conceito: 7.5][c75].

### FIRST

Forum of Incident Response and Security Teams. Organização responsável pela documentação CVSS citada no capítulo 5. A referência não representa endosso ao livro. [Contexto: 5.3][c53].

### Flash

Tecnologia de memória não volátil utilizada, entre outros dispositivos, em SSDs. No caso NAND apresentado, programação de páginas e apagamento de blocos são operações diferentes, administradas pelo controlador. [Conceito: 7.4][c74].

### Flush

No contexto de escrita, solicitação para escoar dados pendentes ao nível de armazenamento pertinente. Não significa simplesmente apagar a cache nem garantir resistência a toda falha futura. [Conceito: 7.4][c74].

### Fonte de ameaça

Origem de ação ou condição capaz de explorar ou acionar uma fraqueza. Pode envolver intenção adversarial ou circunstâncias acidentais. [Conceito: 5.2][c52].

### fork

Interface que cria um processo filho no percurso Linux discutido. É uma operação diferente da substituição de imagem feita por `execve`; nem todo lançador precisa usar esse par exatamente da mesma maneira. [Conceito: 8.3][c83]; [cópia na escrita e compartilhamento: 9.4][c94].

### Formato

Conjunto de regras sobre a estrutura, representação e significado de um conteúdo. Identificar o formato é diferente de confirmar que toda entrada respeita suas regras. [Conceito: 10.2][c102].

### free

Função de C que libera um bloco obtido por operações de alocação compatíveis. Não é garantia de apagar todas as cópias dos dados nem de reduzir imediatamente a memória residente do processo. [Conceito: 9.3][c93].

### Fronteira de confiança

Limite entre contextos com permissões, controle ou suposições de confiança diferentes. Atravessá-lo exige examinar quais decisões e verificações deveriam ocorrer. [Menção: capítulo 1][c1].

### FSGID

Identificador de grupo de sistema de arquivos no Linux, usado em conjunto com grupos suplementares nas verificações de arquivos. Normalmente acompanha o GID efetivo. [Conceito: 15.1](modulo-3/capitulo-15/15.1-identidades-contas-e-contextos.md).

### fstat

Operação que consulta metadados do objeto referenciado por um descritor aberto. No exemplo, dispositivo e inode identificam namespaces apenas no kernel e contexto observados. [Conceito: 17.7](modulo-3/capitulo-17/17.7-investigacao-e-verificacao.md).

### FSUID

Identificador de usuário de sistema de arquivos no Linux, usado nas verificações de arquivos. Normalmente acompanha o UID efetivo, mas é um campo distinto. [Conceito: 15.1](modulo-3/capitulo-15/15.1-identidades-contas-e-contextos.md).

### fsync

Interface de sincronização de um arquivo no Linux. A persistência da entrada de diretório é uma questão adicional. [Conceito: 16.6](modulo-3/capitulo-16/16.6-estado-confirmacao-e-retomada.md).

### Função

Unidade de operações que pode ser chamada por outra parte de um programa. A interface informa argumentos e retorno; o corpo define o comportamento. Uma função de biblioteca não é necessariamente uma chamada de sistema. [Conceitos: 8.1][c81] e [8.3][c83].

No contexto do capítulo 14: Conjunto nomeado de operações que pode ser chamado. Neste capítulo, refere-se às funções da linguagem do shell, não necessariamente a um novo executável. [Conceito: 14.1](modulo-3/capitulo-14/14.1-terminal-shell-e-comandos.md).

## G

### GCC

GNU Compiler Collection. No exemplo, o comando `gcc` coordena etapas de tradução, montagem e ligação conforme as opções utilizadas. Não precisa executar todas essas etapas em toda invocação. [Conceito: 8.2][c82].

### Gerenciador de serviços

Componente que organiza ciclo de vida e contexto de serviços conforme sua configuração. Iniciar ou reiniciar um processo não demonstra que todas as funções do serviço estejam saudáveis. [Conceito: 11.5][c115].

### Get-Acl

Cmdlet PowerShell que consulta um descritor de segurança de recurso suportado. Sua saída não calcula sozinha todo o acesso efetivo de outra execução. [Conceito: 15.7](modulo-3/capitulo-15/15.7-investigacao-e-verificacao.md).

### Get-Member

Cmdlet usado para examinar tipos e membros dos objetos recebidos no PowerShell. Ajuda a distinguir estrutura de dados da apresentação na tela. [Conceito: 14.3](modulo-3/capitulo-14/14.3-fluxos-redirecionamentos-e-pipelines.md).

### getfacl

Utilitário de consulta das ACLs de um recurso, incluindo máscara e comentários de acesso efetivo quando aplicável. [Conceito: 15.3](modulo-3/capitulo-15/15.3-criacao-propriedade-e-acls.md).

### GHz

Gigahertz: um bilhão de ciclos por segundo. Expressa frequência, não diretamente instruções ou tarefas concluídas. [Conceito: 7.2][c72].

### GID

Group identifier, identificador de grupo. Participa do contexto de credenciais das interfaces Unix/Linux; grupos e variantes de identificadores possuem papéis que precisam ser distinguidos. [Conceito: 11.4][c114].

Identificador numérico de grupo. O grupo principal de uma conta não esgota os grupos suplementares presentes numa execução. [Conceito: 15.1](modulo-3/capitulo-15/15.1-identidades-contas-e-contextos.md).

### Globbing

Expansão de padrões de nomes, como *.txt, em correspondências de arquivos segundo as regras e opções aplicáveis. Não equivale a expressão regular. [Conceito: 14.2](modulo-3/capitulo-14/14.2-argumentos-aspas-e-expansoes.md).

### GPU

Graphics Processing Unit, unidade de processamento gráfico. Também pode executar cálculos paralelos adequados ao seu modelo. A adequação da tarefa e os custos de transferência importam; não substitui universalmente a CPU. [Conceito: 7.5][c75].

### Gray hat

Rótulo informal usado para situações que misturam características atribuídas a white hat e black hat. Não constitui autorização nem categoria jurídica adotada pelo livro. [Contexto: capítulo 1][c1].

### grep

Ferramenta para selecionar linhas segundo um padrão. O capítulo usa GNU grep com -F para correspondência literal e distingue ausência de correspondência de erro. [Conceito: 14.3](modulo-3/capitulo-14/14.3-fluxos-redirecionamentos-e-pipelines.md).

### Grupos suplementares

Conjunto de grupos adicionais presente nas credenciais de uma execução Linux. Mudar o cadastro não reescreve automaticamente os grupos de todos os processos existentes. [Conceito: 15.1](modulo-3/capitulo-15/15.1-identidades-contas-e-contextos.md).

### Guest Additions

Componentes de integração do VirtualBox que oferecem recursos entre convidado e hospedeiro, incluindo pastas compartilhadas. Essas passagens não dependem necessariamente da rede virtual. [Conceito: 17.4](modulo-3/capitulo-17/17.4-compartilhamentos-e-autoridade.md).

### GUID

Identificador utilizado para distinguir entidades. Neste capítulo aparece nos nomes de volumes; não é uma descrição do dispositivo físico. [Conceito: 13.2](modulo-3/capitulo-13/13.2-volumes-caminhos-e-perfis.md).

### gzip

Formato de dados comprimidos com cabeçalho, conteúdo comprimido e verificações finais. Seu tamanho externo não limita sozinho os dados reconstruídos ou o trabalho de processamento. [Conceito: 10.6][c106].

## H

### Hack

Termo com diferentes sentidos históricos, como solução engenhosa, modificação criativa ou exploração de um sistema. Seu significado depende do contexto. [Conceito: capítulo 1][c1].

### Hacker

Termo que pode designar quem explora sistemas em profundidade ou, em outros contextos, pessoas associadas a intrusões. A palavra isolada não comprova intenção ou autorização. [Conceito: capítulo 1][c1].

### Handle

Referência opaca usada por uma execução para operar sobre um recurso conforme uma interface. Não é a senha, o conteúdo ou necessariamente o endereço de memória desse recurso. [Conceito: 13.1](modulo-3/capitulo-13/13.1-arquitetura-processos-e-objetos.md).

### Hard link

Ligação física. Outro nome para o mesmo objeto no sistema de arquivos, não uma cópia independente dos dados. A semântica é apresentada no contexto Linux. [Conceito: 10.1][c101].

### Hardware

Componentes físicos de um sistema computacional. Suas funções cooperam com software e não precisam corresponder a peças removíveis independentes. [Conceito: 7.1][c71].

### Hash

Resultado de uma função que transforma uma entrada segundo um algoritmo. No contexto de senhas citado, testar candidatos contra hashes não significa descriptografar a senha. [Menção: capítulo 1][c1]. No capítulo 10, o hash criptográfico ajuda a comparar bytes; o valor esperado ainda precisa de uma referência confiável. [Contexto: 10.6][c106].

### Hashcat

Ferramenta de recuperação e auditoria de senhas que testa candidatos contra representações compatíveis, como hashes. Não é uma operação universal para descobrir qualquer senha. [Menção: capítulo 1][c1]. [Documentação][hashcat-doc].

### HDD

Hard Disk Drive, unidade de disco rígido. Utiliza superfícies magnéticas em pratos e cabeças de leitura/escrita. Movimentos e posicionamento participam do acesso aos dados. [Conceito: 7.4][c74].

### Heap

Armazenamento administrado para alocações dinâmicas. Não é uma peça física separada da RAM nem corresponde obrigatoriamente a uma única região rotulada na lista de mapas do processo. [Conceito: 9.3][c93].

### Hertz

Hz. Unidade de frequência equivalente a um ciclo por segundo. A duração de um ciclo é o inverso da frequência, sob a hipótese de frequência constante. [Conceito: 7.2][c72].

### Hexadecimal

Sistema de base dezesseis, com algarismos 0–9 e A–F. Um algarismo hexadecimal corresponde a quatro bits; um byte pode ser exibido com dois deles. É notação, não criptografia. [Conceito: 6.2][c62].

### Hipervisor

Componente que controla a execução dos ambientes convidados e arbitra seu acesso aos recursos. A plataforma inclui também outros componentes; não se resume à interface gráfica de administração. [Conceito: 17.2](modulo-3/capitulo-17/17.2-maquinas-virtuais-e-hipervisores.md).

### Hipótese

Explicação provisória a confrontar com observações e alternativas. É mais útil quando permite prever um resultado e dizer o que a contrariaria. [Conceito: 4.1][c41].

### Hive

Agrupamento lógico de chaves, subchaves e valores do Registro, associado a armazenamento. Não deve ser equiparado automaticamente a cada chave predefinida exibida na raiz do editor. [Conceito: 13.5](modulo-3/capitulo-13/13.5-registro-ambiente-e-configuracao.md).

### HKCU

Abreviação de HKEY_CURRENT_USER. Chave predefinida de acesso a configurações de usuário, com regras de mapeamento relacionadas ao contexto do processo. [Conceito: 13.5](modulo-3/capitulo-13/13.5-registro-ambiente-e-configuracao.md).

### HKLM

Abreviação de HKEY_LOCAL_MACHINE. Chave predefinida associada a configurações da máquina. Sua existência não concede acesso irrestrito aos valores. [Conceito: 13.5](modulo-3/capitulo-13/13.5-registro-ambiente-e-configuracao.md).

### HKU

Abreviação de HKEY_USERS. Chave predefinida que reúne ramos de perfis de usuário carregados. [Conceito: 13.5](modulo-3/capitulo-13/13.5-registro-ambiente-e-configuracao.md).

### Hospedeiro

Host: plataforma que sustenta o ambiente convidado. Sua autoridade e seus componentes confiáveis precisam ser considerados separadamente das permissões internas do convidado. [Conceito: 17.1](modulo-3/capitulo-17/17.1-virtualizacao-e-fronteiras.md).

### Host-only

Modo de rede VirtualBox que conecta hospedeiro e convidados em uma rede própria. Não equivale a impedir acesso ao host, nem descreve outras interfaces existentes. [Conceito: 17.5](modulo-3/capitulo-17/17.5-conectividade-e-alcance.md).

### HTTP

Hypertext Transfer Protocol. Protocolo de requisições e respostas usado na Web. O código de status integra a resposta, mas não comprova sozinho qual conteúdo ou decisão de acesso ocorreu. [Conceito: 4.3][c43].

### HTTPS

HTTP utilizado por conexão protegida com TLS. Proteger o canal não demonstra correção da aplicação, e o número 443 não certifica o protocolo utilizado. [Menção: capítulo 1][c1]. [Semântica do esquema][https-rfc].

## I

### IA

Inteligência artificial. A sigla aparece em aplicações com modelos de linguagem e no apoio editorial. Conteúdo produzido por IA não é, por si só, evidência nem revisão independente. [Contexto: 4.4][c44].

### id

Utilitário GNU que consulta dados de usuário/grupo. Sem usuário informado, descreve o processo corrente; informar um usuário consulta dados sobre aquela identidade cadastrada. [Conceito: 15.1](modulo-3/capitulo-15/15.1-identidades-contas-e-contextos.md).

### Idempotência

Propriedade de uma operação cujo efeito pretendido não se acumula apenas por repeti-la. Produzir a mesma saída não prova que os efeitos externos sejam idempotentes. [Conceito: 14.5](modulo-3/capitulo-14/14.5-scripts-contexto-e-repetibilidade.md).

No exemplo transacional do capítulo 16, repetir o mesmo lote com o mesmo conteúdo não incrementa o total novamente. A garantia está limitada ao contrato e ao banco do exemplo. [Conceito: 16.6](modulo-3/capitulo-16/16.6-estado-confirmacao-e-retomada.md).

### Identificador

Valor utilizado para distinguir um objeto ou registro. Conhecê-lo não equivale a ter permissão para consultar o objeto. [Conceito: 5.1][c51].

### Identificador de correlação

Valor utilizado para relacionar observações de uma operação. Lote, tentativa e processo podem precisar de identificadores distintos. [Conceito: 16.5](modulo-3/capitulo-16/16.5-logs-tempo-e-evidencias.md).

### IFS

Internal Field Separator: variável usada pelo Bash na separação de palavras em contextos como expansões sem aspas. [Conceito: 14.2](modulo-3/capitulo-14/14.2-argumentos-aspas-e-expansoes.md).

### Imagem de container

Base de camadas de arquivos e metadados usada para criar uma execução. É diferente do processo atual, da camada gravável da instância e de volumes externos. [Conceito: 17.3](modulo-3/capitulo-17/17.3-containers-namespaces-e-recursos.md).

### Impacto

Consequência de uma falha ou ação. Distinguir impacto observado de impacto possível e limitar a afirmação ao que as evidências sustentam. [Conceito: 5.2][c52].

### Impersonação

Uso, por uma thread, de um contexto de segurança de cliente para determinadas operações, sujeito aos mecanismos e permissões aplicáveis. [Conceito: 13.4](modulo-3/capitulo-13/13.4-contas-tokens-e-controle-de-acesso.md).

### Índice de pacotes

Metadados que descrevem pacotes anunciados por uma fonte. Buscar uma versão nova do índice não significa substituir o software já instalado. [Conceito: 12.5][c125].

### Inferência

Conclusão construída a partir de observações e premissas. Não equivale ao registro bruto produzido por tela ou ferramenta. [Conceito: 4.1][c41].

### initramfs

Ambiente inicial de sistemas de arquivos em memória que pode participar da preparação antes de alcançar o sistema de arquivos raiz pretendido no percurso Linux. Sua utilização depende da inicialização configurada. [Conceito: 11.5][c115].

### Inode

Estrutura de metadados de um arquivo no modelo Linux apresentado. Seu número só identifica o objeto no contexto do sistema de arquivos pertinente; não é uma identidade universal e eterna para um documento. [Conceito: 10.1][c101].

### Instrução de máquina

Operação codificada interpretada pelo processador conforme sua arquitetura. Pode transformar dados, acessar memória ou alterar o fluxo de execução. Não equivale necessariamente a uma linha de uma linguagem de programação. [Conceito: 7.2][c72].

### Integridade

Proteção contra alteração ou destruição indevida. Alterar uma data sem permissão é consequência diferente de consultar informação privada. [Conceito: 5.1][c51].

### Inteiro com sinal

Representação numérica que admite valores negativos e não negativos. É preciso conhecer a convenção, como complemento de dois, e a largura em bits para interpretar o campo. [Conceito: 6.3][c63].

### Inteiro sem sinal

Representação de inteiros não negativos. Em n bits com todos os padrões utilizados, sua faixa é de zero a `2^n − 1`. [Conceito: 6.3][c63].

### Interpolação

Construção de uma string substituindo expressões por seus valores em contextos que permitem expansão. Não ocorre da mesma forma em strings literais. [Conceito: 14.2](modulo-3/capitulo-14/14.2-argumentos-aspas-e-expansoes.md).

### Interpretador

Programa que implementa a execução de uma linguagem ou representação. Ele também depende de execução real na plataforma; não faz a CPU entender diretamente qualquer texto recebido. O interpretador indicado num ELF pode ser um carregador dinâmico, outro uso contextual do termo. [Conceitos: 8.4][c84] e [8.3][c83].

### Interpretador de comandos

Programa que lê comandos conforme uma linguagem e coordena sua execução. É distinto da interface de terminal. [Conceito: 14.1](modulo-3/capitulo-14/14.1-terminal-shell-e-comandos.md).

### Interrupção

Sinal ou evento que encaminha a execução a uma rotina de atendimento conforme as condições do sistema. Pode representar uma ocorrência normal, como entrada disponível, e não necessariamente uma pane. [Conceito: 7.5][c75].

### IOMMU

Input/Output Memory Management Unit. Mecanismo de tradução e restrição de acessos à memória originados por dispositivos. Seu efeito depende de configuração e suporte; não se confunde com a MMU dos acessos do processador. [Conceito: 7.5][c75].

### IPC

Interprocess Communication, comunicação entre processos. Mecanismos que permitem troca de informações entre contextos, por exemplo regiões compartilhadas ou canais de mensagens. Separar espaços de endereços não elimina todos os caminhos de comunicação. [Conceito: 9.5][c95].

### ISA

Instruction Set Architecture, arquitetura do conjunto de instruções. Interface de instruções e estado relevante ao software, distinta da organização interna que a implementa. Não determina sozinha toda a compatibilidade de um executável. [Conceito: 7.2][c72].

### Isolamento

Separação que restringe como um contexto pode observar ou afetar outro. A garantia precisa indicar recurso, ação e ameaça; não é uma propriedade absoluta deduzida do nome do ambiente. [Conceito: 17.1](modulo-3/capitulo-17/17.1-virtualizacao-e-fronteiras.md).

## J

### JCS

JSON Canonicalization Scheme. Esquema que define uma representação canônica de JSON segundo regras específicas de valores e ordenação. Não se reduz a ordenar chaves nem aplica normalização Unicode automaticamente. [Conceito: 10.6][c106].

### JIT

Just-in-time compilation, compilação durante a execução. Pode combinar-se com interpretação e outras estratégias; não é obrigatório presumir que todo método foi compilado em toda execução de uma máquina virtual. [Conceito: 8.4][c84].

### Job

Unidade acompanhada pelo controle de trabalhos do shell. Um job em segundo plano não equivale a um serviço gerenciado pelo sistema. [Conceito: 14.4](modulo-3/capitulo-14/14.4-status-condicoes-e-controle.md).

### Journal

No percurso de logs Linux, registro estruturado administrado pelo journald. O rollback journal SQLite, citado no mesmo capítulo, tem outra função: recuperação transacional. [Conceito: 16.5](modulo-3/capitulo-16/16.5-logs-tempo-e-evidencias.md).

### JSON

JavaScript Object Notation. Formato textual de dados com objetos, arrays, strings, números, booleanos e null. A gramática não define sozinha os campos obrigatórios e os limites da aplicação; JSON não é uma ordem para executar JavaScript. [Conceito: 10.4][c104].

### JVM

Java Virtual Machine. Máquina abstrata que especifica representações e comportamento de programas, como o formato `class`. Uma implementação possui escolhas sobre como realizar a execução. Não é a mesma abstração que uma máquina virtual para instalar um sistema operacional convidado. [Conceito: 8.4][c84].

## K

### Kali Linux

Distribuição Linux preparada para tarefas de segurança. O ambiente e suas ferramentas não comprovam habilidade nem autorização de quem os utiliza. [Menção: capítulo 1][c1]. [Documentação][kali-doc].

### kB e KiB

kB, kilobyte, representa 1.000 bytes; KiB, kibibyte, representa 1.024 bytes. Os prefixos decimal e binário não são grafias equivalentes da mesma quantidade. [Conceito: 6.3][c63].

### Kerberos

Protocolo de autenticação em rede baseado em tickets e em uma autoridade de confiança. É mencionado como mecanismo de identidade que terá desenvolvimento próprio. [Menção: capítulo 1][c1]. [Especificação V5][kerberos-rfc].

### Kernel

Parte central do sistema operacional, responsável por funções essenciais de administração e mediação de recursos. Não se confunde com todo programa ou biblioteca disponível no sistema. [Introdução: 8.3][c83].

### kmod

Conjunto de ferramentas para trabalhar com módulos de kernel Linux, incluindo modprobe. Consultar o estado de módulos e solicitar carga ou remoção são operações diferentes. [Conceito: 12.4][c124].

### KVM

Kernel-based Virtual Machine. Interfaces do kernel Linux para criar e controlar máquinas virtuais, memória e processadores virtuais, utilizadas por componentes em espaço de usuário. [Conceito: 17.2](modulo-3/capitulo-17/17.2-maquinas-virtuais-e-hipervisores.md).

## L

### LASTEXITCODE

Variável automática do PowerShell que guarda o código do último programa nativo ou script que a definiu; não corresponde a todo erro de cmdlet. [Conceito: 14.4](modulo-3/capitulo-14/14.4-status-condicoes-e-controle.md).

### Latência

Duração de uma operação entre pontos de início e fim definidos. Não é sinônimo de capacidade nem de vazão; a medida precisa identificar o que está sendo observado. [Conceito: 7.1][c71].

### LGPD

Lei Geral de Proteção de Dados Pessoais, Lei brasileira nº 13.709/2018. O capítulo 3 introduz sua relação com evidências, sem emitir parecer sobre uma operação real. [Contexto: 3.2][c32].

### Ligação

Etapa que combina objetos e trata referências para produzir um artefato utilizável. Conhecer a declaração de uma função não garante que sua definição esteja disponível ao ligador. [Conceito: 8.2][c82].

### Ligação dinâmica

Ligação em que dependências são atendidas com participação de bibliotecas compartilhadas e do carregador dinâmico. Copiar somente o executável pode não transportar tudo de que ele precisa. [Conceitos: 8.2][c82] e [8.3][c83].

### Ligação estática

Ligação que pode incorporar código necessário de bibliotecas ao resultado construído. Um programa pode combinar decisões estáticas e dinâmicas; o comando abreviado não basta para inferir toda a composição do artefato. [Conceito: 8.2][c82].

### Ligador

Linker. Ferramenta que combina objetos, resolve referências a símbolos e realiza ajustes associados à ligação. Pode ser acionada por um coordenador como GCC. [Conceito: 8.2][c82].

### Linha de base

Referência de comportamento em condições identificadas. Ajuda a comparar um caso legítimo com o investigado sem confundir falha geral do serviço com decisão correta de autorização. [Conceito: 4.2][c42].

### Link simbólico

Objeto que guarda um caminho para outro destino. O caminho será resolvido no contexto pertinente e pode apontar para um destino ausente; não é uma cópia dos dados desse destino. [Conceito: 10.1][c101].

### Little-endian

Ordem que coloca primeiro o byte de menor peso de um valor com vários bytes. A convenção deve ser definida pelo formato ou operação, não adivinhada pela aparência dos dados. [Conceito: 6.3][c63].

### LocalAppData

Pasta conhecida destinada a dados locais de aplicações de um usuário. Sua localização deve ser obtida pelo mecanismo apropriado, não presumida a partir de um único equipamento. [Conceito: 13.2](modulo-3/capitulo-13/13.2-volumes-caminhos-e-perfis.md).

### Localidade espacial

Padrão de acesso a posições próximas de memória. Pode favorecer o aproveitamento de blocos trazidos para uma cache; não é garantia sobre toda aplicação. [Conceito: 7.3][c73].

### Localidade temporal

Reutilização de uma informação em um intervalo próximo. Ajuda a explicar por que uma cache pode reduzir acessos a outros níveis. [Conceito: 7.3][c73].

### LocalSystem

Contexto de conta com amplos privilégios locais, também encontrado como `NT AUTHORITY\SYSTEM`. Não equivale a autorização universal sobre recursos remotos. [Conceito: 13.6](modulo-3/capitulo-13/13.6-inicializacao-servicos-e-investigacao.md).

### Log

Registro de eventos produzido por um sistema. Seu valor depende dos campos, procedência, cobertura e relação com a operação examinada. [Conceito: 4.3][c43].

### Loopback

Interface para comunicação local dentro de um contexto de rede. O significado de local depende do namespace e da configuração em que o processo executa. [Conceito: 17.5](modulo-3/capitulo-17/17.5-conectividade-e-alcance.md).

### LSM

Linux Security Modules. Arcabouço do kernel para participação de mecanismos adicionais de segurança. Sua presença não informa sozinha quais políticas estão ativas ou quais operações serão permitidas. [Conceito: 11.4][c114].

## M

### M.2

Especificação de formato e conexão usada por diferentes dispositivos. Não é sinônimo de NVMe: o formato físico não determina sozinho a interface de armazenamento. [Conceito: 7.4][c74].

### main

Função usada como entrada principal no programa C convencional apresentado. Sua execução pode ser precedida por carregamento e inicialização; não é necessariamente a primeira instrução do executável nem da máquina. [Conceitos: 8.2][c82] e [8.3][c83].

### Major page fault

No Linux, falta de página cujo atendimento exigiu atividade de entrada/saída, conforme o contador documentado. Major não significa gravidade de uma vulnerabilidade. [Conceito: 9.4][c94].

### malloc

Função de C que solicita um bloco de memória dinâmica e retorna um ponteiro quando obtém sucesso. Não garante inicialização dos bytes; o atendimento e as políticas de recursos precisam ser considerados. [Conceito: 9.3][c93].

### Mapeamento

Relação que organiza uma região virtual, seus acessos e o conteúdo que ela representa. A existência do mapa não demonstra residência imediata de todos os bytes nem o limite de cada objeto mantido na região. [Conceitos: 9.2][c92] e [9.4][c94].

### Mapeamento anônimo

Região de memória sem um arquivo como origem direta de seu conteúdo. Pode ser privada ou compartilhada conforme o mecanismo; anônimo não significa invisível ou livre de controles. [Conceito: 9.4][c94].

### Mapeamento compartilhado

Região com semântica que permite a participantes observar alterações no conteúdo compartilhado. Sua existência não define, sozinha, a ordem das operações concorrentes. [Conceito: 9.4][c94].

### Mapeamento privado

Região cujas alterações privadas não devem aparecer automaticamente nas outras visões. A implementação pode utilizar cópia na escrita para cumprir esse contrato. [Conceito: 9.4][c94].

### Máquina virtual

No recorte de sistema, modelo de computador que oferece CPU, memória e dispositivos para executar um sistema convidado. É distinto de uma máquina virtual de linguagem e de um simples conjunto de dependências. [Conceito: 17.2](modulo-3/capitulo-17/17.2-maquinas-virtuais-e-hipervisores.md).

### Máscara de ACL

Entrada de ACL POSIX que limita direitos de usuários nomeados e grupos. Não é a umask e não limita da mesma maneira as entradas do proprietário e de outros. [Conceito: 15.3](modulo-3/capitulo-15/15.3-criacao-propriedade-e-acls.md).

### MB e MiB

MB, megabyte, representa 1.000.000 de bytes; MiB, mebibyte, representa 1.048.576. Uma taxa em Mbit/s mede bits por segundo, não bytes armazenados. [Conceito: 6.3][c63].

### Mecanismo

No vocabulário de análise do livro, meio utilizado para realizar uma decisão, como a verificação de uma permissão. A política define o critério; possuir o mecanismo não garante uma política adequada. [Conceito: 11.1][c111].

### Memória não volátil

Memória que conserva informação sem alimentação contínua. A propriedade não garante disponibilidade eterna, imunidade a defeitos ou segurança contra acesso indevido. [Conceitos: 7.3][c73] e [7.4][c74].

### Memória virtual

Organização que fornece contextos de endereços e mapeamentos utilizados na execução, com participação na tradução e no isolamento. Não se resume a utilizar armazenamento quando a RAM é insuficiente. [Introdução: 7.3][c73]; [desenvolvimento: 9.2][c92] e [9.4][c94].

### Memória volátil

Memória cuja manutenção da informação depende de alimentação. Volatilidade não é um procedimento certificado de eliminação segura de todos os dados sensíveis. [Conceito: 7.3][c73].

### Menor privilégio

Princípio de conceder a cada componente ou identidade somente as capacidades necessárias às suas responsabilidades. Limitar o serviço não substitui a autorização dos registros que ele entrega a seus clientes. [Conceito: 11.4][c114].

### Merged-/usr

Organização em que determinados caminhos tradicionais, como /bin, são links para equivalentes em /usr. A relação pode ser prevista pela distribuição e não demonstra, sozinha, corrupção da instalação. [Conceito: 12.2][c122].

### Metadados

Informações sobre um objeto, como tamanho, proprietário e marcas de tempo. Podem pertencer ao sistema de arquivos ou ao próprio documento; precisam ser interpretadas conforme sua origem e regra de atualização. [Conceito: 10.1][c101].

### Metasploit

Framework de segurança com módulos para tarefas distintas, inclusive exploração. O livro usa sua terminologia para separar exploit e payload, sem afirmar que toda falha segue essa arquitetura. [Conceito: 5.2][c52].

### MF

Multifrequency, sinalização multifrequência. Na telefonia histórica discutida, combinações de tons representavam endereçamento. É diferente do tom único de supervisão de certas ligações. [Contexto: capítulo 2][c2].

### MIC

Mandatory Integrity Control. Mecanismo de controle obrigatório que utiliza níveis de integridade e políticas adicionais ao controle discricionário. [Conceito: 13.4](modulo-3/capitulo-13/13.4-contas-tokens-e-controle-de-acesso.md).

### Microarquitetura

Organização interna que implementa uma arquitetura de instruções. Implementações da mesma interface podem ter estruturas e desempenhos diferentes. [Conceito: 7.2][c72].

### Microkernel

Organização que concentra um conjunto reduzido de mecanismos no núcleo e deixa diversos serviços em componentes externos. A comparação com seL4 não certifica a segurança de qualquer sistema montado dessa maneira. [Conceito: 11.1][c111].

### MIME

Multipurpose Internet Mail Extensions. No uso “tipo MIME” do capítulo, refere-se à identificação de um tipo de mídia, como application/json. Essa identificação declarada não substitui a validação do conteúdo. [Contexto: 10.2][c102].

### Minor page fault

No Linux, falta de página atendida sem atividade de entrada/saída, conforme o contador documentado. Pode participar de preparação ou ajustes normais de memória; não significa automaticamente defeito pequeno no programa. [Conceito: 9.4][c94].

### MIT

Massachusetts Institute of Technology, instituição à qual pertence o TMRC. A sigla também nomeia uma licença de software no repositório; são usos distintos. [Contexto histórico][c2]. [Licenciamento](../LICENSE.md).

### MMU

Memory Management Unit, unidade de gerenciamento de memória. Participa da tradução de endereços e das verificações associadas aos mapeamentos administrados pelo sistema operacional. [Introdução: 7.3][c73]; [paginação: 9.2][c92].

### Modelo de linguagem

Modelo computacional usado para processar ou gerar linguagem. A introdução menciona aplicações que recebem contexto e instruções; nem todo modelo possui ferramentas externas. [Menção: capítulo 2][c2].

### Modo kernel

Nível de execução utilizado por componentes centrais do sistema com acessos e responsabilidades distintos dos programas em modo usuário. Não é sinônimo de uma conta administrativa nem exige, em cada entrada, trocar para outro processo. [Conceito: 9.1][c91].

No contexto do capítulo 13: Modo de execução utilizado por componentes centrais do sistema, com acesso a recursos restritos às aplicações comuns. Não é sinônimo de pertencer ao grupo Administradores. [Conceito: 13.1](modulo-3/capitulo-13/13.1-arquitetura-processos-e-objetos.md).

### Modo usuário

Nível de execução típico de aplicações, com acesso mediado aos serviços e recursos protegidos do sistema. É uma classificação diferente da identidade e das permissões da conta que iniciou o programa. [Conceito: 9.1][c91].

No contexto do capítulo 13: Modo de execução em que operam aplicações comuns, com acesso mediado aos serviços e recursos protegidos do sistema. [Conceito: 13.1](modulo-3/capitulo-13/13.1-arquitetura-processos-e-objetos.md).

### modprobe

Ferramenta do conjunto kmod que trata inclusão e remoção de módulos Linux considerando dependências. É citada para explicar seu papel, sem execução dessas alterações no capítulo. [Conceito: 12.4][c124].

### Módulo de kernel

Componente que pode ser carregado separadamente para acrescentar funcionalidade ao kernel, conforme a configuração. Não é um processo de usuário isolado; nem todo driver precisa ser fornecido como módulo carregável. [Conceito: 12.4][c124].

### Montagem

Conversão da representação assembly em código objeto, realizada por um montador ou assembler. É uma responsabilidade distinta da ligação das peças e da execução do programa resultante. [Conceito: 8.2][c82].

### Montagem somente para leitura

Restrição de escrita por uma montagem. Não oculta o conteúdo nem comprova ausência de outro caminho de acesso ou de escrita. [Conceito: 17.4](modulo-3/capitulo-17/17.4-compartilhamentos-e-autoridade.md).

### Morris Worm

Programa autorreplicante associado a Robert Tappan Morris e ao incidente de novembro de 1988. Não é a pessoa do episódio do apito telefônico nem a origem única de cybersecurity. [Contexto: capítulo 2][c2].

### Mount namespace

Namespace Linux que separa a lista de montagens visível. Origens de dados podem continuar compartilhadas, e propagação de montagens depende da configuração. [Conceito: 17.3](modulo-3/capitulo-17/17.3-containers-namespaces-e-recursos.md).

### Movimentação lateral

Uso de acesso ou relação de confiança para alcançar outros sistemas ou contextos do ambiente. Pode combinar-se com escalada de privilégios, mas não é a mesma atividade. [Menção: capítulo 1][c1].

### mtime

No Linux, marca de tempo associada à modificação do conteúdo de um arquivo. Não deve ser confundida com ctime nem com um campo de data escrito pela aplicação dentro do documento. [Conceito: 10.1][c101].

### Mutex

Mecanismo de exclusão mútua que coordena a entrada de participantes numa região protegida. Todos os acessos relevantes precisam respeitar o contrato; proteger apenas a escrita final não corrige necessariamente uma decisão baseada numa leitura antiga. [Conceito: 9.5][c95].

## N

### namei

Utilitário util-linux que acompanha os componentes de um caminho e pode exibir modos e proprietários. Ajuda a localizar onde a resolução depende de uma passagem permitida. [Conceito: 15.7](modulo-3/capitulo-15/15.7-investigacao-e-verificacao.md).

### Namespace

No Linux, visão particular de uma classe de recursos apresentada a um conjunto de processos. O tipo de namespace determina o que se separa; não equivale automaticamente a um limite de consumo. [Conceito: 11.4][c114].

No Linux, instância ou visão de uma categoria de recursos associada a processos. Cada categoria tem alcance próprio; separar uma visão não separa automaticamente todas as outras. [Conceito: 17.3](modulo-3/capitulo-17/17.3-containers-namespaces-e-recursos.md).

### NAT

Network Address Translation, tradução de endereços de rede. No modo VirtualBox apresentado, pode permitir comunicação iniciada pelo convidado; não significa ausência de comunicação externa. [Conceito: 17.5](modulo-3/capitulo-17/17.5-conectividade-e-alcance.md).

### NBS

National Bureau of Standards. Instituição identificada no relatório histórico do workshop de segurança de 1972. A sigla é preservada conforme a fonte histórica. [Contexto: capítulo 2][c2].

### NIST

National Institute of Standards and Technology. Instituição que mantém referências e glossários utilizados no livro. As definições agregadas podem vir de documentos e contextos diferentes. [Contexto: 5.1][c51].

### Nmap

Network Mapper. Ferramenta de exploração e auditoria de redes, incluindo descoberta e investigação de portas e serviços. O resultado exige interpretação, não diagnóstico automático de vulnerabilidade. [Menção: capítulo 1][c1]. [Documentação][nmap-doc].

### Normalização Unicode

Transformação segundo formas definidas de equivalência. NFC e NFD tratam equivalência canônica; NFKC e NFKD acrescentam equivalências de compatibilidade. Não significa remover acentos, igualar toda aparência semelhante ou canonicalizar todo documento. [Conceito: 10.3][c103].

### nosuid

Opção de montagem relacionada à desconsideração de transições privilegiadas por execução. É uma condição do mecanismo, não uma alteração do nome do executável. [Conceito: 15.5](modulo-3/capitulo-15/15.5-privilegios-e-delegacao.md).

### NSS

Name Service Switch. Mecanismo de configuração de fontes e ordem de consulta de bases como usuários e grupos. Não é, por si só, a autorização de acesso a um arquivo. [Conceito: 15.1](modulo-3/capitulo-15/15.1-identidades-contas-e-contextos.md).

### NTFS

New Technology File System. Sistema de arquivos utilizado pelo Windows, com organização de arquivos, metadados e mecanismos de segurança e consistência. [Conceito: 13.2](modulo-3/capitulo-13/13.2-volumes-caminhos-e-perfis.md).

### Núcleo

Core. Unidade de processamento capaz de conduzir execução dentro de um processador. Recursos adicionais ajudam conforme o paralelismo disponível no trabalho; não dividem automaticamente o tempo de qualquer tarefa. [Conceito: 7.2][c72].

### NVMe

Non-Volatile Memory Express. Interface de comandos para armazenamento não volátil, comum sobre PCIe em SSDs locais. Não é formato físico nem garantia isolada de desempenho. [Conceito: 7.4][c74].

### NX

No Execute. Designação associada ao suporte para impedir execução em páginas marcadas como não executáveis. Protege uma classe de acesso, não todas as regras do programa. [Conceito: 9.5][c95].

## O

### Object Manager

Gerenciador de objetos do Windows. Participa do gerenciamento de nomes, referências, direitos e tempo de vida de recursos. [Conceito: 13.1](modulo-3/capitulo-13/13.1-arquitetura-processos-e-objetos.md).

### Objeto do Windows

Representação de um recurso gerenciado pelo sistema, como processo, arquivo, chave do Registro ou token. Não depende do conceito de objeto de uma linguagem específica. [Conceito: 13.1](modulo-3/capitulo-13/13.1-arquitetura-processos-e-objetos.md).

### Observação

Informação registrada por um meio identificado. Pode ter limites ou erros de medição e não contém automaticamente a explicação da causa do que foi percebido. [Conceito: 4.1][c41].

### Octeto

Grupo de oito bits. O termo aparece em especificações de protocolos e explicita o tamanho que chamamos de byte no escopo da obra. [Conceito: 6.3][c63].

### Oneshot

No tipo de serviço systemd apresentado, execução de trabalho finito. A configuração pode manter a unidade considerada ativa após o término dos processos. [Conceito: 16.2](modulo-3/capitulo-16/16.2-servicos-e-supervisao.md).

### OOM

Out of memory, insuficiência de memória. O OOM killer do Linux pode encerrar tarefas para tentar recuperar recursos. Nem todo encerramento inesperado é OOM; sua causa precisa ser conferida. [Conceito: 9.4][c94].

### Opção

Argumento que configura o comportamento de um comando conforme sua interface. Nem todo texto precedido por um hífen é interpretado da mesma forma por todos os programas. [Conceito: 14.2](modulo-3/capitulo-14/14.2-argumentos-aspas-e-expansoes.md).

### Operação atômica

Operação com garantias específicas de indivisibilidade e ordenação segundo a interface e o modelo de memória. Uma sequência de várias operações atômicas não se torna automaticamente uma transação indivisível. [Conceito: 9.5][c95].

### Operação bloqueante

Operação que pode manter o fluxo à espera de condições para prosseguir. A espera por E/S não se resolve necessariamente com maior prioridade de CPU. [Conceito: 11.3][c113].

### Operação não bloqueante

Operação que retorna sem aguardar determinada condição e pode informar que ainda não é possível prosseguir. Não significa que o trabalho já terminou; as garantias dependem da interface e do recurso. [Conceito: 11.3][c113].

### Operador de chamada

Operador & do PowerShell que inicia o comando indicado. Não interpreta automaticamente uma string com comandos e operadores como um novo roteiro. [Conceito: 14.2](modulo-3/capitulo-14/14.2-argumentos-aspas-e-expansoes.md).

### Operando

Valor sobre o qual um comando opera, distinguido de opções que configuram seu comportamento conforme o contrato da ferramenta. [Conceito: 14.6](modulo-3/capitulo-14/14.6-automacao-e-fronteiras-de-confianca.md).

### os-release

Arquivo de identificação da instalação, com campos como ID e PRETTY_NAME. Identifica uma camada diferente da release do kernel em execução e não certifica a integridade de todos os componentes. [Conceito: 12.1][c121].

### OSINT

Open Source Intelligence, inteligência de fontes abertas. Conhecimento produzido a partir de informações publicamente ou comercialmente disponíveis para responder a necessidades de inteligência. Não é sinônimo de software open source.

**Menção no planejamento, ainda sem capítulo desenvolvido:** [mapa da obra](../editorial/master-outline.md). A entrada esclarece a sigla solicitada, sem registrar o assunto como já ensinado. [Referência institucional][osint-doc].

### Overcommit

Política que pode admitir compromissos de memória sem reservar imediatamente todos os recursos físicos para seu possível uso. Um pedido aceito não significa garantia universal de atendimento futuro em qualquer condição. [Conceito: 9.4][c94].

### Overflow

Estouro: situação em que um resultado não cabe na faixa da representação numérica adotada. Reação, sinalização de erro e eventual retenção de bits dependem das regras do sistema ou linguagem. [Conceito: 6.3][c63].

### OWASP

Open Worldwide Application Security Project. Fundação e comunidade que mantêm projetos e referências sobre segurança de software. Não é ferramenta única nem vulnerabilidade. [Ocorrência: 4.1][c41] e [5.1][c51]. [Sobre a fundação][owasp-about].

## P

### Pacote de software

Unidade de distribuição com arquivos e metadados para instalação e administração, podendo incluir dependências e ações de manutenção. Não se confunde com um pacote de rede. [Conceito: 12.5][c125].

### Page fault

Falta de página: situação que exige tratar um acesso que não pôde prosseguir sob as condições presentes. Pode envolver preparação normal, cópia, E/S ou violação de proteção. Não é sinônimo de TLB miss ou defeito físico da RAM. [Conceitos: 9.2][c92] e [9.4][c94].

### Página

Unidade de organização da memória virtual paginada. O tamanho depende do sistema e da arquitetura; uma página não corresponde necessariamente a um único objeto do programa. [Conceito: 9.2][c92].

### Paginação de segundo nível

Tradução com suporte de hardware entre endereços físicos do convidado e do hospedeiro, no percurso de virtualização descrito. Complementa a tradução administrada pelo convidado. [Conceito: 17.2](modulo-3/capitulo-17/17.2-maquinas-virtuais-e-hipervisores.md).

### Paginação sob demanda

Preparação de conteúdo ou mapeamentos quando seu uso exige atendimento, em vez de materializar antecipadamente todo espaço virtual possível. Ter uma região virtual não comprova que ela ocupe imediatamente RAM exclusiva. [Conceito: 9.4][c94].

### Paralelismo

Execução simultânea de trabalhos em recursos capazes de realizá-los. Distingue-se da concorrência, que também pode avançar por alternância numa única unidade de execução. [Conceito: 9.1][c91].

### Parâmetro

Posição ou nome declarado para receber um valor em uma função, script ou comando. É diferente do valor concreto fornecido na chamada. [Conceito: 14.2](modulo-3/capitulo-14/14.2-argumentos-aspas-e-expansoes.md).

### Paravirtualização

Cooperação consciente de componentes do convidado com a plataforma de virtualização, por interfaces próprias. Não constitui autorização irrestrita de acesso ao hospedeiro. [Conceito: 17.2](modulo-3/capitulo-17/17.2-maquinas-virtuais-e-hipervisores.md).

### Parser

Analisador que reconhece a estrutura ou gramática de uma entrada. Parsing é essa atividade de análise. Reconhecer a sintaxe não substitui conferir regras do domínio, permissões ou orçamento de processamento. [Conceito: 10.5][c105].

### Passthrough de dispositivo

Disponibilização de acesso a um dispositivo ao convidado pelo caminho suportado da virtualização. As operações expostas sobre o recurso real entram na análise de confiança. [Conceito: 17.4](modulo-3/capitulo-17/17.4-compartilhamentos-e-autoridade.md).

### Pasta conhecida

Local identificado por interfaces do Windows para uma função, como arquivos de programas ou dados de usuário. Não implica caminho literal universal. [Conceito: 13.2](modulo-3/capitulo-13/13.2-volumes-caminhos-e-perfis.md).

### PATH

Variável de ambiente que participa da busca de executáveis por nome. Não descreve sozinha toda a resolução de funções, aliases ou comandos internos. [Conceito: 14.2](modulo-3/capitulo-14/14.2-argumentos-aspas-e-expansoes.md).

### Payload

No contexto de exploração apresentado, componente que realiza a ação desejada após aproveitar a vulnerabilidade. Nem toda exploração possui payload executável separado. [Conceito: 5.2][c52].

### PCIe

Peripheral Component Interconnect Express. Interconexão utilizada para comunicação entre componentes e dispositivos. É uma camada diferente da interface de comandos NVMe. [Conceito: 7.4][c74].

### PE

Portable Executable. Formato de imagem executável descrito na documentação Windows. O nome não promete executar o mesmo artefato em qualquer sistema; arquitetura, ABI e dependências continuam relevantes. [Introdução: 8.3][c83].

No contexto do capítulo 13: Portable Executable. Formato de imagens executáveis e bibliotecas do Windows, com informações utilizadas no carregamento. O nome não garante compatibilidade com qualquer plataforma. [Conceito: 13.3](modulo-3/capitulo-13/13.3-executaveis-bibliotecas-e-carregamento.md).

### Pentest

Penetration test, teste de intrusão. Avaliação com objetivos, escopo, métodos permitidos e comunicação de resultados; não se resume à obtenção de acesso. [Contexto: capítulo 2][c2] e [capítulo 3][c3].

### Perfil de usuário

Conjunto de dados e configurações associados a um usuário. Conta, perfil carregado e sessão de logon são conceitos relacionados, mas distintos. [Conceito: 13.2](modulo-3/capitulo-13/13.2-volumes-caminhos-e-perfis.md).

### Perfil do shell

Arquivo de personalização executado em determinados contextos de inicialização. Pode definir comportamentos ausentes em outra execução. [Conceito: 14.5](modulo-3/capitulo-14/14.5-scripts-contexto-e-repetibilidade.md).

### Permissão de busca

Permissão representada por x em diretórios Linux, necessária para procurar componentes e atravessar o caminho. Não equivale a enumerar os nomes do diretório. [Conceito: 15.2](modulo-3/capitulo-15/15.2-permissoes-linux-e-caminhos.md).

### Persistência

Meios de conservar ou recuperar acesso apesar de mudanças, como interrupção de uma sessão. Não é etapa obrigatória nem automaticamente autorizada após exploração. [Menção: capítulo 1][c1]. No contexto de armazenamento, persistência é conservação de dados além do estado de trabalho temporário: é outro uso da palavra, desenvolvido em [7.4][c74].

### Phone phreaking

Investigação e manipulação de mecanismos de redes telefônicas. O capítulo discute episódios históricos, sem generalizar métodos para redes atuais ou autorizá-los. [Contexto: capítulo 2][c2].

### pickle

Mecanismo Python de serialização de objetos. Sua desserialização pode executar comportamento e não deve receber conteúdo não confiável como se fosse um leitor de dados inofensivo. Apenas a capacidade documentada é discutida; nenhum pickle foi executado. [Introdução: 10.6][c106].

### PID

Process identifier, identificador de processo. No percurso Linux, a substituição de imagem por `execve` preserva o PID. O número identifica um contexto de processo, não uma versão imutável do programa. [Conceito: 8.3][c83].

No contexto do capítulo 13: Process Identifier. Identificador de um processo. Sua interpretação deve preservar o contexto da execução e do momento investigado. [Conceito: 13.1](modulo-3/capitulo-13/13.1-arquitetura-processos-e-objetos.md).

### PID namespace

Contexto hierárquico de identificação e visibilidade de processos no Linux. Uma mesma execução pode ter identificadores distintos em camadas diferentes. [Conceito: 17.3](modulo-3/capitulo-17/17.3-containers-namespaces-e-recursos.md).

### Pilha de execução

Stack. Organização utilizada para chamadas, retornos e estado associado, conforme ABI e implementação. Nem toda variável local precisa ocupar uma posição visível na pilha, e a pilha própria de um thread não é automaticamente isolada dos demais. [Conceitos: 9.1][c91] e [9.3][c93].

### Pipe

Mecanismo de comunicação que, no modelo Unix apresentado, transporta um fluxo de bytes sem fronteiras próprias de mensagens. [Conceito: 14.3](modulo-3/capitulo-14/14.3-fluxos-redirecionamentos-e-pipelines.md).

### pipefail

Opção do Bash que inclui falhas de etapas anteriores no cálculo do status de um pipeline. Não realiza rollback de efeitos. [Conceito: 14.4](modulo-3/capitulo-14/14.4-status-condicoes-e-controle.md).

### Pipeline

Composição que conecta a saída de uma etapa à entrada de outra. Bash e PowerShell têm modelos e fronteiras diferentes para essa conexão. [Conceito: 14.3](modulo-3/capitulo-14/14.3-fluxos-redirecionamentos-e-pipelines.md).

### PIPESTATUS

Array do Bash com os códigos das etapas do pipeline recente em primeiro plano. Deve ser consultado antes que outra execução substitua a informação. [Conceito: 14.4](modulo-3/capitulo-14/14.4-status-condicoes-e-controle.md).

### Pivotamento

Uso de um ponto intermediário para alcançar recursos que não eram diretamente acessíveis da origem da investigação. Depende do escopo autorizado. [Menção: capítulo 1][c1].

### PNG

Portable Network Graphics. Formato de imagem apresentado como exemplo de assinatura seguida de blocos estruturados. Reconhecer seus bytes iniciais não substitui validar o restante nem identifica criptograficamente o autor. [Menção: 10.2][c102].

### Política

Critério que orienta decisões de uso, distribuição ou acesso a recursos. Um mecanismo pode aplicar corretamente uma política inadequada ou deixar de aplicar a política pretendida. [Conceito: 11.1][c111].

### Polling

Consulta repetida a um estado para descobrir se há evento ou trabalho disponível. Pode ser uma escolha de projeto adequada; não é automaticamente melhor ou pior que interrupções. [Conceito: 7.5][c75].

### Ponteiro

Valor usado para referenciar um objeto ou posição conforme as regras da linguagem. Conhecer onde um objeto esteve não prolonga seu tempo de vida nem autoriza acesso além de seu tamanho. [Conceito: 9.3][c93].

### Ponto de código

Identificador numérico de uma posição no espaço Unicode, escrito frequentemente como U+ seguido de hexadecimal. Não é sinônimo de byte nem de uma unidade visual de texto. [Conceito: 6.4][c64].

### Ponto de entrada

Posição de entrada indicada para um estágio de execução. No executável, não deve ser identificada automaticamente com `main`, pois carregamento e preparação do runtime podem preceder a função principal. [Conceito: 8.3][c83].

### Ponto de montagem

Local de uma árvore de nomes em que uma montagem torna seu conteúdo acessível. O caminho não revela sozinho a origem dos dados nem a visão de todos os processos. [Conceito: 12.2][c122].

### Porta de rede

Identificador usado por protocolos de transporte para distinguir pontos de comunicação. O número isolado não certifica qual serviço está sendo executado. [Menção: capítulo 1][c1].

### Porta publicada

Associação de um ponto de entrada do hospedeiro ao serviço de um container. Endereço de publicação e controles de rede determinam parte do alcance; acesso local não prova acesso exclusivo local. [Conceito: 17.5](modulo-3/capitulo-17/17.5-conectividade-e-alcance.md).

### Pós-exploração

Análise e atividades posteriores ao acesso obtido por exploração, como investigar contexto, permissões e alcance. O objetivo determina o que é necessário e autorizado. [Introdução: capítulo 1][c1].

### PowerShell

Shell e linguagem de automação com pipeline de objetos e regras próprias de comandos, parâmetros, erros e execução. [Conceito: 14.1](modulo-3/capitulo-14/14.1-terminal-shell-e-comandos.md).

### PPID

Parent Process ID, identificador do processo pai no contexto observado. Não é um identificador permanente de uma aplicação. [Conceito: 16.1](modulo-3/capitulo-16/16.1-ciclo-de-vida-e-processos.md).

### Pré-processamento

Etapa que trata diretivas como inclusões de cabeçalhos antes da tradução C propriamente dita. O resultado textual não constitui a execução das operações descritas pelo programa. [Conceito: 8.2][c82].

### Preempção

Interrupção da ocupação da CPU por um fluxo para permitir encaminhar outro segundo as regras de escalonamento. Não garante divisão igual ou atendimento imediato de qualquer tarefa. [Conceito: 11.3][c113].

### Previsão

Resultado que uma hipótese leva a esperar em condições especificadas, formulado antes de observar a execução. Não é evidência de que ocorreu. [Conceito: 4.1][c41].

### printf

Comando de saída formatada. No Bash, possui uma implementação interna; manter o formato separado dos dados evita entregar o dado como linguagem de formatação. [Conceito: 14.1](modulo-3/capitulo-14/14.1-terminal-shell-e-comandos.md).

### Privilégio

Permissão ou capacidade associada a uma identidade ou contexto de execução. Saber que código foi executado não informa, sozinho, quais permissões ele possuía. [Menção: capítulo 1][c1].

### Privilégio do Windows

Direito a determinadas operações relacionadas ao sistema. É distinto de um direito de acesso a um objeto específico e possui estado de habilitação no token. [Conceito: 13.4](modulo-3/capitulo-13/13.4-contas-tokens-e-controle-de-acesso.md).

### Processador lógico

Contexto de execução que o hardware apresenta ao sistema. Contextos do mesmo núcleo podem compartilhar recursos; não equivalem automaticamente a núcleos físicos independentes. [Conceito: 7.2][c72].

### Processo

Instância de execução administrada pelo sistema operacional, com estado, espaço de endereços e referências a recursos. Diferentes processos podem utilizar o mesmo programa sem compartilhar todo seu estado. [Conceito: 8.3][c83]; [organização e threads: 9.1][c91].

No contexto do capítulo 13: Contexto de execução com recursos associados. Não se confunde com o arquivo executável nem com o resultado de negócio que a aplicação deve produzir. [Conceito: 13.1](modulo-3/capitulo-13/13.1-arquitetura-processos-e-objetos.md).

### Processo órfão

Processo que perdeu seu pai e pode ser adotado por outro responsável. Não precisa estar encerrado nem ser um zumbi. [Conceito: 16.1](modulo-3/capitulo-16/16.1-ciclo-de-vida-e-processos.md).

### Processo zumbi

No modelo Linux, processo encerrado que conserva informações mínimas de término ainda não recolhidas pelo responsável. Não continua executando o programa. [Conceito: 16.1](modulo-3/capitulo-16/16.1-ciclo-de-vida-e-processos.md).

### Procfs

Sistema de arquivos normalmente montado em /proc que apresenta informações de processos e do sistema em funcionamento. Seus dados são dinâmicos; várias consultas não equivalem necessariamente a uma fotografia atômica do sistema. [Conceito: 12.3][c123].

### Program Files

Pasta conhecida associada a arquivos de programas. Sua identificação e localização dependem do contexto apropriado da instalação. [Conceito: 13.2](modulo-3/capitulo-13/13.2-volumes-caminhos-e-perfis.md).

### ProgramData

Pasta conhecida associada a dados de aplicações compartilhados na máquina, distinta das áreas particulares de dados de um usuário. [Conceito: 13.2](modulo-3/capitulo-13/13.2-volumes-caminhos-e-perfis.md).

### Prompt

Indicação apresentada para interação com o shell. Seu texto ou símbolo pode ser personalizado e não comprova privilégios. [Conceito: 14.1](modulo-3/capitulo-14/14.1-terminal-shell-e-comandos.md).

### Prompt injection

Manipulação de entradas ou conteúdos processados por uma aplicação com modelo de linguagem para influenciar indevidamente seu comportamento. Os efeitos dependem do contexto e das capacidades da aplicação; não é equivalente a SQL injection. [Menções: capítulos 1][c1] e [2][c2]. [Referência][prompt-doc].

### Prontidão

Condição de preparação para uma operação ou estágio do ciclo de vida, conforme um contrato. No serviço, uma indicação de inicialização concluída não é garantia permanente de funcionamento de todas as capacidades. [Conceito: 11.5][c115].

Condição definida para começar a atender determinada função. Criar um processo, concluir a inicialização e confirmar uma operação são marcos diferentes. [Conceito: 16.2](modulo-3/capitulo-16/16.2-servicos-e-supervisao.md).

### Proprietário

Identidade associada à propriedade de um recurso. Poder administrar sua política e ter uma operação de conteúdo concedida são perguntas diferentes. [Conceito: 15.2](modulo-3/capitulo-15/15.2-permissoes-linux-e-caminhos.md).

### Protobuf

Protocol Buffers. Formato de serialização binária em que números de campo e tipos de transporte são interpretados com apoio de um esquema. A introdução não implementa um codec Protobuf nem promete compatibilidade de qualquer alteração de esquema. [Introdução: 10.4][c104].

### Protocolo

Convenções que permitem a sistemas interpretar uma comunicação. Conhecê-las ajuda a compreender os significados e limites de uma resposta. [Menção: capítulo 1][c1]; [exemplo HTTP: 4.3][c43].

### Prova de conceito (PoC)

Proof of concept. Demonstração de uma possibilidade em condições determinadas. Não comprova automaticamente comprometimento de produção ou ocorrência de ataque anterior. [Conceito: 5.2][c52].

### Pseudoterminal

Par de interfaces que oferece a programas comportamento de terminal sem depender de um terminal físico dedicado. [Conceito: 14.1](modulo-3/capitulo-14/14.1-terminal-shell-e-comandos.md).

### PSS

Proportional Set Size. Medida que atribui proporcionalmente a parcela de memória residente compartilhada entre os participantes considerados. Não tem o mesmo significado de RSS nem de todo o tamanho virtual. [Conceito: 9.4][c94].

### PTES

Penetration Testing Execution Standard. Referência metodológica para testes de intrusão. O capítulo usa sua distinção entre escopo e regras de engajamento, sem adotar toda recomendação histórica como atual. [Contexto: 3.1][c31].

### PTY

Abreviação de pseudoterminal; no modelo Unix, descreve as interfaces pareadas usadas por aplicações de terminal. [Conceito: 14.1](modulo-3/capitulo-14/14.1-terminal-shell-e-comandos.md).

### pwsh

Nome do executável do PowerShell moderno usado nos exemplos; deve ser distinguido de powershell.exe do Windows PowerShell. [Conceito: 14.5](modulo-3/capitulo-14/14.5-scripts-contexto-e-repetibilidade.md).

## Q

### QEMU

Projeto de emulação e virtualização que oferece modelos de máquina e pode utilizar aceleradores. Arquitetura, acelerador, dispositivos e configuração participam do comportamento e do recorte de segurança. [Conceito: 17.2](modulo-3/capitulo-17/17.2-maquinas-virtuais-e-hipervisores.md).

### Quadro de chamada

Stack frame. Organização associada a uma ativação de função, que pode conservar valores e informações para a continuidade. Forma e existência observável dependem da ABI e das decisões do compilador. [Conceito: 9.3][c93].

### Quadro físico

Page frame. Unidade física correspondente ao tamanho de página considerado num mapeamento. O deslocamento seleciona uma posição dentro do quadro; a tabela fornece a relação com a página virtual. [Conceito: 9.2][c92].

### Quoting

Uso de aspas ou escapes para controlar a interpretação de caracteres. A proteção obtida depende da linguagem, do contexto e do consumidor posterior. [Conceito: 14.2](modulo-3/capitulo-14/14.2-argumentos-aspas-e-expansoes.md).

## R

### RAM

Random Access Memory, memória de acesso aleatório. A expressão descreve o acesso a posições, não geração de valores aleatórios. A memória principal convencional discutida utiliza DRAM volátil. [Conceito: 7.3][c73].

### Ransomware

Software malicioso usado para restringir acesso a dados ou sistemas e exigir resgate, frequentemente por criptografia de arquivos. A introdução apenas menciona a categoria, sem análise de amostras. [Menção: capítulo 1][c1]. [Referência CISA][ransomware-doc].

### READ_CONTROL

Direito Windows de consultar partes do descritor de segurança. Não é simplesmente o direito de ler o conteúdo de um arquivo. [Conceito: 15.4](modulo-3/capitulo-15/15.4-tokens-e-acls-no-windows.md).

### Red Team

Atividade ou equipe que utiliza uma perspectiva adversarial orientada a objetivos para avaliar uma organização e suas defesas. Não é automaticamente sinônimo de pentest. [Menção: capítulo 1][c1].

### Rede interna

No VirtualBox, rede entre convidados participantes, sem acrescentar por esse mecanismo uma interface de participação do host. Não garante sigilo contra quem administra a plataforma. [Conceito: 17.5](modulo-3/capitulo-17/17.5-conectividade-e-alcance.md).

### Redirecionamento

Mudança do destino ou origem de um fluxo de entrada ou saída. A ordem pode alterar quais mensagens chegam a cada destino. [Conceito: 14.3](modulo-3/capitulo-14/14.3-fluxos-redirecionamentos-e-pipelines.md).

### Refresh

Renovação periódica do estado armazenado em DRAM para manter a informação durante o funcionamento. Não é releitura de um arquivo nem atualização do software. [Conceito: 7.3][c73].

### REG_BINARY

Tipo de valor do Registro utilizado para dados binários. [Conceito: 13.5](modulo-3/capitulo-13/13.5-registro-ambiente-e-configuracao.md).

### REG_DWORD

Tipo de valor do Registro para um inteiro de 32 bits. [Conceito: 13.5](modulo-3/capitulo-13/13.5-registro-ambiente-e-configuracao.md).

### REG_EXPAND_SZ

Tipo de valor do Registro para texto que pode conter referências a variáveis de ambiente para expansão. [Conceito: 13.5](modulo-3/capitulo-13/13.5-registro-ambiente-e-configuracao.md).

### REG_SZ

Tipo de valor do Registro utilizado para texto. [Conceito: 13.5](modulo-3/capitulo-13/13.5-registro-ambiente-e-configuracao.md).

### Registrador

Pequeno espaço de armazenamento interno utilizado pelo processador na execução. Conservar um valor num registrador não implica gravá-lo num arquivo persistente. [Conceito: 7.2][c72].

### Registro do Windows

Windows Registry. Base hierárquica de configuração com chaves, subchaves e valores tipados. Não é o mesmo mecanismo que o log de eventos. [Conceito: 13.5](modulo-3/capitulo-13/13.5-registro-ambiente-e-configuracao.md).

### Regras de engajamento

Condições sobre como conduzir o teste, incluindo métodos, janela de execução, comunicação e interrupção. Complementam a definição de escopo. [Conceito: 3.1][c31].

### Reload

Recarga de configuração. É necessário identificar quem a relê: aplicação e gerenciador não são o mesmo componente. [Conceito: 16.3](modulo-3/capitulo-16/16.3-configuracao-parada-e-reinicio.md).

### Relocação

Ajuste de referências de endereço conforme a disposição atribuída às partes de um programa. Pode participar da preparação de componentes binários; não é simplesmente renomear ou mover um arquivo numa pasta. [Conceito: 8.2][c82].

### Relógio monotônico

Relógio usado para medir intervalos sob um contrato independente de ajustes descontínuos do calendário. Não fornece sozinho um horário universal entre máquinas. [Conceito: 16.5](modulo-3/capitulo-16/16.5-logs-tempo-e-evidencias.md).

### Repositório de pacotes

Fonte que disponibiliza pacotes e seus metadados para distribuição e manutenção. É distinto de um repositório Git de código; confiar numa nova fonte altera a cadeia de fornecimento do ambiente. [Conceito: 12.5][c125].

### Requisição

Mensagem em que um componente solicita uma operação a outro. Em HTTP, seu significado depende de método, destino e demais elementos, a serem aprofundados no módulo de redes. [Introdução: 4.3][c43].

### Resposta

Mensagem devolvida em relação a uma requisição. Código de status e conteúdo precisam ser interpretados juntos, no contexto da operação. [Introdução: 4.3][c43].

### Restart

Parada seguida de nova inicialização da unidade ou aplicação, conforme seu contrato. Não equivale a reiniciar todo o equipamento nem a recuperar o estado de negócio. [Conceito: 16.3](modulo-3/capitulo-16/16.3-configuracao-parada-e-reinicio.md).

### Resultado desconhecido

Situação em que o solicitante não sabe se o efeito foi confirmado. Ausência de resposta de sucesso não demonstra ausência de efeito. [Conceito: 16.6](modulo-3/capitulo-16/16.6-estado-confirmacao-e-retomada.md).

### Retenção

Política de conservação dos registros por tempo, espaço ou outras condições. Um recorte sem eventos não prova ausência de atividade passada. [Conceito: 16.5](modulo-3/capitulo-16/16.5-logs-tempo-e-evidencias.md).

### Reteste

Nova verificação após uma alteração, voltada ao comportamento que deveria ser corrigido e às propriedades que deveriam permanecer. No exemplo de acesso, inclui o uso legítimo e a preservação das recusas necessárias. [Conceito: 11.5][c115].

### Revogação

Retirada de autoridade cujo alcance deve ser definido: novos pedidos, futuras execuções, sessões ou recursos já abertos. Não implica interrupção instantânea universal. [Conceito: 15.6](modulo-3/capitulo-15/15.6-camadas-revogacao-e-menor-privilegio.md).

### RFC

Request for Comments. Documento numerado de uma série de especificações e outros materiais técnicos. Nem toda RFC é um padrão; categoria e contexto importam. [Menção: capítulo 1][c1]; [referências do capítulo 4][c4-ref].

### Risco

Relação entre possibilidade de um evento adverso e consequências no contexto analisado. Não é sinônimo de vulnerabilidade ou nota de severidade. [Conceito: 5.3][c53].

### Risco residual

Risco que permanece depois de controles ou respostas. Uma medida pode melhorar o cenário sem eliminar todas as possibilidades relevantes. [Conceito: 5.3][c53].

### Rollback

Desfazimento das alterações de uma transação ainda não confirmada, conforme o contrato do mecanismo utilizado. [Conceito: 16.6](modulo-3/capitulo-16/16.6-estado-confirmacao-e-retomada.md).

### root

Conta administrativa no contexto Linux do capítulo. Não é sinônimo de diretório raiz nem do caminho /root; suas capacidades efetivas continuam sujeitas aos mecanismos e políticas do ambiente. [Conceito: 12.2][c122].

### Rootless

No modo Docker apresentado, daemon e containers executam sem privilégios de root no contexto externo. É diferente de somente escolher uma conta não root para a aplicação. [Conceito: 17.3](modulo-3/capitulo-17/17.3-containers-namespaces-e-recursos.md).

### Rotação de logs

Administração do crescimento e da separação dos arquivos de registro. Estratégia de reabertura e janelas de perda precisam ser consideradas. [Conceito: 16.5](modulo-3/capitulo-16/16.5-logs-tempo-e-evidencias.md).

### Round-trip

Percurso de ida e volta, como serializar e desserializar um registro. Concordância entre as duas operações num caso não elimina a necessidade de expectativas independentes, fronteiras e entradas inválidas. [Conceito: 10.5][c105].

### RSS

Resident Set Size. Medida de memória residente associada a um processo. Somar RSS de processos pode contar as mesmas páginas compartilhadas mais de uma vez; a interpretação precisa declarar o recorte. [Conceito: 9.4][c94].

### Runtime

Ambiente de execução da linguagem: mecanismos que sustentam o processamento de código e suas operações. Pode incluir interpretação, bibliotecas e gerenciamento de objetos; não precisa ser um único arquivo isolado. [Conceito: 8.4][c84].

### Runtime de container

Componente que prepara e executa o ambiente de container segundo sua configuração. O contexto resultante depende dos recursos, identidades e restrições efetivamente aplicados. [Conceito: 17.3](modulo-3/capitulo-17/17.3-containers-namespaces-e-recursos.md).

## S

### SACL

System Access Control List. Parte de um descritor de segurança Windows usada para informações como auditoria e rótulos obrigatórios; não é uma segunda DACL somada à primeira. [Conceito: 15.4](modulo-3/capitulo-15/15.4-tokens-e-acls-no-windows.md).

### Safe harbor

Compromisso de uma organização sobre pesquisa de boa-fé, sob condições declaradas. Não amplia automaticamente o escopo nem equivale a imunidade universal perante terceiros. [Conceito: 3.1][c31].

### Saída padrão

Fluxo convencional de resultado de um programa; no modelo Unix corresponde ao descritor 1. Não precisa ter uma tela como destino. [Conceito: 14.3](modulo-3/capitulo-14/14.3-fluxos-redirecionamentos-e-pipelines.md).

### Sandbox

Ambiente projetado para restringir recursos e operações disponíveis à execução. O termo não identifica uma implementação única nem implica desconexão da rede. [Conceito: 17.5](modulo-3/capitulo-17/17.5-conectividade-e-alcance.md).

### SATA

Serial ATA. Interface de armazenamento que não deve ser confundida com um formato físico, como M.2. O equipamento precisa oferecer suporte à interface pertinente. [Conceito: 7.4][c74].

### Scanner

Ferramenta que automatiza observações ou testes. Descoberta de serviços e detecção de vulnerabilidades são tarefas distintas; alerta não substitui investigação. [Menção: capítulo 1][c1]; [conceito: 4.3][c43].

### SCM

Service Control Manager. Gerenciador de controle de serviços do Windows; participa da base de serviços, inicialização, controle e acompanhamento de estado. [Conceito: 13.6](modulo-3/capitulo-13/13.6-inicializacao-servicos-e-investigacao.md).

### Script

Arquivo com instruções para um interpretador. A extensão não prova qual linguagem será usada nem torna confiável o conteúdo. [Conceito: 14.5](modulo-3/capitulo-14/14.5-scripts-contexto-e-repetibilidade.md).

### Seção de ELF

Unidade de organização de material no formato ELF, utilizada, por exemplo, na ligação e na análise. Não é sinônimo de segmento de carregamento; as duas visões possuem responsabilidades diferentes. [Conceito: 8.3][c83].

### Seccomp

Mecanismo Linux de restrição de chamadas de sistema. Seus filtros são uma camada de proteção, não uma sandbox completa ou uma política integral de arquivos e recursos. [Conceito: 17.4](modulo-3/capitulo-17/17.4-compartilhamentos-e-autoridade.md).

### Secure Boot

Mecanismo de verificação de componentes no caminho de inicialização conforme uma política de confiança. Não comprova que todos os programas do computador estejam livres de defeitos. [Conceito: 7.5][c75].

### security.txt

Arquivo padronizado pela RFC 9116 para indicar contatos e informações de divulgação de vulnerabilidades. Sua presença não concede, sozinha, autorização para testar. [Conceito: 3.1][c31].

### Segmentation fault

Falha associada a um acesso de memória que não pôde ser atendido validamente; no percurso Linux, SIGSEGV pode comunicar violações de proteção. O rótulo não identifica sozinho a causa nem prova defeito físico ou exploração bem-sucedida. [Conceito: 9.4][c94].

### Segmento de ELF

Descrição de uma região relevante ao carregamento da imagem. Pode reunir mais de uma seção e apresentar tamanho em memória diferente do material armazenado no arquivo. [Conceito: 8.3][c83].

### SEI

Software Engineering Institute, da Carnegie Mellon University. Instituição associada à criação do CERT/CC no episódio histórico discutido. [Contexto: capítulo 2][c2].

### SELinux

Mecanismo Linux de controle obrigatório baseado em rótulos e política. Conceder acesso discricionário não desativa suas decisões. [Conceito: 15.6](modulo-3/capitulo-15/15.6-camadas-revogacao-e-menor-privilegio.md).

### Separação em palavras

Word splitting. Divisão de resultados de certas expansões sem aspas em Bash, conforme IFS e o contexto sintático. [Conceito: 14.2](modulo-3/capitulo-14/14.2-argumentos-aspas-e-expansoes.md).

### Serialização

Transformação de uma estrutura de dados numa representação armazenável ou transportável, segundo um formato. Não equivale necessariamente a copiar a disposição de memória do processo nem a preservar suas referências internas. [Conceito: 10.4][c104].

### Service Control Manager

Componente Windows que inicia e controla serviços e mantém sua base de configuração. É um exemplo de gerenciador, não o mesmo programa que systemd. [Conceito: 11.5][c115].

### Serviço

Capacidade oferecida por um componente em execução, frequentemente administrado sem interação constante. Pode envolver vários processos; existir um processo não demonstra que a capacidade oferecida está funcionando. [Conceito: 11.5][c115].

### Serviço do Windows

Unidade integrada ao gerenciamento do SCM, executada em processo próprio ou compartilhado. Um processo em segundo plano não é automaticamente um serviço. [Conceito: 13.6](modulo-3/capitulo-13/13.6-inicializacao-servicos-e-investigacao.md).

### Servidor

Programa que atende solicitações; a palavra também pode designar o computador que o executa. Distinguir programa, serviço e equipamento evita conclusões imprecisas. [Conceito: 5.1][c51].

### Sessão

Contexto usado por uma aplicação para associar interações, frequentemente a uma identidade autenticada. Duas abas visíveis não comprovam isolamento entre sessões. [Conceito: 4.2][c42].

### Sessão 0

Sessão em que executam serviços, separada das sessões interativas nos Windows modernos. Não deve ser confundida com toda e qualquer sessão de logon. [Conceito: 13.6](modulo-3/capitulo-13/13.6-inicializacao-servicos-e-investigacao.md).

### Sessão de logon

Contexto relacionado à autenticação. No capítulo, sua importância aparece na visibilidade dos mapeamentos de unidades de rede. [Conceito: 13.6](modulo-3/capitulo-13/13.6-inicializacao-servicos-e-investigacao.md).

### set -e

Opção errexit do Bash, com exceções por contexto. Não deve ser interpretada como garantia de que toda falha interromperá qualquer roteiro. [Conceito: 14.4](modulo-3/capitulo-14/14.4-status-condicoes-e-controle.md).

### setfacl

Utilitário de alteração de ACLs POSIX. O cálculo da máscara faz parte do efeito a conferir após a mudança. [Conceito: 15.3](modulo-3/capitulo-15/15.3-criacao-propriedade-e-acls.md).

### Setgid

Bit especial cujo significado depende do objeto: em diretório participa da herança de grupo; em executável pode participar de uma transição do grupo efetivo. Não concede sozinho todos os acessos ao grupo. [Conceito: 15.3](modulo-3/capitulo-15/15.3-criacao-propriedade-e-acls.md).

### Setuid

Bit especial em executáveis que pode participar de uma transição do usuário efetivo, conforme regras e restrições de execução. Não altera o cadastro da pessoa que iniciou o programa. [Conceito: 15.5](modulo-3/capitulo-15/15.5-privilegios-e-delegacao.md).

### Severidade

Descrição da gravidade de uma vulnerabilidade segundo critérios determinados. Não equivale sozinha ao risco para uma organização específica. [Conceito: 5.3][c53].

### SHA-256

Algoritmo de hash criptográfico utilizado para comparar os bytes de dois documentos no exemplo. Um resumo igual a uma referência não prova, sozinho, origem autorizada ou segurança do arquivo; a referência precisa ser confiável. [Introdução: 10.6][c106].

### Shebang

Linha inicial com #! usada em sistemas compatíveis para indicar o interpretador ao executar diretamente um script. [Conceito: 14.5](modulo-3/capitulo-14/14.5-scripts-contexto-e-repetibilidade.md).

### Shell

Interpretador de comandos que também oferece recursos de linguagem para combinar operações; não é sinônimo de terminal. [Conceito: 14.1](modulo-3/capitulo-14/14.1-terminal-shell-e-comandos.md).

### SID

Security Identifier. Identificador usado pelo Windows para entidades de segurança, como usuários e grupos. Não é uma senha ou o simples nome exibido de uma conta. [Conceito: 13.4](modulo-3/capitulo-13/13.4-contas-tokens-e-controle-de-acesso.md).

### SIGKILL

Sinal Linux que não pode ser capturado, bloqueado ou ignorado. Não oferece à aplicação uma rotina de encerramento para confirmar seu trabalho. [Conceito: 16.1](modulo-3/capitulo-16/16.1-ciclo-de-vida-e-processos.md).

### SIGTERM

Sinal cujo comportamento padrão é terminar; uma aplicação pode tratá-lo para organizar sua saída. Não garante salvar o trabalho automaticamente. [Conceito: 16.1](modulo-3/capitulo-16/16.1-ciclo-de-vida-e-processos.md).

### Símbolo

No contexto de ligação, associa um nome a um elemento do programa, como uma função. Resolver uma referência envolve relacionar seu uso à definição correspondente. Não é o mesmo sentido de símbolo visual de texto. [Conceito: 8.2][c82].

### Sinal

Mecanismo de notificação a processos ou threads no percurso Linux. A reação depende do sinal, da disposição e do contexto. [Conceito: 16.1](modulo-3/capitulo-16/16.1-ciclo-de-vida-e-processos.md).

### Sinalização em banda

Sinais de controle transmitidos pelo mesmo canal do conteúdo de uso, como voz no exemplo telefônico. Supervisão e endereçamento são funções distintas. [Conceito histórico: capítulo 2][c2].

### Sistema operacional

Software que administra recursos e oferece serviços aos programas. Sua participação entre aplicações e dispositivos é introduzida antes do desenvolvimento detalhado nos capítulos próprios. [Introdução: 7.1][c71].

### Snapshot

Ponto de estado restaurável segundo o contrato da plataforma. Seu alcance não inclui automaticamente dados compartilhados, armazenamento remoto ou todos os dispositivos. [Conceito: 17.6](modulo-3/capitulo-17/17.6-imagens-snapshots-e-recuperacao.md).

### Sobreposição de execuções

Condição em que uma nova instância é iniciada enquanto outra ainda trabalha. Sua prevenção não elimina automaticamente repetições sequenciais do mesmo efeito. [Conceito: 16.4](modulo-3/capitulo-16/16.4-agendamento-e-sobreposicao.md).

### Socket do Docker

Uma forma de alcançar a API de administração do daemon. Conceder seu acesso entrega autoridade sobre os recursos que o daemon pode administrar; não é apenas compartilhar um arquivo de entrada. [Conceito: 17.4](modulo-3/capitulo-17/17.4-compartilhamentos-e-autoridade.md).

### Software

Programas e instruções que orientam o funcionamento do sistema. A distinção em relação ao hardware não significa que suas representações existam sem suporte físico. [Conceito: 7.1][c71].

### Soma de verificação

Checksum. Valor calculado sobre conteúdo para detectar determinadas alterações. Seu alcance depende do algoritmo e da referência; CRC não autentica quem produziu os dados. [Conceito: 10.6][c106].

### Source

Incorporação de comandos de um arquivo ao contexto atual do Bash, pelo comando source ou ponto; difere de iniciar outro processo. [Conceito: 14.5](modulo-3/capitulo-14/14.5-scripts-contexto-e-repetibilidade.md).

### Splatting

Recurso do PowerShell que distribui valores de uma coleção para uma chamada. Não é o mesmo que fornecer uma coleção como valor de um único parâmetro. [Conceito: 14.6](modulo-3/capitulo-14/14.6-automacao-e-fronteiras-de-confianca.md).

### SQL

Linguagem de definição, consulta e manipulação de dados em sistemas de banco de dados que a implementam. Aparece na introdução à SQL injection e terá desenvolvimento próprio adiante. [Menção: capítulo 1][c1].

### SQL injection

Falha em que uma entrada influencia indevidamente a estrutura ou significado de uma consulta SQL. Não é qualquer erro de banco de dados. [Menção: capítulo 1][c1]. [Referência técnica][sqli-doc].

### SQLite

Mecanismo de banco de dados utilizado no exemplo local para relacionar efeito, identificação e confirmação transacional. Não torna ações externas parte dessa transação. [Conceito: 16.6](modulo-3/capitulo-16/16.6-estado-confirmacao-e-retomada.md).

### SRAM

Static Random Access Memory, memória estática. Tecnologia de memória convencional que conserva seu estado enquanto alimentada sem o mesmo processo periódico de refresh da DRAM. “Estática” não significa não volátil. [Conceito: 7.3][c73].

### SSD

Solid-State Drive, unidade de armazenamento de estado sólido. Nos dispositivos NAND descritos, o controlador administra páginas, blocos e movimentação interna de dados; não há o mesmo movimento de cabeças e pratos de um HDD. [Conceito: 7.4][c74].

### stderr

Nome convencional do fluxo de erro padrão, frequentemente usado para diagnósticos. Escrever nele não determina sozinho o código de saída. [Conceito: 14.3](modulo-3/capitulo-14/14.3-fluxos-redirecionamentos-e-pipelines.md).

### stdin

Nome convencional do fluxo de entrada padrão, que pode vir de arquivo, pipe ou terminal. [Conceito: 14.3](modulo-3/capitulo-14/14.3-fluxos-redirecionamentos-e-pipelines.md).

### stdin, stdout e stderr

Entrada padrão, saída padrão e saída de erros padrão. São fluxos que podem ser ligados ao terminal, a arquivos ou a outros canais; não são obrigatoriamente teclado e tela. No contexto Unix descrito, relacionam-se aos descritores convencionais 0, 1 e 2. [Conceito: 8.5][c85].

### stdout

Nome convencional do fluxo de saída padrão, que pode ser redirecionado para outro destino. [Conceito: 14.3](modulo-3/capitulo-14/14.3-fluxos-redirecionamentos-e-pipelines.md).

### Sticky bit

Bit especial que restringe remoção e renomeação em diretórios segundo proprietário e privilégio aplicável. Não impede, sozinho, ler ou alterar conteúdo permitido pelo arquivo. [Conceito: 15.2](modulo-3/capitulo-15/15.2-permissoes-linux-e-caminhos.md).

### Substituição de comando

Expansão Bash que usa a saída de um comando no lugar da expressão $(...), retirando quebras de linha finais no caso apresentado. [Conceito: 14.2](modulo-3/capitulo-14/14.2-argumentos-aspas-e-expansoes.md).

### sudo

Execução de comando como outra identidade conforme uma política. O destino não precisa ser root; autenticação, autorização e ambiente precisam ser considerados. [Conceito: 15.5](modulo-3/capitulo-15/15.5-privilegios-e-delegacao.md).

### sudoers

Plugin e formato de política normalmente usados pelo sudo para decidir quem pode executar quais comandos e em qual contexto. Regras por nome de programa não dispensam compreender suas capacidades. [Conceito: 15.5](modulo-3/capitulo-15/15.5-privilegios-e-delegacao.md).

### Superfície de ataque

Pontos e caminhos pelos quais um sistema pode ser alcançado ou influenciado, incluindo interfaces, dados e contextos de acesso. É um mapa do que examinar, não lista de falhas confirmadas. [Conceito: 5.3][c53].

### Supervisor

Componente que acompanha uma atividade segundo regras de início, acompanhamento e encerramento. A existência do processo não demonstra o resultado de negócio. [Conceito: 16.2](modulo-3/capitulo-16/16.2-servicos-e-supervisao.md).

### Swap

Armazenamento de apoio que pode conservar conteúdo retirado da RAM conforme a gestão de memória. Não é o significado inteiro de memória virtual, e nem toda página ausente da RAM está em swap. [Conceito: 9.4][c94].

### Sysfs

Sistema de arquivos normalmente montado em /sys que organiza objetos do kernel e atributos. Algumas escritas acionam operações de controle, não apenas alteram um documento persistente. [Conceito: 12.3][c123].

### System32 e SysWOW64

Diretórios cuja interpretação exige considerar arquitetura e redirecionamento. No recorte Windows x64, System32 contém componentes nativos de 64 bits e SysWOW64 está associado aos de 32 bits. [Conceito: 13.3](modulo-3/capitulo-13/13.3-executaveis-bibliotecas-e-carregamento.md).

### systemd

Conjunto de componentes que inclui um gerenciador de sistema e serviços. No papel de gerenciador de sistema descrito, executa como PID 1 e coordena unidades. Não é o kernel nem um componente obrigatório de toda distribuição. [Conceito: 11.5][c115].

## T

### Tabela de páginas

Estrutura que descreve mapeamentos e condições de acesso entre páginas virtuais e destinos. Pode ser organizada em níveis; não é uma lista de todos os objetos criados pelo programa. [Conceito: 9.2][c92].

### Tag

No contexto de imagens de container, nome que pode ser reassociado a outro conteúdo. Usar a mesma tag em dois momentos não comprova identidade dos artefatos. [Conceito: 17.6](modulo-3/capitulo-17/17.6-imagens-snapshots-e-recuperacao.md).

### TCG

Tiny Code Generator. Mecanismo de tradução do QEMU usado para emular CPUs. A política consultada não lhe atribui a mesma garantia de isolamento dos casos suportados de virtualização. [Conceito: 17.2](modulo-3/capitulo-17/17.2-maquinas-virtuais-e-hipervisores.md).

### Tempo de vida

Período em que um objeto existe validamente segundo o contrato da linguagem e da alocação. A permanência de bytes no antigo local não prolonga automaticamente esse período. [Conceito: 9.3][c93].

### Terminal

Interface de entrada e saída de texto para interagir com programas, inclusive interpretadores de comandos. Não é o mesmo componente que interpreta a linguagem de comandos. [Menção: capítulo 1][c1].

No contexto do capítulo 14: Interface de interação com aplicações de texto. Pode hospedar um shell, mas não define por si a linguagem desse shell. [Conceito: 14.1](modulo-3/capitulo-14/14.1-terminal-shell-e-comandos.md).

### Thread

No contexto de software, fluxo de execução que pode ser organizado junto de outros fluxos. Não é necessariamente um núcleo físico nem uma janela de aplicativo. [Conceito: 7.2][c72]; [compartilhamento e estado próprio: 9.1][c91].

No contexto do capítulo 13: Unidade de execução que recebe tempo de processador no contexto de um processo. Várias threads podem compartilhar recursos desse processo. [Conceito: 13.1](modulo-3/capitulo-13/13.1-arquitetura-processos-e-objetos.md).

### Timer

No systemd, unidade de temporização que pode ativar outra unidade por calendário ou referência monotônica. Não conserva por si só o progresso do negócio. [Conceito: 16.4](modulo-3/capitulo-16/16.4-agendamento-e-sobreposicao.md).

### Tipo de mídia

Identificação de uma representação, como application/json, também chamada de tipo MIME. Comunica a interpretação pretendida; não garante que o conteúdo corresponda a ela ou seja seguro para todo uso. [Conceito: 10.2][c102].

### TLB

Translation Lookaside Buffer. Cache de traduções de endereços, distinta da cache de dados. Um TLB miss pode exigir obter uma tradução por outro caminho, sem demonstrar que houve page fault ou E/S. [Conceito: 9.2][c92].

### Tmpfs

Sistema de arquivos que utiliza memória virtual e pode usar swap conforme a configuração. Não garante conservação após desmontagem ou reinicialização; o nome /tmp não prova que um diretório use tmpfs. [Conceito: 12.3][c123].

### TMRC

Tech Model Railroad Club, clube de ferromodelismo do MIT presente nos episódios de experimentação. Sua história não estabelece origem única da segurança de computadores. [Contexto: capítulos 1][c1] e [2][c2].

### TOCTOU

Time Of Check To Time Of Use. Diferença entre o estado verificado e o estado usado depois, capaz de invalidar uma conclusão de autorização baseada só numa checagem anterior. [Conceito: 15.6](modulo-3/capitulo-15/15.6-camadas-revogacao-e-menor-privilegio.md).

### Token de acesso (Windows)

Objeto que descreve contexto de segurança de um processo ou thread, incluindo identidade, grupos e privilégios. Não é sinônimo de token de sessão Web nem da senha digitada por uma pessoa. [Conceito: 11.4][c114].

### Token de acesso do Windows

Objeto que descreve um contexto de segurança, incluindo identidades, grupos e privilégios. Não equivale a um token Web nem a um handle de arquivo. [Conceito: 13.4](modulo-3/capitulo-13/13.4-contas-tokens-e-controle-de-acesso.md).

### Topologia

Organização das conexões entre ambientes, redes e interfaces. Uma única etiqueta de modo de rede não descreve caminhos acrescentados por outras interfaces ou encaminhamentos. [Conceito: 17.5](modulo-3/capitulo-17/17.5-conectividade-e-alcance.md).

### Transação

Conjunto de operações submetidas a um contrato de confirmação. O exemplo mantém efeito e identificação do lote no mesmo banco e na mesma transação. [Conceito: 16.6](modulo-3/capitulo-16/16.6-estado-confirmacao-e-retomada.md).

### TRIM

Mecanismo pelo qual o sistema informa ao dispositivo de armazenamento que determinados dados lógicos não precisam mais ser preservados. Participa da gestão do SSD, mas não comprova sanitização completa do equipamento. [Conceito: 7.4][c74].

### Troca de contexto

Conservação e preparação do estado necessário para alternar a execução entre fluxos. Não exige copiar toda a RAM para disco e não é sinônimo de toda passagem do modo usuário para o kernel. [Conceito: 9.1][c91].

### Truncamento

Corte de uma sequência ou representação para um tamanho menor. Em texto de largura variável, cortar em um byte arbitrário pode interromper uma sequência de caractere; o formato precisa ser respeitado. [Conceito: 6.4][c64].

No contexto do capítulo 14: Redução do conteúdo de um arquivo, como ocorre em uma abertura para substituir sua saída. A ação pode ocorrer antes de o comando falhar. [Conceito: 14.3](modulo-3/capitulo-14/14.3-fluxos-redirecionamentos-e-pipelines.md).

## U

### UAC

User Account Control. Mecanismo relacionado à elevação administrativa de aplicações. Seu comportamento depende da conta, do modelo de aprovação e da política. [Conceito: 13.4](modulo-3/capitulo-13/13.4-contas-tokens-e-controle-de-acesso.md).

### udev

Componente de gerenciamento dinâmico de dispositivos que recebe eventos do kernel e aplica regras em espaço de usuário. Não é o driver nem uma garantia universal de automontagem. [Conceito: 12.4][c124].

### UEFI

Unified Extensible Firmware Interface. Interface de firmware usada no caminho de inicialização de plataformas compatíveis. O firmware prepara o ambiente e participa da passagem ao carregador; não é o próprio sistema operacional. [Introdução: 7.5][c75].

### UID

User identifier, identificador de usuário. Nas interfaces Unix/Linux há variantes com papéis distintos, como identidade real, efetiva e de sistema de arquivos; o nome mostrado numa tela não descreve todo o contexto. [Conceito: 11.4][c114].

Identificador numérico de usuário. Na investigação Linux, distinguir os IDs real, efetivo e de sistema de arquivos e não inferir identidade apenas pelo nome mostrado. [Conceito: 15.1](modulo-3/capitulo-15/15.1-identidades-contas-e-contextos.md).

### UID efetivo

Identificador de usuário que participa das decisões de autoridade da execução. Pode diferir do real; no acesso a arquivos Linux, o FSUID, normalmente igual ao efetivo, tem papel específico. [Conceito: 15.1](modulo-3/capitulo-15/15.1-identidades-contas-e-contextos.md).

### UID real

Identificador real de usuário associado ao processo; cumpre funções diferentes do UID efetivo e não deve ser confundido com uma variável de ambiente. [Conceito: 15.1](modulo-3/capitulo-15/15.1-identidades-contas-e-contextos.md).

### umask

Máscara de criação do processo. Sem ACL padrão, remove bits do modo solicitado; não é subtração aritmética nem altera retroativamente arquivos existentes. [Conceito: 15.3](modulo-3/capitulo-15/15.3-criacao-propriedade-e-acls.md).

### uname

Utilitário que apresenta informações do sistema; a opção -r identifica a release do kernel em execução. Não lista todas as imagens de kernel instaladas para uma próxima inicialização. [Conceito: 12.1][c121].

### UNC

Universal Naming Convention. Forma de nomear recursos de rede, como `\\servidor-lab\acervo\arquivo`. Um nome explícito não concede autorização de acesso. [Conceito: 13.2](modulo-3/capitulo-13/13.2-volumes-caminhos-e-perfis.md).

### Unicode

Padrão para representar caracteres, com pontos de código e formas de codificação. Identificar um ponto de código e escolher seus bytes são etapas distintas; Unicode não significa que toda letra ocupa um ou dois bytes. [Conceito: 6.4][c64].

### Unidade systemd

Recurso administrado pelo systemd, como serviço, timer ou montagem, com identidade e configuração próprias. Uma unidade não é um PID. [Conceito: 16.2](modulo-3/capitulo-16/16.2-servicos-e-supervisao.md).

### Upstream

Projeto de origem em relação a quem integra ou distribui seu software. Sua versão e a revisão mantida por uma distribuição precisam ser distinguidas ao examinar correções. [Conceito: 12.5][c125].

### URI

Uniform Resource Identifier, identificador uniforme de recurso. A introdução examina somente as regras de codificação percentual e seus componentes; não desenvolve ainda toda a sintaxe de identificação de recursos na Web. [Introdução: 10.3][c103].

### Use-after-free

Uso de uma referência a memória depois de sua liberação, contrariando o tempo de vida do objeto. O espaço pode ter sido reutilizado; observar bytes familiares não torna o acesso válido. [Conceito: 9.3][c93].

### User namespace

Contexto Linux de mapeamento de identificadores de usuário e grupo e de autoridade de capabilities. UID zero dentro de um contexto não descreve sozinho a autoridade fora dele. [Conceito: 17.3](modulo-3/capitulo-17/17.3-containers-namespaces-e-recursos.md).

### useradd

Utilitário shadow-utils para criação de contas locais, sujeito a opções e padrões da instalação. Criar um cadastro não equivale a conceder todos os recursos necessários a uma aplicação. [Conceito: 15.1](modulo-3/capitulo-15/15.1-identidades-contas-e-contextos.md).

### usermod

Utilitário shadow-utils para alterar contas. Modificar associações de grupos exige distinguir acréscimo de substituição; não atualiza automaticamente todas as execuções antigas. [Conceito: 15.1](modulo-3/capitulo-15/15.1-identidades-contas-e-contextos.md).

### UTF-8

Forma de codificação Unicode que utiliza de um a quatro bytes por valor escalar e preserva a representação ASCII. Uma unidade percebida pelo usuário pode reunir vários valores; nem toda sequência arbitrária de bytes é UTF-8 válido. [Conceito: 6.4][c64].

## V

### Validação semântica

Conferência do significado dos valores segundo as regras do domínio. Uma quantidade pode ser representável no formato e ainda exceder o limite permitido pela aplicação. [Conceito: 10.5][c105].

### Validação sintática

Conferência da estrutura e da forma de uma entrada segundo a gramática ou contrato pertinente. Não substitui a análise dos valores de domínio nem a autorização para executar a operação. [Conceito: 10.5][c105].

### Valor do Registro

Entrada com nome, tipo e dados associada a uma chave do Registro. Sua interpretação depende do tipo e do aplicativo consumidor. [Conceito: 13.5](modulo-3/capitulo-13/13.5-registro-ambiente-e-configuracao.md).

### Variável de ambiente

Par de nome e valor fornecido no contexto de um processo. Pode influenciar configuração e localização de recursos, mas não corresponde automaticamente a uma variável local do fonte ou a um estado global idêntico em todos os processos. [Conceito: 8.5][c85].

No contexto do capítulo 13: Associação entre nome e valor disponibilizada no ambiente de um processo. Modificar outro contexto não atualiza automaticamente todos os processos existentes. [Conceito: 13.5](modulo-3/capitulo-13/13.5-registro-ambiente-e-configuracao.md).

No contexto do capítulo 14: Par nome/valor transmitido no contexto de processos. Não equivale automaticamente a toda variável interna do shell. [Conceito: 14.5](modulo-3/capitulo-14/14.5-scripts-contexto-e-repetibilidade.md).

### Vazamento de memória

Memory leak. Retenção indevida de recursos de memória que já não são necessários ao trabalho. Não é sinônimo de divulgação de informações, e crescimento de RSS sozinho não comprova esse defeito. [Conceito: 9.3][c93]; [medidas: 9.4][c94].

### Vazão

Throughput. Quantidade de trabalho concluído por unidade de tempo. Não é o espaço total disponível nem a duração de uma operação individual. [Conceito: 7.1][c71].

### vCPU

Processador virtual apresentado ao convidado. Sua existência não demonstra uma reserva exclusiva de um núcleo físico. [Conceito: 17.2](modulo-3/capitulo-17/17.2-maquinas-virtuais-e-hipervisores.md).

### VDP

Vulnerability Disclosure Policy, política de divulgação de vulnerabilidades. Define canais e condições para comunicar falhas e pode delimitar pesquisa autorizada. Não significa automaticamente pagamento de recompensas. [Conceito: 3.1][c31].

### Verificação de saúde

Observação deliberada de uma capacidade definida de um serviço. Conferir apenas a existência do processo não demonstra que uma importação ou outra função esteja funcionando. [Conceito: 11.5][c115].

### VFS

Virtual File System. Camada do kernel Linux que fornece uma interface de sistemas de arquivos e permite coexistência de implementações. A abstração não garante que todo pedido seja permitido ou atendido pelo mesmo caminho físico. [Conceito: 11.1][c111].

### VirtIO

Interfaces de dispositivos projetadas para operação cooperativa com a virtualização. Introdução ao caminho de entrada e saída; nenhum driver foi implementado. [Conceito: 17.2](modulo-3/capitulo-17/17.2-maquinas-virtuais-e-hipervisores.md).

### Virtualização

Apresentação de recursos por uma camada que administra sua relação com a implementação subjacente. Não comprova, por si só, exclusividade ou restrição de todos os acessos. [Conceito: 17.1](modulo-3/capitulo-17/17.1-virtualizacao-e-fronteiras.md).

### Visualizador de Eventos

Event Viewer. Interface de consulta de logs de eventos; a visualização não substitui interpretar origem, contexto e conteúdo do registro. [Conceito: 13.6](modulo-3/capitulo-13/13.6-inicializacao-servicos-e-investigacao.md).

### VM

Virtual Machine, máquina virtual. Neste capítulo, designa o ambiente de computador apresentado a um sistema operacional convidado. [Conceito: 17.2](modulo-3/capitulo-17/17.2-maquinas-virtuais-e-hipervisores.md).

### VMBus

Canal usado na arquitetura Hyper-V para comunicação entre componentes de virtualização das partições. Menção introdutória, sem configuração ou inspeção executada. [Conceito: 17.2](modulo-3/capitulo-17/17.2-maquinas-virtuais-e-hipervisores.md).

### Volume

Unidade lógica de armazenamento à qual podem ser associados nomes de acesso. Não é sinônimo de uma letra de unidade nem necessariamente de um único disco físico. [Conceito: 13.2](modulo-3/capitulo-13/13.2-volumes-caminhos-e-perfis.md).

### Volumes de container

Recursos de armazenamento cujo ciclo de vida é separado da instância de container. Recriar a instância ligada ao mesmo volume não significa começar sem dados anteriores. [Conceito: 17.6](modulo-3/capitulo-17/17.6-imagens-snapshots-e-recuperacao.md).

### Vulnerabilidade

Fraqueza em código, configuração, controle, procedimento ou implementação que pode ser explorada ou acionada para produzir consequência adversa. Pode existir sem exploit público. [Conceito: 5.1][c51].

## W

### Watchdog

Mecanismo de acompanhamento de notificações periódicas segundo um contrato. Sua evidência depende do que a aplicação verifica antes de notificar. [Conceito: 16.2](modulo-3/capitulo-16/16.2-servicos-e-supervisao.md).

### White hat

Rótulo informal associado a pesquisa ou avaliação autorizada e voltada à proteção. Não comprova por si só a autorização de uma atividade específica. [Contexto: capítulo 1][c1].

### whoami

Utilitário Windows de consulta do contexto corrente, com opções para identidade, grupos e privilégios. Consultar a sessão do técnico não descreve automaticamente outro serviço. [Conceito: 15.7](modulo-3/capitulo-15/15.7-investigacao-e-verificacao.md).

### Windows Event Log

Infraestrutura de publicação e consulta de eventos do Windows. Não registra automaticamente toda ação de qualquer aplicação. [Conceito: 13.6](modulo-3/capitulo-13/13.6-inicializacao-servicos-e-investigacao.md).

### Windows Sandbox

Ambiente descartável do Windows baseado em hipervisor e kernel separado. Rede e integrações possuem configurações próprias; o fragmento do capítulo é documental, não uma avaliação completa executada. [Conceito: 17.5](modulo-3/capitulo-17/17.5-conectividade-e-alcance.md).

### Windows Terminal

Aplicativo hospedeiro de experiências de linha de comando, capaz de apresentar shells diferentes. Não é o interpretador cmd.exe ou PowerShell. [Conceito: 14.1](modulo-3/capitulo-14/14.1-terminal-shell-e-comandos.md).

### Worm

Programa capaz de se executar independentemente e propagar cópias funcionais para outras máquinas. No caso Morris Worm, o primeiro termo identifica o autor e o segundo o tipo de programa. [Conceito: capítulo 2][c2].

### WOW64

Windows 32-bit on Windows 64-bit. Subsistema de compatibilidade para aplicações de 32 bits em Windows de 64 bits, com mecanismos específicos de redirecionamento. [Conceito: 13.3](modulo-3/capitulo-13/13.3-executaveis-bibliotecas-e-carregamento.md).

### WRITE_DAC

Direito Windows de modificar a DACL de um objeto. Administrar a política pode ter consequências diferentes de modificar os dados do objeto. [Conceito: 15.4](modulo-3/capitulo-15/15.4-tokens-e-acls-no-windows.md).

### WRITE_OWNER

Direito Windows relacionado à mudança de proprietário de um objeto. Não é um sinônimo de escrita no conteúdo do arquivo. [Conceito: 15.4](modulo-3/capitulo-15/15.4-tokens-e-acls-no-windows.md).

## X

### XML

Extensible Markup Language. Linguagem de representação estruturada com elementos e atributos. Boa formação do documento e conformidade com regras adicionais de validação são perguntas diferentes. [Introdução: 10.4][c104].

### XSS

Cross-Site Scripting. Classe de falha em que conteúdo controlado por um atacante pode executar código no navegador no contexto de uma aplicação Web. É distinta de SQL injection. [Menção: capítulo 2][c2]. [Referência técnica][xss-doc].

## Y

### YAML

YAML Ain’t Markup Language. Formato textual com mapeamentos, sequências e valores. A resolução de tipos depende da versão e do esquema; o capítulo utiliza a especificação 1.2.2 como referência introdutória, sem executar um parser YAML. [Introdução: 10.4][c104].

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
[c71]: modulo-2/capitulo-7/7.1-componentes-e-caminhos.md
[c72]: modulo-2/capitulo-7/7.2-cpu-e-execucao.md
[c73]: modulo-2/capitulo-7/7.3-memoria-e-cache.md
[c74]: modulo-2/capitulo-7/7.4-armazenamento-e-persistencia.md
[c75]: modulo-2/capitulo-7/7.5-dispositivos-e-firmware.md
[c81]: modulo-2/capitulo-8/8.1-codigo-e-construcao.md
[c82]: modulo-2/capitulo-8/8.2-compilacao-e-ligacao.md
[c83]: modulo-2/capitulo-8/8.3-carregamento-e-processos.md
[c84]: modulo-2/capitulo-8/8.4-interpretadores-e-runtimes.md
[c85]: modulo-2/capitulo-8/8.5-contexto-e-diagnostico.md
[c91]: modulo-2/capitulo-9/9.1-processos-threads-e-contextos.md
[c92]: modulo-2/capitulo-9/9.2-enderecos-paginas-e-traducao.md
[c93]: modulo-2/capitulo-9/9.3-regioes-objetos-e-tempo-de-vida.md
[c94]: modulo-2/capitulo-9/9.4-paginacao-copias-e-medidas.md
[c95]: modulo-2/capitulo-9/9.5-protecao-concorrencia-e-diagnostico.md
[c101]: modulo-2/capitulo-10/10.1-arquivos-nomes-e-leitura.md
[c102]: modulo-2/capitulo-10/10.2-formatos-e-estrutura.md
[c103]: modulo-2/capitulo-10/10.3-codificacoes-e-transformacoes.md
[c104]: modulo-2/capitulo-10/10.4-serializacao-e-contratos.md
[c105]: modulo-2/capitulo-10/10.5-parsing-e-validacao.md
[c106]: modulo-2/capitulo-10/10.6-integridade-e-fronteiras.md
[c2-ref]: modulo-1/capitulo-2/referencias.md
[c3-sol]: modulo-1/capitulo-3/solucoes.md
[c4-ref]: modulo-1/capitulo-4/referencias.md
[c5-ref]: modulo-1/capitulo-5/referencias.md
[c8-ref]: modulo-2/capitulo-8/referencias.md
[c9-ref]: modulo-2/capitulo-9/referencias.md
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

[c111]: modulo-3/capitulo-11/11.1-abstracoes-e-responsabilidades.md
[c112]: modulo-3/capitulo-11/11.2-interfaces-e-chamadas-de-sistema.md
[c113]: modulo-3/capitulo-11/11.3-recursos-espera-e-coordenacao.md
[c114]: modulo-3/capitulo-11/11.4-identidades-e-limites.md
[c115]: modulo-3/capitulo-11/11.5-inicializacao-servicos-e-investigacao.md

[c121]: modulo-3/capitulo-12/12.1-kernel-distribuicao-e-contexto.md
[c122]: modulo-3/capitulo-12/12.2-diretorios-e-montagens.md
[c123]: modulo-3/capitulo-12/12.3-proc-sys-e-dev.md
[c124]: modulo-3/capitulo-12/12.4-drivers-modulos-e-servicos.md
[c125]: modulo-3/capitulo-12/12.5-pacotes-atualizacoes-e-investigacao.md
