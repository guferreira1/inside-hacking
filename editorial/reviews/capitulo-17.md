# Primeira entrega editorial — Capítulo 17

**Data:** 29/09/2026. **Estado:** DRAFT 0.1. **Módulo:** III.

[Capítulo](../../book/modulo-3/capitulo-17/README.md) · [Referências](../../book/modulo-3/capitulo-17/referencias.md) · [Exemplo](../../book/modulo-3/capitulo-17/exemplos/README.md)

## Recorte e continuidade

Sete seções e quatorze perguntas com respostas comentadas. O percurso relaciona virtualização e isolamento, VMs/hipervisores, containers/namespaces, compartilhamentos, conectividade, imagens/snapshots e verificação. Não houve reorganização do sumário: a próxima unidade permanece 18 — Como computadores se comunicam.

O pedido de continuidade registra a aprovação da leitura do capítulo 16. Suas sete seções e quatorze respostas foram relidas; texto e exemplos são preservados, com atualização de estado e navegação. Essa aprovação não registra horas, laboratórios ou domínio prático do leitor.

## Pesquisa e redação

As 38 referências numeradas relacionam 39 URLs primárias de documentação Linux, QEMU, Oracle, Docker, Microsoft e Python. Foram consultados os recortes relacionados às afirmações, não todos os manuais integralmente. O ramo master do QEMU e os endereços de documentação corrente não são versões instaladas.

A redação distingue virtualização e restrição, dependências e confinamento, host e guest, kernel compartilhado e separado, visão e orçamento, concessão e escape, entrada e saída, artefato e instância, snapshot e recuperação de efeitos externos. A Aurora, suas políticas e seu incidente são fictícios. O recorte do capítulo não ensina escapes, análise de malware real ou configuração completa de um laboratório ofensivo.

## Execução local observada

Python 3.13.5; Linux 6.18.44 x86-64; glibc 2.41; UID efetivo 0 no container de execução. O exemplo não utiliza operações administrativas nem tenta mudar identidade ou configuração. Os nove testes próprios passaram sem skips: quatro de contratos e cinco Linux, incluindo observação do próprio filho, fechamento de descritores e saída independente.

A execução independente confirmou processos distintos e igualdade nos seis namespaces comparados. Isso não certifica fronteira externa de VM/container, proteção de outro processo, seccomp, cgroups ou resistência a escapes. Parte dos testes injeta erros para verificar limpeza e ausência de saída parcial; não são incidentes reais de permissão ou timeout.

Não foram instalados virtualizadores, iniciadas VMs, criados containers ou alterados namespaces. A configuração Windows Sandbox é documental, sem execução. Não houve rede de alvo, montagem, acesso a documentos pessoais ou administração de serviços. A impossibilidade de clonar o repositório por resolução de rede no ambiente local deixa a regressão completa para o runner, separadamente da execução local.

## Verificação de conjunto

A regressão, as duas passagens de navegação, o glossário e a consulta de URLs são registrados na [auditoria da entrega](../audits/2026-09-29-capitulo-17.md), depois de efetivamente executados. Arquivos temporários de preparação não integram a árvore publicada.

## Estado e próxima etapa

O capítulo 17 permanece DRAFT para primeira leitura. Com sua escrita, todos os textos previstos do Módulo III existem; o fechamento interno requer a aprovação desta leitura e a revisão de conjunto. Após esse fechamento, a comunicação no LinkedIn é o próximo marco editorial antes de iniciar outro módulo. Não houve postagem nem criação de automação. A pendência do capítulo 1 e o fechamento do Módulo II são preservados. Revisão técnica independente e futura edição PDF continuam etapas distintas.

## Verificação no runner

A [execução de preparação](https://github.com/guferreira1/inside-hacking/actions/runs/36650256040) concluiu 122 testes sem falhas ou skips. A auditoria registra ambientes, observação independente do exemplo, preservação do glossário, consultas HTTP e checagens documentais. A confirmação de integração em main é separada.
