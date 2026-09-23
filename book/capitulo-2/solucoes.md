# Capítulo 2 — Respostas comentadas

[← Voltar ao capítulo](README.md) · [Referências](referencias.md) · [Capítulo 3 →](../capitulo-3/README.md)

**Use depois de tentar responder.** As respostas são modelos de raciocínio; uma formulação diferente pode estar correta. Não é necessário reproduzir estas frases nem memorizar todas as datas.

## 1. O lugar do TMRC

O clube documenta uma comunidade de experimentação e uma ligação entre seus sistemas de controle e os primeiros computadores do MIT. Isso justifica estudá-lo. Não demonstra que todas as formas de hacking nasceram exclusivamente ali. Um registro de origem em uma instituição não é uma prova de origem universal. [R1](referencias.md#r1) [R2](referencias.md#r2)

**Verifique sua resposta:** ela reconhece a importância do clube sem transformá-lo em fundador de toda a área?

## 2. Sinais de controle e o limite do apito

O exemplo mostra que um sinal acessível pelo caminho de comunicação pode ser interpretado como controle. Nos sistemas históricos discutidos, devemos distinguir supervisão da ligação e endereçamento, além das condições de cada arquitetura. Um tom de 2600 Hz não representa sozinho todas as funções de uma rede. [R3](referencias.md#r3) [R4](referencias.md#r4)

**Verifique sua resposta:** “um apito invadia qualquer telefone” é uma generalização que o texto não sustenta. Também seria incorreto concluir que o método se aplica a serviços atuais.

## 3. Conectividade e alcance

No cenário fictício, disponibilizar uma função pela rede acrescenta um caminho para utilizá-la. Esse caminho também pode permitir alcançar uma falha, mas isso depende de existir uma condição explorável e dos controles presentes. Conexão é uma característica da arquitetura, não um diagnóstico automático de vulnerabilidade.

**Verifique sua resposta:** explique a possibilidade sem trocar “pode acontecer” por “sempre acontece”.

## 4. Morris Worm e CERT/CC

Morris Worm é o programa autorreplicante associado a Robert Tappan Morris, não uma pessoa envolvida no episódio do apito. O incidente de novembro de 1988 foi seguido pelo pedido da DARPA ao SEI que originou o CERT/CC. Já existia trabalho organizado de segurança antes disso, como demonstra o workshop NBS/ACM de 1972. [R6](referencias.md#r6) [R7](referencias.md#r7) [R9](referencias.md#r9)

**Verifique sua resposta:** diferencie programa, autor, incidente e instituição. Nenhum desses elementos deve ser chamado de criador único de cybersecurity.

## 5. Do travamento à conclusão

No exemplo, o dado observado é o travamento. A causa, a possibilidade de interferência na memória, o controle pelo usuário e o impacto sobre outras pessoas ainda precisam de investigação. Não é correto saltar diretamente de “travou” para “consigo executar código”.

Uma vulnerabilidade é uma condição do sistema; um exploit é uma maneira de aproveitá-la. A condição pode existir sem que um exploit tenha sido descoberto ou publicado. A sequência da seção 2.7 organiza a investigação, não cria a vulnerabilidade.

**Verifique sua resposta:** marque separadamente o que foi visto, o que é hipótese e o que seria necessário demonstrar. Não trate um resultado negativo isolado como prova de segurança de todo o sistema.

## 6. Capacidade ofensiva e trabalho profissional

Conseguir executar uma técnica é diferente de conduzir uma avaliação com objetivo, permissão, escopo, registro e comunicação de resultados. A organização da atividade é parte do trabalho, não um complemento opcional à obtenção de acesso. [R10](referencias.md#r10)

**Verifique sua resposta:** inclua pelo menos o objetivo do teste, seus limites e a utilidade da evidência produzida.

## 7. Bug Bounty e divulgação

Um programa pode oferecer recompensas e definir critérios para recebê-las. Isso não torna todo método ou sistema autorizado. Uma política de divulgação pode existir sem prêmio, e um canal para receber relatos não deve ser interpretado como permissão geral de teste. [R11](referencias.md#r11) [R12](referencias.md#r12)

**Verifique sua resposta:** separe autorização, elegibilidade para recompensa e regras de comunicação do achado.

## 8. Aprender com a história sem forçar equivalências

Podemos usar os episódios para formular perguntas sobre entradas, autoridade e confiança. Não podemos concluir que a mesma explicação técnica, o mesmo procedimento ou a mesma mitigação serve para telefonia, banco de dados e modelos de linguagem.

O aprendizado transferível é a maneira de investigar. O mecanismo concreto precisa ser estudado em cada sistema. A seção 2.12 é uma comparação didática, não uma afirmação de que prompt injection seja uma nova versão da sinalização telefônica.

**Verifique sua resposta:** apresente uma pergunta que se transfere entre os casos e um detalhe técnico que não pode ser simplesmente transportado.

---

Responder bem a essas questões é evidência de compreensão conceitual deste capítulo, não de domínio prático das técnicas mencionadas. Os fundamentos e laboratórios correspondentes serão desenvolvidos adiante.
