# Capítulo 9 · Referências e limites da pesquisa

[← Capítulo](README.md) · [Bibliografia geral](../../bibliografia.md)

**Consulta:** 24/09/2026. **Versão:** VALIDATED — 1.0 editorial; revisão interna concluída. Revisão técnica independente pendente.

A narrativa dos contadores, os mapas e as contas são construções autorais. O percurso usa sistemas com memória virtual e MMU, especialmente Linux. Referências Windows e convenções de linguagens têm seu contexto identificado. Não se generaliza um tamanho de página, disposição de memória ou política de escalonamento para todas as plataformas.

<a id="s1"></a>
## S1 · Memória virtual, páginas e gestão de recursos

The Linux Kernel documentation. *Concepts overview*, especialmente Virtual Memory Primer, Huge Pages, Anonymous Memory, Reclaim e OOM killer.

https://docs.kernel.org/admin-guide/mm/concepts.html

Uso: visão virtual/física, organização em páginas e tabelas, TLB, preparação sob demanda e recuperação de memória. Os mapas de 256 bytes e as contas de residência são modelos novos, não dados extraídos de equipamentos. A apresentação não presume que toda plataforma tenha MMU, que toda operação de E/S percorra a mesma cache ou que todo page fault exija acesso a disco.

<a id="s2"></a>
## S2 · Atributos compartilhados e próprios de threads

Linux man-pages project. *pthreads(7)*, descrição inicial de threads POSIX e atributos compartilhados ou individuais.

https://man7.org/linux/man-pages/man7/pthreads.7.html

Uso em 9.1: memória global e descritores compartilhados, pilhas e estado por thread. A conclusão de que uma pilha própria não constitui isolamento entre threads decorre da relação entre essas propriedades. Não foram adotadas particularidades históricas de LinuxThreads como descrição de todas as implementações atuais.

<a id="s3"></a>
## S3 · Escalonamento e serviços do kernel

Linux man-pages project. *sched(7)*, introdução a políticas e threads executáveis; *syscalls(2)*, introdução à interface de serviços.

https://man7.org/linux/man-pages/man7/sched.7.html

https://man7.org/linux/man-pages/man2/syscalls.2.html

Uso em 9.1: distinguir oportunidade de execução, espera e atendimento pelo kernel. As três situações didáticas não são uma lista completa dos estados exibidos por ferramentas. Não houve rastreamento ou medição de uma troca de contexto, nem se afirma que toda chamada de sistema troca o processo em execução.

<a id="s4"></a>
## S4 · Níveis de execução

Microsoft Learn. *User mode and kernel mode*.

https://learn.microsoft.com/en-us/windows-hardware/drivers/gettingstarted/user-mode-and-kernel-mode

Uso: distinguir modos de execução e sua relação com aplicações e componentes do sistema. É uma referência de plataforma, não equivalência entre modo kernel e conta administrativa. Não foi executado código em modo kernel.

<a id="s5"></a>
## S5 · Mapeamentos privados e compartilhados

Linux man-pages project. *mmap(2)*, DESCRIPTION e definições de MAP_PRIVATE, MAP_SHARED e MAP_ANONYMOUS.

https://man7.org/linux/man-pages/man2/mmap.2.html

Uso em 9.2, 9.4 e 9.5: criação de regiões, semântica de visibilidade e mapeamentos sem arquivo associado. O exemplo próprio verifica somente dois mapeamentos anônimos herdados por um filho. Não mede endereços físicos, persistência em disco ou todas as combinações de flags.

<a id="s6"></a>
## S6 · Regiões apresentadas por maps

Linux man-pages project. *proc_pid_maps(5)*.

https://man7.org/linux/man-pages/man5/proc_pid_maps.5.html

Uso em 9.2: campos, permissões, regiões e rótulos. O intervalo `[0x4000, 0x5000)` é um exemplo simplificado, explicitamente diferente de uma saída completa do arquivo. Não houve leitura de mapas de outros processos; o acesso real está sujeito às verificações descritas pela interface.

<a id="s7"></a>
## S7 · Seções e estado inicial da imagem

Linux man-pages project. *elf(5)*, descrições de `.text`, `.data`, `.bss`, SHT_NOBITS e segmentos carregáveis.

https://man7.org/linux/man-pages/man5/elf.5.html

Uso em 9.3: código, dados e espaço cujo estado zerado não exige os mesmos bytes no arquivo. Não se apresenta a lista de seções como mapa completo e universal de um processo, nem se transfere a garantia inicial de `.bss` a qualquer alocação posterior.

<a id="s8"></a>
## S8 · Duração de armazenamento e quadros de chamada

GNU Project. *The GNU C Library — Memory Allocation and C*; *Debugging with GDB — Stack Frames*, documentação no Sourceware.

https://sourceware.org/glibc/manual/latest/html_node/Memory-Allocation-and-C.html

https://sourceware.org/gdb/current/onlinedocs/gdb.html/Frames.html

Uso em 9.3: duração automática, estática e dinâmica; papel dos quadros, chamadas e retornos. Detalhes de otimização e ABI impedem tratar cada variável como um bloco necessariamente visível na pilha. Não foram adotadas observações históricas sobre suporte de outras implementações de C como regras contemporâneas universais.

<a id="s9"></a>
## S9 · Alocação, liberação e comportamento do alocador

Linux man-pages project. *malloc(3)*, contratos de malloc/free, notas de implementação e comportamento sob overcommit.

https://man7.org/linux/man-pages/man3/malloc.3.html

Uso em 9.3 e 9.4: tamanho solicitado, ausência de inicialização por malloc, liberação, reutilização e diferentes caminhos de obtenção de memória. Não se fixa limiar universal de mmap, retorno imediato de toda memória ao sistema ou sucesso garantido do uso futuro sob qualquer política. Liberação não é apresentada como sanitização.

<a id="s10"></a>
## S10 · Limites espaciais e temporais

CWE Program. *CWE-787: Out-of-bounds Write* e *CWE-416: Use After Free*, definições e consequências gerais.

https://cwe.mitre.org/data/definitions/787.html

https://cwe.mitre.org/data/definitions/416.html

Uso em 9.3: distinguir escrita além do objeto e uso após o término de sua alocação. Não foram transcritos códigos vulneráveis, casos de exploração ou instruções de ataque. O exemplo de índice 16 foi verificado por aritmética, não por acesso inválido a memória real.

<a id="s11"></a>
## S11 · Permissões e violação de acesso

Linux man-pages project. *mprotect(2)*, DESCRIPTION e NOTES.

https://man7.org/linux/man-pages/man2/mprotect.2.html

Uso em 9.3–9.5: proteções de páginas, SIGSEGV e dependências da arquitetura. Uma região permitida não valida automaticamente os limites e o tempo de vida de cada objeto dentro dela. Nenhuma proteção foi desabilitada nem foi induzida falha de acesso no sistema.

<a id="s12"></a>
## S12 · Contagem de page faults

Linux man-pages project. *getrusage(2)*, campos ru_minflt, ru_majflt e contadores de troca de contexto.

https://man7.org/linux/man-pages/man2/getrusage.2.html

Uso em 9.4: distinção entre faltas atendidas sem E/S e faltas que exigem E/S. Não foram medidos faults do exemplo, nem utilizado ru_maxrss como se fosse medida instantânea de residência. Os termos minor e major não classificam gravidade de vulnerabilidades.

<a id="s13"></a>
## S13 · fork e cópia na escrita

Linux man-pages project. *fork(2)*, semântica de espaços separados e notas da implementação Linux por copy-on-write.

https://man7.org/linux/man-pages/man2/fork.2.html

Uso em 9.4 e 9.5: relação entre pai e filho, preservação de visões privadas e compartilhamento definido por mapeamento. A execução do programa próprio confirma valores visíveis, não observa tabelas de páginas nem contabiliza cópias físicas feitas pelo kernel.

<a id="s14"></a>
## S14 · RSS e PSS

Linux man-pages project. *proc_pid_smaps(5)*, descrições de Rss e Pss.

https://man7.org/linux/man-pages/man5/proc_pid_smaps.5.html

Uso em 9.4: tamanho residente e atribuição proporcional de conteúdo compartilhado. A conta em KiB é um recorte fictício que exclui outros custos do sistema. Não foi medida a memória do usuário nem afirmado que somar RSS equivale a medir RAM física única.

<a id="s15"></a>
## S15 · Prevenção de execução de dados

Microsoft Learn. *Data Execution Prevention*.

https://learn.microsoft.com/en-us/windows/win32/memory/data-execution-prevention

Uso em 9.5: papel de páginas não executáveis e do suporte de hardware. A proteção não foi tratada como prova de ausência de bugs ou substituição de autorização da aplicação. Não foram seguidos procedimentos para alterar configurações.

<a id="s16"></a>
## S16 · Variação da disposição de endereços

The Linux Kernel documentation. *Documentation for /proc/sys/kernel/*, verbete randomize_va_space.

https://docs.kernel.org/admin-guide/sysctl/kernel.html#randomize-va-space

Uso em 9.5: randomização de regiões, dependências de arquitetura, configuração e tipo de executável. Não se afirma que todos os bytes mudam de lugar a cada execução. Não foi lida nem alterada a configuração do computador do leitor.

<a id="s17"></a>
## S17 · Concorrência, sincronização e operações atômicas

CWE Program. *CWE-362: Concurrent Execution using Shared Resource with Improper Synchronization*.

https://cwe.mitre.org/data/definitions/362.html

IEEE/The Open Group. *pthread_mutex_lock*, POSIX.1-2017, reprodução no POSIX Programmer's Manual hospedado pelo man-pages.

https://man7.org/linux/man-pages/man3/pthread_mutex_lock.3p.html

GNU Project. *Built-in Functions for Memory Model Aware Atomic Operations*.

https://gcc.gnu.org/onlinedocs/gcc/_005f_005fatomic-Builtins.html

LLVM Project. *LLVM Atomic Instructions and Concurrency Guide*, Introduction, Optimization outside atomic e NotAtomic.

https://llvm.org/docs/Atomics.html

Uso em 9.5: sincronização de participantes, exclusão mútua e garantias específicas de operações atômicas. A ressalva sobre data races não é uma exposição completa do modelo de memória C/C++ ou LLVM. O intercalamento do contador é simulado sequencialmente; não houve execução deliberada de uma data race. A reprodução POSIX identifica a edição consultada, sem alegação de leitura da especificação mais recente. As tentativas diretas ao site da especificação não retornaram conteúdo utilizável nesta consulta.

<a id="s18"></a>
## S18 · Interfaces Python do exemplo opcional

Python Software Foundation. *os — Miscellaneous operating system interfaces*, os.fork, os.waitpid, os.waitstatus_to_exitcode e os._exit; *mmap — Memory-mapped file support*; *Command line and environment*, opções -I e -S.

https://docs.python.org/3/library/os.html#os.fork

https://docs.python.org/3/library/mmap.html

https://docs.python.org/3/using/cmdline.html#cmdoption-I

Uso nos exemplos: mapeamentos, filho único, espera e término; execução do script como processo independente, sem inicialização automática de site. A documentação pública consultada pode ter versão diferente do Python 3.13.5 usado na execução. O programa deve ser iniciado em um processo sem threads adicionais, não importado em notebook ou servidor. As opções de inicialização reduzem interferências de ambiente Python; não são uma sandbox de segurança.

## Conferência executada e seus limites

Os [sete testes](../../../scripts/tests/test_chapter9_examples.py) passaram na primeira entrega em Linux x86-64, Debian GNU/Linux 13, Python 3.13.5. Seis verificam contas e modelos: tradução, fronteira de página, intervalo, limites de objetos, medidas de memória e intercalamento sequencial. Um executa o script próprio e confere `privado=5` e `compartilhado=9` depois da conclusão do filho.

A execução usou `python3 -I -S` em processo independente. Uma tentativa inicial com a inicialização padrão do ambiente emitiu aviso sobre fork em processo com threads; o procedimento final excluiu essa inicialização e foi executado novamente sem esse aviso. Não se apresenta a tentativa inicial como recomendação de uso em contexto multithread.

Não houve medição de endereços físicos, RSS/PSS, page faults, swap, desempenho ou eficácia de ASLR/DEP; tampouco acesso a outros processos, exploração ou revisão independente. Os exemplos numéricos não simulam integralmente um kernel. A checagem do repositório completo e a regressão são confirmadas pelo workflow associado à entrega, separadamente dos testes locais. O fechamento interno da versão 1.0 e a reconferência dirigida de fontes estão no [registro editorial](../../../editorial/reviews/capitulo-9.md).
