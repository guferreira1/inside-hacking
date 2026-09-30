# Capítulo 16 — Exemplos opcionais

[← Capítulo](../README.md) · [Fontes](../referencias.md) · [Registro editorial](../../../../editorial/reviews/capitulo-16.md)

Os exemplos usam apenas a biblioteca padrão Python, processos filhos conhecidos e arquivos temporários próprios. A leitura do capítulo não depende de executá-los. Não são supervisores de produção nem procedimentos para alterar serviços reais.

## 1. Inicialização, espera e encerramento

```bash
python3 ciclo_proprio.py
```

Execute a partir deste diretório. [ciclo_proprio.py](ciclo_proprio.py) cria um filho, recebe sua mensagem `pronto`, observa que ele ainda espera e envia o pedido de término. As saídas e o código final são conferidos. O protocolo usa um pipe próprio, não systemd ou SCM. Esperas têm timeout; na limpeza, apenas esse filho pode ser encerrado.

## 2. Estado confirmado e resposta ausente

```bash
python3 estado_proprio.py
```

[estado_proprio.py](estado_proprio.py) cria seu diretório temporário e o remove ao final. O modo `--worker` é interno: não deve ser usado com arquivos ou bancos existentes do leitor. As funções de teste recebem somente caminhos gerados pela própria demonstração.

Um filho termina antes do commit, outro depois do commit e antes da resposta. A demonstração consulta o banco e verifica a repetição de identificadores. A saída observada na execução local foi:

```json
{"antes_do_commit": {"aplicados": [], "total": 0}, "depois_da_repeticao": {"aplicados": [["lote-1", 3], ["lote-2", 2]], "total": 5}, "depois_do_commit_sem_resposta": {"aplicados": [["lote-1", 3], ["lote-2", 2]], "total": 5}}
```

Interromper o filho não equivale a desligar o equipamento. O exemplo não testa defeitos físicos, corrupção de setores, concorrência entre escritores, ações em outros bancos ou entrega de mensagens externas. `DELETE` e `FULL` são configurações explícitas de journal e sincronização do experimento, não conclusões de benchmark.

## Verificações

A partir da raiz do repositório:

```bash
python3 -m unittest discover -s scripts/tests -p 'test_chapter16_examples.py' -v
```

Os [14 testes](../../../../scripts/tests/test_chapter16_examples.py) verificam comunicação e códigos de saída, representação de quebra de linha, estado inicial, aplicação, repetição, conflito de conteúdo, entradas recusadas, duas interrupções conhecidas, execução independente e limpeza. A execução local utilizou Linux, Python 3.13.5 e SQLite 3.46.1; os resultados no runner são registrados separadamente. Não se afirma reprodução de serviços, agendadores ou logs Windows.
