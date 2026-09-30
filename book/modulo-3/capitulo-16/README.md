# Capítulo 16 — Processos, serviços, logs e persistência de estado

[← Capítulo 15](../capitulo-15/README.md) · [Índice do módulo](../README.md) · [Glossário](../../glossario.md)

**Módulo III — Sistemas operacionais**

> **Status:** DRAFT 0.1 — primeira entrega de leitura. Fontes, execuções e limites no [registro editorial](../../../editorial/reviews/capitulo-16.md). Revisão técnica independente pendente.

A biblioteca Aurora corrigiu o pedido de acesso do importador. Ele já encontra o catálogo e solicita somente a leitura de que precisa. Durante o teste acompanhado pela equipe, tudo parece funcionar. Na manhã seguinte, porém, alguns livros aparecem duas vezes.

O painel informa que o serviço está ativo. Um registro diz que a importação começou. Outro mostra uma nova inicialização minutos depois. Uma pessoa propõe reiniciar mais uma vez. Outra pergunta se o agendamento disparou duas vezes. Antes de mudar qualquer coisa, precisamos descobrir o que aconteceu entre começar o trabalho, registrar seu resultado e encerrar aquela execução.

Nos capítulos anteriores, conhecemos processos, identidades, comandos e permissões. Agora vamos acompanhar essas peças **ao longo do tempo**. Uma coisa é conseguir executar um programa; outra é administrá-lo durante horas, interpretar suas falhas e retomar o trabalho sem perder ou repetir efeitos.

**A Aurora é um cenário fictício.** Suas mensagens, horários e incidentes são construções didáticas. Os exemplos executáveis usam processos filhos e bancos temporários próprios; não acessam um serviço real da biblioteca. A leitura é completa sem instalar serviços, criar agendamentos ou modificar a configuração do computador.

Neste capítulo, persistência de estado significa conservar informações necessárias à continuidade de um trabalho. Não é sinônimo da persistência de acesso estudada posteriormente na parte ofensiva.

## Percurso de leitura

| Seção | Pergunta central |
| --- | --- |
| [16.1 · Uma execução tem começo, espera e fim](16.1-ciclo-de-vida-e-processos.md) | Como distinguir uma execução existente, uma execução esperando e uma execução encerrada? |
| [16.2 · Trabalhar sem a janela aberta](16.2-servicos-e-supervisao.md) | O que um gerenciador de serviços administra, e o que ele não sabe sobre a aplicação? |
| [16.3 · Mudar a configuração não é mudar a execução](16.3-configuracao-parada-e-reinicio.md) | O que acontece ao recarregar, parar ou reiniciar um serviço? |
| [16.4 · O horário não faz o trabalho](16.4-agendamento-e-sobreposicao.md) | Como disparos, atrasos e sobreposição se relacionam com a tarefa? |
| [16.5 · O registro não é o acontecimento inteiro](16.5-logs-tempo-e-evidencias.md) | Como interpretar origem, tempo, retenção e significado de uma mensagem? |
| [16.6 · O processo acaba; o estado precisa de um contrato](16.6-estado-confirmacao-e-retomada.md) | Que informação permite retomar um trabalho depois de uma interrupção? |
| [16.7 · Reconstruir a execução antes de mudar o sistema](16.7-investigacao-e-verificacao.md) | Como reunir as evidências e conferir uma correção sem apagar a pergunta original? |

Há dois [exemplos opcionais](exemplos/README.md), quatorze perguntas e [respostas comentadas](solucoes.md). As [referências](referencias.md) identificam os mecanismos pesquisados e distinguem documentação consultada de comportamento reproduzido.

**[Começar pela seção 16.1 →](16.1-ciclo-de-vida-e-processos.md)**
