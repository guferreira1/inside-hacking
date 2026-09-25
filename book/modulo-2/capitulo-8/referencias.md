# Capítulo 8 · Referências e limites da pesquisa

[← Capítulo](README.md) · [Bibliografia geral](../../bibliografia.md)

**Consulta:** 24/09/2026. **Versão:** DRAFT 0.1.

A narrativa, os programas e as comparações foram desenvolvidos para a obra. As fontes sustentam os mecanismos delimitados abaixo, não endossam o livro. O percurso nativo utiliza Linux, ELF e uma construção C com GCC; as observações desse ambiente não são generalizadas para todas as plataformas.

<a id="s1"></a>
## S1 · Etapas coordenadas pelo GCC

GNU Project. *Using the GNU Compiler Collection — Options Controlling the Kind of Output*.

https://gcc.gnu.org/onlinedocs/gcc/Overall-Options.html

Uso em 8.1 e 8.2: pré-processamento, compilação propriamente dita, montagem, ligação e opções `-E`, `-S`, `-c`, `-o`. Os comandos a partir de `.c` mostram interrupções diferentes do percurso; não se afirma que cada comando reutiliza o resultado do anterior. A existência de um driver que coordena etapas não elimina suas responsabilidades distintas.

<a id="s2"></a>
## S2 · Cabeçalhos e inclusão

GNU Project. *The C Preprocessor — Header Files*.

https://gcc.gnu.org/onlinedocs/cpp/Header-Files.html

Uso em 8.2: inclusão de conteúdo, declarações compartilhadas e distinção entre interface e implementação. Os arquivos `acervo.h`, `acervo.c` e `principal.c` são exemplos próprios. Não foram copiados cabeçalhos de terceiros para o repositório.

<a id="s3"></a>
## S3 · Ligação, símbolos e relocação

GNU Project. *GNU linker — Overview*, documentação publicada no Sourceware.

https://sourceware.org/binutils/docs/ld/Overview.html

Uso em 8.2: combinação de objetos e arquivos de biblioteca, resolução de referências e relocação. O comando do livro usa GCC como coordenador, não uma invocação manual incompleta de `ld`. A mensagem de erro do teste negativo é dependente das ferramentas; verificamos a referência à função ausente, sem prometer uma redação universal.

<a id="s4"></a>
## S4 · ELF, objetos, seções e segmentos

Linux man-pages project. *elf(5) — format of Executable and Linking Format (ELF) files*.

https://man7.org/linux/man-pages/man5/elf.5.html

Xinuos. *ELF Object File Format — Program Loading*, versão identificada na consulta como 4.3 DRAFT.

https://gabi.xinuos.com/elf/07-pheader.html

Uso em 8.2 e 8.3: tipos de arquivo, cabeçalhos, visões de ligação e carregamento, segmentos carregáveis e diferença entre tamanho no arquivo e tamanho em memória. O pequeno teste de cabeçalho não é um parser ELF completo. Aceita executável `ET_EXEC` ou `ET_DYN` no contexto da construção realizada, em vez de declarar que todo `ET_DYN` é necessariamente uma biblioteca ou um executável.

<a id="s5"></a>
## S5 · Formato Windows e convenção binária

Microsoft Learn. *PE Format* e *x64 calling convention*.

https://learn.microsoft.com/en-us/windows/win32/debug/pe-format

https://learn.microsoft.com/en-us/cpp/build/x64-calling-convention?view=msvc-170

Uso em 8.3: existência de formatos e regras binárias específicos, PE/COFF, parâmetros, retornos e registradores. Não foram executados programas Windows nem reproduzido um ABI completo. A convenção x64 da fonte é um exemplo de contrato, não a convenção universal de todo software x86-64.

<a id="s6"></a>
## S6 · Criação e substituição de processos no Linux

Linux man-pages project. *fork(2)* e *execve(2)*.

https://man7.org/linux/man-pages/man2/fork.2.html

https://man7.org/linux/man-pages/man2/execve.2.html

Uso em 8.3 e 8.5: processo filho, substituição de imagem, preservação do PID em `execve` bem-sucedido, tratamento de executável ELF e atributos de execução. O capítulo diferencia responsabilidades sem exigir que todos os lançadores usem exatamente `fork` seguido de `execve`. Não foi instrumentado o kernel nem testado o tratamento de todas as credenciais, erros e formatos.

<a id="s7"></a>
## S7 · Carregamento dinâmico

Linux man-pages project. *ld.so(8) — dynamic linker/loader*.

https://man7.org/linux/man-pages/man8/ld.so.8.html

Uso em 8.2, 8.3 e 8.5: localização e preparação de objetos compartilhados, dependências e contexto do carregamento. A ordem detalhada de busca, modos especiais de execução e técnicas de abuso não são ensinados nesta introdução. Não usamos a palavra biblioteca como promessa de isolamento do código carregado.

<a id="s8"></a>
## S8 · Preparação antes de main

Linux Foundation. *Linux Standard Base 4.1 — __libc_start_main*.

https://refspecs.linuxfoundation.org/LSB_4.1.0/LSB-Core-generic/LSB-Core-generic/baselib---libc-start-main-.html

Uso em 8.2 e 8.3: exemplo documentado de inicialização do ambiente, chamada de `main` e tratamento do retorno. É uma referência identificada de ABI, não descrição exaustiva de toda biblioteca C contemporânea nem regra de inicialização de todas as linguagens. O nome de entrada no nível do fonte não é confundido com o primeiro estágio executado pela plataforma.

<a id="s9"></a>
## S9 · Serviços do kernel

Linux man-pages project. *syscalls(2) — Linux system calls*.

https://man7.org/linux/man-pages/man2/syscalls.2.html

Uso em 8.3: distinção entre chamadas de biblioteca e interface de serviços do kernel. O capítulo não afirma que cada `printf` corresponda a exatamente uma chamada de sistema nem reproduz um rastreamento completo da saída.

<a id="s10"></a>
## S10 · CPython, compilação e cache

Python Software Foundation. *Glossary*, verbete bytecode; *The Python Tutorial*, seção 6.1.3, Compiled Python files; *Built-in Functions*, função `compile`.

https://docs.python.org/3/glossary.html#term-bytecode

https://docs.python.org/3/tutorial/modules.html#compiled-python-files

https://docs.python.org/3/builtins/functions.html#compile

Uso em 8.4: bytecode, objeto de código, distinção entre compilar e executar, cache de módulos e condição diferente do script executado diretamente. A representação interna não é apresentada como formato estável entre versões. O texto não depende de nomes ou números de instruções de bytecode. As páginas consultadas e o interpretador utilizado nos testes não precisam ter a mesma versão; o ambiente de execução está identificado abaixo.

<a id="s11"></a>
## S11 · Máquina virtual de linguagem e implementação

Oracle. *The Java Virtual Machine Specification, Java SE 25 Edition*, capítulo 2, especialmente seções 2.1 e 2.13.

https://docs.oracle.com/javase/specs/jvms/se25/html/jvms-2.html

Uso em 8.4: máquina abstrata, formato `class`, semântica especificada e liberdade de implementação, inclusive tradução para código nativo em carregamento ou execução. A edição consultada está identificada, sem alegar que seja a mais recente. Nenhuma JVM foi executada ou medida; não se atribui JIT a toda execução de todo método.

<a id="s12"></a>
## S12 · Ambiente e resolução de caminhos

Linux man-pages project. *environ(7)* e *path_resolution(7)*.

https://man7.org/linux/man-pages/man7/environ.7.html

https://man7.org/linux/man-pages/man7/path_resolution.7.html

Uso em 8.5: ambiente por processo, caminhos relativos e diretório corrente. A explicação ressalva operações com bases explícitas. O teste de contexto utiliza um diretório temporário e uma variável criada para o exemplo; não registra o ambiente completo, segredos ou arquivos pessoais.

<a id="s13"></a>
## S13 · Argumentos, saída e término

GNU Project. *The GNU C Library — Program Arguments* e *Exit Status*, documentação publicada no Sourceware.

https://sourceware.org/glibc/manual/latest/html_node/Program-Arguments.html

https://sourceware.org/glibc/manual/latest/html_node/Exit-Status.html

Linux man-pages project. *stdin(3)* e *printf(3)*.

https://man7.org/linux/man-pages/man3/stdin.3.html

https://man7.org/linux/man-pages/man3/printf.3.html

Uso em 8.2 e 8.5: interface de `main`, formato `%d`, quebra de linha, fluxos padrão, descritores e diferença entre saída textual e estado de término. Não se afirma que qualquer programa com retorno zero esteja correto ou seguro, nem que os códigos tenham significado idêntico em todos os programas. Nosso exemplo mínimo não implementa tratamento completo de erros de E/S.

<a id="s14"></a>
## S14 · Tradução e otimização

GNU Project. *Using the GNU Compiler Collection — Options That Control Optimization*.

https://gcc.gnu.org/onlinedocs/gcc/Optimize-Options.html

Uso em 8.1: existência de transformações de otimização e dependência do alvo/configuração. A expressão constante ilustra uma possibilidade de simplificação. Não fixamos a sequência de instruções gerada nem afirmamos uma correspondência entre linhas e instruções ou um ganho de desempenho medido.

## Conferência executada

Os [testes do capítulo](../../../scripts/tests/test_chapter8_examples.py) foram executados no ambiente de edição em Linux x86-64, Debian GNU/Linux 13, GCC 14.2.0 e Python 3.13.5. Os nove testes passaram: seis sobre artefatos e execução C e três sobre compilação/contexto Python. Os arquivos foram construídos em diretórios temporários, sem rede ou alvos externos.

Foram conferidos pré-processamento, saída assembly, tipos de objeto/executável, falha de ligação sem a definição, texto e código de saída, edição de fonte seguida de reconstrução, preservação do binário ao alterar o nome e exemplos limitados de contexto. O teste de namespaces Python não é demonstração de isolamento de processos.

O workflow do repositório executa novamente a suíte ao processar a entrega. Resultado e eventuais saltos de testes devem ser lidos nos logs da execução correspondente; a mera presença dos testes não comprova que rodaram. A parte C exige Linux e GCC e declara essa dependência.

Não houve análise de malware, exploração, teste de Windows/JVM ou revisão técnica independente. As evidências verificam exemplos delimitados, não todas as afirmações do capítulo. Consulte o [registro editorial](../../../editorial/reviews/capitulo-8.md).
