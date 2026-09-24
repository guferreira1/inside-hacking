# Capítulo 4 · Respostas comentadas

[← Perguntas de revisão](4.4-conclusoes-e-limites.md#pare-e-explique) · [Índice do capítulo](README.md) · [Capítulo 5 →](../capitulo-5/README.md)

As respostas usam exclusivamente os cenários fictícios do capítulo. Formulações diferentes podem expressar o mesmo raciocínio. Não houve execução de testes, e responder às questões não equivale a domínio prático de uma ferramenta.

## 1. Observação e inferência

Foi observada uma tela com o nome de B depois da abertura de determinado endereço. O pesquisador acreditava estar em A, mas ainda não havia conferido a identidade efetivamente usada nem estabelecido que o conteúdo era o comprovante privado, e não uma prévia.

Afirmar que A recebeu um documento de B acrescentaria essas condições à observação. H1, H2 e H3 ajudam a torná-las verificáveis: conferir identidade, natureza do conteúdo e regra esperada permite distinguir as explicações. Não basta listar hipóteses; é preciso dizer qual observação as separaria.

## 2. Consultas legítimas como referência

As consultas do próprio documento mostram que o recurso existe e que aquele caminho pode funcionar para a identidade correspondente. Se todas forem recusadas, uma conta sem sessão válida, uma indisponibilidade ou outro impedimento pode explicar a recusa ao documento alheio. Não foi isolada a decisão de autorização que pretendíamos estudar.

A falha do caso normal torna a interpretação inconclusiva; não prova que a aplicação esteja vulnerável, nem que seu controle de acesso esteja correto.

## 3. Várias mudanças simultâneas

Sabemos que duas situações diferentes produziram resultados diferentes. Não isolamos qual alteração explica a recusa. A comparação não permite atribuí-la somente à troca de conta.

Uma próxima análise útil manteria explícitas as condições relevantes e examinaria as diferenças de forma planejada. Se o efeito depender de uma combinação de conta e estado do documento, será necessário estudar essa combinação, em vez de impor a regra de variar sempre um único fator.

## 4. Alertas repetidos e falso positivo

Os três registros podem depender de uma única classificação inicial. A reprodução em painéis não demonstra três verificações independentes.

Seria correto chamar o alerta de falso positivo depois de estabelecer que ele anunciou uma condição ausente no caso classificado — por exemplo, que marcou leitura de comprovante privado quando o conteúdo era apenas uma página pública. Antes disso, o estado pode ser pendente ou inconclusivo. Não conseguir reproduzir imediatamente um alerta não demonstra sozinho que ele era falso.

## 5. Resultado não confirmado e alcance

Uma resposta possível é: “A consulta inicial foi atendida sob B. Depois de separar e conferir as identidades, cada leitor obteve seu comprovante e não recebeu o documento privado do outro nas comparações realizadas. Não foi confirmada quebra de isolamento nesse caminho. Outros caminhos, estados e perfis não foram examinados.”

Evite “a aplicação está segura” e “não existe nenhuma vulnerabilidade”. O exemplo não sustenta essas conclusões universais. O resultado negativo foi útil porque esclareceu uma suspeita sem precisar transformá-la em achado.

## 6. Efeito demonstrado e causa ainda em aberto

No desfecho alternativo, a regra de isolamento foi violada: A recebeu o documento privado de B sem a permissão prevista. Isso sustenta a descrição do comportamento nas condições dadas.

Não determina, sozinho, se falta uma checagem, se a decisão de permissão foi implementada incorretamente ou se outro componente entregou o conteúdo. A causa precisa de evidência adicional pertinente, como análise do processamento ou do código. Não é necessário inventá-la para reportar uma falha demonstrada.

[Voltar ao módulo](../README.md) · [Seguir para o Capítulo 5](../capitulo-5/README.md)
