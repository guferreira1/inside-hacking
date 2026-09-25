# Capítulo 7 — Hardware: CPU, memória, armazenamento e dispositivos

[← Capítulo 6](../capitulo-6/README.md) · [Índice do módulo](../README.md) · [Glossário](../../glossario.md) · [Capítulo 8 →](../capitulo-8/README.md)

**Módulo II — Computadores por dentro**

> **Status:** VALIDATED — versão editorial 1.0; retorno favorável e revisão interna concluída em 24/09/2026. Revisão técnica independente pendente. [Registro editorial](../../../editorial/reviews/capitulo-7.md).

Você escreve uma frase em um editor. Ela aparece na tela. Antes de salvar, falta energia. Quando o computador volta, o arquivo ainda contém a versão anterior.

Vamos assumir que esse editor fictício não possui salvamento automático nem mecanismo de recuperação. A frase existiu na tela, mas não se tornou uma alteração persistente do arquivo. **Onde ela estava?**

Responder “na memória do computador” ajuda pouco se usamos a mesma palavra para tudo. Há armazenamento para conservar arquivos, memória para o trabalho em andamento, pequenos espaços dentro do processador e dispositivos que recebem e apresentam informações. Eles cooperam, mas não oferecem as mesmas garantias.

No capítulo 6, aprendemos a interpretar representações. Agora vamos acompanhar os componentes que as guardam, transportam e transformam. Não faremos um catálogo de peças para comprar. Construiremos um mapa funcional: o que cada componente faz, como depende dos outros e por que essas relações importam para investigar segurança.

A frase do editor será nosso fio condutor. Os exemplos são didáticos, não medições de uma máquina real. Nenhuma instalação, desmontagem ou alteração de firmware é necessária.

## Percurso de leitura

| Seção | Pergunta central |
| --- | --- |
| [7.1 · Um computador não é uma peça só](7.1-componentes-e-caminhos.md) | Que componentes participam quando abrimos, alteramos e salvamos um arquivo? |
| [7.2 · O que o processador realmente executa](7.2-cpu-e-execucao.md) | O que significam instrução, registrador, clock, núcleo e arquitetura? |
| [7.3 · Nem toda memória é a mesma memória](7.3-memoria-e-cache.md) | Por que existem RAM, caches e diferentes tipos de endereço? |
| [7.4 · Guardar não é apenas receber uma escrita](7.4-armazenamento-e-persistencia.md) | O que distingue disco, SSD, cache de escrita e persistência? |
| [7.5 · Dispositivos também participam da confiança](7.5-dispositivos-e-firmware.md) | Como dados entram na memória e que software atua antes do sistema operacional? |

As [referências](referencias.md) delimitam o uso das fontes. No encerramento, há perguntas opcionais e [respostas comentadas](solucoes.md). Os [testes de conferência](../../../scripts/tests/test_chapter7_examples.py) verificam somente contas explícitas do texto, não desempenho ou proteção de hardware.

**[Começar a seção 7.1 →](7.1-componentes-e-caminhos.md)**

Depois deste percurso, siga para o [Capítulo 8 — Como um programa se torna execução](../capitulo-8/README.md).
