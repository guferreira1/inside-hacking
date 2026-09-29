# Capítulo 12 · Referências e limites da pesquisa

[← Capítulo](README.md) · [Bibliografia geral](../../bibliografia.md)

**Consulta:** 29/09/2026. **Versão:** DRAFT 0.1.

A narrativa da Aurora, suas duas instalações e o diagnóstico de montagens são fictícios. As fontes sustentam mecanismos específicos; não constituem uma investigação real nem um texto para reproduzir. Consultas pontuais às seções indicadas não equivalem à leitura integral de todos os manuais. O percurso de pacotes é Debian/APT, não uma descrição universal de todas as distribuições.

<a id="s1"></a>
## S1 · Kernel, origem e composição de uma distribuição

The Linux Kernel documentation. *Linux kernel release 6.x*, seção What is Linux? Debian Project. *About Debian*.

https://www.kernel.org/doc/html/latest/admin-guide/README.html

https://www.debian.org/intro/about

Uso em 12.1: origem do núcleo, tradição Unix, composição com programas externos e participação de GNU. Não se reproduz inventário histórico de arquiteturas do README nem se afirma que toda instalação Linux usa os mesmos componentes. Não foi acrescentada uma cronologia sem documentação.

<a id="s2"></a>
## S2 · Identificação de execução e instalação

GNU Coreutils. *uname(1)*. systemd project. *os-release(5)*, DESCRIPTION e campos ID/PRETTY_NAME. Manuais dos projetos reproduzidos no man7.

https://man7.org/linux/man-pages/man1/uname.1.html

https://man7.org/linux/man-pages/man5/os-release.5.html

Uso em 12.1 e 12.5: kernel em execução, identificação da instalação e precedência de caminhos. Não se recomenda executar conteúdo desconhecido nem se oferece uma saída universal. A reprodução de os-release inclui opções de versões em desenvolvimento; o capítulo usa somente os campos e contratos identificados, sem recomendar essa versão para instalação.

<a id="s3"></a>
## S3 · Contexto da resolução e visões de montagem

Linux man-pages project. *path_resolution(7)*, início e percurso; *mount_namespaces(7)*, DESCRIPTION; *namespaces(7)*, visão por classes de recursos.

https://man7.org/linux/man-pages/man7/path_resolution.7.html

https://man7.org/linux/man-pages/man7/mount_namespaces.7.html

https://man7.org/linux/man-pages/man7/namespaces.7.html

Uso em 12.1–12.2: caminhos absoluto/relativo, raiz do processo e distinção de visões. Não foram criados namespaces nem executados containers. A propagação é reconhecida como condição, não configurada neste capítulo.

<a id="s4"></a>
## S4 · Organização convencional dos diretórios

Linux Foundation. *Filesystem Hierarchy Standard 3.0*, capítulos The Root Filesystem, The /usr Hierarchy e The /var Hierarchy.

https://refspecs.linuxfoundation.org/FHS_3.0/fhs/ch03.html

https://refspecs.linuxfoundation.org/FHS_3.0/fhs/ch04.html

https://refspecs.linuxfoundation.org/FHS_3.0/fhs/ch05.html

Uso em 12.2: funções de diretórios, dados variáveis, temporários e de execução. As convenções não foram confundidas com permissões concretas ou com conformidade garantida de toda instalação. Os diretórios individuais referenciados pelo índice foram consultados para as funções resumidas.

<a id="s5"></a>
## S5 · Organização merged-/usr

Debian Project. *Release Notes for Debian 12 (bookworm)*, A “merged-/usr” is now required.

https://www.debian.org/releases/bookworm/amd64/release-notes/ch-information

Uso em 12.2: links dos caminhos tradicionais para equivalentes em /usr. Referência a uma decisão documentada daquela versão, não afirmação de que Debian 12 seja a versão corrente. Não houve migração de diretórios ou instalação do pacote usrmerge.

<a id="s6"></a>
## S6 · Sistemas de arquivos e incorporação à árvore

The Linux Kernel documentation. *Overview of the Linux Virtual File System*, Introduction. Linux man-pages project. *mount(2)*, DESCRIPTION e Creating a bind mount.

https://docs.kernel.org/filesystems/vfs.html

https://man7.org/linux/man-pages/man2/mount.2.html

Uso em 12.2 e 12.4: interface comum, ponto de montagem, conteúdo encoberto e bind mount. O desenho da Aurora é um modelo. Não foi montado, desmontado ou lido um dispositivo bruto.

<a id="s7"></a>
## S7 · Consultar montagens

Linux man-pages project. *proc_pid_mountinfo(5)*. util-linux. *findmnt(8)*, DESCRIPTION.

https://man7.org/linux/man-pages/man5/proc_pid_mountinfo.5.html

https://man7.org/linux/man-pages/man8/findmnt.8.html

Uso em 12.2: contexto da consulta, campos de montagem e ferramenta de apresentação. Não houve inspeção da visão de um serviço externo nem implementação de parser de mountinfo.

<a id="s8"></a>
## S8 · Estado apresentado por procfs

The Linux Kernel documentation. *The /proc Filesystem*, introdução, informações por processo e notas sobre entradas dinâmicas. Debian Reference. *GNU/Linux tutorials*, procfs and sysfs.

https://docs.kernel.org/filesystems/proc.html

https://www.debian.org/doc/manuals/debian-reference/ch01.en.html

Uso em 12.3: dados gerados, contexto self e caráter mutável das observações. Não foram coletados cmdline, environ, memória, credenciais ou dados de outros processos. As descrições amplas de privilégios de root no tutorial Debian não são adotadas como verdade universal.

<a id="s9"></a>
## S9 · Descritor próprio e metadados

Linux man-pages project. *proc_pid_fd(5)* e *inode(7)*, números de inode, tipo de arquivo e identificador de dispositivo. Python Software Foundation. *os* e *tempfile*, fstat e TemporaryDirectory.

https://man7.org/linux/man-pages/man5/proc_pid_fd.5.html

https://man7.org/linux/man-pages/man7/inode.7.html

https://docs.python.org/3/library/os.html

https://docs.python.org/3/library/tempfile.html

Uso em 12.3 e no exemplo: entrada, destino, comparação local de dispositivo/inode e limpeza de objetos próprios. O programa lê no máximo sete bytes pela referência para seu arquivo de seis bytes. Não equipara aberturas independentes a um descritor duplicado nem alega medir posição compartilhada.

<a id="s10"></a>
## S10 · Objetos e atributos em sysfs

The Linux Kernel documentation. *sysfs — The filesystem for exporting kernel objects*, atributos e callbacks de leitura/escrita.

https://www.kernel.org/doc/html/latest/filesystems/sysfs.html

Uso em 12.3: interface de atributos e possibilidade de efeitos ao escrever. Não houve escrita em sysfs nem alteração de parâmetros do kernel.

<a id="s11"></a>
## S11 · Arquivos especiais de dispositivo

Linux man-pages project. *inode(7)*, tipos e identificadores de dispositivo; *null(4)*, DESCRIPTION.

https://man7.org/linux/man-pages/man7/inode.7.html

https://man7.org/linux/man-pages/man4/null.4.html

Uso em 12.3: distinguir arquivo regular, dispositivos de bloco/caractere e contrato de /dev/null. O texto não sugere explorar ou escrever em dispositivos reais. Não foi executado teste de armazenamento por essa interface.

<a id="s12"></a>
## S12 · Tmpfs e conservação de dados

The Linux Kernel documentation. *Tmpfs*.

https://docs.kernel.org/filesystems/tmpfs.html

Uso em 12.3: memória virtual, possível swap e ausência de conservação após desmontagem. Não se afirma que /tmp seja necessariamente tmpfs nem que conteúdo em tmpfs jamais possa alcançar armazenamento de apoio.

<a id="s13"></a>
## S13 · Módulos e confiança no kernel

kmod project. *modprobe(8)*. Linux man-pages project. *proc_modules(5)*. The Linux Kernel documentation. *Kernel module signing facility* e README, configuração built-in versus módulo.

https://man7.org/linux/man-pages/man8/modprobe.8.html

https://man7.org/linux/man-pages/man5/proc_modules.5.html

https://docs.kernel.org/admin-guide/module-signing.html

https://www.kernel.org/doc/html/latest/admin-guide/README.html

Uso em 12.4: artefato instalado versus componente carregado, dependências e verificação de assinatura conforme configuração. Não foram carregados módulos, compilado kernel, alterado firmware ou enfraquecidas proteções.

<a id="s14"></a>
## S14 · Gerenciamento dinâmico de dispositivos

systemd project. *udev(7)*, DESCRIPTION. Manual do projeto reproduzido no man7.

https://man7.org/linux/man-pages/man7/udev.7.html

Uso em 12.4: eventos, regras, permissões e nomes adicionais em espaço de usuário. Não foi apresentada uma implementação universal de automontagem. A reprodução é identificada como snapshot do projeto, não versão que o leitor precisa instalar.

<a id="s15"></a>
## S15 · Dependência e prontidão de serviços

systemd project. *systemd.unit(5)*, Requires/After e distinção de dependência/ordenação; *systemd.service(5)*, Type.

https://man7.org/linux/man-pages/man5/systemd.unit.5.html

https://man7.org/linux/man-pages/man5/systemd.service.5.html

Uso em 12.4: iniciar depois não substitui declarar e verificar a condição necessária. Não foi instalada unidade nem modificado o ciclo de vida de um serviço.

<a id="s16"></a>
## S16 · Pacotes e administração da instalação

Debian Project. *dpkg(1)*, DESCRIPTION, instalação e scripts de manutenção; *The Debian Administrator's Handbook*, seção 6.2, atualização de listas e instalação.

https://manpages.debian.org/trixie/dpkg/dpkg.1.en.html

https://www.debian.org/doc/manuals/debian-handbook/sect.apt-get.en.html

Uso em 12.5: conteúdo de pacote, metadados, dependências, estado local e diferença entre índices e atualização de software. Não foram executados comandos de instalação, download, upgrade ou alteração das fontes.

<a id="s17"></a>
## S17 · Autenticação de repositórios APT

APT project. *apt-secure(8)*, SIGNED REPOSITORIES e SECURE APT.

https://manpages.debian.org/trixie/apt/apt-secure.8.en.html

Uso em 12.5: cadeia de metadados assinados e hashes, limites da autenticação e distinção de assinatura por pacote. Não foi acrescentada chave de confiança, desabilitada verificação ou avaliada a segurança de um repositório concreto.

<a id="s18"></a>
## S18 · Correções retroportadas

Debian Project. *Debian security FAQ*, Why are you fiddling with an old version of that package? e The version number for a package indicates that I am still running a vulnerable version!

https://www.debian.org/security/faq

Uso em 12.5: backports de segurança, manutenção da versão distribuída e necessidade de comparar revisão completa e avisos. Nenhuma vulnerabilidade específica foi classificada como corrigida neste capítulo.

<a id="s19"></a>
## S19 · Consultas à base de pacotes

Debian Project. *dpkg-query(1)*, DESCRIPTION e Search.

https://manpages.debian.org/trixie/dpkg/dpkg-query.1.en.html

Uso em 12.5: base de pacotes e caminhos registrados. A ferramenta não foi tratada como inventário universal de todo arquivo ou execução da máquina.

## Execução e revisão desta entrega

O exemplo próprio foi executado em Linux x86-64, kernel 6.18.44, glibc 2.41 e Python 3.13.5. Seus quatro testes passaram localmente: contrato da plataforma, metadados/leitura e limpeza, limpeza diante de erro simulado e saída de processo separado. O erro simulado não é um teste de permissões entre contas.

A conferência local abrange esses arquivos, não um clone completo: o acesso de rede do ambiente local não resolveu o GitHub. A suíte geral e a navegação são verificadas separadamente no runner, com resultado registrado no controle editorial. Consultas de documentação não são varreduras de alvos.

Não houve montagem, administração de pacotes, alteração de serviços, inspeção de processos alheios, execução privilegiada exigida pelo procedimento ou teste ofensivo. A leitura do capítulo e a revisão técnica independente permanecem pendentes.
