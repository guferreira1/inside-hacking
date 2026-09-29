# Exemplos opcionais — Capítulo 14

[← Capítulo](../README.md) · [Referências](../referencias.md) · [Registro editorial](../../../../editorial/reviews/capitulo-14.md)

A leitura é independente destes arquivos. Eles tornam observáveis fronteiras de argumentos e a validação de uma pequena coleção, sem operar sobre catálogos ou alvos reais.

## Dois problemas pequenos

[argumentos.bash](argumentos.bash) mostra a quantidade e os valores dos argumentos. [Argumentos.ps1](Argumentos.ps1) devolve essa informação como um objeto PowerShell. Nenhum dos dois abre os nomes recebidos.

[resumo-estados.bash](resumo-estados.bash) e [Resumo-Estados.ps1](Resumo-Estados.ps1) aceitam de um a 256 estados, exclusivamente `disponivel` ou `emprestado`. Só emitem um resumo quando toda a entrada é válida. São exemplos didáticos, não importadores prontos para produção.

## Bash

Em Linux com Bash disponível, a partir desta pasta:

```bash
bash argumentos.bash 'catalogo de teste.txt'
bash resumo-estados.bash disponivel emprestado disponivel
```

O primeiro retorna um argumento; o segundo produz `disponiveis=2` e `emprestados=1`. Não é necessário tornar os arquivos executáveis ou usar sudo. Recursos de Bash não são apresentados como compatíveis com qualquer sh.

## PowerShell

Dentro de uma sessão PowerShell 7, a partir desta pasta:

```powershell
& ./Argumentos.ps1 -Valores @('catalogo de teste.txt', '*.txt')
& ./Resumo-Estados.ps1 -Estados @('disponivel', 'emprestado', 'disponivel')
```

Os resultados são objetos, antes da apresentação. A primeira chamada conserva dois valores; a segunda devolve contagens 2 e 1. Se a política do ambiente impedir a execução, não a altere apenas para acompanhar o capítulo: o texto e os resultados documentados permanecem disponíveis.

## Verificação e limites

Os testes em [test_chapter14_examples.py](../../../../scripts/tests/test_chapter14_examples.py) também criam arquivos temporários próprios para conferir globbing, redirecionamentos, escopos e erros. Cada caso limpa seu diretório ao terminar. Shell ausente é SKIP, não reprodução bem-sucedida. Os testes não alteram Registro, contas, permissões, serviços ou políticas de execução.

Na raiz do repositório, `python3 -m unittest discover -s scripts/tests -p test_chapter14_examples.py -v` executa as verificações compatíveis com o ambiente. Versões e resultados observados constam no registro editorial, separados dos modelos e da narrativa fictícia.

Código licenciado sob [MIT](../../../../LICENSES/MIT.txt), conforme o [mapa de licenças](../../../../LICENSE.md).
