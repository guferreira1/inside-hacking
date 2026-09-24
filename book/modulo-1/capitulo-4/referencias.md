# Capítulo 4 · Referências e limites da pesquisa

[← Índice do capítulo](README.md) · [Bibliografia geral](../../bibliografia.md)

**Consulta inicial:** 23/09/2026. **Reconferência e fechamento interno:** 24/09/2026. **Versão:** VALIDATED 1.0 editorial.

O percurso da Aurora é uma construção didática original. Contas, documentos, mensagens, identidades e desfechos foram definidos para explicar o raciocínio; não são registros de uma aplicação implementada. As fontes abaixo sustentam conceitos delimitados. Não representam endosso à obra, leitura integral de todos os documentos citados por elas ou revisão independente.

<a id="s1"></a>
## S1 · Identidade, permissão e regra esperada

OWASP Cheat Sheet Series. *Authorization Cheat Sheet*.

https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html

**Trechos consultados:** Introduction; Validate the Permissions on Every Request; recomendações sobre verificação de autorização. **Uso:** seção 4.1, para distinguir reconhecimento de identidade de permissão de ação e explicar por que certos recursos podem ser públicos. A política dos comprovantes é fictícia, não imposta pela OWASP.

<a id="s2"></a>
## S2 · Planejar o que será observado

NIST/SEMATECH. *e-Handbook of Statistical Methods*, seção 5.1.1, *What is experimental design?*.

https://www.itl.nist.gov/div898/handbook/pri/section1/pri11.htm

**Trecho consultado:** definição inicial de planejamento experimental, objetivos, fatores e respostas. **Uso:** seção 4.2. A comparação do capítulo não é um estudo estatístico nem uma aplicação integral de design de experimentos; é um exemplo lógico construído com condições explícitas. Não foram utilizadas as equações da página nem calculadas estimativas.

<a id="s3"></a>
## S3 · O limite de alterar um fator de cada vez

NIST/SEMATECH. *e-Handbook of Statistical Methods*, seção 5.2.1.2, *One variable at a time*.

https://www.itl.nist.gov/div898/handbook/pri/section2/pri212.htm

**Trecho consultado:** texto sobre interações entre fatores e limitações da abordagem OFAT. **Uso:** ressalva da seção 4.2. Isolar uma diferença pode ajudar um diagnóstico; isso não garante caracterizar comportamentos que dependem de combinações. Não foram extraídos resultados de gráficos nem reproduzidos experimentos da página.

<a id="s4"></a>
## S4 · Associação não basta para estabelecer causa

NIST/SEMATECH. *e-Handbook of Statistical Methods*, seção 1.3.3.26, *Scatter Plot*.

https://www.itl.nist.gov/div898/handbook/eda/section3/scatterp.htm

**Trecho consultado:** Causality Is Not Proved By Association. **Uso:** seção 4.3, na distinção entre uma diferença de duração e uma explicação causal. Não foram utilizados os dados, gráficos ou regressões do manual. Os tempos mencionados no capítulo são números fictícios, não medições.

<a id="s5"></a>
## S5 · Falso positivo

NIST CSRC. *False Positive — Glossary*.

https://csrc.nist.gov/glossary/term/false_positive

**Trecho consultado:** definição associada à SP 800-115, sobre alerta que indica incorretamente uma vulnerabilidade. **Uso:** seção 4.3. A consulta ao verbete não foi registrada como leitura integral de todas as publicações listadas. O exemplo do verificador é autoral.

<a id="s6"></a>
## S6 · Falso negativo

NIST CSRC. *False Negative — Glossary*.

https://csrc.nist.gov/glossary/term/false_negative

**Trechos consultados:** definições relacionadas à SP 800-83 Rev. 1 e SP 800-86, sobre falha de detecção e classificação incorreta. **Uso:** seção 4.3. Não foram estimadas taxas de falsos positivos ou negativos; resultado inconclusivo não foi automaticamente classificado como erro de detecção.

<a id="s7"></a>
## S7 · Mensagens e códigos HTTP

FIELDING, Roy T.; NOTTINGHAM, Mark; RESCHKE, Julian. *HTTP Semantics*. RFC 9110, junho de 2022. DOI: 10.17487/RFC9110.

https://www.rfc-editor.org/rfc/rfc9110.html

**Trechos consultados:** modelo de requisição/resposta e seções 15.3.1 (200), 15.5.4 (403) e 15.5.5 (404). **Uso:** explicação introdutória da seção 4.3. Os códigos não são tratados como classificações de vulnerabilidade; sua interpretação no caso é raciocínio do livro. Nenhuma requisição foi enviada à Aurora.

<a id="s8"></a>
## S8 · Reutilização de respostas

FIELDING, Roy T.; NOTTINGHAM, Mark; RESCHKE, Julian. *HTTP Caching*. RFC 9111, junho de 2022. DOI: 10.17487/RFC9111.

https://www.rfc-editor.org/rfc/rfc9111.html

**Trecho consultado:** seção 1, definições de cache privado, cache compartilhado e reutilização de respostas. **Uso:** seção 4.2, para explicar por que respostas repetidas não comprovam novo processamento na origem. Não foi avaliada a configuração de nenhum navegador ou servidor. Não se atribui ao cache a causa efetiva do episódio inicial fictício, resolvido pela identidade B.

<a id="s9"></a>
## S9 · O significado e a procedência de registros

OWASP Cheat Sheet Series. *Logging Cheat Sheet*.

https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html

**Trechos consultados:** Event attributes, nota sobre Interaction identifier e Data to exclude. **Uso:** seção 4.3, para campos de contexto, associação de eventos e cautela com dados sensíveis. Não foi adotada a lista completa de recomendações como requisito universal. A discussão sobre fontes derivadas, ausência de registros e limites da interpretação é desenvolvida por exemplos e raciocínio explícito.

## Natureza da entrega

O mantenedor informou ter lido e aprovado o capítulo. A revisão interna confrontou novamente os pontos técnicos com os trechos acima e verificou a coerência dos desfechos e das seis respostas. A separação entre observação, inferência, hipótese e previsão continua sendo vocabulário operacional do capítulo, não uma taxonomia atribuída a uma instituição.

O ciclo interno está concluído nesta versão. Não houve laboratório executável, avaliação de alvo real, medição de tempo, cálculo estatístico ou revisão independente. A aprovação da leitura não foi registrada como execução de exercícios nem domínio prático. Consulte o [registro editorial](../../../editorial/reviews/capitulo-4.md).
