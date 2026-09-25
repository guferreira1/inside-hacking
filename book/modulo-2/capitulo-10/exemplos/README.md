# Capítulo 10 · Exemplos de formato e validação

[← Capítulo](../README.md) · [Contrato binário](../10.2-formatos-e-estrutura.md) · [Parsing](../10.5-parsing-e-validacao.md)

[registro.py](registro.py) contém um codec didático para AUR v1 e um perfil JSON do mesmo registro. Código sob MIT, conforme o [licenciamento](../../../../LICENSE.md). Nenhuma execução é necessária para acompanhar o capítulo.

## O que o exemplo faz

Serializa título e quantidade, confere a estrutura recebida e reconstrói um Registro. Usa apenas a biblioteca padrão do Python. Executado diretamente, cria um registro constante em memória e imprime suas representações; não lê arquivos externos nem abre conexões.

AUR v1 contém assinatura AUR, versão numérica 1, comprimento de título em dois bytes, quantidade em dois bytes e título UTF-8. Os inteiros de dois bytes são big-endian. O cabeçalho tem oito bytes; o título ocupa 1–80 bytes, a quantidade vai de 0 a 1000 e não há bytes adicionais.

O perfil JSON exige UTF-8 sem BOM inicial, um objeto com exatamente titulo e quantidade e nomes não repetidos. A quantidade deve ser um inteiro Python obtido de um número JSON sem fração nem expoente; booleanos, strings numéricas, null e constantes NaN/Infinity são rejeitados. Esse perfil é deliberadamente mais restrito que todos os valores possíveis em JSON. Não usa o padrão JSON Schema nem produz JCS.

O título não recebe normalização ou filtro de saída. As restrições de bytes são ilustrativas, não um contrato completo de qualidade, autorização ou apresentação de catálogo.

## Execução opcional

A partir da raiz do repositório, com Python 3.10 ou posterior:

```sh
python3 -I -S book/modulo-2/capitulo-10/exemplos/registro.py
python3 -m unittest discover -s scripts/tests -p 'test_chapter10_examples.py' -v
```

Saída observada do programa em Python 3.13.5:

```text
binario: 41 55 52 01 00 05 00 03 4C 69 76 72 6F
json: {"titulo":"Livro","quantidade":3}
retorno: Registro(titulo='Livro', quantidade=3)
```

As opções -I e -S reduzem interferências de inicialização do Python; não constituem uma sandbox. A declaração de Python 3.10 indica os recursos de sintaxe utilizados; a execução documentada foi em 3.13.5, não em todas as versões possíveis.

## Testes e limites

A suíte possui 23 testes: quatorze de formato, oito de transformação e um de arquivos. O teste de hard links e remoção de nomes é restrito ao Linux e deve aparecer como ignorado em outras plataformas. As transformações usam dados pequenos e constantes; não executam pickle, XML/YAML, exploração, bomba de descompressão ou parser de terceiros sobre conteúdo desconhecido.

Os codecs recebem um objeto bytes já existente. Quem os incorpora em outra aplicação continua responsável por limitar aquisição, memória, tempo e tratamento de falhas. O exemplo não é um importador de produção. As [referências](../referencias.md) e o [registro editorial](../../../../editorial/reviews/capitulo-10.md) delimitam o que foi verificado.
