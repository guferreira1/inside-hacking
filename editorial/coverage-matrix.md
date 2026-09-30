# Matriz de cobertura

**Status:** cobertura inicial dos capítulos disponíveis; atualização em 29/09/2026.

[Editorial](README.md) · [Sumário mestre](master-outline.md) · [Estado editorial](publication-status.md)

A matriz relaciona conteúdos efetivamente desenvolvidos, sua profundidade e o que continua em aberto. Uma referência a uma técnica em uma introdução não significa que seu mecanismo completo ou um laboratório já foi entregue. O sumário mestre mantém o planejamento amplo; esta matriz começa pela cobertura concreta dos módulos em produção.

## Campos de acompanhamento

| Campo | Finalidade |
| --- | --- |
| ID | Identificador estável do grupo de cobertura. |
| Tema e categoria | Fundamento, vulnerabilidade, técnica, ferramenta, defesa etc. |
| Pré-requisitos | Conhecimentos necessários, conforme o capítulo. |
| Teoria | Onde o mecanismo é explicado. |
| Aplicação | Onde é demonstrado, exercitado ou reproduzido, quando aplicável. |
| Defesa | Onde prevenção, detecção ou mitigação são discutidas. |
| Profundidade | Introdução, desenvolvimento intermediário ou aprofundamento. |
| Fontes e validação | Referências e registro editorial; não é certificação do leitor. |
| Gap | Pendência ou conteúdo ainda não desenvolvido. |

## Módulo I — Hacking, segurança e método

| ID | Tema / teoria disponível | Aplicação e defesa | Profundidade / fonte e limite |
| --- | --- | --- | --- |
| M01-01 | [Significado de hacking e ferramentas](../book/modulo-1/capitulo-1/README.md) | Exemplos conceituais e perguntas; distinção entre capacidade e permissão. | Introdução. Revisão factual própria ainda aberta no [controle](publication-status.md). Nenhuma prática de ferramentas entregue. |
| M01-02 | [História da cultura hacker](../book/modulo-1/capitulo-2/README.md) | Telefonia histórica, incidentes e resposta coordenada explicados, não reproduzidos. | Introdução; [fontes R1–R14](../book/modulo-1/capitulo-2/referencias.md). Revisão interna encerrada, revisão histórica independente pendente. |
| M01-03 | [Autorização, escopo e evidências](../book/modulo-1/capitulo-3/README.md) | Cenário Aurora, decisões e soluções; limites de coleta e divulgação. | Introdução operacional e jurídica; [fontes](../book/modulo-1/capitulo-3/referencias.md). Revisão jurídica especializada pendente. |
| M01-04 | [Raciocínio investigativo](../book/modulo-1/capitulo-4/README.md) | Comparações fictícias, hipóteses concorrentes, resultado negativo, questões e soluções. | Desenvolvimento conceitual; [fontes S1–S9](../book/modulo-1/capitulo-4/referencias.md). Sem laboratório executável ou medição. |
| M01-05 | [Ativos, ameaças, exploração e risco](../book/modulo-1/capitulo-5/README.md) | Cenários de autorização e exposição; controle de causa, consequências e limites. | Fundamentos; [fontes S1–S12](../book/modulo-1/capitulo-5/referencias.md). Não há cálculo CVSS, medição de probabilidade ou exploração real. |

## Módulo II — Computadores por dentro

Pré-requisito editorial: leitura introdutória e disposição para acompanhar exemplos; não é exigida programação prévia. O capítulo 7 utiliza as representações e unidades construídas no 6. O capítulo 8 explica o código mínimo de seu percurso. O 9 aprofunda os contextos de memória e execução. O 10 acompanha a representação de estruturas em arquivos e sua interpretação por outro componente.

| ID | Tema / teoria disponível | Aplicação e defesa | Profundidade / fonte e limite |
| --- | --- | --- | --- |
| M02-01 | [Bits, bases e unidades](../book/modulo-2/capitulo-6/README.md) | Contas explicadas e testes de conversões. Distingue capacidade de imprevisibilidade, largura de interpretação. | Fundamentos; [fontes S1–S8](../book/modulo-2/capitulo-6/referencias.md). Revisão interna 1.0. Não ensina circuitos completos ou segurança de chaves. |
| M02-02 | [Texto e interpretação](../book/modulo-2/capitulo-6/6.4-texto-e-interpretacao.md) | ASCII, UTF-8, pontos de código, agrupamentos e cortes; exemplos conferidos. | Introdução a codificações. Não implementa decodificador, normalização completa ou parser seguro. |
| M02-03 | [CPU e componentes](../book/modulo-2/capitulo-7/README.md) | Percurso didático do editor, ciclo de instrução, clock, núcleo, ISA e microarquitetura. | Introdução funcional; [fontes S1–S16](../book/modulo-2/capitulo-7/referencias.md). Revisão interna 1.0; não benchmark nem projeto de CPU. |
| M02-04 | [Hierarquia de memória](../book/modulo-2/capitulo-7/7.3-memoria-e-cache.md) | RAM, cache, endereço/conteúdo e média hipotética; separa MMU e representação física. | Fundamentos. Memória virtual, processos e permissões aprofundados conceitualmente no [capítulo 9](../book/modulo-2/capitulo-9/README.md). |
| M02-05 | [Armazenamento e dispositivos](../book/modulo-2/capitulo-7/7.4-armazenamento-e-persistencia.md) | Persistência, interfaces e controles de escrita; [DMA e firmware](../book/modulo-2/capitulo-7/7.5-dispositivos-e-firmware.md). | Introdução. Sem ensaio de energia, driver, configuração de firmware ou exploração de hardware. |
| M02-06 | [Fonte, construção e ligação](../book/modulo-2/capitulo-8/8.2-compilacao-e-ligacao.md) | Três arquivos C e testes de estágios, definição ausente e reconstrução. | Fundamentos, revisão interna 1.0; [fontes S1–S14](../book/modulo-2/capitulo-8/referencias.md). GCC/Linux como percurso concreto, não todas as toolchains. |
| M02-07 | [Carregamento e processo](../book/modulo-2/capitulo-8/8.3-carregamento-e-processos.md) | ELF, ABI, imagem, PID, fork/exec e preparação antes de main. | Introdução. Testes de artefatos não instrumentam todo carregamento nem comprovam isolamento do sistema. Memória aprofundada no capítulo 9. |
| M02-08 | [Runtimes](../book/modulo-2/capitulo-8/8.4-interpretadores-e-runtimes.md) e [contexto](../book/modulo-2/capitulo-8/8.5-contexto-e-diagnostico.md) | CPython, bytecode, JIT, argumentos, ambiente e saída. Testes próprios de contexto Python. | Introdução. JVM e Windows pesquisados por documentação, não executados; nenhum abuso de carregamento ou exploração foi realizado. |
| M02-09 | [Processos e threads](../book/modulo-2/capitulo-9/9.1-processos-threads-e-contextos.md) | Espaços, compartilhamento, escalonamento e distinção de modo/contexto. | Desenvolvimento conceitual, revisão interna 1.0; [fontes S1–S18](../book/modulo-2/capitulo-9/referencias.md). Sem medição de escalonador ou modo kernel. |
| M02-10 | [Paginação e tradução](../book/modulo-2/capitulo-9/9.2-enderecos-paginas-e-traducao.md) | Modelos calculáveis de páginas, quadros, offsets, limites e TLB. | Fundamentos. Não são tabelas físicas reais nem um simulador completo de MMU. |
| M02-11 | [Regiões, objetos e duração](../book/modulo-2/capitulo-9/9.3-regioes-objetos-e-tempo-de-vida.md) | Pilha, heap, alocação e limites; distingue permissão de página e validade de objeto. | Introdução a falhas espaciais/temporais. Sem acesso inválido real ou desenvolvimento de exploit. |
| M02-12 | [Residência e compartilhamento](../book/modulo-2/capitulo-9/9.4-paginacao-copias-e-medidas.md) | COW, faults, swap, RSS/PSS e exemplo próprio de visibilidade de mapeamentos. | Desenvolvimento conceitual; execução Linux delimitada, sem medir quadros físicos, RSS/PSS ou OOM. |
| M02-13 | [Proteções e concorrência](../book/modulo-2/capitulo-9/9.5-protecao-concorrencia-e-diagnostico.md) | DEP/NX, ASLR, camadas de autorização e intercalamento do contador. | Introdução. Modelo sequencial, não data race executada; não desabilita proteções nem certifica sua eficácia. |
| M02-14 | [Nomes, arquivos e conteúdo](../book/modulo-2/capitulo-10/10.1-arquivos-nomes-e-leitura.md) | Hard links, descritores, metadados e leitura; exemplo temporário próprio. | Fundamentos, revisão interna 1.0; [fontes S1–S18](../book/modulo-2/capitulo-10/referencias.md). Sem recuperação forense ou leitura de arquivos pessoais. |
| M02-15 | [Formatos e campos](../book/modulo-2/capitulo-10/10.2-formatos-e-estrutura.md) | AUR v1, comprimentos e endian; distingue extensão, tipo declarado e assinatura. | Formato autoral didático. PNG apenas introdutório; não é implementação de leitor PNG. |
| M02-16 | [Transformações](../book/modulo-2/capitulo-10/10.3-codificacoes-e-transformacoes.md) | UTF-8, Base64, escape, camadas percentuais e normalização. | Exemplos pequenos executados. Não implementa todas as codificações nem certifica todo Unicode da referência. |
| M02-17 | [Serialização](../book/modulo-2/capitulo-10/10.4-serializacao-e-contratos.md) e [parsing](../book/modulo-2/capitulo-10/10.5-parsing-e-validacao.md) | Codec AUR/JSON, esquema restrito, duplicatas, tipos e testes positivos/negativos. | Fundamentos aplicados, não importador de produção. XML/YAML/Protobuf apenas por documentação; aquisição precisa de orçamento próprio. |
| M02-18 | [Integridade e contexto posterior](../book/modulo-2/capitulo-10/10.6-integridade-e-fronteiras.md) | Compressão pequena, CRC, hash, JCS e capacidades de desserialização. | Introdução. Não executa pickle, não implementa JCS nem constrói bomba de descompressão ou bypass de upload. |

## Módulo III — Sistemas operacionais

Pré-requisitos: representações, recursos, processos e arquivos apresentados nos capítulos 6 a 10. O capítulo 11 conecta essas peças às responsabilidades do sistema operacional, sem exigir administração prévia ou execução de comandos. Seu ciclo interno da versão 1.0 foi concluído; [fontes S1–S14](../book/modulo-3/capitulo-11/referencias.md) e [registro da entrega](reviews/capitulo-11.md) delimitam a validação.

| ID | Tema / teoria disponível | Aplicação e defesa | Profundidade / fonte e limite |
| --- | --- | --- | --- |
| M03-01 | [Abstrações e responsabilidades](../book/modulo-3/capitulo-11/11.1-abstracoes-e-responsabilidades.md) | VFS, mecanismo/política, kernel, espaço de usuário e composição da instalação. | Introdução funcional. Microkernel é comparação documental, não sistema instalado ou garantia universal. |
| M03-02 | [Interfaces e chamadas de sistema](../book/modulo-3/capitulo-11/11.2-interfaces-e-chamadas-de-sistema.md) | Exemplo Linux próprio de leitura, fim de arquivo, EBADF e ENOENT. | Fundamentos aplicados; sem rastreamento de syscalls ou teste de acesso entre identidades. |
| M03-03 | [Recursos, espera e coordenação](../book/modulo-3/capitulo-11/11.3-recursos-espera-e-coordenacao.md) | Linha do tempo, limites, cgroups e dependência circular. | Modelos explicados e testados, não benchmark, exaustão, deadlock real ou configuração de controladores. |
| M03-04 | [Identidade e limites](../book/modulo-3/capitulo-11/11.4-identidades-e-limites.md) | Distingue identidade do serviço/cliente, permissões do sistema e autorização da aplicação; menor privilégio. | UID/GID, token Windows, capabilities, LSM, namespaces e containers apenas introduzidos. Nenhuma mudança de credenciais ou avaliação de isolamento. |
| M03-05 | [Inicialização e serviços](../book/modulo-3/capitulo-11/11.5-inicializacao-servicos-e-investigacao.md) | Caso fictício de diagnóstico por contexto, prontidão, saúde, registros e reteste. | Percurso Linux/systemd e comparação documental Windows. Nenhum serviço ou sistema de boot alterado. |
| M03-06 | [Kernel, distribuição e contexto](../book/modulo-3/capitulo-12/12.1-kernel-distribuicao-e-contexto.md) | Identificação de kernel versus instalação, composição e dependências. | Fundamentos, revisão interna 1.0; [fontes S1–S19](../book/modulo-3/capitulo-12/referencias.md). Sem diagnóstico universal por versão ou prova de container. |
| M03-07 | [Diretórios e montagens](../book/modulo-3/capitulo-12/12.2-diretorios-e-montagens.md) | FHS, merged-/usr, pontos de montagem e contexto da observação. | Explicação por modelo, sem montar dispositivos, alterar diretórios ou entrar em namespaces. |
| M03-08 | [Procfs, sysfs e dispositivos](../book/modulo-3/capitulo-12/12.3-proc-sys-e-dev.md) | Distingue documento e interface de estado; exemplo de descritor próprio e tmpfs. | Leitura local limitada; não lê processos alheios, não escreve em sysfs nem comprova isolamento. |
| M03-09 | [Drivers, módulos e serviços](../book/modulo-3/capitulo-12/12.4-drivers-modulos-e-servicos.md) | Instalado versus carregado, gerenciamento de dispositivos e condição de prontidão. | Introdução por documentação; sem carregar módulos, alterar firmware ou configurar serviços. |
| M03-10 | [Pacotes e manutenção](../book/modulo-3/capitulo-12/12.5-pacotes-atualizacoes-e-investigacao.md) | dpkg/APT, índices, cadeia de confiança, backports e diagnóstico da Aurora. | Percurso Debian identificado; não instala pacotes nem atesta correção de vulnerabilidade real. |

| M03-11 | [13.1 — O sistema não termina na área de trabalho](../book/modulo-3/capitulo-13/13.1-arquitetura-processos-e-objetos.md) | Narrativa fictícia, perguntas e soluções; sem laboratório Windows. | Revisão interna 1.0; revisão independente pendente. |
| M03-12 | [13.2 — Um caminho também carrega contexto](../book/modulo-3/capitulo-13/13.2-volumes-caminhos-e-perfis.md) | Narrativa fictícia, perguntas e soluções; sem laboratório Windows. | Revisão interna 1.0; revisão independente pendente. |
| M03-13 | [13.3 — O executável não trabalha sozinho](../book/modulo-3/capitulo-13/13.3-executaveis-bibliotecas-e-carregamento.md) | Narrativa fictícia, perguntas e soluções; sem laboratório Windows. | Revisão interna 1.0; revisão independente pendente. |
| M03-14 | [13.4 — A identidade de uma execução](../book/modulo-3/capitulo-13/13.4-contas-tokens-e-controle-de-acesso.md) | Narrativa fictícia, perguntas e soluções; sem laboratório Windows. | Revisão interna 1.0; revisão independente pendente. |
| M03-15 | [13.5 — Configuração tem lugar, tipo e momento](../book/modulo-3/capitulo-13/13.5-registro-ambiente-e-configuracao.md) | Narrativa fictícia, perguntas e soluções; sem laboratório Windows. | Revisão interna 1.0; revisão independente pendente. |
| M03-16 | [13.6 — Do sistema iniciado ao trabalho concluído](../book/modulo-3/capitulo-13/13.6-inicializacao-servicos-e-investigacao.md) | Narrativa fictícia, perguntas e soluções; sem laboratório Windows. | Revisão interna 1.0; revisão independente pendente. |
| M03-17 | [14.1 — A janela não é o interpretador](../book/modulo-3/capitulo-14/14.1-terminal-shell-e-comandos.md) | Exemplos pequenos, dados sintéticos, scripts e testes delimitados; separação entre dados, código e autorização. | Fundamentos desenvolvidos, revisão interna 1.0 0.1; não é um catálogo completo dos shells ou automação de exploração. |
| M03-18 | [14.2 — O programa não recebe a linha que você enxerga](../book/modulo-3/capitulo-14/14.2-argumentos-aspas-e-expansoes.md) | Exemplos pequenos, dados sintéticos, scripts e testes delimitados; separação entre dados, código e autorização. | Fundamentos desenvolvidos, revisão interna 1.0 0.1; não é um catálogo completo dos shells ou automação de exploração. |
| M03-19 | [14.3 — A tela é só um dos destinos](../book/modulo-3/capitulo-14/14.3-fluxos-redirecionamentos-e-pipelines.md) | Exemplos pequenos, dados sintéticos, scripts e testes delimitados; separação entre dados, código e autorização. | Fundamentos desenvolvidos, revisão interna 1.0 0.1; não é um catálogo completo dos shells ou automação de exploração. |
| M03-20 | [14.4 — Terminar não é necessariamente dar certo](../book/modulo-3/capitulo-14/14.4-status-condicoes-e-controle.md) | Exemplos pequenos, dados sintéticos, scripts e testes delimitados; separação entre dados, código e autorização. | Fundamentos desenvolvidos, revisão interna 1.0 0.1; não é um catálogo completo dos shells ou automação de exploração. |
| M03-21 | [14.5 — Da sequência digitada a um contrato repetível](../book/modulo-3/capitulo-14/14.5-scripts-contexto-e-repetibilidade.md) | Exemplos pequenos, dados sintéticos, scripts e testes delimitados; separação entre dados, código e autorização. | Fundamentos desenvolvidos, revisão interna 1.0 0.1; não é um catálogo completo dos shells ou automação de exploração. |
| M03-22 | [14.6 — Automatizar sem transformar dados em ordens](../book/modulo-3/capitulo-14/14.6-automacao-e-fronteiras-de-confianca.md) | Exemplos pequenos, dados sintéticos, scripts e testes delimitados; separação entre dados, código e autorização. | Fundamentos desenvolvidos, revisão interna 1.0 0.1; não é um catálogo completo dos shells ou automação de exploração. |
| M03-23 | [O nome da conta não conta a história inteira](../book/modulo-3/capitulo-15/15.1-identidades-contas-e-contextos.md) | UID/GID/NSS e SID/token; cadastro não atualiza todas as execuções. Sem criação de contas. | Fundamentos desenvolvidos, revisão interna 1.0; [fontes](../book/modulo-3/capitulo-15/referencias.md) e [registro](reviews/capitulo-15.md). Revisão independente pendente. |
| M03-24 | [Permissão para fazer o quê?](../book/modulo-3/capitulo-15/15.2-permissoes-linux-e-caminhos.md) | rwx, classes, caminhos e unlink. Observações somente do proprietário de arquivos temporários. | Fundamentos desenvolvidos, revisão interna 1.0; [fontes](../book/modulo-3/capitulo-15/referencias.md) e [registro](reviews/capitulo-15.md). Revisão independente pendente. |
| M03-25 | [Como uma permissão chega ao arquivo](../book/modulo-3/capitulo-15/15.3-criacao-propriedade-e-acls.md) | Criação, umask, setgid e ACL POSIX. Contas de bits não equivalem a testar ACLs reais. | Fundamentos desenvolvidos, revisão interna 1.0; [fontes](../book/modulo-3/capitulo-15/referencias.md) e [registro](reviews/capitulo-15.md). Revisão independente pendente. |
| M03-26 | [O pedido encontra um token e uma lista](../book/modulo-3/capitulo-15/15.4-tokens-e-acls-no-windows.md) | Direitos solicitados, ACEs, ordem e herança. Modelo didático e fontes Microsoft; sem AccessCheck executado. | Fundamentos desenvolvidos, revisão interna 1.0; [fontes](../book/modulo-3/capitulo-15/referencias.md) e [registro](reviews/capitulo-15.md). Revisão independente pendente. |
| M03-27 | [Privilégio não é apenas uma permissão maior](../book/modulo-3/capitulo-15/15.5-privilegios-e-delegacao.md) | Capabilities, sudo, setuid, UAC e impersonação por documentação. Nenhuma autoridade elevada ou configurada. | Fundamentos desenvolvidos, revisão interna 1.0; [fontes](../book/modulo-3/capitulo-15/referencias.md) e [registro](reviews/capitulo-15.md). Revisão independente pendente. |
| M03-28 | [Uma autorização tem camadas e duração](../book/modulo-3/capitulo-15/15.6-camadas-revogacao-e-menor-privilegio.md) | DAC, controles adicionais e revogação. Descritor Linux observado não generaliza recursos Windows/remotos. | Fundamentos desenvolvidos, revisão interna 1.0; [fontes](../book/modulo-3/capitulo-15/referencias.md) e [registro](reviews/capitulo-15.md). Revisão independente pendente. |
| M03-29 | [Investigar sem abrir todas as portas](../book/modulo-3/capitulo-15/15.7-investigacao-e-verificacao.md) | Consultas por documentação; quatro observações Linux e nove testes delimitados. Sem matriz de contas ou alvos externos. | Fundamentos desenvolvidos, revisão interna 1.0; [fontes](../book/modulo-3/capitulo-15/referencias.md) e [registro](reviews/capitulo-15.md). Revisão independente pendente. |

### Capítulo 16 — Ciclo de vida e continuidade

| Seção | Teoria | Aplicação e verificação | Limites |
| --- | --- | --- | --- |
| 16.1 | [Ciclo de vida](../book/modulo-3/capitulo-16/16.1-ciclo-de-vida-e-processos.md) | Filho próprio, inicialização, espera, saídas e término. | Sem manipular processos externos ou criar zumbis deliberadamente. |
| 16.2 | [Serviços e supervisão](../book/modulo-3/capitulo-16/16.2-servicos-e-supervisao.md) | Tipos, prontidão, watchdog e contratos SCM/systemd. | Pesquisa documental; nenhum serviço foi instalado. |
| 16.3 | [Configuração e reinício](../book/modulo-3/capitulo-16/16.3-configuracao-parada-e-reinicio.md) | Reload, restart, dependências, contexto e recuperação. | Nenhum comando de alteração foi aplicado ao host. |
| 16.4 | [Agendamento](../book/modulo-3/capitulo-16/16.4-agendamento-e-sobreposicao.md) | Cron, timers e Agendador de Tarefas; sobreposição. | Modelos de tempo fictícios; nenhuma tarefa registrada. |
| 16.5 | [Logs e tempo](../book/modulo-3/capitulo-16/16.5-logs-tempo-e-evidencias.md) | Origem, correlação, retenção, rotação e relógios. | Somente teste JSON sintético; sem extrair logs reais. |
| 16.6 | [Estado e confirmação](../book/modulo-3/capitulo-16/16.6-estado-confirmacao-e-retomada.md) | SQLite, transação local, repetição e resposta ausente. | Interrupções do processo; sem energia, corrupção física ou concorrência testada. |
| 16.7 | [Investigação](../book/modulo-3/capitulo-16/16.7-investigacao-e-verificacao.md) | Linha do tempo, hipótese, confirmação e limites de autoridade. | Caso Aurora fictício; sem diagnóstico de incidente real. |


### Capítulo 17 — Fronteiras entre ambientes

| Seção | Teoria | Aplicação e verificação | Limites |
| --- | --- | --- | --- |
| 17.1 | [Separado de quê, protegido contra quem?](../book/modulo-3/capitulo-17/17.1-virtualizacao-e-fronteiras.md) | Requisito de proteção e base de confiança; venv e chroot como recortes. | Fundamento documental; sem configurar VM, container ou host. |
| 17.2 | [Um computador apresentado por outro](../book/modulo-3/capitulo-17/17.2-maquinas-virtuais-e-hipervisores.md) | Modelo de máquina, acelerador, memória e dispositivos. | Fundamento documental; sem configurar VM, container ou host. |
| 17.3 | [Processos com visões e limites próprios](../book/modulo-3/capitulo-17/17.3-containers-namespaces-e-recursos.md) | Visões, identidade, kernel compartilhado e orçamento de recursos. | Fundamento documental; sem configurar VM, container ou host. |
| 17.4 | [As passagens que nós mesmos abrimos](../book/modulo-3/capitulo-17/17.4-compartilhamentos-e-autoridade.md) | Origens de arquivos, integrações, administração e filtragem. | Fundamento documental; sem configurar VM, container ou host. |
| 17.5 | [Uma rede virtual continua sendo uma rede](../book/modulo-3/capitulo-17/17.5-conectividade-e-alcance.md) | Entrada e saída, topologia e opções de conectividade. | Fundamento documental; sem configurar VM, container ou host. |
| 17.6 | [Voltar no tempo tem um alcance](../book/modulo-3/capitulo-17/17.6-imagens-snapshots-e-recuperacao.md) | Estado incluído, efeito externo e identificação de artefatos. | Fundamento documental; sem configurar VM, container ou host. |
| 17.7 | [Conferir a fronteira antes de confiar nela](../book/modulo-3/capitulo-17/17.7-investigacao-e-verificacao.md) | Caso Aurora e comparação real de namespaces de pai e filho. | Nove testes delimitados; não comprova isolamento externo nem resistência a escapes. |

Capítulo 17 em primeira leitura; [fontes](../book/modulo-3/capitulo-17/referencias.md) e [registro](reviews/capitulo-17.md). O capítulo 16 concluiu o ciclo interno 1.0 com limites preservados.

## Cobertura ainda planejada

A matriz continuará a detalhar redes e sistemas, reconhecimento, autenticação, ataques a credenciais, Web, APIs, injeções, autorização, lógica de negócio, infraestrutura, Linux, Windows, Active Directory, cloud, containers, supply chain, exploração de software, pós-exploração, escalada de privilégios, persistência, pivotamento, movimentação lateral, segurança de IA, redes sem fio, mobile, IoT, privacidade, dark web, OSINT, investigação e defesa.

Esses temas pertencem ao planejamento, não são capítulos concluídos por aparecerem nesta lista. Os capítulos a partir do 18 não recebem linhas de cobertura efetiva antes da produção dos textos. Os fundamentos dos capítulos 11 a 17 não substituem as unidades futuras de administração aplicada, segurança de plataformas ou pós-exploração. A matriz não afirma completude e não substitui os registros específicos de revisão.
