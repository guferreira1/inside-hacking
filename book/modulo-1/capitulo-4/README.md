# Capítulo 4 — Como pensar como investigador de segurança

[← Capítulo 3](../capitulo-3/README.md) · [Índice do módulo](../README.md) · [Capítulo 5 →](../capitulo-5/README.md)

**Módulo I — Hacking, segurança e método**

> **Status:** VALIDATED — versão editorial 1.0; leitura aprovada e revisão interna concluída em 24/09/2026. Revisão técnica independente pendente. [Registro editorial](../../../editorial/reviews/capitulo-4.md).

Você muda um número e aparece o nome de outra pessoa.

Por alguns segundos, a conclusão parece pronta: encontrou uma falha de segurança. O próximo impulso pode ser procurar mais registros, abrir uma ferramenta ou começar a escrever o relatório. Mas ainda falta responder a uma pergunta menor, e muito mais importante: **o que aconteceu de fato?**

Talvez a aplicação tenha entregue informação que deveria proteger. Talvez a tela mostre um exemplo público. Talvez o pedido tenha sido feito com uma identidade diferente da que você imaginou. A mesma impressão inicial pode nascer de mecanismos distintos.

Investigar não é escolher a explicação mais emocionante. É organizar observações e testes até conseguir dizer qual explicação os dados sustentam, em quais condições e com quais limites.

No capítulo anterior, discutimos quando podemos testar. Agora vamos estudar como decidir o que testar e como interpretar a resposta. O fio condutor será uma nova situação da biblioteca fictícia Aurora: dois leitores, um comprovante e uma aparente quebra de isolamento. O caso será desenvolvido aqui desde o início e não pressupõe que o leitor conheça redes, programação ou ferramentas de pentest.

**Todos os acontecimentos e resultados do caso são construções didáticas.** Não existe uma execução real por trás das telas descritas, e nenhuma instalação é necessária. A proposta é acompanhar uma investigação explicada, não cumprir um laboratório imaginário.

## Percurso de leitura

| Seção | Pergunta central |
| --- | --- |
| [4.1 · Uma tela não conta a história inteira](4.1-observacao-e-hipoteses.md) | Como separar o que vimos da explicação que estamos propondo? |
| [4.2 · Escolher o teste antes da ferramenta](4.2-testes-e-comparacoes.md) | Qual comparação realmente ajuda a distinguir as hipóteses? |
| [4.3 · Quando a ferramenta parece ter a resposta](4.3-resultados-e-evidencias.md) | O que alertas, códigos e registros demonstram — e o que deixam em aberto? |
| [4.4 · Uma conclusão do tamanho da evidência](4.4-conclusoes-e-limites.md) | Quando já sabemos o suficiente para comunicar um resultado? |

Ao final há perguntas opcionais de revisão, com [respostas comentadas](solucoes.md) em arquivo separado. As [referências](referencias.md) identificam os fundamentos técnicos utilizados; o percurso narrativo e as decisões do caso são explicações autorais.

**[Começar a seção 4.1 →](4.1-observacao-e-hipoteses.md)**
