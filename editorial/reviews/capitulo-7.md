# Primeira entrega editorial — Capítulo 7

**Data:** 24/09/2026. **Estado:** DRAFT 0.1. **Módulo:** II.  
**Base da entrega:** `d148c59ffa5dfdedfc06e9586fc203bb7cf295d7`.

[Manuscrito](../../book/modulo-2/capitulo-7/README.md) · [Referências](../../book/modulo-2/capitulo-7/referencias.md)

## Objetivo e recorte

Conectar a representação estudada no capítulo 6 às funções de processamento, memória, armazenamento e entrada/saída. O exemplo do editor sem recuperação fornece um fio narrativo. Não é um catálogo de componentes para compra nem um laboratório de montagem.

Cinco seções apresentam CPU, registradores, ALU, clock, núcleos, ISA, hierarquia de memória, endereços, persistência de escrita, interfaces de armazenamento, dispositivos, DMA, IOMMU, GPU e firmware. Memória virtual e boot são introduzidos somente no necessário para compreender os limites entre componentes; execução de programas e processos serão aprofundados nos capítulos 8 e 9.

## Verificações e escolhas

As referências S1–S16 identificam trechos primários efetivamente consultados. Valores históricos de desempenho do material didático não foram importados como especificações atuais. As páginas comerciais de fabricantes foram utilizadas apenas para mecanismos e terminologia, não recomendações de compra.

O texto distingue ciclos de instruções, núcleos de contextos lógicos, endereços de conteúdo, MMU de IOMMU, formato físico de interface e confirmação temporária de persistência. Secure Boot não é apresentado como prova de ausência de vulnerabilidades. A ausência de conteúdo recuperável em tentativas de acesso à especificação UEFI foi registrada, sem alegar revisão da especificação inteira.

As quatro funções de teste em [test_chapter7_examples.py](../../scripts/tests/test_chapter7_examples.py) verificam contas e um mapeamento didático. Não constituem simulador de CPU, medição de cache, ensaio de perda de energia ou validação de DMA. A execução deve ser conferida no workflow associado ao commit de publicação; não basta a existência do script para declará-lo aprovado.

Nove questões opcionais e respostas foram revisadas contra as premissas do texto. Não há requisito de instalar ferramentas, desmontar hardware ou modificar firmware. Novos termos entram no glossário nesta entrega, com referência à seção correspondente. Índices, navegação, bibliografia, matriz de cobertura e controle editorial acompanham o manuscrito.

## Estado e próxima revisão

Primeira leitura do mantenedor e revisão técnica independente pendentes. Nenhum laboratório ofensivo, benchmark de hardware ou PDF foi produzido. O estado permanece DRAFT; os testes editoriais não o promovem automaticamente.

A próxima revisão deve observar se a narrativa do editor mantém clareza ao alternar camadas, especialmente na passagem entre memória e persistência. O próximo capítulo planejado é **8 — Como um programa se torna execução**.
