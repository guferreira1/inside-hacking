# Capítulo 10 — Arquivos, formatos, codificação e serialização

[← Capítulo 9](../capitulo-9/README.md) · [Índice do módulo](../README.md) · [Glossário](../../glossario.md)

**Módulo II — Computadores por dentro**

> **Status:** DRAFT 0.1 — primeira entrega de leitura. Exemplos próprios e verificações documentados; leitura do mantenedor e revisão independente pendentes. [Registro editorial](../../../editorial/reviews/capitulo-10.md).

A biblioteca Aurora exporta um registro do catálogo. Uma pessoa o salva como `livro.json`; outra muda o nome para `livro.txt`. O editor de texto abre os dois. O importador aceita apenas um deles.

O que mudou? Talvez somente o nome. Talvez os bytes tenham sido transformados por uma ferramenta. Talvez o importador escolha como ler pelo sufixo. Dizer “é o mesmo arquivo” ainda deixa várias perguntas sem resposta.

Nos capítulos anteriores, acompanhamos representações, hardware e processos. Agora chegamos ao ponto em que um programa entrega informação a outro: um conjunto de bytes precisa atravessar a fronteira sem perder a estrutura ou ganhar uma interpretação indevida.

Acompanharemos um registro simples: título **Livro**, quantidade **3**. Vamos separar seu nome no sistema de arquivos, seus bytes, seu formato, as transformações aplicadas e a decisão de aceitar seus valores. Um formato binário pequeno, criado para esta obra, permitirá localizar cada campo. JSON e outros formatos mostrarão maneiras diferentes de resolver o mesmo tipo de problema.

Não é necessário instalar ferramentas. O texto explica o percurso; o [programa de exemplo](exemplos/README.md) permite conferir algumas etapas opcionalmente, sem serviços de rede ou arquivos desconhecidos.

## Percurso de leitura

| Seção | Pergunta central |
| --- | --- |
| [10.1 · O nome aponta; os bytes contam outra parte](10.1-arquivos-nomes-e-leitura.md) | Qual é a diferença entre caminho, arquivo aberto, metadados e conteúdo? |
| [10.2 · Um formato é um acordo sobre posições e significado](10.2-formatos-e-estrutura.md) | Como reconhecer e interpretar campos sem confiar apenas na extensão? |
| [10.3 · Transformar a escrita não transforma tudo na mesma coisa](10.3-codificacoes-e-transformacoes.md) | O que fazem codificação, escape, Base64 e normalização? |
| [10.4 · Levar uma estrutura para fora do processo](10.4-serializacao-e-contratos.md) | O que a serialização preserva e o que o receptor ainda precisa decidir? |
| [10.5 · Ler o formato é verificar suas promessas](10.5-parsing-e-validacao.md) | Como um leitor transforma bytes em dados aceitos, sem ignorar limites e ambiguidades? |
| [10.6 · O conteúdo vai continuar sua viagem](10.6-integridade-e-fronteiras.md) | Por que validação, integridade e segurança de uso são perguntas diferentes? |

As [referências](referencias.md) delimitam as fontes utilizadas. Ao final, há perguntas opcionais e [respostas comentadas](solucoes.md).

**[Começar a seção 10.1 →](10.1-arquivos-nomes-e-leitura.md)**
