# Capítulo 11 · Respostas comentadas

[← Perguntas](11.5-inicializacao-servicos-e-investigacao.md#pare-e-explique) · [Índice do capítulo](README.md)

As respostas retomam os mecanismos e as premissas do texto. O caso Aurora é fictício; o exemplo de descritores foi executado separadamente. Uma explicação equivalente com suas próprias palavras é mais útil que reproduzir estas frases.

## 1. Uma interface não elimina condições

A abstração de arquivo oferece operações sem exigir que a aplicação administre cada detalhe do dispositivo e do sistema de arquivos. Não garante existência, permissão ou atendimento imediato. A mesma interface precisa permitir comunicar resultados distintos; o caminho real continua sujeito a recursos e falhas.

## 2. Componentes com papéis diferentes

O kernel administra funções centrais e serviços protegidos. Uma distribuição integra o kernel e outros componentes numa instalação mantida. Terminal e área de trabalho são interfaces de interação; não constituem o núcleo nem substituem seus mecanismos. Um sistema pode oferecer serviços sem interface gráfica.

## 3. Solicitação não é transferência irrestrita de autoridade

A entrada no kernel encaminha o atendimento a código que implementa uma interface e suas verificações. Não autoriza a aplicação a executar arbitrariamente com o nível de acesso do núcleo. A volta ao modo usuário preserva essa distinção. Também não se deve confundir a transição de modo com a troca obrigatória para outro processo.

## 4. A referência existe, mas o modo não permite a escrita

A abertura foi realizada com O_RDONLY. O descritor continua válido para leitura, mas a tentativa de escrita utiliza uma operação incompatível com aquela abertura. A interface documenta EBADF também para esse caso. O teste não mostra que outra identidade foi impedida de abrir o arquivo nem que as permissões do arquivo foram modificadas. Ampliar privilégios não é a conclusão do exemplo.

## 5. Fim do conteúdo e ausência do caminho

Na leitura do arquivo regular já consumido, o retorno sem bytes indica fim de arquivo naquele momento. A tentativa de abrir um nome não criado é outra operação e produz ENOENT no exemplo. Não é adequado interpretar ambos como falta de permissão. Em outros recursos e circunstâncias, o contrato da leitura precisa ser consultado.

## 6. Reduzimos somente uma parcela

O modelo possui 7 ms de CPU, 20 ms de espera de E/S e 5 ms de fila. Reduzir somente CPU à metade produz `3,5 + 20 + 5 = 28,5 ms`. As premissas não descrevem uma medição real nem permitem concluir a causa da lentidão de outra aplicação. Mostram que tempo total e tempo de CPU não são a mesma grandeza.

## 7. Visão e consumo

Namespaces Linux organizam visões de classes de recursos. Cgroups administram recursos segundo controladores, com mecanismos como pesos e limites. Separar identificadores de processos não limita automaticamente CPU; limitar memória não estabelece sozinho quais arquivos podem ser lidos. Uma configuração completa pode combinar controles, mas seus papéis precisam continuar distintos.

## 8. A permissão do serviço não é a permissão do cliente

O sistema operacional permite que a identidade do serviço leia o arquivo para realizar suas responsabilidades. A aplicação ainda precisa decidir quais registros podem ser entregues a cada leitor. No cenário, a leitura de B pelo serviço é permitida, mas entregar B a A viola a regra da aplicação. Isso pode acontecer sem alterar privilégios ou explorar o kernel.

## 9. Cada afirmação verifica um marco

Processo existente informa que uma instância foi criada e ainda existe. Prontidão informa que um critério de inicialização foi atendido ou comunicado. Saúde diz respeito a uma capacidade definida em uma observação. Um processo pode estar vivo e falhar na importação; uma inicialização concluída não garante ausência de problemas futuros. A interpretação também depende do contrato do gerenciador de serviços.

## 10. Permitir o necessário e preservar o que deve ser recusado

O reteste precisa mostrar que o serviço alcança e utiliza o recurso legítimo e que identidades sem essa responsabilidade continuam limitadas. No caso fictício, reiniciar sem mudar a condição do diretório repetiria a recusa; não explicaria sua origem. Se a causa fosse outro caminho resolvido ou um formato inválido, a correção também mudaria. O diagnóstico deve acompanhar a etapa da falha.

[Voltar ao capítulo](README.md) · [Módulo III](../README.md) · [Glossário](../../glossario.md)
