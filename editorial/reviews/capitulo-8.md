# Primeira entrega editorial — Capítulo 8

**Data:** 24/09/2026. **Estado:** DRAFT 0.1. **Módulo:** II.  
**Base:** `05af26d7776887be714fb58a00056124460b24ac`.

[Manuscrito](../../book/modulo-2/capitulo-8/README.md) · [Referências](../../book/modulo-2/capitulo-8/referencias.md) · [Exemplos](../../book/modulo-2/capitulo-8/exemplos/README.md)

## Objetivo e percurso

Cinco seções conectam código-fonte, construção, ligação, carregamento, contexto de processo e runtimes. Um programa C em três arquivos torna concreta a diferença entre declaração e definição, fonte editado e executável produzido, saída textual e código de encerramento. Python e JVM ampliam a explicação sem impor uma dicotomia universal entre compilado e interpretado.

O texto não exige experiência prévia em C. Os elementos utilizados são explicados; a execução é opcional. Não foi criado laboratório ofensivo ou serviço de rede. O capítulo 9 permanece responsável por aprofundar a organização da memória e dos processos.

## Pesquisa e revisão interna

As fontes S1–S14 foram consultadas nos trechos documentados. A redação distingue arquivos ELF de tipos diferentes, ABI de ISA, `fork` de `execve`, ponto de entrada de `main`, chamada de biblioteca de chamada de sistema e bytecode de executável nativo. As nove questões foram comparadas às soluções.

O caminho Linux/GCC é um exemplo de implementação. PE, convenções Windows, LSB e JVM possuem seus próprios limites identificados, sem alegação de execução ou universalidade. Não se afirma que toda chamada `printf` corresponda a uma única chamada de sistema nem que todo ELF `ET_DYN` seja obrigatoriamente uma biblioteca.

## Execução efetivamente realizada

Os [nove testes](../../scripts/tests/test_chapter8_examples.py) passaram no ambiente de edição: Debian GNU/Linux 13, Linux x86-64, GCC 14.2.0 e Python 3.13.5. Seis conferem artefatos e execução C; três conferem objetos de código e contextos Python. Os programas são próprios, executados em temporários; não houve rede ou coleta de dados do usuário.

Foram conferidos resultados positivos e a falha esperada de ligação quando a implementação é omitida. Falha esperada no cenário negativo é um comportamento examinado pelo teste, não falha da suíte. Renomear um executável foi examinado apenas no ambiente Linux utilizado. Namespaces separados em Python não foram apresentados como isolamento real de processos.

A checagem do repositório completo deve ser confirmada pelo workflow do commit, pois não houve clone local bem-sucedido do repositório. Execução local dos exemplos não equivale a varredura local de todos os Markdown. Os testes C declaram Linux e GCC como requisitos; um caso ignorado deve permanecer visível nos logs.

## Documentação e continuidade

A entrega atualiza README principal, índice geral e do módulo, bibliografia, glossário, matriz de cobertura, estado editorial e a passagem entre capítulos. Os termos novos possuem ocorrência no manuscrito; o glossário não importa capítulos futuros para inflar cobertura.

Primeira leitura do mantenedor e revisão técnica independente do capítulo 8 permanecem pendentes. Não houve geração de PDF. O capítulo 7 encerra seu ciclo interno separadamente; o capítulo 1 continua em revisão e o Módulo I não é declarado encerrado.

**Próxima revisão:** receber a leitura do capítulo 8, observando se a distinção entre etapas ficou clara sem tornar a narrativa um manual de comandos. Próximo capítulo planejado: **9 — Memória, processos e arquitetura de computadores**.
