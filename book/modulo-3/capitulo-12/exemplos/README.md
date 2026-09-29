# Capítulo 12 · Um descritor do próprio processo

[← Capítulo](../README.md) · [Explicação: 12.3](../12.3-proc-sys-e-dev.md)

[proc_proprio.py](proc_proprio.py) cria um arquivo temporário de seis bytes, mantém uma abertura e consulta apenas a entrada correspondente em `/proc/self/fd`. Código sob [MIT](../../../../LICENSE.md). A execução é opcional.

## Requisitos e alcance

Linux com `/proc/self/fd` disponível e acessível; Python 3.10 ou posterior pela sintaxe utilizada. A execução documentada foi em Python 3.13.5, não em todas as versões. O procedimento não pede sudo, não lê outros processos e não modifica montagens, serviços ou parâmetros do kernel.

O código compara metadados da entrada, do destino e da abertura original. A leitura pela referência é limitada a sete bytes; o arquivo criado contém `Livro` seguido de uma quebra de linha. A pasta e o arquivo são removidos ao concluir, inclusive diante do erro simulado nos testes.

## Execução opcional

Na raiz do repositório:

```sh
python3 -I -S book/modulo-3/capitulo-12/exemplos/proc_proprio.py
python3 -m unittest discover -s scripts/tests -p 'test_chapter12_examples.py' -v
```

Saída observada na execução local documentada:

```text
entrada_em_proc=link
destino=mesmo_arquivo_regular
leitura=Livro
bytes_lidos=6
```

`-I` e `-S` reduzem interferências de inicialização do Python; não são uma sandbox. Falta da interface ou recusa da consulta resulta em `EXEMPLO_NAO_EXECUTADO` e código de encerramento 2, não em saída simulada de sucesso. Outros erros inesperados não são silenciados.

## Limites

A comparação de dispositivo e inode vale para os objetos observados naquele momento. Não estabelece identidade permanente ou universal, não acessa arquivos de outras contas e não comprova compartilhamento da posição de leitura entre as duas aberturas.

Os quatro testes distinguem comportamento real, contrato de plataforma e injeção local de erro. A falha simulada fica restrita à referência de módulo usada pelo exemplo; não substitui funções globais utilizadas pela limpeza do runtime. O teste Linux deve ser ignorado explicitamente quando a plataforma necessária não existe, sem transformar SKIP em PASS.
