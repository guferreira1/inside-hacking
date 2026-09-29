# Capítulo 12 — Linux por dentro

[← Capítulo 11](../capitulo-11/README.md) · [Capítulo 13 →](../capitulo-13/README.md) · [Índice do módulo](../README.md) · [Glossário](../../glossario.md)

**Módulo III — Sistemas operacionais**

> **Status:** VALIDATED — versão editorial 1.0; leitura aprovada e ciclo interno concluído em 29/09/2026. Fontes e limites no [registro editorial](../../../editorial/reviews/capitulo-12.md). Revisão técnica independente pendente.

A biblioteca Aurora prepara uma segunda instalação de seu sistema. A equipe copia o programa, organiza seus arquivos e conecta uma unidade com uma exportação do catálogo. A atendente encontra o documento no gerenciador de arquivos, mas o serviço automático procura o mesmo nome e não o encontra.

Alguém resume a situação: “os dois usam Linux; deveria funcionar igual”.

A frase parece razoável, mas esconde várias perguntas. É o mesmo kernel? Os mesmos programas estão instalados? O caminho começa na mesma raiz? O dispositivo foi apenas reconhecido ou seu sistema de arquivos já foi incorporado à árvore? O serviço enxerga essa incorporação?

No capítulo anterior, aprendemos a separar operação, identidade, recurso e contexto. Agora vamos encontrar essas peças dentro de uma instalação Linux. A história da Aurora continua fictícia; seu papel é conduzir a explicação, não simular evidências de um incidente.

Não vamos trocar seu sistema, montar discos nem instalar pacotes. A leitura é completa por si só. Um pequeno exemplo opcional consulta apenas um descritor do próprio processo, para observar uma das interfaces que estudaremos.

## Percurso de leitura

| Seção | Pergunta central |
| --- | --- |
| [12.1 · Linux é o núcleo de qual sistema?](12.1-kernel-distribuicao-e-contexto.md) | O que é compartilhado entre instalações e o que depende da distribuição? |
| [12.2 · Uma árvore de nomes, várias origens](12.2-diretorios-e-montagens.md) | Como caminhos, diretórios e montagens se relacionam? |
| [12.3 · Arquivos que mostram o sistema em funcionamento](12.3-proc-sys-e-dev.md) | Por que nem tudo que parece arquivo é um documento guardado no disco? |
| [12.4 · Do dispositivo ao serviço](12.4-drivers-modulos-e-servicos.md) | Quem reconhece o equipamento, oferece suas interfaces e inicia o trabalho? |
| [12.5 · Instalar, atualizar e investigar sem adivinhar](12.5-pacotes-atualizacoes-e-investigacao.md) | Como relacionar software instalado, execução atual e confiança? |

As [referências](referencias.md) identificam o recorte de cada fonte. Ao final há dez perguntas opcionais, com [respostas comentadas](solucoes.md) separadas.

**[Começar pela seção 12.1 →](12.1-kernel-distribuicao-e-contexto.md)**
