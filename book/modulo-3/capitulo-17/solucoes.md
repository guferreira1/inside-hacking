# Capítulo 17 — Respostas comentadas

[← Capítulo](README.md) · [Perguntas](17.7-investigacao-e-verificacao.md#para-conferir-a-compreensao)

## 1. Organização não é confinamento

Uma pasta ou conjunto de dependências não demonstra a retirada de autoridade sobre outros recursos. Precisamos conhecer identidade, políticas e caminhos acessíveis. O exemplo de venv organiza pacotes; não é apresentado como uma barreira completa de execução. Veja a [seção 17.1](17.1-virtualizacao-e-fronteiras.md).

## 2. Representação e limite

Virtualizar fornece uma representação administrada de um recurso. Restringir acesso estabelece quais operações um contexto pode realizar. A representação pode continuar ligada a um recurso compartilhado. A exigência precisa indicar o que proteger, de quem e quais operações ainda são necessárias.

## 3. As responsabilidades da plataforma

O convidado é o sistema executado no ambiente virtual; o hospedeiro sustenta a plataforma. O hipervisor controla aspectos da execução e da divisão de recursos. A interface de gerenciamento permite administrar essa configuração, mas não é a totalidade do mecanismo. Outros componentes, como dispositivos emulados, também participam. Veja a [seção 17.2](17.2-maquinas-virtuais-e-hipervisores.md).

## 4. Físico é relativo à camada

O convidado administra o que lhe é apresentado como memória física. A plataforma precisa relacionar esse espaço à memória atribuída no hospedeiro e aplicar limites. A sequência virtual do convidado → físico do convidado → físico do hospedeiro descreve espaços distintos, não acesso irrestrito à RAM real.

## 5. Qual kernel atende as operações

No modelo usual de containers Linux e no isolamento de processo Windows, o kernel hospedeiro é compartilhado. No isolamento Hyper-V, o container tem uma VM otimizada e um kernel próprio. A palavra container, sem o modo de execução, não determina sozinha a fronteira. Veja a [seção 17.3](17.3-containers-namespaces-e-recursos.md).

## 6. Visões diferentes podem alcançar a mesma origem

Mount namespaces separam a visão das montagens. Uma origem pode continuar compartilhada entre essas visões, e a propagação depende da configuração. É necessário conhecer origem, destino, permissões e relação entre montagens; nomes diferentes não demonstram dados independentes.

## 7. A autoridade de root depende do contexto

Faltam o mapeamento de identidades, o user namespace, as capabilities, os recursos concedidos e a autoridade do runtime ou daemon. Root remapeado e root no contexto inicial não devem ser confundidos. Mesmo sem privilégios externos, o processo pode alcançar recursos que a conta hospedeira consegue acessar e que foram disponibilizados a ele.

## 8. Visibilidade e orçamento

Um namespace de PID trata a identificação e visibilidade de processos. Um controlador de memória pode restringir consumo. Enxergar menos não implica consumir menos, e receber um orçamento menor não demonstra que dados foram ocultados. Os controles se complementam porque protegem propriedades diferentes.

## 9. Concessão ou violação da fronteira

Antes de concluir que houve escape, precisamos demonstrar que a ação atravessou um limite que deveria impedi-la. Se a escrita já era permitida pela configuração, há uma concessão incompatível com o objetivo, não evidência automática de uma falha no hipervisor. Veja a [seção 17.4](17.4-compartilhamentos-e-autoridade.md).

## 10. A rede é apenas um canal

Pastas compartilhadas por integração do virtualizador, área de transferência e dispositivos podem existir independentemente da interface de rede virtual. É necessário inventariar cada passagem. Desabilitar uma delas não modifica automaticamente as outras.

## 11. Saída também importa

NAT pode permitir conexões iniciadas pelo convidado, mesmo quando entradas dependem de encaminhamento adicional. Ausência de entrada direta não comprova bloqueio de saída. A configuração completa, incluindo outras interfaces, precisa corresponder ao alcance pretendido. Veja a [seção 17.5](17.5-conectividade-e-alcance.md).

## 12. Restauração parcial do estado

A VM pode voltar a considerar pendente um lote cujo efeito permanece confirmado fora dela. Repetir sem reconhecer esse efeito pode duplicá-lo. O snapshot só abrange os recursos de seu contrato; não cria uma transação com sistemas externos. Veja a [seção 17.6](17.6-imagens-snapshots-e-recuperacao.md).

## 13. Identidade, ponto de retorno e recuperação

O digest identifica o conteúdo de um artefato. O snapshot conserva um ponto do estado abrangido pela plataforma. Uma cópia de segurança independente pretende permitir recuperação diante de falhas especificadas, inclusive quando a origem deixa de estar disponível. Nenhum desses recursos, sozinho, certifica que o conteúdo é seguro ou que todos os dados externos foram incluídos.

## 14. Alcance da observação

O programa compara seis namespaces do pai e de um filho que ele mesmo criou, no mesmo kernel observado. PIDs diferentes e namespaces iguais mostram que outra execução não criou automaticamente novas separações nessas categorias. Ambos podem estar juntos dentro de uma VM ou container; o experimento não identifica a fronteira externa nem avalia todos os controles. Veja a [seção 17.7](17.7-investigacao-e-verificacao.md).
