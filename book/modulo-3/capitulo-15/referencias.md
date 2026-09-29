# Capítulo 15 — Referências e limites da pesquisa

[← Capítulo](README.md) · [Bibliografia geral](../../bibliografia.md)

**Consulta:** 29/09/2026. **Versão:** DRAFT 0.1.

A narrativa e os exemplos de contas, modos e políticas são autorais. As fontes sustentam mecanismos delimitados, não o relato de um incidente. As consultas concentraram-se nas seções relacionadas ao texto; não representam leitura integral de todos os manuais. Páginas reproduzidas no man7 identificam seus projetos de origem. Versão da documentação não deve ser confundida com versão de software executada.

As ACLs POSIX do Linux não são apresentadas como equivalentes a DACLs Windows. Também não se confunde revisão documental com execução: as quatro observações de arquivos Linux foram reproduzidas; as consultas administrativas Windows e os mecanismos privilegiados foram pesquisados, não acionados. Resultados e ambientes estão no [registro editorial](../../../editorial/reviews/capitulo-15.md).

<a id="s1"></a>
## S1 · Credenciais de processos Linux

Linux man-pages. *credentials(7)*, User and group identifiers; herança e IDs de sistema de arquivos.

https://man7.org/linux/man-pages/man7/credentials.7.html

<a id="s2"></a>
## S2 · Registro de contas locais

Linux man-pages. *passwd(5)*, campos do registro e relação com senhas sombreadas.

https://man7.org/linux/man-pages/man5/passwd.5.html

<a id="s3"></a>
## S3 · Autenticação e envelhecimento de senha

shadow-utils. *shadow(5)*, formato e restrições do arquivo. A fonte foi consultada, não o arquivo de senhas de uma máquina.

https://man7.org/linux/man-pages/man5/shadow.5.html

<a id="s4"></a>
## S4 · Fontes de resolução de identidades

Linux man-pages. *nsswitch.conf(5)*, bases, fontes e ordem de consulta.

https://man7.org/linux/man-pages/man5/nsswitch.conf.5.html

<a id="s5"></a>
## S5 · Registro de grupos

Linux man-pages. *group(5)*, nome, GID e lista de membros; não substitui as credenciais da execução.

https://man7.org/linux/man-pages/man5/group.5.html

<a id="s6"></a>
## S6 · Consulta de identidade corrente ou cadastrada

GNU coreutils. *id(1)*, uso com e sem usuário. A página do manual é a reprodução consultada; a abertura direta do manual GNU completo falhou nesta pesquisa.

https://man7.org/linux/man-pages/man1/id.1.html

<a id="s7"></a>
## S7 · Identificadores Windows

Microsoft Learn. *Security Identifiers*, identidade, nome e recriação de contas.

https://learn.microsoft.com/en-us/windows/win32/secauthz/security-identifiers

<a id="s8"></a>
## S8 · Contexto de segurança Windows

Microsoft Learn. *Access Tokens*, elementos do token, token primário e contexto de execução.

https://learn.microsoft.com/en-us/windows/win32/secauthz/access-tokens

<a id="s9"></a>
## S9 · Propriedade, tipo e modo de arquivos Linux

Linux man-pages. *inode(7)*, user/group IDs e significado dos bits de modo.

https://man7.org/linux/man-pages/man7/inode.7.html

<a id="s10"></a>
## S10 · Resolução de caminhos e busca

Linux man-pages. *path_resolution(7)*, componentes, permissões e credenciais de sistema de arquivos.

https://man7.org/linux/man-pages/man7/path_resolution.7.html

<a id="s11"></a>
## S11 · Alteração de modo e bits especiais

Linux man-pages. *chmod(2)*, requisitos de autoridade, setgid, sticky bit e efeito sobre descritores já abertos no sistema local.

https://man7.org/linux/man-pages/man2/chmod.2.html

<a id="s12"></a>
## S12 · Remoção de uma entrada de diretório

Linux man-pages. *unlink(2)*, permissões no diretório, sticky bit e objetos ainda abertos.

https://man7.org/linux/man-pages/man2/unlink.2.html

<a id="s13"></a>
## S13 · Pedido de abertura e recurso aberto

Linux man-pages. *open(2)*, modo de acesso, criação e descrição de arquivo aberto.

https://man7.org/linux/man-pages/man2/open.2.html

<a id="s14"></a>
## S14 · Máscara de criação

Linux man-pages. *umask(2)*, operação sobre bits e exceção da ACL padrão na criação.

https://man7.org/linux/man-pages/man2/umask.2.html

<a id="s15"></a>
## S15 · ACLs POSIX no Linux

Projeto Linux ACL. *acl(5)*, tipos, máscara, correspondência com bits de modo, criação e algoritmo de verificação. A especificação histórica referida pelo projeto é um draft POSIX.1e, não um padrão final de equivalência com Windows.

https://man7.org/linux/man-pages/man5/acl.5.html

<a id="s16"></a>
## S16 · Consulta de ACLs e permissões efetivas

Projeto Linux ACL. *getfacl(1)*, apresentação de entradas, máscara e comentários de acesso efetivo.

https://man7.org/linux/man-pages/man1/getfacl.1.html

<a id="s17"></a>
## S17 · Alteração de ACLs e cálculo da máscara

Projeto Linux ACL. *setfacl(1)*, opções e regras de recalculação. Nenhuma ACL do host foi alterada nesta entrega.

https://man7.org/linux/man-pages/man1/setfacl.1.html

<a id="s18"></a>
## S18 · Alteração de propriedade

Linux man-pages. *chown(2)*, requisitos para mudar proprietário e grupo.

https://man7.org/linux/man-pages/man2/chown.2.html

<a id="s19"></a>
## S19 · Descritores de segurança

Microsoft Learn. *Security Descriptors*, proprietário, grupo primário, DACL e SACL.

https://learn.microsoft.com/en-us/windows/win32/secauthz/security-descriptors

<a id="s20"></a>
## S20 · Direitos e máscaras de acesso

Microsoft Learn. *Access Rights and Access Masks*, direitos genéricos, padronizados e específicos do objeto.

https://learn.microsoft.com/en-us/windows/win32/secauthz/access-rights-and-access-masks

<a id="s21"></a>
## S21 · Avaliação discricionária de acesso Windows

Microsoft Learn. *How AccessCheck Works*, relação entre pedido, token, ACEs e término da avaliação. O modelo R/W do texto não implementa toda a API.

https://learn.microsoft.com/en-us/windows/win32/secauthz/how-dacls-control-access-to-an-object

<a id="s22"></a>
## S22 · Ordenação de ACEs

Microsoft Learn. *Order of ACEs in a DACL*, ordem preferida, entradas explícitas e herdadas.

https://learn.microsoft.com/en-us/windows/win32/secauthz/order-of-aces-in-a-dacl

<a id="s23"></a>
## S23 · Ausência de DACL e lista vazia

Microsoft Learn. *Null DACLs and Empty DACLs*, distinção de estados no controle discricionário.

https://learn.microsoft.com/en-us/windows/win32/secauthz/null-dacls-and-empty-dacls

<a id="s24"></a>
## S24 · Herança de regras Windows

Microsoft Learn. *ACE Inheritance*, flags, propagação e aplicação a objetos filhos.

https://learn.microsoft.com/en-us/windows/win32/secauthz/ace-inheritance

<a id="s25"></a>
## S25 · Direitos de acesso a arquivos Windows

Microsoft Learn. *File Security and Access Rights*, tipos de direitos e acesso solicitado na abertura.

https://learn.microsoft.com/en-us/windows/win32/fileio/file-security-and-access-rights

<a id="s26"></a>
## S26 · Capabilities Linux

Linux man-pages. *capabilities(7)*, divisão de privilégios, CAP_CHOWN, CAP_DAC_OVERRIDE e conjuntos associados à execução. O capítulo não ensina ou executa sua configuração completa.

https://man7.org/linux/man-pages/man7/capabilities.7.html

<a id="s27"></a>
## S27 · Execução e transições de identidade

Linux man-pages. *execve(2)*, setuid/setgid, restrições, scripts e contexto da nova imagem.

https://man7.org/linux/man-pages/man2/execve.2.html

<a id="s28"></a>
## S28 · Execução delegada

Projeto sudo. *sudo(8)*, identidade de destino, política e consulta -l. Reprodução identificada do manual, não execução de sudo nesta entrega.

https://man7.org/linux/man-pages/man8/sudo.8.html

<a id="s29"></a>
## S29 · Política sudoers

Projeto sudo. *sudoers(5)*, autenticação, especificações de usuário/comando, ambiente e limites de restrições. A reprodução no man7 foi consultada após falha de abertura no domínio sudo.ws.

https://man7.org/linux/man-pages/man5/sudoers.5.html

<a id="s30"></a>
## S30 · Privilégios Windows

Microsoft Learn. *Privileges*, distinção entre privilégios de sistema e direitos sobre objetos.

https://learn.microsoft.com/en-us/windows/win32/secauthz/privileges

<a id="s31"></a>
## S31 · Privilégio presente, habilitado ou removido

Microsoft Learn. *Changing Privileges in a Token*, limites de AdjustTokenPrivileges.

https://learn.microsoft.com/en-us/windows/win32/secbp/changing-privileges-in-a-token

<a id="s32"></a>
## S32 · Elevação e aprovação administrativa

Microsoft Learn. *How User Account Control works*. O texto delimita o fluxo de token filtrado; não generaliza todas as políticas e versões nem reproduz elevação.

https://learn.microsoft.com/en-us/windows/security/application-security/application-control/user-account-control/how-it-works

<a id="s33"></a>
## S33 · Controle obrigatório de integridade

Microsoft Learn. *Mandatory Integrity Control*, níveis, rótulos e relação com controle discricionário.

https://learn.microsoft.com/en-us/windows/win32/secauthz/mandatory-integrity-control

<a id="s34"></a>
## S34 · Contexto de um cliente

Microsoft Learn. *Client Impersonation* e *Impersonation Tokens*, atuação da thread e distinção de tokens.

https://learn.microsoft.com/en-us/windows/win32/secauthz/client-impersonation

https://learn.microsoft.com/en-us/windows/win32/secauthz/impersonation-tokens

<a id="s35"></a>
## S35 · Verificação da falha de impersonação

Microsoft Learn. *ImpersonateLoggedOnUser*, Remarks. Fundamenta o tratamento da falha; não apresenta procedimento de exploração.

https://learn.microsoft.com/en-us/windows/win32/api/securitybaseapi/nf-securitybaseapi-impersonateloggedonuser

<a id="s36"></a>
## S36 · Perfis AppArmor

The Linux Kernel documentation. *AppArmor*, propósito e relação com controles adicionais.

https://docs.kernel.org/admin-guide/LSM/apparmor.html

<a id="s37"></a>
## S37 · Política SELinux

The Linux Kernel documentation. *SELinux*, controle obrigatório e políticas. Nenhuma política foi desabilitada ou modificada.

https://docs.kernel.org/admin-guide/LSM/SELinux.html

<a id="s38"></a>
## S38 · Verificar não substitui a operação efetiva

Linux man-pages. *access(2)*, IDs reais/efetivos e intervalo entre checagem e uso. TOCTOU é introduzido conceitualmente, sem corrida executada.

https://man7.org/linux/man-pages/man2/access.2.html

<a id="s39"></a>
## S39 · Consulta de descritores por PowerShell

Microsoft Learn. *Get-Acl*, objetos retornados e LiteralPath. Vista documental identificada: PowerShell 7.5, não alegação de runtime executado.

https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.security/get-acl?view=powershell-7.5

<a id="s40"></a>
## S40 · Consulta do contexto Windows

Microsoft Learn. *whoami*, opções /user, /groups e /priv.

https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/whoami

<a id="s41"></a>
## S41 · Inspeção dos componentes de um caminho

util-linux. *namei(1)*, resolução de componentes e apresentação de modo/propriedade.

https://man7.org/linux/man-pages/man1/namei.1.html

<a id="s42"></a>
## S42 · Interfaces usadas no exemplo

Python documentation. *os*, identidades, chmod, listdir e interfaces de arquivos. A versão efetivamente executada fica no registro editorial.

https://docs.python.org/3/library/os.html

<a id="s43"></a>
## S43 · Recursos temporários próprios

Python documentation. *tempfile*, TemporaryDirectory e limpeza automática.

https://docs.python.org/3/library/tempfile.html

<a id="s44"></a>
## S44 · Criação de uma conta local

shadow-utils. *useradd(8)*, opções, padrões e diretório pessoal. Consultado para explicar responsabilidades; nenhuma conta foi criada.

https://man7.org/linux/man-pages/man8/useradd.8.html

<a id="s45"></a>
## S45 · Alteração de cadastro e grupos

shadow-utils. *usermod(8)*, opções -G/-a e limites de mudanças. Não foi executado contra uma conta do leitor.

https://man7.org/linux/man-pages/man8/usermod.8.html

<a id="s46"></a>
## S46 · Autorização da aplicação e menor privilégio

OWASP Cheat Sheet Series. *Authorization Cheat Sheet*, distinção de autenticação, menor privilégio e testes de autorização. A matriz Aurora é um exemplo próprio, não extraído da fonte.

https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html

<a id="s47"></a>
## S47 · Atributos de SIDs no token

Microsoft Learn. *SID Attributes in an Access Token*, grupos habilitados e atributos somente para negação.

https://learn.microsoft.com/en-us/windows/win32/secauthz/sid-attributes-in-an-access-token
