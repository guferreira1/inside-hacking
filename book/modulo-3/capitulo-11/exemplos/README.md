# Capítulo 11 · Pedidos diferentes, resultados diferentes

[← Seção 11.2](../11.2-interfaces-e-chamadas-de-sistema.md) · [Capítulo](../README.md) · [Código](pedidos.py)

O exemplo é opcional. Ele cria uma pasta temporária própria, grava os cinco bytes de `Livro` e abre o arquivo somente para leitura. Depois distingue leitura, fim de arquivo, escrita incompatível com a abertura e ausência de outro nome. O conteúdo inicial é conferido novamente antes da limpeza.

## Execução

Requisitos: Linux e Python 3.10 ou superior para a sintaxe utilizada. A execução documentada ocorreu em Python 3.13.5; isso não declara teste de todas as versões. Não são necessários pacotes externos, rede, sudo ou dados pessoais.

A partir da raiz do repositório:

```sh
python3 -I -S book/modulo-3/capitulo-11/exemplos/pedidos.py
```

Resultado observado no ambiente registrado:

```text
leitura=Livro
fim_da_leitura=0
escrita=EBADF
ausente=ENOENT
conteudo_preservado=sim
```

As opções -I e -S reduzem a influência de personalizações da inicialização Python; não isolam o programa como uma sandbox. Não utilize uma conta administrativa por causa deste exemplo. O script não recebe caminhos para examinar arquivos externos.

## Como interpretar

EBADF aparece porque a abertura utilizada não admite escrita; não comprova falta de permissão de uma identidade sobre o arquivo. ENOENT aparece na tentativa sobre o nome não criado. O zero refere-se à leitura sem bytes após consumir o arquivo regular, não a um erro retornado pela mesma operação de abertura.

O código trata leituras parciais com um laço limitado e fecha o descritor em finally. Erros diferentes dos esperados são propagados e levam a uma mensagem de exemplo não concluído. Não se transforma qualquer falha em sucesso didático.

## Testes e limites

```sh
python3 -m unittest discover -s scripts/tests -p 'test_chapter11_examples.py' -v
```

São [seis testes](../../../../scripts/tests/test_chapter11_examples.py). Três tratam interfaces, saída literal e limpeza; três conferem modelos do texto. Os testes Linux são marcados como não aplicáveis em outras plataformas, não como comportamento testado nelas.

Não foram rastreadas syscalls, alteradas permissões, instalados serviços, criadas contas ou executados testes de exaustão. As [referências](../referencias.md) e o [registro editorial](../../../../editorial/reviews/capitulo-11.md) delimitam o que foi realmente observado. Código sob a licença [MIT](../../../../LICENSES/MIT.txt).
