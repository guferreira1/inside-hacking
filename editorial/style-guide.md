# Style Guide

**Status:** guia de trabalho em evolução.

[Editorial](README.md) · [Modelo de capítulo](chapter-template.md) · [Política de glossário](glossary-policy.md)

## Voz

Português brasileiro, prosa técnica, didática e agradável. Profundidade não deve ser substituída por listas de definições. Alternar explicação e exemplo quando isso favorecer a compreensão; não transformar todo parágrafo em aviso, regra ou metacomentário editorial.

## Princípios

1. Explicar o sistema antes de explicar como ele falha.
2. Explicar mecanismos antes de apresentar ferramentas.
3. Introduzir termos e siglas antes de depender deles.
4. Distinguir observação, inferência e hipótese.
5. Não inventar resultados de laboratório nem criar laboratório apenas para preencher uma estrutura.
6. Não apresentar uma técnica como universal quando depende de versão, configuração ou contexto.
7. Usar referências para fundamentar e verificar; escrever explicações autorais.
8. Relacionar ataque, impacto, mitigação e detecção quando aplicável.
9. Diferenciar claramente exemplos fictícios de casos reais.
10. Prática ofensiva deve permanecer em ambientes autorizados.

## Módulos, capítulos e subcapítulos

Seguir `book/modulo-M/capitulo-N/`, com numeração global dos capítulos. Subcapítulos devem representar unidades conceituais úteis. Não existe quantidade mínima ou máxima fixa. A divisão deve melhorar leitura, estudo, revisão, navegação no GitHub e manutenção da obra.

## Ferramentas

Ferramentas serão ensinadas pelo problema que ajudam a investigar, pelo mecanismo relevante, pela interpretação das saídas e por suas limitações. O livro não será um catálogo de comandos. Distinguir ferramenta, protocolo, técnica, vulnerabilidade e instituição.

## História

Contexto histórico será usado quando ajudar a explicar por que uma tecnologia, comportamento ou problema existe. Não será incluído apenas para preencher cronologia.

## Glossário

O glossário serve para consulta e revisão, nunca para substituir a primeira explicação adequada de um conceito. **Atualizá-lo junto com cada capítulo novo ou alterado**, usando apenas termos efetivamente presentes e identificando menções introdutórias. A [política de glossário](glossary-policy.md) define ocorrência, fontes, grafia, expansão de siglas e segunda conferência.

## Prática e laboratórios

A prática deve existir quando houver algo útil e reproduzível a observar ou executar. Laboratório não é requisito para todos os capítulos. Em capítulos fundamentais ou conceituais, exemplos, cenários, exercícios mentais, análise de comportamento e interpretação de evidências podem ser suficientes para o objetivo editorial.

Quando um laboratório for incluído, documentar o ambiente. Distinguir uma previsão fundamentada do resultado de uma execução. A equipe pode explicar o comportamento esperado sem ter executado um teste, desde que não o apresente como observação e registre o limite de validação.

## Notas de produção e estados

Manter status e avisos necessários breves, com vínculo ao controle editorial. Feedback pessoal de leitores, histórico de revisão e detalhes de manutenção ficam em `editorial/`, não interrompem a narrativa do livro. Não apagar pendências reais nem chamar a revisão assistida por IA de revisão independente.

## Segunda passagem

Depois de editar, verificar novamente navegação, âncoras, índices, nomes, estados e glossário. Uma checagem automática de links não substitui a revisão factual ou a leitura visual de uma futura edição em PDF.
