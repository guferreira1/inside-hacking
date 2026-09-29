# Respostas comentadas — Capítulo 14

[← Perguntas](14.6-automacao-e-fronteiras-de-confianca.md#para-conferir-a-compreensao) · [Abertura](README.md) · [Glossário](../../glossario.md)

As respostas explicam os mecanismos. Uma tentativa com suas palavras é mais útil do que memorizar a redação abaixo.

## 1 — A aparência das abas

Precisamos identificar o aplicativo de terminal, o shell em cada aba e sua versão. Depois, o comando realmente resolvido e o contexto de execução. A mesma janela pode hospedar linguagens diferentes; cores ou um símbolo no prompt não demonstram privilégios. Se um nome corresponde a uma função em uma aba e a um executável em outra, nem sequer estamos comparando necessariamente o mesmo comando.

[Retomar 14.1](14.1-terminal-shell-e-comandos.md).

## 2 — Os espaços não desapareceram

O valor da variável pode continuar exatamente igual. O que muda é a construção dos argumentos depois da expansão. No contexto demonstrado, sem aspas e com a separação padrão, os espaços dividem o valor em palavras; com `"$arquivo"`, o valor é preservado como um argumento. Não se deve generalizar isso a qualquer posição de uma variável na sintaxe Bash: atribuições e construções condicionais podem ter regras próprias.

[Retomar 14.2](14.2-argumentos-aspas-e-expansoes.md).

## 3 — Quem expandiu o padrão

Com os dois arquivos da pasta sintética, Bash expande `*.txt` em dois nomes antes de chamar o observador. Com `'*.txt'`, passa o asterisco literalmente. O observador somente percorre os argumentos que recebeu; não procurou arquivos. Outro programa poderia interpretar esse argumento por conta própria, porque as aspas do shell não desativam a linguagem do consumidor.

[Retomar 14.2](14.2-argumentos-aspas-e-expansoes.md).

## 4 — Uma fronteira adicional

Na chamada com `printf '%s\n' "$rotulo"`, o ponto e vírgula veio do conteúdo de um argumento; não há nova leitura desse conteúdo como sintaxe de comandos. Uma chamada explícita a `eval`, por exemplo, pode solicitar essa nova interpretação. A diferença central não é a presença isolada de um caractere, mas o papel entregue ao dado em cada etapa.

[Retomar 14.6](14.6-automacao-e-fronteiras-de-confianca.md).

## 5 — A ordem dos destinos

Em `> conjunto.txt 2>&1`, a saída padrão passa a apontar para o arquivo; depois, o erro padrão é duplicado a partir desse destino. Na ordem inversa, o erro padrão primeiro acompanha o destino que a saída padrão possuía naquele momento, e só depois a saída padrão é redirecionada para o arquivo. A duplicação não é uma promessa de acompanhar todas as mudanças futuras do outro descritor. Os testes capturam o destino anterior em vez de supor que seja sempre uma tela.

[Retomar 14.3](14.3-fluxos-redirecionamentos-e-pipelines.md).

## 6 — Diagnóstico não é código de saída

É possível escrever em stderr e terminar com zero, assim como imprimir uma frase de sucesso e retornar um código de erro. São canais diferentes. Precisamos conhecer o contrato da ferramenta, suas opções e a etapa que produziu o código observado. O exemplo da função que imprime um aviso não atribui por isso um estado de falha à operação.

[Retomar 14.3](14.3-fluxos-redirecionamentos-e-pipelines.md) e [14.4](14.4-status-condicoes-e-controle.md).

## 7 — O resultado do pipeline

Sem `pipefail`, o status do exemplo vem da última etapa, `true`, e vale zero. Com `pipefail`, a falha da etapa anterior participa do cálculo e o resultado é um. Isso melhora a informação sobre a cadeia; não desfaz efeitos já produzidos, não torna comandos idempotentes e não confirma o resultado de negócio. Também precisamos interpretar por que uma etapa falhou, inclusive quando um consumidor encerrou a leitura antes do produtor.

[Retomar 14.4](14.4-status-condicoes-e-controle.md).

## 8 — Dados antes da aparência

Uma tabela pode omitir propriedades, abreviar valores ou variar com a largura de exibição. Preservar os objetos permite selecionar, filtrar e transformar suas propriedades sem tentar reconstruí-las pela posição visual dos caracteres. `Format-Table` serve à apresentação; não é a etapa adequada para preservar os objetos originais para processamento posterior. Ao cruzar uma fronteira com um programa nativo, também precisamos conferir a conversão realizada.

[Retomar 14.3](14.3-fluxos-redirecionamentos-e-pipelines.md).

## 9 — Perfil não é contrato do script

Um perfil pode definir funções, aliases e outras personalizações que não estarão presentes em outra conta, host ou invocação não interativa. O script deve declarar de que depende. `-NoProfile` evita carregar os perfis correspondentes, mas não isola o processo de seu ambiente, identidade, diretório, módulos disponíveis ou políticas. É uma escolha de inicialização, não uma sandbox.

[Retomar 14.5](14.5-scripts-contexto-e-repetibilidade.md).

## 10 — Executar ou incorporar

Executar o roteiro em um novo processo permite herdar um contexto inicial, mas mudanças comuns de variável e diretório nesse filho não atualizam automaticamente o shell pai. Com source em Bash ou dot-sourcing em PowerShell, o código é incorporado ao contexto/escopo correspondente da sessão chamadora e pode alterar o que permanecerá nela. Isso não torna a primeira forma uma barreira completa de segurança: um processo filho ainda pode alterar recursos aos quais tiver acesso.

[Retomar 14.5](14.5-scripts-contexto-e-repetibilidade.md).

## 11 — Um resumo não pode parecer completo pela metade

O roteiro valida a quantidade e os estados antes de emitir o resumo final. Assim, uma entrada inválida no meio não deixa na saída de resultado um resumo parcial com aparência de sucesso. Esse é o contrato pequeno escolhido para o exemplo. Repetir uma saída não demonstra idempotência de um programa que grava registros, envia mensagens ou modifica outros recursos; é preciso examinar seus efeitos. O exemplo não possui essas integrações.

[Retomar 14.5](14.5-scripts-contexto-e-repetibilidade.md).

## 12 — Dados externos não autorizam a execução

É preciso verificar quais alvos e operações estão autorizados, a necessidade real de privilégios e como cada valor será interpretado. Uma lista ou mensagem não pode ampliar o escopo nem decidir automaticamente que o processo deve ser elevado. Mesmo com autorização, os argumentos devem conservar suas fronteiras e a operação precisa de limites e registros adequados, sem segredos expostos. Os exemplos do capítulo usam somente dados próprios, não executam essa lista hipotética.

[Retomar 14.6](14.6-automacao-e-fronteiras-de-confianca.md).

[← Índice do Módulo III](../README.md) · [Referências](referencias.md)
