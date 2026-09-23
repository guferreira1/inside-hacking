# Capítulo 5 · Referências e limites da pesquisa

[← Índice do capítulo](README.md) · [Bibliografia geral](../bibliografia.md)

**Consulta:** 23 de setembro de 2026. **Versão do capítulo:** DRAFT 0.1.

As definições abaixo foram consultadas para orientar uma explicação original. As situações da biblioteca Aurora são fictícias, inclusive as mudanças de configuração, os caminhos de exploração e as comparações de risco. Não descrevem testes executados. Nenhum laboratório foi criado ou necessário para esta entrega conceitual.

O glossário do NIST agrega definições de documentos distintos. As entradas identificadas abaixo permitem localizar os contextos usados; citar a página não equivale a afirmar leitura integral de todas as publicações que ela referencia. Não tratamos todas as variantes de um termo como uma definição universal.

<a id="s1"></a>
## S1 · Ativos

NIST CSRC. *Asset — Glossary*.

https://csrc.nist.gov/glossary/term/asset

Trechos usados: definições de valor para pessoas, organizações e partes interessadas, incluindo itens tangíveis e intangíveis; entradas associadas a SP 800-160. Aplicação: seção 5.1. A escolha dos ativos da Aurora é parte do exemplo autoral, não inventário de uma organização real.

<a id="s2"></a>
## S2 · Segurança da informação

NIST CSRC. *Information security — Glossary*.

https://csrc.nist.gov/glossary/term/information_security

Trecho usado: definição que relaciona proteção contra acesso, uso, divulgação, interrupção, modificação e destruição indevidos a confidencialidade, integridade e disponibilidade. Aplicação: introdução dessas propriedades na seção 5.1. Não se pretende esgotar suas definições ou todas as propriedades de segurança.

<a id="s3"></a>
## S3 · Vulnerabilidade

NIST CSRC. *Vulnerability — Glossary*.

https://csrc.nist.gov/glossary/term/vulnerability

Trechos usados: fraqueza em sistemas, procedimentos, controles ou implementação que pode ser explorada ou acionada por uma fonte de ameaça; entradas relacionadas a SP 800-30 Rev. 1 e SP 800-115. Aplicação: seção 5.1. Uma vulnerabilidade não depende da disponibilidade pública de um exploit para existir; esta última observação decorre da distinção entre condição e demonstração, não da execução de um ataque.

<a id="s4"></a>
## S4 · Ameaça e fonte de ameaça

NIST CSRC. *Threat — Glossary* e *Threat source — Glossary*.

https://csrc.nist.gov/glossary/term/threat

https://csrc.nist.gov/glossary/term/threat_source

Trechos usados: circunstância ou evento com potencial de consequência adversa; exploração intencional e acionamento acidental de fraquezas. Aplicação: seção 5.2. Os atores e eventos da Aurora foram construídos para distinguir os conceitos; não são afirmações sobre frequência de ataques.

<a id="s5"></a>
## S5 · Verificação de autorização

OWASP Cheat Sheet Series. *Authorization Cheat Sheet*.

https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html

Seções consultadas: Introduction; Validate the Permissions on Every Request; Ensure Lookup IDs are Not Accessible Even When Guessed or Cannot Be Tampered With; Verify that Authorization Checks are Performed in the Right Location. Aplicação: distinção entre autenticação e autorização, permissões sobre objetos e controles no ponto adequado, nas seções 5.1 e 5.3. Não se afirma que exista um laboratório Aurora implementado.

<a id="s6"></a>
## S6 · Famílias de fraquezas

CWE Program. *About CWE*.

https://cwe.mitre.org/about/index.html

Trecho usado: descrição da CWE como lista e taxonomia de fraquezas de software e hardware que podem contribuir para vulnerabilidades. Aplicação: seção 5.1. Não foram atribuídos IDs CWE específicos ao caso fictício nesta entrega.

<a id="s7"></a>
## S7 · Identificação de vulnerabilidades

NIST CSRC. *Common vulnerabilities and exposures (CVE) — Glossary*.

https://csrc.nist.gov/glossary/term/common_vulnerabilities_and_exposures

Trecho usado: identificação comum de vulnerabilidades publicamente conhecidas, com registros contendo identificador, descrição e referências. Aplicação: distinção introdutória de CWE e CVE na seção 5.1. Não foram descritos processos atuais de atribuição, financiamento ou governança do programa.

<a id="s8"></a>
## S8 · Exploit e payload no contexto de uma ferramenta

Rapid7. *Glossary — Metasploit Documentation*. Verbetes Exploit, Exploit Module e Payload.

https://docs.rapid7.com/metasploit/glossary/

Rapid7. *Working with Payloads — Metasploit Documentation*.

https://docs.rapid7.com/metasploit/working-with-payloads/

Aplicação: separação de responsabilidades no vocabulário da ferramenta, na seção 5.2. O capítulo usa uma definição operacional de exploit mais ampla que um módulo específico. Não generaliza payload como requisito de toda vulnerabilidade, nem adota afirmações sobre indetectabilidade, estabilidade ou atualidade de exemplos presentes nessas páginas. Não houve execução do Metasploit.

<a id="s9"></a>
## S9 · Superfície de ataque

OWASP Cheat Sheet Series. *Attack Surface Analysis Cheat Sheet*.

https://cheatsheetseries.owasp.org/cheatsheets/Attack_Surface_Analysis_Cheat_Sheet.html

Seções consultadas: What is Attack Surface Analysis and Why is it Important; Defining the Attack Surface of an Application; Identifying and Mapping the Attack Surface. Aplicação: seção 5.3, com foco em interfaces, dados, controles e perfis de acesso. A própria fonte declara seu recorte em aplicações e distingue superfícies internas e externas. Sua relação histórica de ferramentas não foi adotada como recomendação atual.

<a id="s10"></a>
## S10 · Risco

NIST CSRC. *Risk — Glossary*.

https://csrc.nist.gov/glossary/term/risk

Trechos usados: definições associadas à SP 800-30 Rev. 1 que relacionam consequências adversas e possibilidade de ocorrência. Aplicação: seção 5.3. O capítulo não estima probabilidades, não calcula perdas e não apresenta uma fórmula quantitativa universal. Comparações são raciocínios sobre premissas fictícias.

<a id="s11"></a>
## S11 · Severidade e contexto

FIRST. *CVSS v4.0 User Guide*.

https://www.first.org/cvss/v4.0/user-guide

Seção usada: CVSS Base Score (CVSS-B) Measures Severity, not Risk, incluindo a distinção entre características intrínsecas e métricas de ameaça e ambiente. Aplicação: seção 5.3. Nenhum escore foi calculado ou atribuído a um sistema. A referência identifica a versão consultada, sem afirmar que o capítulo ensina integralmente sua especificação.

<a id="s12"></a>
## S12 · Risco residual

NIST CSRC. *Residual risk — Glossary*.

https://csrc.nist.gov/glossary/term/residual_risk

Trechos usados: risco que permanece depois da aplicação de medidas ou respostas; entrada associada à SP 800-30 Rev. 1. Aplicação: seção 5.3. Não se atribuiu eficácia mensurada aos controles imaginados na narrativa.

## Verificação desta entrega

As páginas acima foram consultadas, a redação foi revisada internamente e as distinções técnicas foram relacionadas às fontes. Não houve revisão independente, avaliação de um sistema real, execução de exploração ou medição de risco. O capítulo permanece DRAFT para leitura e revisão; as fontes não representam endosso institucional à obra.
