# Primeira entrega editorial — Capítulo 15

**Data:** 29/09/2026. **Estado atual:** VALIDATED — versão editorial 1.0. **Módulo:** III.

[Capítulo](../../book/modulo-3/capitulo-15/README.md) · [Referências](../../book/modulo-3/capitulo-15/referencias.md) · [Exemplo](../../book/modulo-3/capitulo-15/exemplos/README.md)

## Recorte e continuidade

Sete seções, quatorze perguntas e respostas comentadas. Identidades e credenciais, permissões por operação, criação e ACLs Linux, tokens/DACLs Windows, privilégios e delegação, camadas/revogação e investigação. O capítulo 16 continua sendo Processos, serviços, logs e persistência de estado. O sumário não foi reorganizado.

O pedido de avançar registra a aprovação da leitura do capítulo 14, conforme a convenção editorial. Isso não comprova domínio prático nem permite preencher horas, laboratórios ou autonomia que o mantenedor não relatou.

## Fontes e redação

Foram pesquisadas fontes primárias Linux man-pages, Linux ACL, GNU coreutils, shadow-utils, util-linux, sudo, documentação do kernel, Microsoft, Python e OWASP. As reproduções de manuais no man7 são identificadas, inclusive nas alternativas usadas após falhas de abertura direta de GNU e sudo.ws. A lista contém 47 referências numeradas; consultas pontuais não equivalem à leitura integral dos manuais.

O texto distingue modelos POSIX e Windows; máscara de ACL e umask; dono do objeto e identidade da execução; arquivo e entrada; acesso solicitado e necessário; privilégio presente e habilitado; recurso já aberto e nova abertura. As contas, identificadores e políticas da Aurora são fictícios. As explicações não incluem procedimentos de exploração ou configuração privilegiada do host.

## Execução local observada

Python 3.13.5; Linux 6.18.44 x86-64; glibc 2.41. O lançador estava em container com UID zero, portanto os testes e a execução independente foram feitos em subprocesso com UID/GID 65534, sem grupos suplementares. O exemplo confirmou ausência de capabilities efetivas. Nenhuma conta foi criada ou alterada; somente o subprocesso perdeu privilégios.

**Nove testes próprios passaram, sem skips:** três verificam modelos de bits/seleção de classe e a guarda de ambiente; seis executam operações Linux, saída de processo independente e limpeza, incluindo falha injetada. As quatro observações reais produziram os oito indicadores previstos: recusa de escrita, remoção de nome, recusa de nova abertura, leitura pelo descritor anterior, recusa de listagem com busca, leitura de nome conhecido, listagem sem busca e recusa da abertura nesse último contexto.

Nenhuma ACL Windows, UAC, sudo, setuid, capability, conta ou política obrigatória foi alterada. As consultas Windows são documentais e não foram executadas nesta entrega. Testes PowerShell anteriores, quando presentes na regressão, não validam retroativamente os controles Windows deste capítulo.

## Verificações de conjunto

A regressão completa, a atualização do glossário, os índices e a checagem de navegação são verificações separadas da execução local. Seus resultados serão registrados pela preparação da árvore final, sem considerar um workflow pendente como sucesso.

## Limites

A revisão é interna, assistida por IA; revisão técnica independente permanece pendente. As observações usam o proprietário dos próprios arquivos, não uma matriz de contas reais. Contas de modo e máscaras não são testes completos de ACL. Não houve publicação no LinkedIn nem geração de edição PDF.


## Verificação no runner

Os resultados da regressão e da segunda passagem documental estão na [auditoria desta entrega](../audits/2026-09-29-capitulo-15.md), separados da execução local descrita acima.

## Aprovação e fechamento interno

O pedido de continuidade do mantenedor registra aprovação da leitura do capítulo 15. Foram preservados o manuscrito, as fontes, os nove testes e os limites da validação anterior, com atualização de estado e navegação. A regressão desta entrega é registrada na [auditoria do capítulo 16](../audits/2026-09-29-capitulo-16.md). Não houve revisão técnica independente nem atribuição de domínio prático ao leitor.
