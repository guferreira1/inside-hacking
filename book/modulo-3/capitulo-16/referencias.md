# Capítulo 16 — Referências e limites da pesquisa

[← Capítulo](README.md) · [Bibliografia geral](../../bibliografia.md)

**Consulta:** 29/09/2026. **Versão:** VALIDATED 1.0 — fechamento interno em 29/09/2026; revisão independente pendente.

Fontes primárias sustentam mecanismos específicos; a explicação e a narrativa são autorais. Consultas pontuais não equivalem à leitura integral dos manuais. As páginas de systemd, procps-ng, Cronie e logrotate abaixo são reproduções identificadas da documentação dos projetos no man7. A abertura direta de cinco manuais systemd no freedesktop retornou 403; isso não foi tratado como desaparecimento da documentação.

Versão de desenvolvimento do manual não significa versão instalada ou recomendada. Referências PowerShell usam a vista documental 7.5; a documentação Python em /3/ pode avançar independentemente do runtime dos testes. Ambientes realmente executados estão no [registro editorial](../../../editorial/reviews/capitulo-16.md).

<a id="s1"></a>
## S1 · Identificação e estados de processo

Linux man-pages. *proc_pid_stat(5)*. Uso: PID, PPID, início, tempos e estados; não diagnóstico de saúde por um campo isolado.

https://man7.org/linux/man-pages/man5/proc_pid_stat.5.html

<a id="s2"></a>
## S2 · Encerramento e recolhimento

Linux man-pages. *wait(2)*. Uso: wait, informações de término, zumbis e adoção. Não foi criado laboratório de zumbis.

https://man7.org/linux/man-pages/man2/waitpid.2.html

<a id="s3"></a>
## S3 · Sinais

Linux man-pages. *signal(7)*. Uso: notificação, ações e limites de SIGTERM/SIGKILL. Não autoriza sinalizar processos de terceiros.

https://man7.org/linux/man-pages/man7/signal.7.html

<a id="s4"></a>
## S4 · Encerramento no Windows

Microsoft. *Terminating a Process*. Uso: término, recursos, handles, ExitProcess e TerminateProcess; não equivalência com sinais Unix.

https://learn.microsoft.com/en-us/windows/win32/procthread/terminating-a-process

<a id="s5"></a>
## S5 · Fotografias de processos

procps-ng. *ps(1)*, reprodução no man7. Uso: campos e formato da consulta limitada ao shell do leitor.

https://man7.org/linux/man-pages/man1/ps.1.html

<a id="s6"></a>
## S6 · Consulta de processo em PowerShell

Microsoft. *Get-Process*. Uso: propriedades de processo e limites de plataforma e acesso. Consulta não executada em Windows nesta entrega.

https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-process?view=powershell-7.5

<a id="s7"></a>
## S7 · Daemons e supervisão

systemd. *daemon(7)*, reprodução no man7. Uso: modelos tradicional e supervisionado; não instalação de um daemon.

https://man7.org/linux/man-pages/man7/daemon.7.html

<a id="s8"></a>
## S8 · Tipos e ciclo de vida de serviços

systemd. *systemd.service(5)*, reprodução no man7. Uso: Type, RemainAfterExit, ExecStart e política de reinício. Bloco de configuração fictício, não aplicado.

https://man7.org/linux/man-pages/man5/systemd.service.5.html

<a id="s9"></a>
## S9 · Notificações de prontidão

systemd. *sd_notify(3)*, reprodução no man7. Uso: READY, parada, recarga e watchdog; exige suporte do programa.

https://man7.org/linux/man-pages/man3/sd_notify.3.html

<a id="s10"></a>
## S10 · Transições de serviço Windows

Microsoft. *Service State Transitions*. Uso: estados e comunicação com o SCM, sem afirmar resultado de negócio pelo estado corrente.

https://learn.microsoft.com/en-us/windows/win32/services/service-status-transitions

<a id="s11"></a>
## S11 · Informação de progresso do serviço

Microsoft. *SERVICE_STATUS*. Uso: controles aceitos, checkpoint, wait hint e limites envolvendo serviços no mesmo processo.

https://learn.microsoft.com/en-us/windows/win32/api/winsvc/ns-winsvc-service_status

<a id="s12"></a>
## S12 · Operações sobre o gerenciador

systemd. *systemctl(1)*, reprodução no man7. Uso: enable/start e reload/daemon-reload/restart. Não há execução de comandos de alteração.

https://man7.org/linux/man-pages/man1/systemctl.1.html

<a id="s13"></a>
## S13 · Unidades, composição e dependências

systemd. *systemd.unit(5)*, reprodução no man7. Uso: unidades, drop-ins, precedência e distinção entre ordenação e ativação.

https://man7.org/linux/man-pages/man5/systemd.unit.5.html

<a id="s14"></a>
## S14 · Contexto de execução

systemd. *systemd.exec(5)*, reprodução no man7. Uso: identidade, diretório, ambiente e StateDirectory, sem administração do host.

https://man7.org/linux/man-pages/man5/systemd.exec.5.html

<a id="s15"></a>
## S15 · Alcance e sequência de parada

systemd. *systemd.kill(5)*, reprodução no man7. Uso: KillMode, sinais e relação com prazos de parada; não receita de encerramento forçado.

https://man7.org/linux/man-pages/man5/systemd.kill.5.html

<a id="s16"></a>
## S16 · Limites de recursos

systemd. *systemd.resource-control(5)*, reprodução no man7. Uso: controle de grupos e limites de memória, CPU e tarefas, sem configurar controladores.

https://man7.org/linux/man-pages/man5/systemd.resource-control.5.html

<a id="s17"></a>
## S17 · Recuperação de serviços Windows

Microsoft. *SERVICE_FAILURE_ACTIONSA*. Uso: contagem, sequência, atrasos e redefinição de falhas; recuperação do processo não é recuperação dos dados.

https://learn.microsoft.com/en-us/windows/win32/api/winsvc/ns-winsvc-service_failure_actionsa

<a id="s18"></a>
## S18 · Programação em crontab

Cronie. *crontab(5)*, reprodução no man7. Uso: campos de tempo, contexto e comando. Recorte identificado; não universaliza extensões entre implementações.

https://man7.org/linux/man-pages/man5/crontab.5.html

<a id="s19"></a>
## S19 · Timers

systemd. *systemd.timer(5)*, reprodução no man7. Uso: calendário, referências monotônicas, unidade já ativa e Persistent. Não foi criado timer.

https://man7.org/linux/man-pages/man5/systemd.timer.5.html

<a id="s20"></a>
## S20 · Organização do Agendador de Tarefas

Microsoft. *Task Scheduler for developers*. Uso: ações, gatilhos e configurações da tarefa. Não houve execução ou registro de tarefas.

https://learn.microsoft.com/en-us/windows/win32/taskschd/task-scheduler-start-page

<a id="s21"></a>
## S21 · Horário perdido

Microsoft. *TaskSettings.StartWhenAvailable*. Uso: condições de uma execução posterior; não garantia de replay de trabalho.

https://learn.microsoft.com/en-us/windows/win32/taskschd/tasksettings-startwhenavailable

<a id="s22"></a>
## S22 · Mais de uma instância

Microsoft. *TaskSettings.MultipleInstances*. Uso: política diante de uma tarefa já em andamento.

https://learn.microsoft.com/en-us/windows/win32/taskschd/tasksettings-multipleinstances

<a id="s23"></a>
## S23 · Armazenamento e retenção do journal

systemd. *journald.conf(5)*, reprodução no man7. Uso: modos de armazenamento, limitações e rate limiting; nenhum padrão de distribuição é presumido.

https://man7.org/linux/man-pages/man5/journald.conf.5.html

<a id="s24"></a>
## S24 · Proveniência dos campos

systemd. *systemd.journal-fields(7)*, reprodução no man7. Uso: campos do cliente e campos acrescentados pelo journal; particularidade de fluxos herdados.

https://man7.org/linux/man-pages/man7/systemd.journal-fields.7.html

<a id="s25"></a>
## S25 · Consultas ao journal

systemd. *journalctl(1)*, reprodução no man7. Uso: unidade, usuário, inicialização, período e limite da consulta.

https://man7.org/linux/man-pages/man1/journalctl.1.html

<a id="s26"></a>
## S26 · Registro de eventos Windows

Microsoft. *Windows Event Log*. Uso: publicação, canais e consulta de eventos, sem leitura de registros de uma máquina Windows.

https://learn.microsoft.com/en-us/windows/win32/wes/windows-event-log

<a id="s27"></a>
## S27 · Campos de um evento

Microsoft. *SystemPropertiesType Complex Type*. Uso: provedor, identificadores, versão, tempo e contexto de execução.

https://learn.microsoft.com/en-us/windows/win32/wes/eventschema-systempropertiestype-complextype

<a id="s28"></a>
## S28 · Filtragem de eventos

Microsoft. *Get-WinEvent*. Uso: FilterHashtable, MaxEvents e objetos retornados; exemplo documental de provedor fictício.

https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.diagnostics/get-winevent?view=powershell-7.5

<a id="s29"></a>
## S29 · Relógios

Linux man-pages. *clock_gettime(2)*. Uso: contratos de CLOCK_REALTIME e CLOCK_MONOTONIC; não sincronização de máquinas ou benchmark.

https://man7.org/linux/man-pages/man2/clock_gettime.2.html

<a id="s30"></a>
## S30 · Segurança de logs

OWASP. *Logging Cheat Sheet*. Uso: dados necessários, dados sensíveis, codificação, acesso e falha de coleta. Recomendações não substituem uma avaliação do sistema real.

https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html

<a id="s31"></a>
## S31 · Escrita e confirmação

Linux man-pages. *write(2)*. Uso: escrita parcial, retorno e limites de persistência.

https://man7.org/linux/man-pages/man2/write.2.html

<a id="s32"></a>
## S32 · Sincronização e diretórios

Linux man-pages. *fsync(2)*. Uso: arquivo, metadados e necessidade de considerar a entrada de diretório.

https://man7.org/linux/man-pages/man2/fsync.2.html

<a id="s33"></a>
## S33 · Troca de nomes

Linux man-pages. *rename(2)*. Uso: substituição do destino e limites da atomicidade de uma operação.

https://man7.org/linux/man-pages/man2/rename.2.html

<a id="s34"></a>
## S34 · Arquivos abertos e nomes

Linux man-pages. *open(2)*. Uso: descritor e objeto aberto, independentemente de alterações posteriores no nome.

https://man7.org/linux/man-pages/man2/open.2.html

<a id="s35"></a>
## S35 · Confirmação atômica SQLite

SQLite. *Atomic Commit In SQLite*. Uso: efeito integral da transação e modo rollback journal. Não afirma que nossos dois failpoints reproduzem a suíte de falhas do projeto.

https://www.sqlite.org/atomiccommit.html

<a id="s36"></a>
## S36 · Transações explícitas

SQLite. *Transaction*. Uso: BEGIN, IMMEDIATE, COMMIT e ROLLBACK.

https://sqlite.org/lang_transaction.html

<a id="s37"></a>
## S37 · Configuração de journal e sincronização

SQLite. *PRAGMA Statements*. Uso: journal_mode e synchronous; a configuração do experimento é explicitamente DELETE/FULL.

https://sqlite.org/pragma.html

<a id="s38"></a>
## S38 · Restrições das tabelas

SQLite. *CREATE TABLE*. Uso: chave primária e NOT NULL; não atribui deduplicação de efeitos externos a uma restrição local.

https://sqlite.org/lang_createtable.html

<a id="s39"></a>
## S39 · Interface Python para SQLite

Python. *sqlite3*. Uso: conexão, parâmetros, execução de comandos, transações explícitas e fechamento.

https://docs.python.org/3/library/sqlite3.html

<a id="s40"></a>
## S40 · Processos filhos

Python. *subprocess*. Uso: argumentos separados, pipes, communicate, timeout, poll e retorno; testes somente com filhos próprios.

https://docs.python.org/3/library/subprocess.html

<a id="s41"></a>
## S41 · Saída imediata do filho

Python. *os*. Uso: os._exit nos dois pontos conhecidos de interrupção; não recebe PID nem sinaliza processos externos.

https://docs.python.org/3/library/os.html

<a id="s42"></a>
## S42 · Estrutura de registros sintéticos

Python. *json*. Uso: serialização e recuperação de uma mensagem com quebra de linha; não certificação de um pipeline de logs.

https://docs.python.org/3/library/json.html

<a id="s43"></a>
## S43 · Consulta de serviços Windows

Microsoft. *Get-Service*. Uso: propriedades e disponibilidade no Windows. Exemplo não executado.

https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-service?view=powershell-7.5

<a id="s44"></a>
## S44 · Rotação e janelas de perda

logrotate. *logrotate(8)*, reprodução no man7. Uso: reabertura, copytruncate e sua janela documentada; nenhum registro do host foi rotacionado ou apagado.

https://man7.org/linux/man-pages/man8/logrotate.8.html
