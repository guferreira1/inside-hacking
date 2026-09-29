# Auditoria final do Módulo II — Computadores por dentro

**Data:** 28/09/2026.  
**Escopo:** capítulos 6 a 10 e todos os Markdown sob `book/modulo-2/`.  
**Base auditada:** `694f6e8a5e5756e64f89d27236ae574abb306efb`.

[← Estado editorial](../publication-status.md) · [Módulo II](../../book/modulo-2/README.md)

## Objetivo

Executar uma segunda passagem antes do marco público do módulo: revisar ortografia e fluidez, coerência técnica e didática, exemplos e soluções, terminologia, navegação, links internos, referências externas e regressão dos testes. Esta é uma revisão interna; não é revisão técnica independente.

## Leitura editorial

Foram relidos os **44 arquivos Markdown** do Módulo II, incluindo aberturas, subcapítulos, soluções, referências e READMEs dos exemplos. O percurso permaneceu coerente: representação → hardware → construção/execução → memória/processos → arquivos/formatos/serialização.

Não foram identificados erros conceituais que exigissem reescrever conclusões. Foram aplicados dois refinamentos pequenos de redação:

- no capítulo 10.4, “três entradas” passou a “três representações” para evitar ambiguidade;
- no capítulo 10.6, a descrição do teste de compressão foi reescrita para deixar claro que `Livro\n` forma a sequência de seis bytes repetida vinte vezes.

Os ajustes não mudam os mecanismos ensinados nem os resultados dos exemplos.

## Navegação e Markdown

A checagem permanente do repositório foi executada sobre a base da auditoria:

- **60 testes aprovados**;
- **113 arquivos Markdown** examinados pelo verificador global;
- **888 destinos internos** conferidos;
- **0 erros internos** de caminho ou âncora;
- **373 verbetes** no glossário global.

Uma verificação adicional de higiene percorreu os 44 Markdown do Módulo II e não encontrou tabulações, espaços residuais ou repetição acidental de palavras fora dos blocos de código. Alinhamentos intencionais dentro de exemplos monoespaçados foram preservados.

## Links externos

Foram inventariadas e consultadas **102 URLs externas únicas** presentes no Módulo II.

- **100** responderam normalmente ao verificador automatizado;
- **2** páginas da Kingston responderam HTTP 403 ao agente do runner, comportamento compatível com bloqueio automatizado e não com ausência do recurso;
- as duas páginas foram reconferidas por uma segunda rota e continuavam acessíveis com seus títulos e conteúdo.

URLs reconferidas:

- https://www.kingston.com/en/blog/pc-performance/ssd-form-factors
- https://www.kingston.com/en/blog/pc-performance/ssd-garbage-collection-trim-explained

O workflow temporário da auditoria está registrado em https://github.com/guferreira1/inside-hacking/actions/runs/36508065269. Ele não faz parte do workflow permanente da obra.

## Exemplos, fontes e limites

Os testes existentes dos capítulos 6 a 10 voltaram a passar na suíte de regressão. Os capítulos continuam distinguindo modelos didáticos de observações executadas; nenhum resultado novo de laboratório foi inventado nesta auditoria.

As páginas de referências mantêm o uso delimitado de documentação Linux, GNU/GCC, Microsoft, Python, RFC Editor, W3C, Unicode, NIST, OWASP, CWE e materiais auxiliares já registrados. A disponibilidade de uma URL não substitui avaliação da afirmação que ela sustenta; essa relação foi relida no contexto de cada capítulo.

O glossário foi conferido junto da releitura. Não foi identificado termo técnico já exigido pelo Módulo II que justificasse novo verbete nesta passagem; nenhuma entrada futura foi adicionada apenas para aumentar a lista.

## Estado resultante

Os capítulos 6, 7, 8, 9 e 10 possuem leitura aprovada e ciclo interno da versão editorial 1.0 encerrado. Com esta segunda passagem, o **Módulo II — Computadores por dentro** fica internamente concluído.

Esse estado não significa revisão técnica independente, publicação de PDF ou release estável. Essas etapas permanecem futuras e podem reabrir capítulos se revelarem correções necessárias.
