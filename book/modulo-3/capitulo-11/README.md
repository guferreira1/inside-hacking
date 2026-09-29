# Capítulo 11 — O papel de um sistema operacional

[← Capítulo 10](../../modulo-2/capitulo-10/README.md) · [Índice do módulo](../README.md) · [Glossário](../../glossario.md)

**Módulo III — Sistemas operacionais**

> **Status:** DRAFT 0.1 — primeira entrega de leitura. Fontes e verificações delimitadas no [registro editorial](../../../editorial/reviews/capitulo-11.md). Revisão técnica independente pendente.

O importador da biblioteca Aurora funciona quando uma atendente o inicia no terminal. A equipe prepara o mesmo programa para trabalhar automaticamente depois de ligar o computador. Na manhã seguinte, o serviço inicia, mas não consegue abrir o arquivo do catálogo.

O programa não mudou. O arquivo continua no equipamento. O formato foi conferido. Por que o resultado mudou?

A pergunta conecta o módulo anterior ao que começamos agora. Conhecer os bytes e as instruções é necessário, mas ainda precisamos entender quem entrega recursos a uma execução, interpreta seus caminhos, aplica limites e organiza sua continuidade.

Neste cenário fictício, acompanharemos a relação entre a aplicação e o sistema operacional. Vamos descobrir por que o kernel não é a área de trabalho, por que chamar um serviço do sistema não transforma o programa em administrador e por que uma recusa pode indicar uma proteção funcionando, não um defeito a remover.

O percurso não exige instalação. Há um [exemplo opcional](exemplos/README.md), executado apenas sobre arquivos temporários próprios, para distinguir leitura, fim de arquivo e erros de operação. Os demais cenários são modelos explicados, não incidentes observados.

## Percurso de leitura

| Seção | Pergunta central |
| --- | --- |
| [11.1 · Um equipamento, muitas promessas](11.1-abstracoes-e-responsabilidades.md) | O que o sistema operacional oferece além de uma interface para clicar? |
| [11.2 · O pedido atravessa uma fronteira](11.2-interfaces-e-chamadas-de-sistema.md) | Como uma aplicação solicita um recurso e interpreta a resposta? |
| [11.3 · Executar também é esperar](11.3-recursos-espera-e-coordenacao.md) | Quem divide recursos e por que estar lento não significa falta de CPU? |
| [11.4 · Quem pede faz parte da operação](11.4-identidades-e-limites.md) | Como identidade, permissão e isolamento influenciam o resultado? |
| [11.5 · Ligar a máquina não é concluir o serviço](11.5-inicializacao-servicos-e-investigacao.md) | Como o sistema chega ao estado de funcionamento e como investigar a falha da Aurora? |

As [referências](referencias.md) identificam os contextos das interfaces Linux, dos exemplos Windows e da comparação com microkernel. Dez perguntas opcionais encerram o capítulo; as [respostas comentadas](solucoes.md) ficam separadas.

**[Começar pela seção 11.1 →](11.1-abstracoes-e-responsabilidades.md)**
