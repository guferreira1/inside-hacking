# Capítulo 17 — Exemplo opcional de namespaces próprios

[← Capítulo](../README.md) · [Explicação](../17.7-investigacao-e-verificacao.md) · [Testes](../../../../scripts/tests/test_chapter17_examples.py)

## Pergunta

Um processo filho comum possui automaticamente novos namespaces? O exemplo compara pai e filho sem pedir mudança de namespace. Não cria VM, container, montagem, usuário ou conexão de rede.

## Requisitos e execução

Linux, Python 3 e acesso de leitura às referências de namespaces sob `/proc/self/ns/`. Não é necessário sudo. Falta de suporte ou acesso produz resultado indisponível e código 2, sem alegar observação concluída.

A partir da raiz do repositório:

```bash
python3 book/modulo-3/capitulo-17/exemplos/namespaces_proprios.py
```

## O que acontece

O pai abre suas seis referências e conserva os descritores durante a observação. Um único filho conhecido executa o mesmo arquivo, consulta suas próprias referências e devolve uma estrutura pequena pelo pipe. O pai compara os pares dispositivo/inode por categoria. Argumentos são separados e não há shell; a espera pelo filho tem limite de cinco segundos.

A saída pública informa apenas se os PIDs diferem e se os seis namespaces comparados coincidem. Não lista processos alheios, nomes de usuários, arquivos pessoais ou dados de rede. O modo `--filho` é usado pelo protocolo interno, não é necessário para a leitura.

## Resultado e limites

Na execução local documentada, os processos eram distintos e os seis namespaces coincidiram. Isso não identifica a fronteira externa: os dois podem estar juntos dentro de uma VM ou de um container. Não foram observados limites de cgroup, perfis seccomp, políticas de arquivo ou resistência a escapes.

Os nove testes separam quatro verificações de contrato de cinco testes Linux. Há falhas injetadas somente para conferir ausência de saída parcial e fechamento de descritores. O teste de timeout injeta a exceção, não mantém um processo desconhecido rodando. Arquivos e configurações do host não são alterados; o fim da operação fecha as referências.

Ambiente, regressão e resultados da entrega constam no [registro editorial](../../../../editorial/reviews/capitulo-17.md).
