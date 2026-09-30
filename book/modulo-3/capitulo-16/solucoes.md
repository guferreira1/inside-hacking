# Capítulo 16 — Respostas comentadas

[← Capítulo](README.md) · [Perguntas](16.7-investigacao-e-verificacao.md#para-conferir-a-compreensao)

## 1. Nome, PID e início

O nome pode ser compartilhado por várias execuções. O PID identifica um processo dentro de determinado contexto e período, mas pode ser reutilizado depois. O início ajuda a distinguir gerações da execução e a relacioná-las ao histórico. Uma fotografia de agora não identifica, por si só, quem atuou ontem. Veja a [seção 16.1](16.1-ciclo-de-vida-e-processos.md).

## 2. Espera legítima ou falta de progresso

Falta conhecer a atividade esperada e a condição pela qual o processo espera. Aguardar um lote inexistente pode ser normal; aguardar indefinidamente uma dependência que deveria responder pode ser um problema. Duração, estado, registros e progresso da aplicação precisam ser relacionados. Baixa CPU não é sinônimo de saúde nem de falha.

## 3. Zumbi e órfão

O zumbi já encerrou e mantém informações mínimas para recolhimento pelo responsável. O órfão perdeu seu pai, mas pode continuar executando. Recolher o resultado de um filho encerrado e supervisionar um processo em andamento são responsabilidades diferentes. A [seção 16.1](16.1-ciclo-de-vida-e-processos.md) delimita o modelo Linux.

## 4. O contrato de ativo

Uma unidade oneshot pode permanecer considerada ativa após o término dos processos quando configurada para isso. Mesmo quando há um processo contínuo, a condição reconhecida pelo gerenciador pode não incluir o sucesso da operação de negócio. Precisamos do tipo da unidade e da definição de prontidão, não apenas de uma palavra do painel. Veja a [seção 16.2](16.2-servicos-e-supervisao.md).

## 5. Notificação sem emissor

A configuração espera uma mensagem que a aplicação não sabe produzir. Não basta mudar o tipo de serviço para inventar uma confirmação de prontidão. A aplicação deve implementar o protocolo e anunciar um marco coerente com a funcionalidade que oferece.

## 6. Três alterações

Recarregar a aplicação muda a configuração que ela utiliza, quando esse mecanismo existe. Recarregar o gerenciador atualiza a interpretação das unidades. Reiniciar substitui a execução por uma nova sequência de parada e início, com os efeitos do contrato correspondente. A [seção 16.3](16.3-configuracao-parada-e-reinicio.md) explica por que essas ações não são intercambiáveis.

## 7. Ordem não é disponibilidade permanente

Ordenação organiza transições; não garante que um arquivo particular exista, que uma dependência permaneça saudável nem que uma conexão remota continue disponível. Também não deve ser confundida com uma dependência que ativa a outra unidade. É necessário definir qual condição está sendo ordenada e como a aplicação reage a mudanças posteriores.

## 8. Sobreposição e repetição

É preciso decidir o que ocorre quando um novo disparo chega com a tarefa anterior em andamento: paralelismo, fila, descarte ou substituição, conforme o mecanismo. Mesmo sem sobreposição, uma tentativa posterior pode repetir um efeito confirmado cujo checkpoint ficou desatualizado. Concorrência e reconhecimento de trabalho aplicado são problemas diferentes. Veja a [seção 16.4](16.4-agendamento-e-sobreposicao.md).

## 9. Disparo não é lote

O timer acompanha a programação da ativação. Não conhece automaticamente quais lotes a aplicação confirmou. Recuperar uma oportunidade perdida pode iniciar uma nova execução, mas é o estado da aplicação que permite decidir o trabalho restante. Vários horários perdidos também não implicam várias importações necessárias.

## 10. O significado de sucesso

Sem identificar a operação e o marco da mensagem, não sabemos se houve leitura, validação ou confirmação durável. Sem lote e tentativa, não sabemos a que trabalho a mensagem pertence. Mesmo conhecendo a origem, ainda precisamos conferir o significado atribuído pelo código. Veja a [seção 16.5](16.5-logs-tempo-e-evidencias.md).

## 11. Tempo e recorte

O relógio de calendário pode ser ajustado; o monotônico mede intervalos sob outro contrato, sem oferecer um horário universal entre máquinas. A identificação da inicialização ajuda a delimitar eventos e a interpretar valores relativos àquele contexto. Um filtro apenas da inicialização atual pode deixar de fora a falha anterior.

## 12. Uma operação não confirma duas alterações

Uma escrita aceita não garante todas as propriedades de persistência. Renomear atomicamente um destino não reúne atualizações de arquivos distintos numa transação. Se o efeito e seu checkpoint forem confirmados separadamente, uma interrupção entre eles pode deixar estados incompatíveis. Veja a [seção 16.6](16.6-estado-confirmacao-e-retomada.md).

## 13. Efeito sem resposta

O commit pode ter terminado antes de a resposta ser emitida ou observada. Inferir “nada aconteceu” a partir da ausência de sucesso repetiria o efeito. No exemplo, a identidade estável do lote e o registro no mesmo banco permitem reconhecer a repetição. A mesma identidade com outro conteúdo é recusada, não tratada como equivalente.

## 14. Alcance do experimento

Os testes verificam interrupções do processo filho em dois pontos conhecidos, a leitura posterior do banco e a repetição controlada. Não desligam a máquina, não simulam corrupção de setores, não percorrem todos os caminhos de recuperação do SQLite nem abrangem ações externas à transação local. A [seção 16.7](16.7-investigacao-e-verificacao.md) relaciona esses limites à explicação causal.
