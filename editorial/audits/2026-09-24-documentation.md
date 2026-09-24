# Auditoria de documentação e glossário

**Data da execução:** 24/09/2026 (UTC).  
**Base:** `8143687b4bb1f9a31f2eaf95885691d0510221f6`.  
**Escopo:** Markdown, navegação, coerência de apresentação/estados e glossário. Não é fechamento factual integral dos capítulos.

[Editorial](../README.md) · [Glossário](../../book/glossario.md) · [Política de terminologia](../glossary-policy.md)

## Primeira passagem

A execução [35949096475](https://github.com/guferreira1/inside-hacking/actions/runs/35949096475), no commit `4eabc2eda85dbdc47bad122cc338b25e5404b780`, percorreu os **49 arquivos Markdown** da base. O verificador encontrou **232 destinos internos distintos por arquivo**, com **zero destinos ou âncoras inválidos** nas formas de Markdown reconhecidas. O glossário possuía **11 verbetes**.

A verificação foi executada em runner do GitHub Actions. O ambiente local de trabalho não conseguiu clonar o repositório por indisponibilidade de resolução de rede; não foi declarado um clone local inexistente como evidência.

## Achados e correções

| Área | Achado | Ação |
| --- | --- | --- |
| Glossário | Cobertura pequena diante dos termos já citados. | Definições originais com expansão de siglas, ocorrência e contexto; preservação dos 11 conceitos anteriores. |
| Escopo do glossário | Risco de importar tópicos ainda não ensinados. | Nenhuma importação em massa do outline; OSINT identificado como menção do planejamento, em resposta à dúvida de terminologia. |
| Capítulo 1 | Sem links de continuidade; cabeçalho sugeria fact-check encerrado apesar de pendências. | Navegação, vínculo ao glossário e status REVIEW coerente com o controle editorial. |
| Capítulo 1 | Formulações imprecisas sobre terminal e sobre testar hipóteses. | Separação de interface e interpretador; redação que distingue contrariar uma hipótese de falsificar registros. |
| Capítulo 3 | Página de referências ainda dizia DRAFT, embora o fechamento interno já estivesse registrado. | Sincronização do estado, preservando a pendência de revisão jurídica independente. |
| Capítulo 3 | Nota de bastidores sobre cansaço de leitura no corpo do livro. | Removida da abertura; feedback permanece no registro editorial já existente. |
| Contribuição | Glossário não era item obrigatório de entrega. | Política, template, guia de estilo e checklist de PR atualizados. |
| Diretórios auxiliares | README sem caminho de retorno para leitura ou editorial. | Links de navegação e delimitação do que realmente existe. |
| Comunicação | Arquivo de lançamento ainda se apresentava apenas como rascunho. | Registro do post feito pelo mantenedor, conforme relato/captura, sem alegar publicação por ferramenta. |
| Automação | Sem checagem permanente de Markdown. | Verificador local, testes sintéticos e workflow de leitura em push/PR. |

## Links externos

As referências externas da base foram inventariadas e submetidas a tentativas de abertura. A recuperação de uma página confirma acesso nesta consulta, não correção integral do conteúdo, estabilidade futura ou leitura completa de um PDF.

Duas páginas históricas do TMRC não retornaram dentro do limite de tempo, mesmo com nova tentativa:

- https://tmrc.mit.edu/old/hackers-ref.html
- https://tmrc.mit.edu/old/history/index.html

Elas permanecem como **acessibilidade inconclusiva**, não como links definitivamente mortos. Os demais documentos históricos e fontes consultadas não foram substituídos silenciosamente por resumos.

A referência adicional de ransomware da CISA foi localizada por busca, mas a abertura direta retornou 403 nesta consulta: https://www.cisa.gov/stopransomware/ransomware-guide. Um bloqueio de acesso automatizado não prova remoção da página. O link do post no LinkedIn é um registro informado pelo mantenedor; não foi tratado como página pública recuperável nesta auditoria.

A explicação de OSINT foi conferida no documento oficial ICS 206-01, Apêndice A, página impressa 6: https://archive.dni.gov/files/documents/ICD/ICS-206-01.pdf. OWASP foi conferido na página da própria fundação: https://owasp.org/about. Não foram adicionadas entradas VASP ou Zint como supostos sinônimos dessas siglas.

## Segunda passagem e reprodução

Após as correções, a execução [35950478332](https://github.com/guferreira1/inside-hacking/actions/runs/35950478332), no commit `34ffa50917aaccbaa208281bac4211678f0c76d5`, terminou com **success**. Os logs registram **52 arquivos Markdown**, **314 destinos internos distintos por arquivo**, **zero erros internos** e **115 verbetes no glossário**. Os **seis testes automatizados do próprio verificador passaram**. Essas contagens descrevem esse commit, não uma promessa de tamanho final da obra.

Os testes sintéticos verificam detecção de destino/âncora ausente, links HTML, referências Markdown, títulos duplicados, exclusão de exemplos em blocos de código e caminhos que escapam da raiz. Exemplos deliberadamente inválidos pertencem às fixtures de teste, não à navegação publicada.

O [workflow de checagem](../../.github/workflows/docs-check.yml) repete a validação a cada push e pull request. O histórico de [execuções](https://github.com/guferreira1/inside-hacking/actions/workflows/docs-check.yml) permite conferir resultados de commits posteriores, inclusive esta atualização do relatório.

Para repetir: `python3 -m unittest discover -s scripts/tests -v` e `python3 scripts/check_docs.py --inventory` a partir da raiz. O verificador cobre o subconjunto de Markdown adotado pelo projeto, não todas as extensões possíveis de GFM. URLs externas são apenas inventariadas pelo script; a consulta de rede descrita acima foi separada. Sucesso do workflow não é validação semântica automática das definições nem certificação técnica do manuscrito.

## Limites e continuidade

Não houve laboratório ofensivo, PDF ou revisão independente de todo o conteúdo. A lista de termos é uma revisão editorial baseada em ocorrência e contexto, não prova automática de que nenhum conceito adicional possa merecer explicação. A regra permanente é atualizar e conferir o glossário em cada nova entrega.

Capítulos 4 e 5 permanecem **DRAFT, pendentes da primeira leitura do mantenedor**. Capítulos 2 e 3 mantêm seu fechamento interno, e o 1 continua REVIEW. Esta auditoria não encerra capítulos nem o Módulo I.
