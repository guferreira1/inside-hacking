# Revisão editorial — Capítulo 12

**Primeira entrega:** 29/09/2026. **Estado atual:** VALIDATED — versão editorial 1.0. **Módulo:** III.
**Base da primeira entrega:** `9ace0862c456f01b3d8b03e8857349448f086215`.

[Manuscrito](../../book/modulo-3/capitulo-12/README.md) · [Referências](../../book/modulo-3/capitulo-12/referencias.md) · [Exemplo](../../book/modulo-3/capitulo-12/exemplos/README.md)

## Objetivo e recorte

Cinco seções desenvolvem a organização de uma instalação Linux: núcleo e distribuição, árvore de nomes e montagens, procfs/sysfs/dispositivos/tmpfs, drivers e módulos, serviços e cadeia de pacotes. O cenário fictício da Aurora distingue uma origem ausente da visão do serviço de uma recusa de permissão no mesmo caminho. Há dez perguntas opcionais com respostas comentadas.

A leitura independe de instalar Linux, de ter acesso administrativo ou de executar comandos. O capítulo não substitui as unidades sobre terminal, permissões, serviços ou isolamento. O percurso de gerenciamento de pacotes é explicitamente Debian/APT, não uma regra universal de todas as distribuições.

## Pesquisa e redação

As fontes S1–S19 relacionam documentação do kernel, Linux man-pages, Debian, FHS, systemd, kmod, util-linux e Python. A redação e os cenários são autorais. FHS 3.0 é convenção, não fotografia de todo sistema atual; Debian 12 é referência identificada para merged-/usr, não indicação de release corrente; os manuais systemd reproduzidos no man7 não são recomendação para instalar sua versão de desenvolvimento.

São distinguidos diretório raiz e conta root; link e cópia; caminho e montagem; estado e arquivo persistente; assinatura e correção do software; metadados disponíveis, pacote instalado e execução; versão upstream e correção da distribuição. Não foi diagnosticada vulnerabilidade em uma versão concreta.

## Execução local realmente realizada

Linux x86-64, kernel 6.18.44, glibc 2.41, Python 3.13.5. O programa `proc_proprio.py` foi executado separadamente com `python3 -I -S` e produziu as quatro linhas documentadas. Os quatro testes próprios passaram: contrato de plataforma, metadados/leitura e limpeza, limpeza após erro simulado na consulta e saída de processo separado.

A falha simulada altera apenas a referência ao módulo `os` utilizada pelo exemplo, preservando as funções necessárias à limpeza do runtime. Ela não comprova uma política de autorização entre contas. A comparação de dispositivo/inode é local e momentânea; não comprova compartilhamento de posição de leitura. A leitura tem limite de sete bytes para conteúdo próprio de seis bytes.

Nenhuma montagem, instalação de pacote, modificação de serviço, inspeção de processo alheio, escrita em sysfs, carga de módulo, alteração de firmware ou teste ofensivo foi realizada. O procedimento não exige sudo. Uma plataforma não compatível é identificada como tal; não se fabrica saída de sucesso.

O clone local completo não foi obtido por falha de resolução de rede. A execução local cobre o exemplo e seus testes; a regressão de todo o repositório e os links internos são conferidos separadamente no runner.

## Continuidade e documentação

A aprovação da leitura do capítulo 11 foi registrada pelo pedido de seguir ao próximo, conforme a convenção do mantenedor. A releitura das cinco seções, dez respostas e referências conservou a separação entre validação editorial interna e revisão independente. Não foram inventadas horas, execução de labs pelo leitor ou domínio prático.

README principal, índice geral, índice do Módulo III, navegação 11→12, bibliografia, glossário, matriz de cobertura e controle editorial acompanharam a primeira entrega. O Módulo II manteve seu fechamento interno; a pendência do capítulo 1 permaneceu independente. Não houve publicação no LinkedIn nem geração de PDF naquela rodada.

## Verificação de conjunto da primeira entrega

A preparação no [workflow de apoio](https://github.com/guferreira1/inside-hacking/actions/runs/36615055086) executou **64 testes com sucesso**, incluindo os quatro novos. A checagem global percorreu **124 Markdown**, conferiu **984 destinos internos** e não detectou erro de caminho ou âncora. Esse verificador inventaria URLs externas; não certifica sua disponibilidade por HTTP.

O glossário passou de **373 para 401 verbetes**, com **28 entradas novas** e preservação dos 373 blocos anteriores. As entradas têm ocorrência no capítulo, explicação delimitada e navegação para as respectivas seções. Nenhum assunto apenas planejado foi adicionado.

O workflow e o auxiliar usados apenas para preparar aquela alteração foram excluídos da árvore final. A publicação da árvore preparada permaneceu pendente até a recuperação documentada na entrega do capítulo 14; a preparação bem-sucedida não foi uma integração automática à main.

## Aprovação e integração de 29/09/2026

A leitura do capítulo 12 foi aprovada antes do avanço ao 13. O ciclo interno da versão editorial 1.0 está concluído, com os limites de fontes e reprodução preservados. A integração recupera a entrega anterior sem reorganizar capítulos. A [auditoria desta entrega](../audits/2026-09-29-capitulos-12-14.md) registra os testes e a navegação efetivamente executados.

**Próxima revisão deste capítulo:** revisão técnica independente e preparação de uma futura edição estável. A leitura do capítulo 12 não está pendente. O percurso já avançou pelo Windows e continua no capítulo 14, sem alterar a ordem original.
