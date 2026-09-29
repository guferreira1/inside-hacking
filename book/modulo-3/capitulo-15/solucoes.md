# Capítulo 15 — Respostas comentadas

[← Capítulo](README.md) · [Perguntas](15.7-investigacao-e-verificacao.md#para-conferir-a-compreensao) · [Referências](referencias.md)

Estas respostas discutem os cenários delimitados no capítulo. Não são autorização para alterar contas, políticas ou recursos de terceiros.

## 1. Cadastro e execução

Compararia a associação de grupos registrada para a conta com as credenciais que a execução realmente possui. Um processo antigo pode conservar grupos anteriores. A consulta ao cadastro não comprova que o serviço foi iniciado novamente com o contexto esperado. Também conferiria se a recusa envolve realmente o grupo, em vez de presumir essa causa. [Seção 15.1](15.1-identidades-contas-e-contextos.md).

## 2. A classe do proprietário

No modelo tradicional delimitado, a correspondência com o proprietário seleciona sua classe. Em `046`, ela não contém escrita. Os bits de outros não são uma segunda tentativa nem uma concessão somada. Poder alterar a política como proprietário é outra operação; não equivale a ignorá-la silenciosamente ao abrir. [Seção 15.2](15.2-permissoes-linux-e-caminhos.md).

## 3. Listar e procurar

Leitura do diretório permite enumerar nomes; busca permite percorrer seus componentes. Conhecer um nome e ter busca pode permitir chegar ao arquivo sem poder listar a pasta, desde que as demais verificações permitam. Enumerar o nome, por outro lado, não basta para abri-lo sem a busca necessária. [Seção 15.2](15.2-permissoes-linux-e-caminhos.md).

## 4. Conteúdo e entrada

A escrita recusada diz respeito ao conteúdo do arquivo. Remover o nome envolve a entrada no diretório pai e seus controles de escrita e busca, além de condições como sticky bit. O modo somente leitura do arquivo não basta para proteger seu nome contra remoção. [Seção 15.2](15.2-permissoes-linux-e-caminhos.md).

## 5. Operação sobre bits

Os resultados são `640` e `600`. Aplicamos `pedido & (~mascara & 0777)` aos nove bits, não uma subtração. No segundo caso, a máscara não retira nada que estivesse presente no pedido `600`. Esses resultados pressupõem ausência de ACL padrão e nenhum ajuste posterior. [Seção 15.3](15.3-criacao-propriedade-e-acls.md).

## 6. Herança do grupo não concede leitura

O arquivo pode herdar o identificador de grupo e continuar sem bits de leitura para essa classe. Setgid no diretório e modo de criação tratam de aspectos diferentes. É necessário conferir a criação do arquivo, a política resultante e as credenciais do processo leitor. [Seção 15.3](15.3-criacao-propriedade-e-acls.md).

## 7. Entrada e máscara de ACL

A entrada `rw-`, limitada pela máscara `r--`, permite somente leitura. Ampliar a máscara para `rw-` permite que a escrita já registrada naquela entrada se torne efetiva. Isso também pode afetar outras entradas limitadas pela mesma máscara, motivo para revisar a ACL inteira após uma mudança. [Seção 15.3](15.3-criacao-propriedade-e-acls.md).

## 8. Não reduzir uma DACL a um slogan

A decisão envolve direitos pedidos, identidades e atributos do token, ACEs aplicáveis e sua ordem. A ordem preferida distingue entradas explícitas e herdadas. Uma palavra isolada, como allow ou deny, não descreve todos esses elementos, e o algoritmo pode concluir a avaliação antes de outras entradas. [Seção 15.4](15.4-tokens-e-acls-no-windows.md).

## 9. Vazia e nula

Uma DACL vazia não tem entradas que concedam os acessos discricionários em análise; uma DACL nula não impõe a restrição discricionária da lista. Confundir os estados pode inverter a intenção de proteção. Isso não apaga os demais controles da plataforma. [Seção 15.4](15.4-tokens-e-acls-no-windows.md).

## 10. Corrigir o pedido excessivo

É necessário verificar se o programa pode pedir somente leitura. Caso escrita não faça parte do trabalho, concedê-la ao processo resolve a falha à custa de autoridade desnecessária. O teste deve usar a chamada e a identidade da aplicação corrigida, não apenas uma leitura realizada por um administrador. [Seções 15.4](15.4-tokens-e-acls-no-windows.md) e [15.7](15.7-investigacao-e-verificacao.md).

## 11. Presença, habilitação e elevação

Um privilégio pode existir no token sem estar habilitado naquele instante; habilitar o que já existe é diferente de adicionar um privilégio ausente. A elevação altera o contexto de autoridade, não transforma o código da aplicação em execução de modo kernel. [Seção 15.5](15.5-privilegios-e-delegacao.md).

## 12. Falha ao assumir o contexto do cliente

Continuar pode realizar a operação com a autoridade original do serviço, possivelmente maior do que a do cliente. É preciso verificar o resultado do mecanismo de impersonação e tratar a falha sem prosseguir como se a identidade esperada estivesse ativa. [Seção 15.5](15.5-privilegios-e-delegacao.md).

## 13. Nova abertura e descritor anterior

No experimento Linux de arquivo regular local, o descritor já referencia um recurso aberto. Alterar o modo pode impedir novas aberturas sem fechar aquele descritor. Uma revogação precisa definir se abrange novos pedidos, execuções futuras, sessões ou recursos já abertos; o experimento não é uma regra universal para sistemas remotos. [Seções 15.6](15.6-camadas-revogacao-e-menor-privilegio.md) e [15.7](15.7-investigacao-e-verificacao.md).

## 14. Demonstrar o limite preservado

Um exemplo seria verificar, em ambiente autorizado e com dados de teste, que a identidade de importação continua impedida de substituir o próprio programa ou acessar dados de outro serviço. O teste precisa corresponder a uma restrição expressa no contrato. Recusar uma ação aleatória não demonstra, por si só, que a política está correta. [Seção 15.6](15.6-camadas-revogacao-e-menor-privilegio.md).
