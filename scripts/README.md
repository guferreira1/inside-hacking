# Verificação da documentação

[Página inicial](../README.md) · [Política de glossário](../editorial/glossary-policy.md)

O verificador usa somente a biblioteca padrão de Python 3. Não instala ferramentas nem acessa alvos de segurança.

```sh
python3 -m unittest discover -s scripts/tests -v
python3 scripts/check_docs.py
python3 scripts/check_docs.py --inventory
```

`--root` permite apontar para outra cópia local do repositório. A opção `--inventory` mostra os arquivos analisados, termos candidatos em maiúsculas, estados encontrados e URLs externas. O comando termina com erro quando encontra destino interno ou âncora inexistente nas formas de link reconhecidas.

## Escopo

São conferidos caminhos e âncoras de links Markdown inline, referências explícitas e atributos HTML `href`/`src`; blocos de código e comentários não são tratados como links de navegação. O resultado conta destinos distintos por arquivo, não todas as repetições de um link.

A implementação atende ao subconjunto de Markdown utilizado pela obra; não é um parser completo de todas as extensões de GitHub Flavored Markdown. Os testes mantêm exemplos desse contrato e devem crescer quando uma nova forma de link for adotada.

URLs externas são inventariadas, **não testadas por rede** neste comando. Acessibilidade externa, conteúdo das fontes, correção conceitual, cobertura semântica do glossário e renderização PDF exigem verificações próprias.

Os candidatos de terminologia são auxiliares: incluem falsos candidatos, como identificadores de fontes. Não são automaticamente novos verbetes. A [política editorial](../editorial/glossary-policy.md) exige revisão humana/assistida de ocorrência e definição.

## Automação

O workflow [docs-check.yml](../.github/workflows/docs-check.yml) executa testes e checagem em push e pull request, com permissão somente de leitura. Ele não faz merge, não publica PDF e não promove estados editoriais.
