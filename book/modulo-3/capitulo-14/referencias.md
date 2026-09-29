# Capítulo 14 — Referências e limites de verificação

[Abertura](README.md) · [Respostas comentadas](solucoes.md)

**Consulta:** 29/09/2026. **Versão editorial:** DRAFT 0.1.

A pesquisa usa documentação primária do GNU, do projeto Linux man-pages, da Microsoft e do Python. O texto é autoral: os links fundamentam e delimitam os mecanismos, não substituem sua explicação.

A documentação PowerShell consultada está identificada como 7.5; detalhes sobre mudanças em 7.3 e 7.4 foram delimitados. Os exemplos não alegam compatibilidade universal com Windows PowerShell 5.1, cmd.exe ou qualquer interpretador chamado sh. A versão da documentação e a versão realmente executada são informações distintas.

Parte das páginas GNU apresentou demora no acesso direto. Nesses casos, foi consultado o conteúdo oficial indexado nas páginas indicadas. Isso não equivale a uma auditoria HTTP independente de disponibilidade de todas as referências.

A reprodução usa strings, argumentos, objetos sintéticos e arquivos temporários próprios. Não houve teste contra sistemas de terceiros nem alterações de permissões, contas, serviços ou execution policies. Ambiente, resultados e testes não executados ficam no [registro editorial](../../../editorial/reviews/capitulo-14.md).

<a id="s1"></a>

## S1 — Windows Terminal overview

**Microsoft.** [Windows Terminal overview](https://learn.microsoft.com/en-us/windows/terminal/).

**Recorte:** Terminal como aplicativo hospedeiro de diferentes shells; não é a linguagem de cada aba.

<a id="s2"></a>

## S2 — pty(7)

**Linux man-pages.** [pty(7)](https://man7.org/linux/man-pages/man7/pty.7.html).

**Recorte:** Par de pseudoterminais e comunicação com aplicações de terminal; não equipara terminal a shell.

<a id="s3"></a>

## S3 — Consoles

**Microsoft.** [Consoles](https://learn.microsoft.com/en-us/windows/console/consoles).

**Recorte:** Interfaces de console do Windows e separação entre aplicação e interação.

<a id="s4"></a>

## S4 — Bash Reference Manual — What is Bash? / What is a shell?

**GNU.** [Bash Reference Manual — What is Bash? / What is a shell?](https://www.gnu.org/software/bash/manual/html_node/What-is-a-shell_003f.html).

**Recorte:** Shell como interpretador e linguagem; contexto de Bourne-Again SHell. Manual consultado identifica edição 5.3; a execução local usou outra versão, registrada separadamente.

Complemento documental: [página relacionada 1](https://www.gnu.org/software/bash/manual/html_node/What-is-Bash_003f.html).

<a id="s5"></a>

## S5 — What is PowerShell?

**Microsoft.** [What is PowerShell?](https://learn.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.5).

**Recorte:** Linguagem, automação, cmdlets e uso multiplataforma. Não afirma equivalência total com Windows PowerShell 5.1.

<a id="s6"></a>

## S6 — cmd

**Microsoft.** [cmd](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/cmd).

**Recorte:** Identificação do processador de comandos cmd.exe; comandos do capítulo não são anunciados como compatíveis com ele.

<a id="s7"></a>

## S7 — Bash Builtin Commands

**GNU.** [Bash Builtin Commands](https://www.gnu.org/software/bash/manual/html_node/Bash-Builtins.html).

**Recorte:** printf, type e help; argumentos de formato e consulta dos comandos internos. Os resultados do printf também foram conferidos com dados próprios.

<a id="s8"></a>

## S8 — Bourne Shell Builtins

**GNU.** [Bourne Shell Builtins](https://www.gnu.org/software/bash/manual/html_node/Bourne-Shell-Builtins.html).

**Recorte:** cd, export, ponto/source e eval. O comportamento de contexto é complementado pelos testes de processo filho e source; não se afirma isolamento de segurança.

Complemento documental: [página relacionada 1](https://www.gnu.org/software/bash/manual/html_node/Command-Execution-Environment.html).

Complemento documental: [página relacionada 2](https://www.gnu.org/software/bash/manual/html_node/Environment.html).

<a id="s9"></a>

## S9 — about_Command_Precedence

**Microsoft.** [about_Command_Precedence](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_command_precedence?view=powershell-7.5).

**Recorte:** Resolução de comandos, aliases, funções, cmdlets e executáveis; Get-Command como instrumento de consulta.

<a id="s10"></a>

## S10 — Special Parameters

**GNU.** [Special Parameters](https://www.gnu.org/software/bash/manual/html_node/Special-Parameters.html).

**Recorte:** Quantidade de argumentos, parâmetros posicionais e expansão de "$@" mantendo elementos separados.

<a id="s11"></a>

## S11 — Word Splitting

**GNU.** [Word Splitting](https://www.gnu.org/software/bash/manual/html_node/Word-Splitting.html).

**Recorte:** Divisão de resultados de expansões sem aspas, condicionada ao contexto e ao IFS; não é uma regra sobre qualquer expressão da linguagem.

<a id="s12"></a>

## S12 — Single Quotes

**GNU.** [Single Quotes](https://www.gnu.org/software/bash/manual/html_node/Single-Quotes.html).

**Recorte:** Preservação literal do conteúdo entre aspas simples.

<a id="s13"></a>

## S13 — Double Quotes

**GNU.** [Double Quotes](https://www.gnu.org/software/bash/manual/html_node/Double-Quotes.html).

**Recorte:** Expansões que permanecem em aspas duplas e proteção das fronteiras de argumentos.

<a id="s14"></a>

## S14 — about_Quoting_Rules

**Microsoft.** [about_Quoting_Rules](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_quoting_rules?view=powershell-7.5).

**Recorte:** Strings literais e expansíveis; as regras são do PowerShell, não uma tradução das regras Bash.

<a id="s15"></a>

## S15 — Filename Expansion

**GNU.** [Filename Expansion](https://www.gnu.org/software/bash/manual/html_node/Filename-Expansion.html).

**Recorte:** Expansão de padrões de nomes e influência das opções do shell; exemplos usam uma pasta sintética com correspondências conhecidas.

<a id="s16"></a>

## S16 — Get-Content

**Microsoft.** [Get-Content](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-content?view=powershell-7.5).

**Recorte:** Distinção entre Path e LiteralPath; leitura de conteúdo e uso delimitado de ErrorAction.

<a id="s17"></a>

## S17 — Command Substitution

**GNU.** [Command Substitution](https://www.gnu.org/software/bash/manual/html_node/Command-Substitution.html).

**Recorte:** Substituição pela saída padrão e remoção das quebras de linha finais em $(...). Não é transporte binário arbitrário.

<a id="s18"></a>

## S18 — Command Search and Execution

**GNU.** [Command Search and Execution](https://www.gnu.org/software/bash/manual/html_node/Command-Search-and-Execution.html).

**Recorte:** Funções, builtins, PATH e cache de localização para nomes sem barra; aliases são tratados antes, durante a leitura da linguagem.

<a id="s19"></a>

## S19 — about_Operators

**Microsoft.** [about_Operators](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_operators?view=powershell-7.5).

**Recorte:** Operador de chamada & e dot-sourcing; & não reparsa uma string inteira como uma nova linha de comandos.

<a id="s20"></a>

## S20 — about_Parsing

**Microsoft.** [about_Parsing](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_parsing?view=powershell-7.5).

**Recorte:** Modos de interpretação e argumentos de comandos nativos; diferenças de passagem introduzidas no PowerShell 7.3 são delimitadas, não testadas em todas as versões.

<a id="s21"></a>

## S21 — stdin(3)

**Linux man-pages.** [stdin(3)](https://man7.org/linux/man-pages/man3/stdin.3.html).

**Recorte:** Entrada padrão, saída padrão e erro padrão; descritores convencionais 0, 1 e 2.

<a id="s22"></a>

## S22 — Redirections

**GNU.** [Redirections](https://www.gnu.org/software/bash/manual/html_node/Redirections.html).

**Recorte:** Ordem dos redirecionamentos, duplicação de descritores, truncamento e append; casos de ordem e falha usam arquivos temporários próprios.

<a id="s23"></a>

## S23 — Pipelines

**GNU.** [Pipelines](https://www.gnu.org/software/bash/manual/html_node/Pipelines.html).

**Recorte:** Conexão entre comandos e cálculo de status do pipeline Bash; não é uma transação nem a comprovação de resultado de negócio.

<a id="s24"></a>

## S24 — pipe(7)

**Linux man-pages.** [pipe(7)](https://man7.org/linux/man-pages/man7/pipe.7.html).

**Recorte:** Fluxo de bytes, ausência de fronteiras de mensagens e capacidade limitada; não generaliza toda IPC como pipe.

<a id="s25"></a>

## S25 — GNU grep manual — Matching Control

**GNU.** [GNU grep manual — Matching Control](https://www.gnu.org/software/grep/manual/grep.html#Matching-Control).

**Recorte:** -F como padrões de strings fixas; dados do exemplo têm formato conhecido.

<a id="s26"></a>

## S26 — about_Pipelines

**Microsoft.** [about_Pipelines](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_pipelines?view=powershell-7.5).

**Recorte:** Objetos no pipeline PowerShell e distinção da representação para exibição; comandos nativos têm fronteiras específicas.

<a id="s27"></a>

## S27 — Format-Table

**Microsoft.** [Format-Table](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/format-table?view=powershell-7.5).

**Recorte:** Formatação para apresentação; não usar aparência de tabela como substituta dos objetos de domínio.

<a id="s28"></a>

## S28 — about_Redirection

**Microsoft.** [about_Redirection](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_redirection?view=powershell-7.5).

**Recorte:** Fluxos próprios do PowerShell, redirecionamento e preservação de bytes em cenários nativos a partir da versão 7.4; não atribui essa garantia a toda cadeia mista.

<a id="s29"></a>

## S29 — Coreutils — Exit status

**GNU.** [Coreutils — Exit status](https://www.gnu.org/software/coreutils/manual/html_node/Exit-status.html).

**Recorte:** Convenção de resultado de comandos. A consulta imediata a $? no Bash também é coberta por S10 e por um teste do capítulo.

<a id="s30"></a>

## S30 — grep — Exit Status

**GNU.** [grep — Exit Status](https://www.gnu.org/software/grep/manual/html_node/Exit-Status.html).

**Recorte:** Zero, um, dois e ressalva de -q; ausência de correspondência é distinta de erro de coleta.

<a id="s31"></a>

## S31 — Lists of Commands

**GNU.** [Lists of Commands](https://www.gnu.org/software/bash/manual/html_node/Lists.html).

**Recorte:** Sequenciamento, &&, || e execução assíncrona; associatividade e limites da abreviação A && B || C.

<a id="s32"></a>

## S32 — The Set Builtin

**GNU.** [The Set Builtin](https://www.gnu.org/software/bash/manual/html_node/The-Set-Builtin.html).

**Recorte:** pipefail, exceções de errexit e rastreamento com -x; essas opções não são política completa de segurança ou rollback.

<a id="s33"></a>

## S33 — Bash Variables

**GNU.** [Bash Variables](https://www.gnu.org/software/bash/manual/html_node/Bash-Variables.html).

**Recorte:** PIPESTATUS e tempo de consulta; o teste copia status antes de executar outro comando.

<a id="s34"></a>

## S34 — about_Automatic_Variables

**Microsoft.** [about_Automatic_Variables](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_automatic_variables?view=powershell-7.5).

**Recorte:** Diferença entre $? e LASTEXITCODE; contexto, scripts e comandos nativos.

<a id="s35"></a>

## S35 — about_Try_Catch_Finally

**Microsoft.** [about_Try_Catch_Finally](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_try_catch_finally?view=powershell-7.5).

**Recorte:** Tratamento de erros terminantes; ErrorAction Stop na operação que precisa interromper o caminho.

<a id="s36"></a>

## S36 — about_Preference_Variables

**Microsoft.** [about_Preference_Variables](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_preference_variables?view=powershell-7.5).

**Recorte:** Preferências que influenciam erros e execução nativa; não presume um comportamento universal a partir de uma versão apenas.

<a id="s37"></a>

## S37 — Job Control Basics

**GNU.** [Job Control Basics](https://www.gnu.org/software/bash/manual/html_node/Job-Control-Basics.html).

**Recorte:** Jobs, primeiro e segundo plano, suspensão e interação com o terminal. O capítulo não alega reprodução de sinais em uma sessão interativa.

<a id="s38"></a>

## S38 — Shell Scripts

**GNU.** [Shell Scripts](https://www.gnu.org/software/bash/manual/html_node/Shell-Scripts.html).

**Recorte:** Arquivo lido como roteiro por Bash e identidade do interpretador. A escolha do interpretador não é provada pela extensão.

<a id="s39"></a>

## S39 — about_Pwsh

**Microsoft.** [about_Pwsh](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_pwsh?view=powershell-7.5).

**Recorte:** Invocação de pwsh e -NoProfile; a ausência de perfil não elimina variáveis de ambiente ou políticas do sistema.

<a id="s40"></a>

## S40 — Bash Startup Files

**GNU.** [Bash Startup Files](https://www.gnu.org/software/bash/manual/html_node/Bash-Startup-Files.html).

**Recorte:** Arquivos lidos em contextos de inicialização distintos; BASH_ENV no contexto não interativo.

<a id="s41"></a>

## S41 — about_Profiles

**Microsoft.** [about_Profiles](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_profiles?view=powershell-7.5).

**Recorte:** Scripts de perfil, escopos de usuário e host; dependências interativas precisam ser explícitas.

<a id="s42"></a>

## S42 — about_Environment_Variables

**Microsoft.** [about_Environment_Variables](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_environment_variables?view=powershell-7.5).

**Recorte:** Ambiente de processo e herança; não confunde variável PowerShell com variável de ambiente.

<a id="s43"></a>

## S43 — Bash Reference Manual — Conditional Constructs

**GNU.** [Bash Reference Manual — Conditional Constructs](https://www.gnu.org/software/bash/manual/html_node/Conditional-Constructs.html).

**Recorte:** if e case; páginas complementares cobrem for e avaliação aritmética usada no roteiro próprio. O roteiro é delimitado, executado e testado; não é um importador de produção.

Complemento documental: [página relacionada 1](https://www.gnu.org/software/bash/manual/html_node/Looping-Constructs.html).

Complemento documental: [página relacionada 2](https://www.gnu.org/software/bash/manual/html_node/Arithmetic-Expansion.html).

<a id="s44"></a>

## S44 — about_Comparison_Operators

**Microsoft.** [about_Comparison_Operators](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_comparison_operators?view=powershell-7.5).

**Recorte:** Uso explícito de -ceq para o contrato sensível a maiúsculas dos dois estados didáticos.

<a id="s45"></a>

## S45 — Invoke-Expression

**Microsoft.** [Invoke-Expression](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/invoke-expression?view=powershell-7.5).

**Recorte:** Interpretação de strings e preferência por chamadas sem reinterpretação quando suficientes; o capítulo não executa conteúdo remoto.

<a id="s46"></a>

## S46 — Bash Reference Manual — Arrays

**GNU.** [Bash Reference Manual — Arrays](https://www.gnu.org/s/bash/manual/bash.html#Arrays).

**Recorte:** Coleções de argumentos e expansão de "${argumentos[@]}"; o caso com espaço, padrão e valor vazio foi testado.

<a id="s47"></a>

## S47 — about_Splatting

**Microsoft.** [about_Splatting](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_splatting?view=powershell-7.5).

**Recorte:** Distribuição de valores para parâmetros; diferencia splatting de passar uma coleção como valor de um parâmetro.

<a id="s48"></a>

## S48 — subprocess — Security Considerations

**Python Software Foundation.** [subprocess — Security Considerations](https://docs.python.org/3/library/subprocess.html#security-considerations).

**Recorte:** Fronteira de shell, sequência de argumentos e particularidade de arquivos de lote no Windows; comparação documental, não execução de um programa de terceiros.

<a id="s49"></a>

## S49 — about_Execution_Policies

**Microsoft.** [about_Execution_Policies](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.5).

**Recorte:** Políticas de execução e limites como mecanismo de segurança; nenhuma política é alterada nos exemplos.
