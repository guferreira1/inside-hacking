# Capítulo 11 · Referências e limites da pesquisa

[← Capítulo](README.md) · [Bibliografia geral](../../bibliografia.md)

**Consulta:** 28/09/2026. **Versão:** DRAFT 0.1.

A narrativa da Aurora, o diagnóstico do diretório, a linha do tempo e as comparações são construções autorais. As referências sustentam mecanismos específicos; não descrevem uma investigação real na biblioteca. O percurso principal usa interfaces Linux, com comparações identificadas de Windows e seL4. Não se impõe uma divisão universal de componentes a todos os sistemas operacionais.

<a id="s1"></a>
## S1 · Sistema operacional, kernel e modos de execução

Debian Project. *About Debian*, definição introdutória de sistema, kernel e composição da distribuição; *Introduction to Debian*.

https://www.debian.org/intro/about

https://www.debian.org/intro/

Microsoft Learn. *User mode and kernel mode*.

https://learn.microsoft.com/en-us/windows-hardware/drivers/gettingstarted/user-mode-and-kernel-mode

Uso em 11.1 e 11.2: distinguir a instalação do núcleo, aplicações e serviços fora dele e níveis de execução. O trecho do Debian é usado para composição conceitual, não para reproduzir números de pacotes, requisitos de instalação ou afirmações históricas sobre ports como inventário atual. O exemplo Windows não estabelece equivalência entre conta administrativa e modo kernel.

<a id="s2"></a>
## S2 · Abstração de sistemas de arquivos

The Linux Kernel documentation. *Overview of the Linux Virtual File System*, Introduction e The File Object.

https://docs.kernel.org/filesystems/vfs.html

Uso em 11.1 e no percurso de 11.2: papel da interface VFS e coexistência de implementações. A analogia da biblioteca é nova. O diagrama não afirma que toda leitura passa por armazenamento físico nem que todos os sistemas colocam os mesmos serviços no kernel.

<a id="s3"></a>
## S3 · Outra organização da fronteira

seL4 Foundation. *Frequently Asked Questions*, especialmente What devices does seL4 support?; *The seL4 microkernel*, documentação do projeto.

https://sel4.systems/About/FAQ.html

https://docs.sel4.systems/projects/sel4/

Uso em 11.1: exemplo de microkernel e drivers de dispositivo em modo usuário, com exceções necessárias ao núcleo. Não foi instalado seL4, analisada uma prova formal ou comparado seu desempenho com Linux. As garantias de um componente não foram extrapoladas para um sistema inteiro.

<a id="s4"></a>
## S4 · Chamadas de sistema e funções de biblioteca

Linux man-pages project. *syscalls(2)*, DESCRIPTION e System calls and library wrapper functions.

https://man7.org/linux/man-pages/man2/syscalls.2.html

Uso em 11.1–11.2: interface aplicação/kernel e trabalho das funções envoltórias. A tabela histórica de chamadas não foi adotada como catálogo exaustivo da versão atual do kernel. Não foi realizado rastreamento de syscalls.

<a id="s5"></a>
## S5 · Contratos de abertura, leitura, escrita e erros

Linux man-pages project. *open(2)*, DESCRIPTION, access modes, O_NONBLOCK e ERRORS; *read(2)*, DESCRIPTION, RETURN VALUE e ERRORS; *write(2)*, ERRORS; *close(2)*, DESCRIPTION; *errno(3)*, descrição e nomes simbólicos.

https://man7.org/linux/man-pages/man2/open.2.html

https://man7.org/linux/man-pages/man2/read.2.html

https://man7.org/linux/man-pages/man2/write.2.html

https://man7.org/linux/man-pages/man2/close.2.html

https://man7.org/linux/man-pages/man3/errno.3.html

Uso em 11.2–11.3: descritor, modo de abertura, leitura parcial, fim de arquivo regular, erro EBADF numa escrita em abertura somente de leitura, ENOENT e EACCES. A ressalva de O_NONBLOCK identifica arquivos regulares no Linux; não generaliza todos os recursos. A demonstração verifica resultados da interface Python, não a sequência interna exata de chamadas.

<a id="s6"></a>
## S6 · Interfaces Python do exemplo

Python Software Foundation. *os — Miscellaneous operating system interfaces*, os.open/read/write/close; *tempfile — Generate temporary files and directories*, TemporaryDirectory; *io — Core tools for working with streams*, texto, buffers e fluxos.

https://docs.python.org/3/library/os.html

https://docs.python.org/3/library/tempfile.html

https://docs.python.org/3/library/io.html

Uso em 11.2 e no código: exceções OSError, operações sobre descritores, criação e limpeza de diretório próprio. As páginas públicas consultadas identificavam Python 3.14.7; a execução local utilizou Python 3.13.5. Não se afirma teste de todas as versões. O código evita depender de números fixos de errno e limita o trabalho ao pequeno conteúdo criado por ele.

<a id="s7"></a>
## S7 · Escalonamento e espera

Linux man-pages project. *sched(7)*, definição do escalonador, Scheduling policies e preempção; *poll(2)*, DESCRIPTION, RETURN VALUE e NOTES.

https://man7.org/linux/man-pages/man7/sched.7.html

https://man7.org/linux/man-pages/man2/poll.2.html

Uso em 11.3: distinguir fluxo apto, espera, oportunidade de CPU e prontidão de E/S. A abertura de sched(7) contém uma caracterização histórica de CFS; ela não foi usada para afirmar qual algoritmo interno é o padrão de todo kernel atual. Não houve mudança de prioridades, teste de tempo real ou execução de carga. A linha de 32 ms e o impasse são modelos autorais, não medições.

<a id="s8"></a>
## S8 · Limites e distribuição de recursos

Linux man-pages project. *getrlimit(2)*, especialmente RLIMIT_NOFILE.

https://man7.org/linux/man-pages/man2/getrlimit.2.html

The Linux Kernel documentation. *Control Group v2*, Introduction e Resource Distribution Models: Weights, Limits, Protections e Allocations.

https://docs.kernel.org/admin-guide/cgroup-v2.html

Uso em 11.3: limites por processo e diferença entre distribuição por pesos e tetos de consumo. Não foi configurado cgroup, induzida exaustão ou medida a eficácia de isolamento. Um limite não é apresentado como criação de capacidade física ou validação da lógica da aplicação.

<a id="s9"></a>
## S9 · Identificadores e resolução de caminhos

Linux man-pages project. *credentials(7)*, User and group identifiers e notas sobre credenciais; *path_resolution(7)*, caminho inicial, percurso de componentes e permissões.

https://man7.org/linux/man-pages/man7/credentials.7.html

https://man7.org/linux/man-pages/man7/path_resolution.7.html

Uso em 11.4 e no caso 11.5: identidade da execução, grupos, papéis de identificadores e busca nos diretórios. Não foram atribuídas permissões reais à conta do leitor. A narrativa explicita que sua causa é definida pelas premissas; a presença de EACCES sozinha não identificaria a política responsável. Não se ensina alterar UIDs nem contornar controles.

<a id="s10"></a>
## S10 · Contexto de segurança no Windows

Microsoft Learn. *Access Tokens*.

https://learn.microsoft.com/en-us/windows/win32/secauthz/access-tokens

Uso em 11.4: identidade, grupos e privilégios no token de acesso. Introdução documental, não execução Windows nem comparação completa de todos os mecanismos de autorização. O token de acesso do sistema não foi confundido com token de aplicação Web.

<a id="s11"></a>
## S11 · Controles distintos de identidade, política e visão

Linux man-pages project. *capabilities(7)*, introdução à divisão de privilégios; *namespaces(7)*, DESCRIPTION e tipos de namespace.

https://man7.org/linux/man-pages/man7/capabilities.7.html

https://man7.org/linux/man-pages/man7/namespaces.7.html

The Linux Kernel documentation. *Linux Security Modules: General Security Hooks for Linux*.

https://docs.kernel.org/security/lsm.html

Uso em 11.4: introduzir capabilities Linux, arcabouço LSM e visões de recursos. Containers aparecem apenas para relacionar mecanismos; não há imagem executada ou isolamento certificado. Configuração, mapeamentos e controles adicionais serão desenvolvidos nos capítulos correspondentes. Capabilities Linux não são apresentadas como equivalentes a todo modelo de segurança baseado em capabilities.

<a id="s12"></a>
## S12 · Inicialização e organização do sistema

systemd project. *bootup(7)* e *systemd(1)*, documentação do projeto reproduzida no man7: DESCRIPTION, etapas de inicialização e gerenciador de sistema/serviços.

https://man7.org/linux/man-pages/man7/bootup.7.html

https://man7.org/linux/man-pages/man1/systemd.1.html

Uso em 11.5: etapas, possível initramfs, PID 1 e unidades. É um percurso Linux/systemd, não descrição obrigatória de toda distribuição, de Windows ou de ambientes de container. As tentativas aos endereços freedesktop.org/software/systemd/man/latest não retornaram conteúdo utilizável; a consulta efetiva foi à reprodução da documentação identificada acima. Não houve inicialização de VM nem alteração do sistema de boot.

<a id="s13"></a>
## S13 · Ciclo de vida, contexto e prontidão de serviços

systemd project. *systemd.service(5)*, Type e notificação de prontidão; *systemd.exec(5)*, User, Group e WorkingDirectory. Documentação reproduzida no man7.

https://man7.org/linux/man-pages/man5/systemd.service.5.html

https://man7.org/linux/man-pages/man5/systemd.exec.5.html

Microsoft Learn. *Service control manager*.

https://learn.microsoft.com/en-us/windows/win32/services/service-control-manager

Uso em 11.5: distinção entre processo, inicialização e capacidade oferecida; configuração do contexto e organização do ciclo de vida. Nenhuma unidade systemd ou serviço Windows foi instalado. As variações do importador são fictícias. A definição operacional de verificação de saúde não é um protocolo universal de qualquer gerenciador.

<a id="s14"></a>
## S14 · Aplicação, menor privilégio e registros

OWASP Cheat Sheet Series. *Authorization Cheat Sheet*, Enforce Least Privileges, Validate the Permissions on Every Request e Create Unit and Integration Test Cases for Authorization Logic; *Logging Cheat Sheet*, Event attributes e Data to exclude.

https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html

https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html

Uso em 11.4–11.5: decisões próprias da aplicação, limites de acesso, reteste de casos permitidos e recusados, seleção de registros. Não foram coletados dados pessoais ou logs de uma aplicação real. A política de históricos A/B foi inventada para distinguir autorização no sistema e na aplicação.

## Conferência executada e limites

Os [seis testes](../../../scripts/tests/test_chapter11_examples.py) passaram localmente em Linux x86-64, kernel 6.18.44, glibc 2.41 e Python 3.13.5. Três verificam interfaces do exemplo, execução independente com saída literal e limpeza da pasta temporária. Três conferem modelos de duração, autorização em camadas e dependência circular, sem configurar mecanismos correspondentes no kernel.

O script completo foi executado com `python3 -I -S` e produziu as cinco linhas documentadas em 11.2. Não houve execução privilegiada solicitada pelo procedimento, acesso a arquivos do usuário, mudança de identidade, alteração de permissões, criação de serviços, stress de recursos ou rastreamento de syscalls. As opções -I e -S reduzem interferências da inicialização Python; não são uma sandbox.

A checagem do repositório completo é realizada separadamente pelo workflow da entrega. O clone local não pôde ser concluído por falha de resolução de rede. Um teste de EBADF não demonstra uma política de acesso entre contas; um modelo de espera não é medição de escalonamento. Revisão técnica independente e leitura do capítulo 11 permanecem pendentes. Consulte o [registro editorial](../../../editorial/reviews/capitulo-11.md).
