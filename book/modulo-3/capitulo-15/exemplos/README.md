# Capítulo 15 — Observações opcionais de permissões

[← Capítulo](../README.md) · [Discussão](../15.7-investigacao-e-verificacao.md) · [Registro editorial](../../../../editorial/reviews/capitulo-15.md)

O programa [permissoes_proprias.py](permissoes_proprias.py) executa quatro observações sobre arquivos e diretórios temporários do próprio usuário em Linux. Não recebe um alvo ou caminho externo, não cria contas e não modifica grupos, ACLs, políticas obrigatórias, serviços ou configurações do host.

## Condições e execução

Use Python 3.10 ou posterior em Linux, como usuário comum e sem capabilities efetivas. O programa verifica UID efetivo e CapEff do próprio processo. Se não conseguir confirmar o contexto ou observar as recusas esperadas, interrompe a execução. **Não execute com sudo para tentar fazê-lo passar.** Não é necessário executar o exemplo para ler o capítulo.

A partir deste diretório:

```bash
python3 -I -S permissoes_proprias.py
```

O procedimento cria somente recursos temporários privados, aplica modos a esses recursos e os remove ao terminar. Permissões de diretórios são restauradas antes da limpeza. A perda abrupta do processo ou do sistema pode impedir a limpeza automática; isso não transforma TemporaryDirectory em uma garantia de recuperação após qualquer falha.

## O que observar

A saída JSON contém quatro grupos de resultados: escrita recusada e nome removido; nova abertura recusada e descritor anterior ainda legível; diretório com busca sem listagem; diretório com listagem sem busca. Uma saída bem-sucedida só é produzida depois que as operações e recusas são conferidas.

A observação local documentada encontrou os oito resultados booleanos como verdadeiros. Isso **não** comprova segurança de uma conta de serviço, toda a semântica de ACLs, controle remoto de arquivos ou comportamento Windows. O usuário usado pelo programa é dono de todos os objetos criados, e nenhum teste entre contas foi realizado.

## Testes e limites

Os [testes próprios](../../../../scripts/tests/test_chapter15_examples.py) separam três verificações de modelos/guarda de ambiente de seis verificações Linux, incluindo execução independente e limpeza após uma falha injetada. O teste de umask é uma conta de bits, não altera a máscara real do processo; o modelo de classes não é um simulador completo de autorização.

Os testes Linux são explicitamente pulados em ambiente incompatível. Um skip não é aprovação. As execuções local e do runner devem ser identificadas separadamente no registro editorial.

Na execução local, o processo que iniciou os testes estava em um container com UID zero. O teste foi executado em um subprocesso reduzido ao UID/GID 65534, sem grupos suplementares e sem capabilities efetivas; nenhuma conta foi criada ou alterada. Essa preparação do ambiente não faz parte do script do leitor e não exige que ele reproduza uma troca de identidade.
