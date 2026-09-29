# Capítulo 14 — Terminal, shells e automação

[← Capítulo 13](../capitulo-13/README.md) · [Índice do módulo](../README.md) · [Glossário](../../glossario.md)

**Módulo III — Sistemas operacionais**

> **Status:** DRAFT 0.1 — primeira entrega de leitura. Fontes, verificações e limites no [registro editorial](../../../editorial/reviews/capitulo-14.md). Revisão técnica independente pendente.

A equipe da biblioteca Aurora quer deixar de repetir a mesma conferência todos os dias. Uma pessoa abre um terminal, informa o catálogo e obtém o resultado esperado. Outra coloca uma sequência parecida em um script. O arquivo se chama `catalogo de teste.txt`. Na execução automatizada, o programa passa a receber três nomes em vez de um.

Depois aparece uma segunda surpresa: uma etapa falha, mas a mensagem final do roteiro diz que tudo terminou bem.

Nenhuma dessas situações exige uma vulnerabilidade misteriosa. Antes de investigar o importador, precisamos entender como uma linha escrita se transforma em comandos, argumentos, fluxos de dados e decisões de execução.

Nos capítulos anteriores, separamos kernel, aplicações, identidades, arquivos e serviços. Agora vamos estudar uma das interfaces usadas para coordenar essas peças: o **shell**, que é ao mesmo tempo um interpretador de comandos e uma linguagem de programação. O terminal é a interface de interação; não é ele que decide sozinho o significado de uma variável ou de um `|`.

**A Aurora continua sendo um cenário fictício.** Os exemplos próprios deste capítulo são pequenos e independentes do sistema da biblioteca. Seus resultados reproduzidos e seus limites estão documentados; não são evidências de um incidente real.

A leitura não exige instalar outro sistema, mudar permissões ou executar um laboratório. Quando aparecer código, acompanharemos o que cada parte faz. Os blocos identificam **Bash**, **PowerShell** ou **texto**: não são três grafias intercambiáveis da mesma linguagem.

## Percurso de leitura

| Seção | Pergunta central |
| --- | --- |
| [14.1 · A janela não é o interpretador](14.1-terminal-shell-e-comandos.md) | Quem recebe a interação, interpreta a linha e executa o trabalho? |
| [14.2 · O programa não recebe a linha que você enxerga](14.2-argumentos-aspas-e-expansoes.md) | Como nomes, aspas e expansões constroem os argumentos? |
| [14.3 · A tela é só um dos destinos](14.3-fluxos-redirecionamentos-e-pipelines.md) | O que passa entre comandos e o que muda quando redirecionamos uma saída? |
| [14.4 · Terminar não é necessariamente dar certo](14.4-status-condicoes-e-controle.md) | Como representar resultados e decidir a próxima operação? |
| [14.5 · Da sequência digitada a um contrato repetível](14.5-scripts-contexto-e-repetibilidade.md) | O que um script precisa declarar para não depender de coincidências da sessão? |
| [14.6 · Automatizar sem transformar dados em ordens](14.6-automacao-e-fronteiras-de-confianca.md) | Como preservar interpretação, escopo e evidências ao automatizar? |

Os [exemplos opcionais](exemplos/README.md) usam argumentos e dados sintéticos. As [referências](referencias.md) registram o recorte das fontes. Há doze perguntas de raciocínio, com [respostas comentadas](solucoes.md) separadas.

**[Começar pela seção 14.1 →](14.1-terminal-shell-e-comandos.md)**
