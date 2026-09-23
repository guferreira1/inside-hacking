# Master Outline

**Status:** v0.2 — arquitetura macro revisável

Este documento define os capítulos previstos para **Por Dentro do Hacking**. A numeração é editorial e pode mudar conforme a pesquisa revelar dependências, lacunas ou necessidade de reorganização.

**Regra:** capítulos são planejados antecipadamente; subcapítulos surgem durante pesquisa e escrita quando representam unidades conceituais úteis.

## Módulo I — Hacking, segurança e método
1. O que é hacking?
2. História da cultura hacker e da segurança ofensiva
3. Ética, legalidade, autorização e escopo
4. Como pensar como investigador de segurança
5. Ameaças, vulnerabilidades, exploits, risco e superfície de ataque

## Módulo II — Computadores por dentro
6. Bits, bytes e representação da informação
7. Hardware: CPU, memória, armazenamento e dispositivos
8. Como um programa se torna execução
9. Memória, processos e arquitetura de computadores
10. Arquivos, formatos, codificação e serialização

## Módulo III — Sistemas operacionais
11. O papel de um sistema operacional
12. Linux por dentro
13. Windows por dentro
14. Terminal, shells e automação
15. Usuários, grupos, permissões e privilégios
16. Processos, serviços, logs e persistência de estado
17. Virtualização e isolamento

## Módulo IV — Redes e Internet
18. Como computadores se comunicam
19. Modelos de camadas e encapsulamento
20. Ethernet, ARP e redes locais
21. Endereçamento IP, sub-redes e IPv6
22. Roteamento, NAT e firewalls
23. TCP, UDP, portas e sockets
24. DNS por dentro
25. DHCP e serviços essenciais de rede
26. Como a Internet funciona
27. HTTP e HTTPS
28. TLS, certificados e confiança na rede
29. Proxies, VPNs, túneis e anonimização
30. Observação e análise de tráfego

## Módulo V — Programação, dados e aplicações
31. Fundamentos de programação para segurança
32. Python, shell e automação para investigação
33. C e memória para segurança
34. Estruturas de dados, formatos e parsing
35. Bancos de dados e SQL
36. Arquitetura cliente-servidor
37. Como aplicações Web funcionam
38. Como APIs funcionam
39. Arquiteturas modernas, microsserviços e mensageria
40. Git, dependências e cadeia de construção de software

## Módulo VI — Fundamentos de segurança
41. Confidencialidade, integridade, disponibilidade e confiança
42. Modelagem de ameaças e fronteiras de confiança
43. Criptografia: fundamentos
44. Hashes, MACs, assinaturas e integridade
45. Senhas e armazenamento seguro
46. Autenticação, MFA e identidade
47. Autorização e controle de acesso
48. Sessões, tokens, cookies, JWT e OAuth/OIDC
49. Segredos, chaves e certificados
50. Hardening, least privilege e defesa em profundidade

## Módulo VII — Laboratório e metodologia ofensiva
51. Construindo um laboratório seguro
52. Kali Linux e o ambiente do pesquisador
53. Metodologia de pentest
54. Hipóteses, evidências e validação
55. Documentação, notas e cadeia de evidências
56. Ferramentas: como escolher, entender e validar
57. Relatórios, impacto, correção e reteste

## Módulo VIII — Reconhecimento e enumeração
58. Reconhecimento passivo e ativo
59. OSINT aplicado à superfície de ataque
60. Descoberta de hosts e mapeamento de redes
61. Port scanning e Nmap por dentro
62. Enumeração de serviços
63. Fingerprinting de sistemas e tecnologias
64. Reconhecimento Web
65. Reconhecimento de APIs
66. Descoberta de conteúdo, endpoints e ativos
67. Vulnerability scanning e seus limites

## Módulo IX — Credenciais e acesso inicial
68. Ataques a senhas e espaço de busca
69. Dicionários, regras e cracking offline
70. Brute force online, password spraying e credential stuffing
71. Phishing e engenharia social: mecanismos, riscos e defesa
72. Exposição e reutilização de credenciais
73. Falhas de autenticação e recuperação de contas
74. Exploração de serviços expostos

## Módulo X — Web Hacking
75. Método de teste de aplicações Web
76. Burp Suite e proxies de interceptação
77. Manipulação de requisições e parâmetros
78. SQL Injection
79. Command Injection
80. Cross-Site Scripting (XSS)
81. Cross-Site Request Forgery (CSRF)
82. Server-Side Request Forgery (SSRF)
83. Path Traversal e File Inclusion
84. Upload de arquivos e processamento inseguro
85. XXE e parsers inseguros
86. Desserialização insegura
87. Server-Side Template Injection (SSTI)
88. Falhas de autenticação e sessão
89. Broken Access Control, IDOR/BOLA e privilege escalation em aplicações
90. CORS, Same-Origin Policy e segurança do navegador
91. HTTP Host Header, cache e ataques de infraestrutura Web
92. HTTP Request Smuggling e desynchronization
93. Race Conditions
94. WebSockets e comunicação em tempo real
95. GraphQL
96. Lógica de negócio e encadeamento de vulnerabilidades
97. Client-side security e DOM
98. Validação de impacto, correção e reteste Web

## Módulo XI — API Hacking
99. Metodologia de teste de APIs
100. REST, RPC, SOAP e outras interfaces
101. Autenticação e autorização em APIs
102. BOLA, BFLA e controle de propriedades
103. Mass Assignment e exposição excessiva de dados
104. Consumo irrestrito de recursos e abuso
105. Fluxos de negócio sensíveis
106. Inventário, versões e APIs esquecidas
107. Integrações de terceiros e SSRF em APIs
108. Testes automatizados e fuzzing de APIs
109. Encadeamento de falhas em APIs

## Módulo XII — Linux, Windows e pós-exploração
110. O que muda depois do acesso inicial
111. Enumeração local em Linux
112. Escalada de privilégios em Linux
113. Persistência e credenciais em Linux
114. Enumeração local em Windows
115. Escalada de privilégios em Windows
116. Persistência e credenciais em Windows
117. Processos, serviços e tarefas agendadas
118. Segredos, tokens e material de autenticação
119. Pivotamento, port forwarding e túneis
120. Movimentação lateral
121. Coleta controlada, impacto e encerramento do teste

## Módulo XIII — Active Directory e ambientes corporativos
122. Diretórios, domínios e identidade corporativa
123. Active Directory por dentro
124. LDAP, DNS e serviços do domínio
125. Kerberos por dentro
126. NTLM e autenticação Windows
127. Enumeração de Active Directory
128. Relações de confiança e caminhos de ataque
129. Ataques a credenciais e autenticação em AD
130. Escalada de privilégios em domínio
131. Delegação, ACLs e configurações perigosas
132. Movimento lateral em ambientes Windows
133. Persistência em domínio
134. AD CS e infraestrutura de certificados
135. Hardening, detecção e investigação em AD

## Módulo XIV — Cloud, containers e supply chain
136. Modelos de cloud e responsabilidade compartilhada
137. Identidade e IAM em cloud
138. Redes e exposição em cloud
139. Storage, segredos e configurações inseguras
140. Containers por dentro
141. Docker security
142. Kubernetes security
143. CI/CD e pipelines
144. Dependências, pacotes e supply chain
145. IaC e infraestrutura como código
146. Serverless e workloads gerenciados
147. Escalada, movimento lateral e impacto em cloud
148. Cloud pentest: escopo, evidências e limites

## Módulo XV — Exploit Development e engenharia reversa
149. Do bug à vulnerabilidade
150. Assembly e arquitetura para exploração
151. Debuggers e análise dinâmica
152. Stack, heap e corrupção de memória
153. Buffer Overflows
154. Use-After-Free e classes de memória
155. Format Strings e outros erros de baixo nível
156. Mitigações modernas: ASLR, DEP/NX, canaries e CFI
157. Return-Oriented Programming e técnicas de controle de fluxo
158. Fuzzing
159. Leitura e adaptação de provas de conceito
160. Introdução à engenharia reversa
161. Análise estática e dinâmica de binários
162. Fundamentos de análise de malware

## Módulo XVI — Wireless, mobile, IoT e outras superfícies
163. Fundamentos de redes Wi-Fi
164. Segurança e testes em Wi-Fi
165. Bluetooth e comunicações de curto alcance
166. Arquitetura e segurança Android
167. Arquitetura e segurança iOS
168. Mobile application testing
169. IoT e sistemas embarcados
170. Firmware e interfaces de hardware
171. Introdução a OT/ICS e suas particularidades

## Módulo XVII — Segurança de IA
172. Como sistemas modernos de IA são construídos
173. LLMs, contexto, tokens e inferência
174. RAG, embeddings e bancos vetoriais
175. Agentes, ferramentas e permissões
176. Threat modeling para aplicações de IA
177. Prompt Injection direta
178. Prompt Injection indireta
179. Vazamento de informações e dados sensíveis
180. Tratamento inseguro das saídas do modelo
181. Data e Model Poisoning
182. RAG e vector/embedding weaknesses
183. Supply chain de modelos e componentes
184. Excessive Agency e abuso de ferramentas
185. Model DoS, consumo de recursos e abuso
186. Avaliação ofensiva e Red Team de sistemas de IA
187. Guardrails, monitoramento e defesa

## Módulo XVIII — Dark Web, privacidade e anonimato
188. Surface Web, Deep Web e Dark Web
189. Privacidade, anonimato e modelos de ameaça
190. Tor por dentro
191. Onion Services
192. Outras redes e tecnologias de anonimato
193. Ecossistemas clandestinos e economia do cibercrime
194. Mercados, fóruns, reputação e fraude entre criminosos
195. Vazamentos, data brokers criminosos e negociação de acessos
196. Investigação segura e limites operacionais

## Módulo XIX — OSINT, fraude e investigação digital
197. Fundamentos de OSINT
198. Pesquisa, fontes e avaliação de confiabilidade
199. Identidades, personas e correlação de informações
200. Domínios, infraestrutura e inteligência técnica
201. Investigação de fraudes digitais
202. Threat Intelligence e indicadores
203. Attribution: evidências, incerteza e limites
204. Preservação de evidências e fundamentos forenses
205. Investigação de campanhas e incidentes
206. Comunicação de achados e escalonamento responsável

## Módulo XX — Red Team, defesa e Purple Team
207. Do pentest ao Red Team
208. Objetivos, regras de engajamento e OPSEC
209. Adversary emulation e MITRE ATT&CK
210. Command and Control: arquitetura e conceitos
211. Persistência, evasão e detecção
212. Movimento lateral em operações
213. Simulação segura de coleta e exfiltração
214. Telemetria, logs e detecção
215. EDR, SIEM e controles defensivos
216. Detection Engineering
217. Incident Response visto pelo atacante e pelo defensor
218. Purple Team e validação conjunta
219. Relatório executivo e técnico de operações

## Módulo XXI — Bug Bounty, AppSec e atuação profissional
220. Como funciona um pentest profissional
221. Bug Bounty por dentro
222. Escolha de programas, escopo e regras
223. Estratégia de pesquisa em Bug Bounty
224. Validação, evidência e relatórios de vulnerabilidade
225. Duplicates, informatives e aprendizado
226. Secure Coding e revisão de código
227. Threat Modeling aplicado a produtos
228. Application Security
229. Product Security
230. Gestão de vulnerabilidades
231. CVE, CWE, CVSS e ecossistema de divulgação
232. Responsible Disclosure
233. Construindo portfólio e evidências técnicas
234. Pesquisa contínua e como continuar aprendendo

## Regra de evolução

Este índice não é uma promessa de que existirão exatamente 234 capítulos na edição final. Durante a pesquisa, capítulos podem ser unidos, divididos, reordenados ou acrescentados. A cobertura é mais importante que preservar a numeração.

Subcapítulos serão definidos durante a construção de cada capítulo.
