# Capítulo 9 · Exemplo opcional de memória privada e compartilhada

[← Capítulo](../README.md) · [Explicação em 9.4](../9.4-paginacao-copias-e-medidas.md) · [Referências](../referencias.md#s18)

O arquivo [privado_e_compartilhado.py](privado_e_compartilhado.py) foi criado para observar uma única diferença: quais alterações o pai vê após um filho escrever em mapeamentos privados e compartilhados. A leitura do capítulo não depende de sua execução.

## Ambiente e execução

O exemplo requer Linux e Python 3.9 ou superior com as interfaces fork e mmap da biblioteca padrão. Foi conferido em Debian GNU/Linux 13, Linux x86-64 e Python 3.13.5. Não requer instalação de pacotes, privilégios administrativos, rede ou arquivos de outros processos.

A partir da raiz do repositório, execute o script como programa independente:

```sh
python3 -I -S book/modulo-2/capitulo-9/exemplos/privado_e_compartilhado.py
```

`-I` reduz interferências de variáveis e caminhos do ambiente Python; `-S` evita a inicialização automática do módulo site e de personalizações associadas. Não são uma sandbox. Não importe o exemplo em notebook, servidor ou aplicação que já tenha outros threads: o uso de fork em um processo multithread possui restrições e avisos documentados pelo Python.

## O que o código faz

O programa cria duas regiões anônimas de uma página cada, usando o tamanho fornecido pela plataforma. A primeira possui MAP_PRIVATE; a segunda, MAP_SHARED. Ambas recebem cinco no primeiro byte. É criado um único filho, que muda os dois valores para nove e termina. O pai aguarda com waitpid antes de consultar seus próprios mapeamentos.

Na execução conferida, a saída foi:

```text
privado=5
compartilhado=9
```

O código de saída foi zero. Uma plataforma não suportada ou erro operacional recebe uma mensagem em stderr e código não zero. O teste automatizado mantém um limite de dez segundos para a execução.

## O que o resultado não prova

A saída confirma visibilidade dos valores neste exemplo. Não mede quadros físicos, número de cópias COW, RSS/PSS, faults ou desempenho. Também não demonstra sincronização suficiente para uma aplicação concorrente arbitrária: aqui o pai lê somente depois do término do filho.

Não há leitura de memória de terceiros, desativação de proteções ou acesso fora dos limites. Os mapeamentos do pai são fechados ao sair dos gerenciadores de contexto; os recursos do filho são liberados pelo sistema no término. Nenhum arquivo de dados precisa ser restaurado.

Os [testes editoriais](../../../../scripts/tests/test_chapter9_examples.py) acrescentam seis contas e modelos sequenciais à conferência do programa. Eles não transformam esses modelos em medições de hardware.
