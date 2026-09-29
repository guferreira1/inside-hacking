# Capítulo 13 — Respostas comentadas

[← Perguntas](13.6-inicializacao-servicos-e-investigacao.md#para-conferir-a-compreensao) · [Abertura](README.md)

As respostas não exigem repetir as frases do capítulo. O importante é preservar as distinções e justificar a conclusão. As situações da Aurora continuam sendo modelos fictícios.

## 1. Elevação e modo kernel

A elevação modifica o contexto de segurança com que uma aplicação realiza operações. Modo usuário e modo kernel distinguem condições de execução e acesso do código à plataforma. Um aplicativo administrativo pode continuar executando em modo usuário e solicitar serviços ao sistema. Ter mais direitos não elimina essa fronteira. Veja [13.1](13.1-arquitetura-processos-e-objetos.md) e [13.4](13.4-contas-tokens-e-controle-de-acesso.md).

## 2. Nome e handle

O nome participa da localização de um recurso. O handle é uma referência opaca obtida por uma execução para usar um recurso por meio de operações compatíveis. Ele não é o conteúdo do arquivo, uma senha ou necessariamente um endereço de memória. Fechar o handle e apagar o arquivo também são operações distintas. Veja [13.1](13.1-arquitetura-processos-e-objetos.md).

## 3. A barra depois da letra

`C:\Aurora\catalogo.json` especifica um caminho a partir da raiz da unidade C. `C:catalogo.json` depende do diretório corrente associado à unidade C. A letra, sozinha, não torna o segundo caminho totalmente qualificado. Para comparar resultados, é necessário preservar a forma do nome e o contexto que completa sua interpretação. Veja [13.2](13.2-volumes-caminhos-e-perfis.md).

## 4. O arquivo acessível à atendente

A observação demonstra que aquela operação, realizada no contexto da atendente, conseguiu chegar ao recurso e abri-lo. Não demonstra que o serviço possui o mesmo mapeamento de unidade, nem a mesma autorização. Um nome UNC pode eliminar a dependência de uma letra mapeada sem, por isso, conceder acesso ao recurso. Veja [13.2](13.2-volumes-caminhos-e-perfis.md).

## 5. Dependências e fases da execução

O executável pode depender de bibliotecas, runtime, configurações e outros recursos. Algumas dependências só são solicitadas quando determinada função é usada. Abrir uma janela demonstra progresso de parte da execução, não a disponibilidade de todos os componentes necessários a qualquer tarefa. Veja [13.3](13.3-executaveis-bibliotecas-e-carregamento.md).

## 6. Nome de conta e identidade

O nome é uma forma de apresentação e resolução da conta. O modelo de segurança utiliza identificadores como SIDs. Contas locais de computadores diferentes podem ter o mesmo nome sem serem a mesma identidade. Também é necessário distinguir conta, sessão de logon e contexto do processo que realizou a operação. Veja [13.4](13.4-contas-tokens-e-controle-de-acesso.md).

## 7. Três perguntas sobre acesso

Direitos de acesso tratam de operações sobre um objeto, como ler um arquivo. Privilégios habilitam determinadas operações relacionadas ao sistema e têm estado no token. A elevação diz respeito ao contexto administrativo usado pela execução. Uma lista de grupos, isolada, não substitui essas distinções nem a análise dos controles aplicáveis. Veja [13.4](13.4-contas-tokens-e-controle-de-acesso.md).

## 8. HKCU não identifica universalmente a atendente

A tela e o serviço podem consultar contextos de configuração diferentes. HKCU é uma chave predefinida cujo mapeamento depende de regras do contexto da execução; não é simplesmente “a configuração da pessoa diante do monitor”. Também precisamos saber se o serviço usa o Registro e se leu aquela configuração no momento investigado. Veja [13.5](13.5-registro-ambiente-e-configuracao.md).

## 9. Alteração e valor efetivamente consumido

Processos possuem blocos de ambiente próprios. Modificar outro contexto ou uma configuração persistente não obriga a atualização retroativa de processos existentes. Além disso, o programa pode conservar em memória um valor lido anteriormente. É preciso verificar a origem do ambiente e a política de leitura ou recarga da aplicação. Veja [13.5](13.5-registro-ambiente-e-configuracao.md).

## 10. Serviço, processo e tarefa

Processo é um contexto de execução. Serviço é uma unidade integrada ao gerenciamento do SCM, podendo executar em processo próprio ou compartilhado. Tarefa agendada descreve ações, gatilhos e condições gerenciados pelo Agendador de Tarefas. Essas estruturas podem se relacionar, mas não são equivalentes. Veja [13.6](13.6-inicializacao-servicos-e-investigacao.md).

## 11. Um número não é o evento inteiro

É preciso preservar o provedor, o identificador do evento, o canal, o instante, a máquina e os dados relevantes disponíveis. EventID não é a mesma coisa que EventRecordID. O primeiro é definido no contexto do provedor; o segundo identifica um registro no log. Também devemos separar o que o evento demonstra das hipóteses construídas a partir dele. Veja [13.6](13.6-inicializacao-servicos-e-investigacao.md).

## 12. Mudar de hipótese quando a evidência muda

Se a mesma execução abriu o recurso pretendido e depois rejeitou os dados, “não conseguiu resolver o caminho” deixa de explicar aquela falha específica. A investigação deve examinar a etapa de interpretação ou validação dos dados. Isso não prova que não haja outros problemas de configuração; apenas limita a conclusão ao comportamento observado. Veja [13.6](13.6-inicializacao-servicos-e-investigacao.md).

## Uma verificação adicional

Explique, com suas palavras, por que cada uma destas frases é insuficiente: “o exe está instalado”, “a pessoa é administradora”, “o serviço está rodando” e “a configuração está certa”. Uma boa resposta identifica qual verificação adicional falta, em vez de substituir uma certeza por outra.
