# Primeira entrega editorial — Capítulo 9

**Data:** 24/09/2026. **Estado:** DRAFT 0.1. **Módulo:** II.  
**Base:** `6547111cae636b1e4afdefbe131d49f0b8ed94d4`.

[Manuscrito](../../book/modulo-2/capitulo-9/README.md) · [Referências](../../book/modulo-2/capitulo-9/referencias.md) · [Exemplo](../../book/modulo-2/capitulo-9/exemplos/README.md)

## Objetivo e recorte

Cinco seções aprofundam a organização da execução introduzida nos capítulos 7 e 8. O cenário dos contadores liga processos, threads, tradução por páginas, regiões, objetos, duração, residência, compartilhamento, proteções e concorrência. Dez perguntas opcionais possuem respostas comentadas.

Os números de endereços e medidas são modelos explícitos. Não foram copiados diagramas de terceiros nem exigidos conhecimentos prévios de administração do kernel. O leitor pode acompanhar sem executar programas. Exploração de memória, leitura de processos de terceiros e mudanças nas proteções não fazem parte desta entrega.

## Pesquisa e revisão interna

As fontes S1–S18 delimitam trechos da documentação Linux, Microsoft, GNU, LLVM, Python, CWE e uma reprodução identificada de POSIX. A redação distingue thread de processo, troca de contexto de passagem de modo, TLB miss de page fault, mapeamento de objeto, endereço de destino, tamanho virtual de residência, liberação de sanitização e proteção de páginas de autorização de negócio.

As respostas foram confrontadas com as premissas. O modelo de intercalamento não é anunciado como execução de data race C. Os tamanhos de página fictícios não são apresentados como configuração universal, e o resultado de mmap não é medição de cópias físicas.

## Evidência executada

Sete testes passaram localmente em Debian GNU/Linux 13, Linux x86-64, Python 3.13.5. Seis conferem contas ou modelos sequenciais e um executa o programa Python com mapeamentos privado e compartilhado. A saída observada foi `privado=5` e `compartilhado=9`, com término normal.

O processo de teste inicia o exemplo com `-I -S`, sem personalizações automáticas de site, em vez de fazer fork de um notebook ou processo hospedeiro multithread. Uma tentativa anterior com a inicialização padrão emitiu um aviso sobre threads e não foi adotada como procedimento recomendado. A execução final foi repetida sem esse aviso. Os argumentos não foram descritos como sandbox.

O repositório completo deve ser conferido pelo workflow do commit: o clone local não foi concluído por falha de resolução de rede. Não se equipara teste local dos exemplos à auditoria local de todos os arquivos.

## Documentação e estado

Índices, navegação entre capítulos, bibliografia, glossário contextual, matriz de cobertura e controle editorial acompanham a entrega. O capítulo 8 recebe registro separado de retorno favorável e fechamento interno; o capítulo 1 mantém suas pendências. Nenhum módulo ou PDF é declarado lançado.

Primeira leitura do capítulo 9 e revisão técnica independente pendentes. Não foram executados benchmark, stress de memória, OOM, medição de RSS/PSS, exploração ou avaliação de eficácia de ASLR/DEP.

**Próxima revisão:** conferir se a passagem entre página, região e objeto permanece clara para quem lê pela primeira vez. Próximo capítulo planejado: **10 — Arquivos, formatos, codificação e serialização**.
