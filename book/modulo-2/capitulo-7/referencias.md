# Capítulo 7 · Referências e limites da pesquisa

[← Capítulo](README.md) · [Bibliografia geral](../../bibliografia.md)

**Consulta:** 24/09/2026. **Versão:** VALIDATED 1.0 — fechamento interno, sem revisão independente.

A narrativa do editor, as analogias e as contas são construções autorais. O capítulo apresenta mecanismos, não uma avaliação de hardware real. Foram consultados os trechos delimitados abaixo; isso não equivale à leitura integral de todas as especificações ou à revisão independente.

<a id="s1"></a>
## S1 · Componentes, instruções e arquitetura

WARD, Steve. *Computation Structures — Instruction Set Architectures*. Seções 14.2, 14.3 e 14.4.2.

https://computationstructures.org/notes/isas/notes.html

Uso: modelo de programa armazenado, CPU, memória, entrada/saída, estado de execução, endereçamento por byte e ISA. O capítulo não importa a ISA Beta como descrição universal nem repete simplificações históricas sobre larguras de endereço ou processadores contemporâneos.

<a id="s2"></a>
## S2 · Clock e execução

Intel. *What Is Clock Speed?* Seções What Is Clock Speed? e What Does Turbo Frequency Mean?

https://www.intel.com/content/www/us/en/gaming/resources/cpu-clock-speed.html

Uso: ciclos por segundo, distinção de instruções por ciclo e dependências da frequência efetiva. Não foram usadas recomendações de compra, promessas de desempenho, jogos ou procedimentos de overclock. As contas de 2 GHz são próprias e hipotéticas.

<a id="s3"></a>
## S3 · Núcleos, threads e contextos lógicos

Intel. *What Is Hyper-Threading?* Seções What Is Multithreading? e What Is Hyper-Threading?

https://www.intel.com/content/www/us/en/gaming/resources/hyper-threading.html

Uso: diferença entre trabalho dividido em threads, núcleos e contextos lógicos que compartilham recursos. Não se atribui a todas as CPUs a mesma quantidade de contextos, nem se promete ganho de desempenho.

<a id="s4"></a>
## S4 · Tecnologias e hierarquia de memória

TERMAN, Chris. *Computation Structures — L14: The Memory Hierarchy*. Texto sobre SRAM, DRAM, armazenamento não volátil e caches.

https://computationstructures.org/lectures/caches/caches.html

Uso: compromissos entre capacidade e acesso, refresh, níveis de cache, hit/miss, HDD e flash. Não foram adotados números históricos de latência, custo, durabilidade ou velocidade como especificações atuais. Não foram copiados gráficos. A conta de duas e vinte unidades é um modelo novo e deliberadamente simplificado.

<a id="s5"></a>
## S5 · Localidade e tradução de memória

TERMAN, Chris. *Computation Structures — L16: Virtual Memory*. Introdução e desenvolvimento inicial de MMU, endereços virtuais/físicos e mapeamento.

https://computationstructures.org/lectures/vm/vm.html

Uso: relação entre acessos, hierarquia, tradução e isolamento. Não se generaliza que toda memória virtual corresponde a dados no disco, que todo page fault exige E/S ou que toda plataforma usa uma página de tamanho fixado nesta introdução.

<a id="s6"></a>
## S6 · Administração de flash NAND

Kingston Technology. *The importance of Garbage Collection and TRIM processes for SSD performance*. Seções What is Garbage Collection? e What is TRIM?

https://www.kingston.com/en/blog/pc-performance/ssd-garbage-collection-trim-explained

Uso: programação de páginas, apagamento de blocos, papel do controlador e informação de descarte. A fonte não é utilizada como procedimento de sanitização ou garantia de irrecuperabilidade. Comandos e instruções de sistemas operacionais do artigo não fazem parte da entrega.

<a id="s7"></a>
## S7 · Formato e interface de SSD

Kingston Technology. *Types of SSD Form Factors*. Seções sobre M.2 e interfaces.

https://www.kingston.com/en/blog/pc-performance/ssd-form-factors

Uso: distinguir M.2, SATA, PCIe e NVMe; nem todo M.2 é NVMe. Não foram adotadas comparações comerciais de velocidade, recomendações de compra ou generalizações sobre compatibilidade de conectores.

<a id="s8"></a>
## S8 · Dispositivos, endereços e DMA

The Linux Kernel documentation. *Dynamic DMA mapping Guide*. Seção CPU and DMA addresses.

https://docs.kernel.org/core-api/dma-api-howto.html

Uso: driver, buffer, dispositivo, endereços da CPU e do barramento, tradução por IOMMU. Não foi escrito nem executado um driver. A explicação não presume que endereços virtuais, físicos e de DMA sejam intercambiáveis.

<a id="s9"></a>
## S9 · Confirmação e persistência de escritas

The Linux Kernel documentation. *Explicit volatile write back cache control*. Introduction, Explicit cache flushes e Forced Unit Access.

https://docs.kernel.org/block/writeback_cache_control.html

Uso: cache volátil no dispositivo, conclusão antes de persistência e mecanismos para controlar essa relação. Não foi realizada falha de energia nem avaliado um sistema de arquivos. Não se promete durabilidade sem considerar o contrato completo das camadas.

<a id="s10"></a>
## S10 · Arquivos e cache de páginas

The Linux Kernel documentation. *Overview of the Linux Virtual File System*. Introdução e descrição de page cache/address_space.

https://docs.kernel.org/filesystems/vfs.html

Uso: distinguir a interface de arquivos da organização física e reconhecer operações atendidas ou intermediadas por memória. O percurso do editor é conceitual, não rastreamento de chamadas de um aplicativo real.

<a id="s11"></a>
## S11 · Entrada/saída e interrupções

TERMAN, Chris. *Computation Structures — L18: Devices and Interrupts*. Introdução, interação com dispositivos, buffers e atendimento de eventos.

https://computationstructures.org/lectures/interrupts/interrupts.html

Uso: mediação entre aplicativos e dispositivos, eventos, polling, buffers e interrupções. O exemplo específico de teclado da arquitetura didática não é apresentado como implementação universal de teclados modernos.

<a id="s12"></a>
## S12 · Restrições de DMA em uma plataforma

Microsoft Learn. *Kernel DMA Protection*. Seção How Windows protects against DMA drive-by attacks.

https://learn.microsoft.com/en-us/windows/security/hardware-security/kernel-dma-protection-for-thunderbolt

Uso: IOMMU, regiões atribuídas e dependências de configuração/driver. Não foi verificada compatibilidade de um computador do leitor. Nenhuma configuração foi modificada.

<a id="s13"></a>
## S13 · Firmware e sequência de boot

Microsoft Learn. *Secure the Windows boot process*. Distinção entre firmware, bootloader e kernel; seções Secure Boot e Trusted Boot.

https://learn.microsoft.com/en-us/windows/security/operating-system-security/system-security/secure-the-windows-10-boot-process

Uso restrito: diferentes estágios e verificação de componentes de inicialização. Não foram adotadas afirmações abrangentes de proteção total, irreversibilidade de configurações ou exigência universal de TPM para Secure Boot. As tentativas de abrir o HTML da especificação UEFI não retornaram conteúdo utilizável; não foram registradas como consulta bem-sucedida à especificação.

<a id="s14"></a>
## S14 · Registradores e transformação de valores

TERMAN, Chris. *Computation Structures — L13: Building the Beta*. Descrição de datapath, registradores, ALU, controle e etapas de uma instrução.

https://computationstructures.org/lectures/beta/beta.html

Uso: explicar os papéis dos componentes por uma operação pequena. Não foram copiados circuitos, diagramas, programas ou números de desempenho. Não se generaliza uma instrução por ciclo da máquina didática para CPUs atuais.

<a id="s15"></a>
## S15 · Retenção da informação

NIST CSRC. *Volatile Memory* e *Non-Volatile Memory*, glossário.

https://csrc.nist.gov/glossary/term/volatile_memory

https://csrc.nist.gov/glossary/term/non_volatile_memory

Uso: dependência de alimentação para conservar dados. A consulta dos verbetes não é leitura integral das publicações listadas. Retenção não foi confundida com sanitização certificada ou resistência a todas as falhas.

<a id="s16"></a>
## S16 · CPU e GPU em cooperação

NVIDIA. *CUDA Programming Guide — Programming Model*. Introdução ao modelo heterogêneo de execução.

https://docs.nvidia.com/cuda/cuda-programming-guide/01-introduction/programming-model.html

Uso: GPU como processamento adicional e importância de adequação e movimentação de trabalho. Não foram executados kernels CUDA nem comparados produtos.

## O que pode ser conferido por execução

[test_chapter7_examples.py](../../../scripts/tests/test_chapter7_examples.py) verifica somente as equivalências de clock, o tempo hipotético em ciclos, a média de acesso construída e a distinção entre endereço e conteúdo no pequeno modelo. Esses testes não simulam fielmente uma CPU, não reproduzem DMA e não medem persistência.

A navegação e os testes editoriais são conferidos pelo workflow de documentação. Seu sucesso não valida automaticamente toda a semântica do manuscrito. O retorno favorável foi recebido e o ciclo de revisão interna da versão 1.0 foi encerrado; a revisão técnica independente continua pendente. Consulte o [registro editorial](../../../editorial/reviews/capitulo-7.md).
