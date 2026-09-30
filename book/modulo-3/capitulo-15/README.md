# Capítulo 15 — Usuários, grupos, permissões e privilégios

[← Capítulo 14](../capitulo-14/README.md) · [Índice do módulo](../README.md) · [Glossário](../../glossario.md)

**Módulo III — Sistemas operacionais**

> **Status:** VALIDATED — versão editorial 1.0; leitura aprovada e ciclo interno concluído em 29/09/2026. Fontes e verificações anteriores preservadas; revisão técnica independente pendente. [Registro editorial](../../../editorial/reviews/capitulo-15.md).

O roteiro de importação da biblioteca Aurora finalmente recebe os argumentos corretos. Os caminhos estão explícitos, os erros não são mais escondidos e o serviço procura o catálogo no lugar esperado. Mesmo assim, a importação falha: acesso negado.

Uma pessoa sugere liberar a pasta para todos. Outra prefere executar tudo como administrador. Antes que alguém escolha o atalho, a equipe faz uma pergunta mais útil: **qual operação foi recusada, sobre qual recurso e sob qual identidade?**

A pergunta muda a investigação. Ler o catálogo não é o mesmo que substituí-lo. Participar de um grupo no cadastro não demonstra que uma execução antiga já possui esse grupo. E um programa pode ter permissão para abrir um arquivo sem ter autorização para entregá-lo a qualquer cliente.

Neste capítulo, vamos acompanhar como Linux e Windows representam identidades e decidem acessos. O objetivo não é decorar números de permissões ou aprender a contornar recusas, mas explicar por que uma decisão acontece e como conceder apenas a autoridade necessária.

**A Aurora é um cenário fictício.** Contas, caminhos, números e listas usados nas comparações são exemplos didáticos. Os pequenos experimentos executados usam somente arquivos temporários próprios e têm seus limites registrados. A leitura não exige criar usuários, alterar grupos, elevar privilégios ou modificar a configuração do computador.

## Percurso de leitura

| Seção | Pergunta central |
| --- | --- |
| [15.1 · O nome da conta não conta a história inteira](15.1-identidades-contas-e-contextos.md) | Qual é a diferença entre uma pessoa, uma conta e a identidade de uma execução? |
| [15.2 · Permissão para fazer o quê?](15.2-permissoes-linux-e-caminhos.md) | Como interpretar permissões Linux sem confundir arquivo, diretório e operação? |
| [15.3 · Como uma permissão chega ao arquivo](15.3-criacao-propriedade-e-acls.md) | Como criação, propriedade, umask e ACLs participam do acesso? |
| [15.4 · O pedido encontra um token e uma lista](15.4-tokens-e-acls-no-windows.md) | Como Windows relaciona identidades, direitos solicitados e regras de um objeto? |
| [15.5 · Privilégio não é apenas uma permissão maior](15.5-privilegios-e-delegacao.md) | O que muda com sudo, setuid, capabilities, elevação e delegação? |
| [15.6 · Uma autorização tem camadas e duração](15.6-camadas-revogacao-e-menor-privilegio.md) | Por que um controle isolado não explica todo acesso nem toda revogação? |
| [15.7 · Investigar sem abrir todas as portas](15.7-investigacao-e-verificacao.md) | Como localizar a recusa e conferir a correção sem conceder acesso em excesso? |

Os [exemplos opcionais](exemplos/README.md) distinguem contas sobre bits de operações reais no Linux. As [referências](referencias.md) identificam os mecanismos pesquisados. Ao final há quatorze perguntas, com [respostas comentadas](solucoes.md) separadas.

**[Começar pela seção 15.1 →](15.1-identidades-contas-e-contextos.md)**
