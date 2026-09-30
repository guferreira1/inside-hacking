# Capítulo 17 — Referências e limites da pesquisa

[← Capítulo](README.md) · [Bibliografia geral](../../bibliografia.md)

**Consulta:** 29/09/2026. **Versão:** DRAFT 0.1.

As explicações e o cenário Aurora são autorais. As fontes abaixo fundamentam mecanismos delimitados; consultas às seções indicadas não equivalem à leitura integral de todos os manuais. URLs que acompanham a documentação corrente podem mudar. A versão de um manual consultado não é apresentada como versão instalada ou testada.

Não foi inicializada uma VM nem criado um container nesta entrega. A execução própria compara seis namespaces entre pai e filho em Linux. Seu alcance e os testes estão no [registro editorial](../../../editorial/reviews/capitulo-17.md). Configurações VirtualBox, Hyper-V, Docker e Windows Sandbox são explicadas por documentação, sem alegação de reprodução.

<a id="s1"></a>
## S1 · Ambientes virtuais de dependências

Python Software Foundation. *venv — Creation of virtual environments*.

https://docs.python.org/3/library/venv.html

Uso: o isolamento de pacotes e interpretador não é apresentado como confinamento de todo o acesso do programa.

<a id="s2"></a>
## S2 · Raiz de caminhos e limites de chroot

Linux man-pages. *chroot(2)*.

https://man7.org/linux/man-pages/man2/chroot.2.html

Uso: alteração da raiz de resolução, diretório corrente, descritores e aviso explícito sobre o recorte de segurança. Nenhuma técnica de saída de chroot é executada.

<a id="s3"></a>
## S3 · Modelo de máquina, emulação e aceleradores

QEMU Project. *System Emulation — Introduction*.

https://www.qemu.org/docs/master/system/introduction.html

Uso: modelo de CPU/memória/dispositivos, TCG, aceleradores e dispositivos VirtIO. O ramo master é referência documental, não instalação recomendada.

<a id="s4"></a>
## S4 · Interfaces KVM

Linux Kernel documentation. *The Definitive KVM API Documentation*.

https://docs.kernel.org/virt/kvm/api.html

Uso: visão geral das interfaces de sistema, VM e vCPU. Não implementamos monitor de máquina virtual.

<a id="s5"></a>
## S5 · Tradução de memória no KVM x86

Linux Kernel documentation. *The x86 kvm shadow mmu*.

https://docs.kernel.org/virt/kvm/x86/mmu.html

Uso: espaços de endereços do convidado e hospedeiro e traduções entre eles. Não observamos tabelas físicas nem medimos desempenho.

<a id="s6"></a>
## S6 · Organização do Hyper-V

Microsoft Learn. *Hyper-V Architecture*.

https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/architecture

Uso: hipervisor, partição raiz, partições filhas e caminho de entrada e saída. Não generalizamos cada detalhe x64 a todas as arquiteturas.

<a id="s7"></a>
## S7 · Fronteira de segurança da virtualização QEMU

QEMU Project. *Security*.

https://www.qemu.org/docs/master/system/security.html

Uso: componentes expostos, escape para o contexto do processo hospedeiro, menor privilégio e diferença entre casos de virtualização suportados e emulação TCG. A política de suporte consultada não é promessa universal de ausência de falhas.

<a id="s8"></a>
## S8 · Confiança no hospedeiro

QEMU Project. *Confidential Guest Support*.

https://www.qemu.org/docs/master/system/confidential-guest-support.html

Uso: diferença entre virtualização tradicional e mecanismos adicionais de proteção contra parte das ameaças da plataforma hospedeira. Apenas introdução; nenhum mecanismo confidencial foi configurado.

<a id="s9"></a>
## S9 · Namespaces e suas referências

Linux man-pages. *namespaces(7)*.

https://man7.org/linux/man-pages/man7/namespaces.7.html

Uso: categorias, referências em procfs, comparação local de dispositivo/inode e manutenção de um namespace por descritor aberto. Não criamos namespaces.

<a id="s10"></a>
## S10 · Identificação de processos em namespaces

Linux man-pages. *pid_namespaces(7)*.

https://man7.org/linux/man-pages/man7/pid_namespaces.7.html

Uso: hierarquia, visibilidade e processo inicial. Não houve teste de sinais em PID 1.

<a id="s11"></a>
## S11 · Mapeamento de identidades

Linux man-pages. *user_namespaces(7)*.

https://man7.org/linux/man-pages/man7/user_namespaces.7.html

Uso: UID/GID, capabilities e contexto de autoridade. Não alteramos mapeamentos nem privilégios.

<a id="s12"></a>
## S12 · Visão das montagens

Linux man-pages. *mount_namespaces(7)*.

https://man7.org/linux/man-pages/man7/mount_namespaces.7.html

Uso: separação da lista de montagens e propagação. Não há montagem ou entrada em namespace de outro processo.

<a id="s13"></a>
## S13 · Contabilização e controle de recursos

Linux Kernel documentation. *Control Group v2*.

https://docs.kernel.org/admin-guide/cgroup-v2.html

Uso: distinção entre controladores, limites e namespace de cgroup. Nenhum ensaio de exaustão ou configuração de controlador foi realizado.

<a id="s14"></a>
## S14 · Limites de recursos em containers Docker

Docker Docs. *Resource constraints*.

https://docs.docker.com/engine/containers/resource_constraints/

Uso: controles precisam estar configurados; existência de container não é evidência de orçamento aplicado.

<a id="s15"></a>
## S15 · Imagem e instância

Docker Docs. *What is an image?*

https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-an-image/

Uso: camadas e base de uma execução, distinguindo imagem de estado gravável.

<a id="s16"></a>
## S16 · Composição da segurança de containers

Docker Docs. *Docker Engine security*.

https://docs.docker.com/engine/security/

Uso: kernel, namespaces, cgroups, daemon e configuração. Não importamos afirmações genéricas da página como uma certificação de qualquer configuração.

<a id="s17"></a>
## S17 · Execução rootless

Docker Docs. *Rootless mode*.

https://docs.docker.com/engine/security/rootless/

Uso: daemon e containers sem autoridade de root no contexto externo e diferença em relação a apenas escolher outro usuário para a aplicação.

<a id="s18"></a>
## S18 · Perfil seccomp no Docker

Docker Docs. *Seccomp security profiles for Docker*.

https://docs.docker.com/engine/security/seccomp/

Uso: filtragem de chamadas de sistema como uma camada, não configuração completa de isolamento.

<a id="s19"></a>
## S19 · Recorte dos filtros seccomp

Linux Kernel documentation. *Seccomp BPF*.

https://docs.kernel.org/userspace-api/seccomp_filter.html

Uso: o filtro de chamadas não constitui sozinho uma sandbox. Não foi aplicado filtro ao host.

<a id="s20"></a>
## S20 · Origem e destino de bind mounts

Docker Docs. *Bind mounts*.

https://docs.docker.com/engine/storage/bind-mounts/

Uso: compartilhamento, escrita, somente leitura, origem no host do daemon e limites recursivos. Não foi disponibilizado nenhum diretório pessoal a um container.

<a id="s21"></a>
## S21 · Persistência fora da instância

Docker Docs. *Volumes*.

https://docs.docker.com/engine/storage/volumes/

Uso: ciclo de vida do armazenamento e compartilhamento. Não removemos volumes nem dados reais.

<a id="s22"></a>
## S22 · Autoridade de administração do daemon

Docker Docs. *Protect the Docker daemon socket*.

https://docs.docker.com/engine/security/protect-access/

Uso: controle do daemon como autoridade relevante e necessidade de proteger o canal. Nenhuma API administrativa é acessada pelo exemplo.

<a id="s23"></a>
## S23 · Integração de pastas entre convidado e host

Oracle. *VirtualBox 7.2 User Guide — Guest Additions*, seção Shared Folders.

https://docs.oracle.com/en/virtualization/virtualbox/7.2/user/guestadditions.html

Uso: pastas compartilhadas por componentes de integração, sem dependência de rede entre os sistemas.

<a id="s24"></a>
## S24 · Recursos compartilhados e risco

Oracle. *VirtualBox 7.2 User Guide — Security Guide*.

https://docs.oracle.com/en/virtualization/virtualbox/7.2/user/Security.html

Uso: área de transferência, compartilhamentos e passthrough como concessões. O manual não substitui avaliação da configuração concreta.

<a id="s25"></a>
## S25 · Modos de isolamento de containers Windows

Microsoft Learn. *Isolation modes*.

https://learn.microsoft.com/en-us/virtualization/windowscontainers/manage-containers/hyperv-container

Uso: kernel compartilhado no modo process e kernel separado no modo Hyper-V. Compatibilidade de versões e requisitos não foram testados.

<a id="s26"></a>
## S26 · Modos de rede VirtualBox

Oracle. *VirtualBox 7.2 User Guide — Virtual Networking*.

https://docs.oracle.com/en/virtualization/virtualbox/7.2/user/networkingdetails.html

Uso: recortes de NAT, bridge, host-only e rede interna. A comparação não representa uma avaliação da rede do leitor nem sigilo contra um administrador do hospedeiro.

<a id="s27"></a>
## S27 · Redes de containers e contexto local

Docker Docs. *Networking overview* e *None network driver*.

https://docs.docker.com/engine/network/

https://docs.docker.com/engine/network/drivers/none/

Uso: conectividade de saída, compartilhamento de contexto no modo host, loopback e modo none. Outros canais compartilhados permanecem perguntas separadas.

<a id="s28"></a>
## S28 · Publicação de portas

Docker Docs. *Port publishing and mapping*.

https://docs.docker.com/engine/network/port-publishing/

Uso: endereço de publicação e alcance de entrada. Não publicamos uma aplicação nem enviamos tráfego externo.

<a id="s29"></a>
## S29 · Snapshots, cópias e estado incluído

Oracle. *VirtualBox 7.2 User Guide — Working with Virtual Machines*, seções Snapshots e Cloning a Virtual Machine.

https://docs.oracle.com/en/virtualization/virtualbox/7.2/user/working-with-vms.html

Uso: estado incluído, discos excepcionados, memória e dependências de clones. O cenário sobre efeitos externos é um raciocínio autoral com premissas explícitas, não uma reprodução de snapshot.

<a id="s30"></a>
## S30 · Identificação de imagens e manutenção

Docker Docs. *Building best practices*, seção Pin base image versions.

https://docs.docker.com/build/building/best-practices/

Uso: tags mutáveis, digest e necessidade de processo de atualização. Não há imagem de teste externa indicada para execução.

<a id="s31"></a>
## S31 · Kernel separado no Windows Sandbox

Microsoft Learn. *Windows Sandbox*.

https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/

Uso: ambiente descartável, isolamento por hipervisor e configuração de rede independente. Não foi instalado Windows Sandbox.

<a id="s32"></a>
## S32 · Configuração Windows Sandbox

Microsoft Learn. *Use and configure Windows Sandbox*.

https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-configure-using-wsb-file

Uso: opções Networking, ClipboardRedirection e VGpu no fragmento apresentado para leitura. Não se afirma teste em Windows ou proteção integral.

<a id="s33"></a>
## S33 · Criação e espera do filho próprio

Python Software Foundation. *subprocess — Subprocess management*.

https://docs.python.org/3/library/subprocess.html

Uso: argumentos sem shell, captura de saída, retorno e timeout. A documentação corrente não é a versão de runtime observada.

<a id="s34"></a>
## S34 · Descritores e metadados do exemplo

Python Software Foundation. *os — Miscellaneous operating system interfaces*.

https://docs.python.org/3/library/os.html

Uso: open, close, fstat e getpid. As chamadas se limitam a referências do próprio processo.

<a id="s35"></a>
## S35 · Diretório de namespaces por processo

Linux man-pages. *proc_pid_ns(5)*.

https://man7.org/linux/man-pages/man5/proc_pid_ns.5.html

Uso: localização das referências em procfs; mecanismos detalhados em S9.

<a id="s36"></a>
## S36 · Hospedeiro, convidado e virtualização hospedada

Oracle. *VirtualBox 7.2 User Guide — About Oracle VirtualBox*.

https://docs.oracle.com/en/virtualization/virtualbox/7.2/user/Introduction.html

Uso: vocabulário de VM e distinção tradicional de hipervisores tipo 1 e tipo 2. Não usamos o rótulo como classificação universal de segurança.

<a id="s37"></a>
## S37 · Novo processo e recursos herdados

Linux man-pages. *fork(2)*.

https://man7.org/linux/man-pages/man2/fork.2.html

Uso: distinção entre identidade do filho e recursos herdados. Não se afirma que toda implementação Python cria processos por uma única chamada interna.

<a id="s38"></a>
## S38 · Metadados referenciados por descritor

Linux man-pages. *stat(2)*.

https://man7.org/linux/man-pages/man2/stat.2.html

Uso: fstat sobre descritor e campos st_dev/st_ino. Comparação limitada ao mesmo kernel e à categoria de namespace correspondente.
