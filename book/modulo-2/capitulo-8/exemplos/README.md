# Capítulo 8 · Exemplos de construção e execução

[← Capítulo](../README.md) · [Seção 8.2](../8.2-compilacao-e-ligacao.md) · [Referências e execução](../referencias.md#conferência-executada)

Estes três arquivos são o programa mínimo explicado no capítulo. São autorais, sob a licença MIT do repositório. A função devolve um inteiro fixo e o programa apresenta esse valor; não é a implementação da biblioteca Aurora nem um serviço de rede.

## Arquivos

| Arquivo | Papel |
| --- | --- |
| [acervo.h](acervo.h) | Declara a interface da função. |
| [acervo.c](acervo.c) | Define o cálculo usado pelo exemplo. |
| [principal.c](principal.c) | Chama a função e apresenta o resultado. |

## Reprodução opcional

A leitura não exige executar os arquivos. Para reproduzir este percurso específico, use Linux com GCC e os componentes de desenvolvimento da biblioteca C. O ambiente de edição utilizou GCC 14.2.0; saída assembly, mensagens e configuração de ligação podem diferir em outras versões. Não há necessidade de privilégios administrativos, rede ou instalação de uma aplicação vulnerável.

Copie os três arquivos para um diretório de trabalho separado. Nesse diretório:

```sh
gcc -E principal.c -o principal.i
gcc -S principal.c -o principal.s
gcc -std=c17 -Wall -Wextra -Werror -c principal.c -o principal.o
gcc -std=c17 -Wall -Wextra -Werror -c acervo.c -o acervo.o
gcc principal.o acervo.o -o catalogo
./catalogo
```

Cada opção é explicada na seção 8.2. `-Wall`, `-Wextra` e `-Werror` habilitam diagnósticos adicionais e fazem advertências impedirem a construção; não certificam segurança. Os dois primeiros comandos permitem examinar representações intermediárias. O executável é obtido pela ligação dos objetos.

Na execução conferida, a saída padrão foi `Exemplares: 5` seguida de quebra de linha e o código de saída foi zero. O texto apresentado não é o código de saída.

A comparação sobre edição do fonte e o teste negativo de ligação estão automatizados: não é necessário danificar manualmente seus arquivos para conferi-los. A partir da raiz de uma cópia do repositório:

```sh
python3 -m unittest discover -s scripts/tests -p 'test_chapter8_examples.py' -v
```

A suíte usa temporários e os remove ao terminar. Os testes Python utilizam código fixo do exemplo; nunca forneça código externo a `exec` apenas por ele aparecer numa demonstração. Se Linux ou GCC estiverem ausentes, os casos C são marcados como ignorados, não como execuções aprovadas.

O exemplo não trata todas as falhas de saída, não implementa análise robusta de parâmetros e não constitui programa de produção. Não utiliza dados pessoais, credenciais ou sistemas de terceiros. Remover a cópia de trabalho é suficiente para descartar seus artefatos de construção; nada é instalado no sistema.
