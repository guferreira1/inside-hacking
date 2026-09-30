# Primeira entrega editorial — Capítulo 16

**Primeira entrega:** 29/09/2026. **Estado atual:** VALIDATED — versão editorial 1.0; ciclo interno concluído em 29/09/2026. **Módulo:** III.

[Manuscrito](../../book/modulo-3/capitulo-16/README.md) · [Referências](../../book/modulo-3/capitulo-16/referencias.md) · [Exemplos](../../book/modulo-3/capitulo-16/exemplos/README.md)

## Recorte e continuidade

Sete seções desenvolvem ciclos de vida, supervisão, prontidão, configuração e reinício, agendamento, logs e tempo, estado confirmado e recuperação. Quatorze perguntas com respostas comentadas. O próximo capítulo continua sendo 17 — Virtualização e isolamento; nenhum título foi reorganizado.

O pedido de avançar confirma a aprovação de leitura do capítulo 15. Sua validação técnica anterior e seus limites são preservados; nova regressão é registrada separadamente. Não foram informadas horas, resolução de exercícios, execução de labs ou autonomia do leitor. Aprovação editorial não é classificação de domínio prático.

## Pesquisa

Quarenta e quatro referências numeradas, baseadas em Linux man-pages, documentação upstream de systemd, procps-ng, Cronie e logrotate reproduzida no man7, Microsoft Learn, Python, SQLite e OWASP. A abertura direta de cinco manuais no freedesktop retornou 403; os textos originais foram consultados nas reproduções identificadas. As páginas systemd consultadas identificam uma versão de desenvolvimento, não a versão instalada ou recomendada ao leitor. Interfaces usadas têm seu escopo descrito; não se assume o padrão de configuração de toda distribuição.

A consulta pontual não significa leitura integral de todos os manuais. Documentação Python consultada em /3/ e referências PowerShell com view=7.5 não são confundidas com versões executadas.

Foram separados processo e serviço, estado ativo e prontidão, configuração armazenada e aplicada, agendamento e lote, origem do log e veracidade do conteúdo, relógio de calendário e monotônico, escrita/atomicidade/durabilidade, efeito confirmado e resposta recebida. A narrativa Aurora é fictícia. Não houve criação de serviços, agendamentos ou procedimentos ofensivos.

## Execução local observada

Linux 6.18.44 x86-64, glibc 2.41, Python 3.13.5 e SQLite 3.46.1. O container local utilizava EUID 0; os testes não necessitam desse privilégio e atuam somente sobre filhos e arquivos temporários próprios. Diferentemente dos testes de permissão do capítulo 15, os casos deste capítulo não comparam concessões e recusas entre identidades; a condição do lançador não foi escondida.

Os **14 testes novos passaram**, sem skips ou falhas. `estado_proprio.py` também foi executado separadamente. O total foi 0 após interrupção antes do commit; 5 depois da confirmação do segundo lote sem resposta; e permaneceu 5 depois de repetir esse lote. Os resultados são obtidos por consulta ao SQLite.

O filho termina por os._exit somente nos dois pontos explicitamente selecionados. Não há corte de energia, injeção de corrupção física, controle de cache do dispositivo ou teste de concorrência entre escritores. O exemplo não valida semântica distribuída nem efeitos externos à transação.

As consultas e configurações systemd, cron, SCM e Windows Event Log são explicações documentais. Não foram instaladas ou executadas no host do leitor. Nenhum serviço alheio foi parado e nenhum registro real foi limpo ou alterado.

## Revisão e documentação

READMEs, índices, glossário, bibliografia, matriz de cobertura e estados acompanham a entrega. Os verbetes adicionados exigem ocorrência textual e vínculo à seção. A checagem automática cobre navegação e regressão, não revisão técnica independente. O capítulo 1 conserva sua pendência, o Módulo II conserva seu fechamento e o Módulo III continua em produção.

A verificação de conjunto e o estado da integração serão registrados na auditoria desta entrega depois da execução, sem antecipar sucesso de CI. Não houve publicação no LinkedIn nem geração de PDF.

## Verificação de conjunto

Os resultados executados constam na [auditoria desta entrega](../audits/2026-09-29-capitulo-16.md) e no [registro de verificações](../updates/capitulo-16-checks.json). A integração em main e a checagem posterior são etapas distintas.

## Aprovação e reconferência interna

O pedido de continuidade confirma a aprovação da leitura. As sete seções e quatorze respostas foram relidas, preservando o conteúdo e os limites dos experimentos. Fontes e execuções da entrega anterior não são apresentadas como novas execuções; a regressão desta rodada está na [auditoria do capítulo 17](../audits/2026-09-29-capitulo-17.md). Não foram atribuídas horas ou competência prática não relatadas. Revisão técnica independente permanece pendente.
