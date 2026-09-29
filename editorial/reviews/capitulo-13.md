# Revisão editorial — Capítulo 13

**Primeira entrega e aprovação de leitura:** 29/09/2026. **Estado:** VALIDATED — versão editorial 1.0; revisão interna concluída. Integração e checagem global nesta entrega do capítulo 14.

[Capítulo](../../book/modulo-3/capitulo-13/README.md) · [Fontes](../../book/modulo-3/capitulo-13/referencias.md)

## Escopo e decisão editorial

Windows por dentro ocupa a posição 13 do sumário existente. A ordem não foi reorganizada. A leitura do capítulo 12 foi confirmada pelo mantenedor antes desta entrega; o pedido posterior de seguir ao capítulo 14 confirma também a leitura do 13.

Abertura, seis seções, doze perguntas, respostas comentadas e 44 referências primárias da Microsoft foram preservadas da entrega local. A narrativa da biblioteca Aurora é fictícia e independente do histórico de chats.

## Pesquisa, revisão e limites

A revisão interna examinou modo kernel versus elevação; nome de usuário versus SID; sessão de logon versus sessão interativa; identidade versus direitos do objeto; DACL versus outros controles; presença versus habilitação de privilégio; arquitetura e redirecionamento; configuração visível versus efetivamente consumida; estado de serviço versus resultado de negócio.

A explicação do UAC permanece limitada ao modelo tradicional. A menção a Administrator protection não afirma disponibilidade universal ou implantação por KB.

As perguntas e respostas foram reconferidas contra as seções. A aprovação é editorial, não certificação ou demonstração de domínio prático do leitor. Revisão técnica independente continua pendente.

**Não foi executado laboratório de kernel, UAC, Registro, SCM ou rede em Windows para este capítulo.** Os testes de PowerShell do capítulo 14, quando executados, são evidência apenas daqueles exemplos, não reprodução retroativa do capítulo 13.

Não houve acesso aos recursos fictícios da Aurora nem alterações de contas, permissões, credenciais, Registro ou serviços.

## Histórico da publicação

A primeira entrega existiu como HTML, Markdown e ZIP, sem commit porque a sessão então disponibilizava apenas consultas. A main consultada estava em `9ace0862c456f01b3d8b03e8857349448f086215`.

Na continuidade, a árvore preparada do capítulo 12 foi recuperada no commit `0da3c29cc4d4a9d143c96dce8c7ccdc459826cd9`, sobre aquela main. Os manuscritos do capítulo 13 foram transferidos do pacote aprovado sem mudar a sequência ou recriar um conteúdo diferente. O resultado efetivo da integração, da suíte e da navegação será registrado na auditoria desta entrega.


## Aprovação e integração de 29/09/2026

A leitura foi aprovada antes do avanço. O ciclo interno da versão editorial 1.0 está concluído, com os limites de fontes e reprodução preservados. A integração recupera a entrega anterior sem reorganizar capítulos. A [auditoria desta entrega](../audits/2026-09-29-capitulos-12-14.md) registra os testes e a navegação efetivamente executados. Revisão independente permanece pendente.
