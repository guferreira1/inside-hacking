# Capítulo 17 — Virtualização e isolamento

[← Capítulo 16](../capitulo-16/README.md) · [Índice do módulo](../README.md) · [Glossário](../../glossario.md)

**Módulo III — Sistemas operacionais**

> **Status:** DRAFT 0.1 — primeira entrega de leitura. Fontes, execução e limites no [registro editorial](../../../editorial/reviews/capitulo-17.md). Revisão técnica independente pendente.

A biblioteca Aurora prepara um ambiente para testar uma nova versão do importador. A equipe cria uma máquina virtual, copia o programa e compartilha a pasta dos catálogos para não precisar transferir arquivos a cada tentativa. Antes do teste, salva um snapshot.

O importador altera um catálogo que não deveria alterar. A equipe restaura o snapshot, abre novamente a pasta compartilhada e descobre que o documento continua modificado.

“Mas não estava tudo dentro da máquina virtual?”

A pergunta revela a diferença entre executar em um ambiente separado e saber exatamente o que foi separado. A máquina pode ter seu próprio sistema operacional e, ao mesmo tempo, receber acesso a arquivos, dispositivos e redes que existem fora dela.

**A Aurora é um cenário fictício.** O incidente e as configurações usados na narrativa são premissas didáticas, não resultados de um teste real. Vamos explicar as peças que tornam essa história possível: máquinas virtuais, hipervisores, containers, namespaces, limites de recursos, compartilhamentos e recuperação de estado.

A leitura não exige instalar um virtualizador, executar imagens desconhecidas nem alterar a rede do computador. O exemplo opcional observa apenas namespaces do próprio processo e de um filho criado por ele, sem criar containers ou modificar o isolamento existente.

## Percurso de leitura

| Seção | Pergunta central |
| --- | --- |
| [17.1 · Separado de quê, protegido contra quem?](17.1-virtualizacao-e-fronteiras.md) | Que diferença existe entre representar um recurso, separar ambientes e restringir ações? |
| [17.2 · Um computador apresentado por outro](17.2-maquinas-virtuais-e-hipervisores.md) | Como um sistema convidado executa sobre recursos administrados por outra camada? |
| [17.3 · Processos com visões e limites próprios](17.3-containers-namespaces-e-recursos.md) | O que um container separa sem necessariamente possuir seu próprio kernel? |
| [17.4 · As passagens que nós mesmos abrimos](17.4-compartilhamentos-e-autoridade.md) | Como arquivos, dispositivos e interfaces de administração atravessam a fronteira? |
| [17.5 · Uma rede virtual continua sendo uma rede](17.5-conectividade-e-alcance.md) | Quem pode conversar com o ambiente, e a quem ele consegue alcançar? |
| [17.6 · Voltar no tempo tem um alcance](17.6-imagens-snapshots-e-recuperacao.md) | O que uma imagem ou um snapshot conserva, e o que permanece fora da restauração? |
| [17.7 · Conferir a fronteira antes de confiar nela](17.7-investigacao-e-verificacao.md) | Como transformar uma expectativa de isolamento em perguntas verificáveis? |

As [referências](referencias.md) identificam o recorte de cada fonte. Há um [exemplo opcional](exemplos/README.md), quatorze perguntas e [respostas comentadas](solucoes.md). A próxima unidade, após este capítulo, é **18 — Como computadores se comunicam**, na sequência original do livro.

**[Começar pela seção 17.1 →](17.1-virtualizacao-e-fronteiras.md)**
