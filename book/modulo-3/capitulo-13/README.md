# Capítulo 13 — Windows por dentro

[← Capítulo 12](../capitulo-12/README.md) · [Índice do módulo](../README.md) · [Glossário](../../glossario.md)

**Módulo III — Sistemas operacionais**

> **Status:** DRAFT 0.1 — primeira entrega de leitura. Fontes e limites de verificação no [registro editorial](../../../editorial/reviews/capitulo-13.md). Revisão técnica independente pendente.

A biblioteca Aurora recebeu uma versão de seu importador para Windows. A atendente abre o programa, escolhe um arquivo e vê o catálogo atualizado. A equipe então configura a execução automática. O processo aparece em funcionamento, mas nenhum livro novo chega ao catálogo.

Na discussão, surgem três explicações: “faltou instalar alguma coisa”, “o serviço precisa de administrador” e “o Windows não encontrou o arquivo”. Todas parecem possíveis. Nenhuma está demonstrada.

O programa que abre uma janela e o trabalho executado sem essa janela podem depender de componentes parecidos e, ainda assim, usar identidades, configurações e nomes diferentes. Para investigar, precisamos conhecer mais do que o botão que inicia o aplicativo.

Neste capítulo, vamos acompanhar essas peças por dentro do Windows. O objetivo não é traduzir cada diretório do Linux para um nome parecido, mas entender a organização própria deste sistema: objetos e handles, executáveis e bibliotecas, contas e tokens, caminhos e perfis, Registro e serviços.

**A Aurora é um cenário fictício.** Os detalhes apresentados ao longo da história são premissas didáticas, não resultados de um incidente ou laboratório executado. A base técnica foi pesquisada na documentação oficial; não é necessário ter um computador Windows para acompanhar a leitura.

## Percurso de leitura

| Seção | Pergunta central |
| --- | --- |
| [13.1 · O sistema não termina na área de trabalho](13.1-arquitetura-processos-e-objetos.md) | Como aplicações, componentes do sistema e recursos se relacionam? |
| [13.2 · Um caminho também carrega contexto](13.2-volumes-caminhos-e-perfis.md) | O que uma letra de unidade ou uma pasta realmente identifica? |
| [13.3 · O executável não trabalha sozinho](13.3-executaveis-bibliotecas-e-carregamento.md) | O que precisa acontecer para um arquivo se tornar uma aplicação em funcionamento? |
| [13.4 · A identidade de uma execução](13.4-contas-tokens-e-controle-de-acesso.md) | Como Windows distingue quem pede, o que foi pedido e o acesso permitido? |
| [13.5 · Configuração tem lugar, tipo e momento](13.5-registro-ambiente-e-configuracao.md) | Por que uma configuração visível para uma pessoa pode não valer para outro processo? |
| [13.6 · Do sistema iniciado ao trabalho concluído](13.6-inicializacao-servicos-e-investigacao.md) | Como separar inicialização, serviço, sessão, logs e resultado da aplicação? |

As [referências](referencias.md) relacionam as afirmações à documentação consultada. Ao final, há doze perguntas de raciocínio, com [respostas comentadas](solucoes.md) separadas.

**[Começar pela seção 13.1 →](13.1-arquitetura-processos-e-objetos.md)**
