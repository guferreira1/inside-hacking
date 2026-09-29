# Capítulo 13 — Referências e limites de verificação

[Abertura](README.md) · [Respostas comentadas](solucoes.md)

**Consulta:** 29/09/2026. **Versão editorial:** VALIDATED 1.0 — fechamento interno em 29/09/2026; revisão independente pendente.

O capítulo foi escrito em português com explicações autorais. As fontes abaixo são documentação primária da Microsoft, usada para verificar mecanismos e delimitar afirmações, não para reproduzir trechos. Os identificadores S1–S44 permitem voltar da explicação ao material que a sustenta.

Não foi executado laboratório em Windows nesta entrega. Os caminhos, contas e componentes da Aurora são fictícios; as previsões são raciocínios baseados nas regras documentadas. A revisão local de Markdown e navegação é uma verificação editorial, não comprovação experimental de kernel, UAC, Registro ou serviços.

As páginas oficiais podem conter exemplos e observações de versões antigas. O recorte de cada referência, explicitado abaixo, é o que foi utilizado. Datas de atualização de páginas não foram confundidas com datas de introdução de mecanismos. A pesquisa consultou conteúdo, não realizou uma auditoria HTTP independente de todos os links.

<a id="s1"></a>

## S1 — User mode and kernel mode

**Microsoft Learn.** [User mode and kernel mode](https://learn.microsoft.com/en-us/windows-hardware/drivers/gettingstarted/user-mode-and-kernel-mode).

**Uso no capítulo:** 13.1. Separação de modos; aplicação e drivers. Não implica independência absoluta entre aplicações ou ausência de APIs autorizadas para comunicação.

<a id="s2"></a>

## S2 — Windows Kernel-Mode Executive Support Library

**Microsoft Learn.** [Windows Kernel-Mode Executive Support Library](https://learn.microsoft.com/en-us/windows-hardware/drivers/kernel/windows-kernel-mode-executive-support-library).

**Uso no capítulo:** 13.1. Recorte do termo Executive e suas responsabilidades; não é um catálogo exaustivo de componentes.

<a id="s3"></a>

## S3 — Processes and Threads

**Microsoft Learn.** [Processes and Threads](https://learn.microsoft.com/en-us/windows/win32/procthread/processes-and-threads).

**Uso no capítulo:** 13.1 e 13.6. Processos, threads e unidade de alocação de tempo de processador.

<a id="s4"></a>

## S4 — About Processes and Threads

**Microsoft Learn.** [About Processes and Threads](https://learn.microsoft.com/en-us/windows/win32/procthread/about-processes-and-threads).

**Uso no capítulo:** 13.1. Recursos, espaço de endereços e identificação de uma execução.

<a id="s5"></a>

## S5 — Windows kernel-mode object manager

**Microsoft Learn.** [Windows kernel-mode object manager](https://learn.microsoft.com/en-us/windows-hardware/drivers/kernel/windows-kernel-mode-object-manager).

**Uso no capítulo:** 13.1. Representação e gerenciamento de objetos; não confundir com orientação a objetos de uma linguagem.

<a id="s6"></a>

## S6 — Object Handles

**Microsoft Learn.** [Object Handles](https://learn.microsoft.com/en-us/windows-hardware/drivers/kernel/object-handles).

**Uso no capítulo:** 13.1. Handles opacos e ciclo de uso. O texto não reproduz APIs de kernel ou procedimentos de desenvolvimento de drivers.

<a id="s7"></a>

## S7 — Naming a Volume

**Microsoft Learn.** [Naming a Volume](https://learn.microsoft.com/en-us/windows/win32/fileio/naming-a-volume).

**Uso no capítulo:** 13.2. Letras, caminhos de montagem e nomes de volume.

<a id="s8"></a>

## S8 — NTFS overview

**Microsoft Learn.** [NTFS overview](https://learn.microsoft.com/en-us/windows-server/storage/file-server/ntfs-overview).

**Uso no capítulo:** 13.2. Organização, metadados e segurança do NTFS. Não usamos limites máximos de capacidade nem alegamos equivalência entre recuperação de consistência e backup.

<a id="s9"></a>

## S9 — Naming Files, Paths, and Namespaces

**Microsoft Learn.** [Naming Files, Paths, and Namespaces](https://learn.microsoft.com/en-us/windows/win32/fileio/naming-a-file).

**Uso no capítulo:** 13.2. Separadores, nomes UNC e dependência de contexto. O capítulo não ensina toda a gramática de namespaces.

<a id="s10"></a>

## S10 — File path formats on Windows systems

**Microsoft Learn.** [File path formats on Windows systems](https://learn.microsoft.com/en-us/dotnet/standard/io/file-path-formats).

**Uso no capítulo:** 13.2. Diferença entre caminho totalmente qualificado, relativo à unidade e relativo à raiz da unidade corrente.

<a id="s11"></a>

## S11 — Services and Redirected Drives

**Microsoft Learn.** [Services and Redirected Drives](https://learn.microsoft.com/en-us/windows/win32/services/services-and-redirected-drives).

**Uso no capítulo:** 13.2 e 13.6. Mapeamentos de rede e sessões de logon; distinção entre nome explícito e autorização. Cenário Aurora é fictício.

<a id="s12"></a>

## S12 — KNOWNFOLDERID

**Microsoft Learn.** [KNOWNFOLDERID](https://learn.microsoft.com/en-us/windows/win32/shell/knownfolderid).

**Uso no capítulo:** 13.2. Papéis de pastas conhecidas, incluindo Program Files, ProgramData e LocalAppData; caminhos concretos não são universalizados.

<a id="s13"></a>

## S13 — Registry Hives

**Microsoft Learn.** [Registry Hives](https://learn.microsoft.com/en-us/windows/win32/sysinfo/registry-hives).

**Uso no capítulo:** 13.2 e 13.5. Hives e configurações de perfil. Não usamos tabelas de caminhos de versões antigas como descrição de toda instalação atual.

<a id="s14"></a>

## S14 — PE Format

**Microsoft Learn.** [PE Format](https://learn.microsoft.com/en-us/windows/win32/debug/pe-format).

**Uso no capítulo:** 13.3. Cabeçalhos, arquitetura, seções e endereços relativos de imagem. Nenhum binário Windows foi analisado nesta entrega.

<a id="s15"></a>

## S15 — About Dynamic-Link Libraries

**Microsoft Learn.** [About Dynamic-Link Libraries](https://learn.microsoft.com/en-us/windows/win32/dlls/about-dynamic-link-libraries).

**Uso no capítulo:** 13.3. Bibliotecas dinâmicas, funções e dados no contexto dos processos.

<a id="s16"></a>

## S16 — Dynamic-link library search order

**Microsoft Learn.** [Dynamic-link library search order](https://learn.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-search-order).

**Uso no capítulo:** 13.3. Dependência das regras de busca em relação ao modo de carregamento e tipo de aplicação. Não reproduzimos uma ordem supostamente universal.

<a id="s17"></a>

## S17 — Managed Execution Process

**Microsoft Learn.** [Managed Execution Process](https://learn.microsoft.com/en-us/dotnet/standard/managed-execution-process).

**Uso no capítulo:** 13.3. Execução gerenciada e papel do runtime. Não fazemos da compilação JIT uma regra universal de todas as formas de implantação .NET.

<a id="s18"></a>

## S18 — How User Account Control works

**Microsoft Learn.** [How User Account Control works](https://learn.microsoft.com/en-us/windows/security/application-security/application-control/user-account-control/how-it-works).

**Uso no capítulo:** 13.1 e 13.4. Modelo tradicional de UAC, tokens limitados e elevação; sujeito a conta e política.

<a id="s19"></a>

## S19 — File System Redirector

**Microsoft Learn.** [File System Redirector](https://learn.microsoft.com/en-us/windows/win32/winprog64/file-system-redirector).

**Uso no capítulo:** 13.3. WOW64 e diretórios no recorte Windows x64; regras e exceções preservadas.

<a id="s20"></a>

## S20 — Digital Signatures

**Microsoft Learn.** [Digital Signatures](https://learn.microsoft.com/en-us/windows-hardware/drivers/install/digital-signatures).

**Uso no capítulo:** 13.3. Autenticidade de signatário e integridade sob política de confiança. Não reproduzimos a simplificação criptográfica de assinatura como mera cifragem de hash.

<a id="s21"></a>

## S21 — Importance of Protecting Authenticode Signing Keys

**Microsoft Learn.** [Importance of Protecting Authenticode Signing Keys](https://learn.microsoft.com/en-us/windows-hardware/drivers/install/importance-of-protecting-authenticode-signing-keys).

**Uso no capítulo:** 13.3. Limite de confiança: uma assinatura não comprova comportamento benigno.

<a id="s22"></a>

## S22 — Security Identifiers

**Microsoft Learn.** [Security Identifiers](https://learn.microsoft.com/en-us/windows/win32/secauthz/security-identifiers).

**Uso no capítulo:** 13.4. Identidades por SID e diferença em relação ao nome exibido.

<a id="s23"></a>

## S23 — Local accounts

**Microsoft Learn.** [Local accounts](https://learn.microsoft.com/en-us/windows/security/identity-protection/access-control/local-accounts).

**Uso no capítulo:** 13.4. Recorte de contas locais; não é um aprofundamento em domínio ou Active Directory.

<a id="s24"></a>

## S24 — Access tokens

**Microsoft Learn.** [Access tokens](https://learn.microsoft.com/en-us/windows/win32/secauthz/access-tokens).

**Uso no capítulo:** 13.4. Token primário, impersonação, grupos e privilégios. Não reduzimos autenticação a senha, pois o Windows admite outros mecanismos.

<a id="s25"></a>

## S25 — Access control model

**Microsoft Learn.** [Access control model](https://learn.microsoft.com/en-us/windows/win32/secauthz/access-control-model).

**Uso no capítulo:** 13.4. Relação entre processos, objetos protegidos e acesso solicitado.

<a id="s26"></a>

## S26 — DACLs and ACEs

**Microsoft Learn.** [DACLs and ACEs](https://learn.microsoft.com/en-us/windows/win32/secauthz/dacls-and-aces).

**Uso no capítulo:** 13.4. Entradas e ordem na interpretação das listas; sem ensinar um algoritmo incompleto como se fosse universal.

<a id="s27"></a>

## S27 — Null DACLs and Empty DACLs

**Microsoft Learn.** [Null DACLs and Empty DACLs](https://learn.microsoft.com/en-us/windows/win32/secauthz/null-dacls-and-empty-dacls).

**Uso no capítulo:** 13.4. Distinção limitada à DACL; outros controles não desaparecem.

<a id="s28"></a>

## S28 — Privileges

**Microsoft Learn.** [Privileges](https://learn.microsoft.com/en-us/windows/win32/secauthz/privileges).

**Uso no capítulo:** 13.4. Privilégios e direitos de objetos; presença e habilitação no token.

<a id="s29"></a>

## S29 — Mandatory Integrity Control mechanism

**Microsoft Learn.** [Mandatory Integrity Control mechanism](https://learn.microsoft.com/en-us/windows/win32/secauthz/mandatory-integrity-control).

**Uso no capítulo:** 13.4. Níveis de integridade e controles adicionais aos discricionários.

<a id="s30"></a>

## S30 — Administrator protection

**Microsoft Learn.** [Administrator protection](https://learn.microsoft.com/en-us/windows/security/application-security/application-control/administrator-protection/).

**Uso no capítulo:** 13.4. Menção delimitada à conta gerenciada e separação de perfil. Não fixamos disponibilidade por edição, KB ou estado de implantação.

<a id="s31"></a>

## S31 — Structure of the Registry

**Microsoft Learn.** [Structure of the Registry](https://learn.microsoft.com/en-us/windows/win32/sysinfo/structure-of-the-registry).

**Uso no capítulo:** 13.5. Chaves, subchaves, valores e estrutura hierárquica.

<a id="s32"></a>

## S32 — Registry value types

**Microsoft Learn.** [Registry value types](https://learn.microsoft.com/en-us/windows/win32/sysinfo/registry-value-types).

**Uso no capítulo:** 13.5. REG_SZ, REG_DWORD, REG_BINARY e REG_EXPAND_SZ.

<a id="s33"></a>

## S33 — Predefined Keys

**Microsoft Learn.** [Predefined Keys](https://learn.microsoft.com/en-us/windows/win32/sysinfo/predefined-keys).

**Uso no capítulo:** 13.5. HKLM, HKCU e HKU; mapeamento por contexto e cautela com serviços e impersonação.

<a id="s34"></a>

## S34 — Registry Redirector

**Microsoft Learn.** [Registry Redirector](https://learn.microsoft.com/en-us/windows/win32/winprog64/registry-redirector).

**Uso no capítulo:** 13.5. Visões lógicas de partes do Registro; não significa duplicação integral.

<a id="s35"></a>

## S35 — Environment Variables

**Microsoft Learn.** [Environment Variables](https://learn.microsoft.com/en-us/windows/win32/procthread/environment-variables).

**Uso no capítulo:** 13.5. Ambiente por processo e herança ou bloco explícito na criação.

<a id="s36"></a>

## S36 — Windows startup issues troubleshooting

**Microsoft Learn.** [Windows startup issues troubleshooting](https://learn.microsoft.com/en-us/troubleshoot/windows-client/performance/windows-boot-issues-troubleshooting).

**Uso no capítulo:** 13.6. Etapas da inicialização e diferença entre UEFI e cenário legado; sem instruções de reparo de boot.

<a id="s37"></a>

## S37 — Service control manager

**Microsoft Learn.** [Service control manager](https://learn.microsoft.com/en-us/windows/win32/services/service-control-manager).

**Uso no capítulo:** 13.6. Gerenciamento, base de serviços e estado.

<a id="s38"></a>

## S38 — Service Programs

**Microsoft Learn.** [Service Programs](https://learn.microsoft.com/en-us/windows/win32/services/service-programs).

**Uso no capítulo:** 13.6. Integração com o SCM; processo próprio ou compartilhado.

<a id="s39"></a>

## S39 — Service User Accounts

**Microsoft Learn.** [Service User Accounts](https://learn.microsoft.com/en-us/windows/win32/services/service-user-accounts).

**Uso no capítulo:** 13.6. Escolha de identidade de execução de um serviço.

<a id="s40"></a>

## S40 — LocalSystem Account

**Microsoft Learn.** [LocalSystem Account](https://learn.microsoft.com/en-us/windows/win32/services/localsystem-account).

**Uso no capítulo:** 13.6. Poder local e contexto de rede; não é autorização universal remota.

<a id="s41"></a>

## S41 — Interactive Services

**Microsoft Learn.** [Interactive Services](https://learn.microsoft.com/en-us/windows/win32/services/interactive-services).

**Uso no capítulo:** 13.6. Separação dos serviços e interação do usuário. Não recomendamos técnicas legadas para reativar interação com a sessão 0.

<a id="s42"></a>

## S42 — Task Scheduler for developers

**Microsoft Learn.** [Task Scheduler for developers](https://learn.microsoft.com/en-us/windows/win32/taskschd/task-scheduler-start-page).

**Uso no capítulo:** 13.6. Tarefas, ações e gatilhos; diferente do escalonamento de threads.

<a id="s43"></a>

## S43 — Windows Event Log

**Microsoft Learn.** [Windows Event Log](https://learn.microsoft.com/en-us/windows/win32/wes/windows-event-log).

**Uso no capítulo:** 13.6. Publicação e consumo de eventos; ausência de registro não é evidência universal de ausência de atividade.

<a id="s44"></a>

## S44 — SystemPropertiesType Complex Type

**Microsoft Learn.** [SystemPropertiesType Complex Type](https://learn.microsoft.com/en-us/windows/win32/wes/eventschema-systempropertiestype-complextype).

**Uso no capítulo:** 13.6. Provedor, canal, tempo, EventID e EventRecordID; os campos disponíveis variam conforme o evento.

## Observação sobre documentação em evolução

Em Administrator protection, resultados de diferentes versões linguísticas apresentavam informações de implantação diferentes. O capítulo utiliza apenas o mecanismo descrito na página em inglês consultada e não afirma que o recurso esteja habilitado, presente ou disponível em todas as instalações. O leitor deve verificar a documentação aplicável ao ambiente que for analisar.

## O que não foi alegado

Não houve acesso a serviços da Aurora, montagem de unidades, alteração de permissões, leitura de credenciais, edição do Registro, análise de binários de terceiros ou testes de exploração. Não foi produzida uma “saída real” de Windows para ilustrar um experimento não realizado.
