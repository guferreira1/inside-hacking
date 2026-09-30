from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from collections import Counter
import hashlib
import json
import os
import platform
import re
import sqlite3
import subprocess
import sys
import unicodedata
import unittest
import urllib.error
import urllib.request

ROOT = Path.cwd()
REPO = 'guferreira1/inside-hacking'
BASE = '1d3817567d78a03aa12c174ac5eb1e71e57b437b'
CH = 'book/modulo-3/capitulo-16'
AUDIT = 'editorial/audits/2026-09-29-capitulo-16.md'
CHECKS = 'editorial/updates/capitulo-16-checks.json'
changed = set()


def read(path):
    return Path(path).read_text(encoding='utf-8')


def write(path, text):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text.rstrip() + '\n', encoding='utf-8')
    changed.add(path)


def line_change(path, prefix, transform):
    text = read(path)
    lines = text.splitlines()
    indexes = [i for i, line in enumerate(lines) if line.startswith(prefix)]
    if len(indexes) != 1:
        raise RuntimeError(f'{path}: expected one line starting {prefix!r}, got {len(indexes)}')
    i = indexes[0]
    lines[i] = transform(lines[i])
    write(path, '\n'.join(lines))


def replace(path, old, new):
    text = read(path)
    if text.count(old) != 1:
        raise RuntimeError(f'{path}: replacement count for {old!r}: {text.count(old)}')
    write(path, text.replace(old, new))


def section_transform(path, heading, transform):
    text = read(path)
    start = text.index(heading)
    end = text.find('\n## ', start + len(heading))
    if end < 0:
        end = len(text)
    write(path, text[:start] + transform(text[start:end]) + text[end:])


sections = sorted(Path(CH).glob('16.*.md'))
if len(sections) != 7:
    raise RuntimeError('Chapter 16 must have seven sections.')
section_by_number = {p.name.split('-', 1)[0]: p for p in sections}
all_text = '\n'.join(read(p) for p in sections)
refs = read(CH + '/referencias.md')
expected_sources = set(range(1,45))
used_sources = {int(x) for x in re.findall(r'\[S(\d+)\]\(referencias.md#s\d+\)', all_text)}
if used_sources != expected_sources:
    raise RuntimeError(f'Reference coverage mismatch: {used_sources ^ expected_sources}')
if len(re.findall(r'^\d+\. ', read(str(sections[-1])), re.M)) != 14:
    raise RuntimeError('Question count mismatch.')
if len(re.findall(r'^## \d+\. ', read(CH + '/solucoes.md'), re.M)) != 14:
    raise RuntimeError('Answer count mismatch.')

# Prior approval: preserve manuscripts, sources and test limitations.
line_change('book/modulo-3/capitulo-15/README.md', '> **Status:**', lambda _: '> **Status:** VALIDATED — versão editorial 1.0; leitura aprovada e ciclo interno concluído em 29/09/2026. Fontes e verificações anteriores preservadas; revisão técnica independente pendente. [Registro editorial](../../../editorial/reviews/capitulo-15.md).')
replace('book/modulo-3/capitulo-15/15.7-investigacao-e-verificacao.md', 'A próxima unidade prevista é **16 — Processos, serviços, logs e persistência de estado**, mantendo a sequência do módulo.', 'O percurso continua no [Capítulo 16 — Processos, serviços, logs e persistência de estado](../capitulo-16/README.md), mantendo a sequência do módulo.')
path = 'book/modulo-3/capitulo-15/referencias.md'
text = read(path)
if 'DRAFT 0.1' not in text:
    raise RuntimeError('Chapter 15 source header is not the expected draft.')
write(path, text.replace('DRAFT 0.1', 'VALIDATED 1.0 — fechamento interno em 29/09/2026; revisão independente pendente', 1))
path = 'editorial/reviews/capitulo-15.md'
replace(path, '**Estado:** DRAFT 0.1.', '**Estado atual:** VALIDATED — versão editorial 1.0.')
write(path, read(path) + '\n## Aprovação e fechamento interno\n\nO pedido de continuidade do mantenedor registra aprovação da leitura do capítulo 15. Foram preservados o manuscrito, as fontes, os nove testes e os limites da validação anterior, com atualização de estado e navegação. A regressão desta entrega é registrada na [auditoria do capítulo 16](../audits/2026-09-29-capitulo-16.md). Não houve revisão técnica independente nem atribuição de domínio prático ao leitor.\n')

# Reader indexes: update only the current chapter and current module.
line_change('README.md', '| [15 · ', lambda line: line.replace('Rascunho para leitura — v0.1', 'Revisão interna concluída — v1.0') + '\n| [16 · Processos, serviços, logs e persistência de estado](book/modulo-3/capitulo-16/README.md) | Ciclos de vida, supervisão, agendamento, logs e retomada do trabalho. | Rascunho para leitura — v0.1 |')
line_change('README.md', 'Os capítulos 1 a 15 estão disponíveis.', lambda line: line.replace('1 a 15', '1 a 16', 1).replace('11 a 14', '11 a 15', 1).replace('capítulo 15 está', 'capítulo 16 está', 1))
line_change('book/README.md', '| [III · ', lambda _: '| [III · Sistemas operacionais](modulo-3/README.md) | Capítulos 11 a 17 | Capítulos 11 a 16 disponíveis; 17 planejado |')
line_change('book/README.md', '| 15 | ', lambda line: line.replace('Rascunho para leitura — v0.1', 'Revisão interna concluída — v1.0') + '\n| 16 | [Processos, serviços, logs e persistência de estado](modulo-3/capitulo-16/README.md) | Rascunho para leitura — v0.1 |')
block = '\n### Dentro do Capítulo 16\n\n'
for p in sections:
    title = read(p).splitlines()[0].removeprefix('# ')
    block += '- [' + title + '](modulo-3/capitulo-16/' + p.name + ')\n'
block += '- [Exemplos opcionais](modulo-3/capitulo-16/exemplos/README.md), [respostas comentadas](modulo-3/capitulo-16/solucoes.md) e [referências](modulo-3/capitulo-16/referencias.md).\n'
replace('book/README.md', '\n## Como navegar', block + '\n## Como navegar')
line_change('book/modulo-3/README.md', '| 15 | ', lambda line: line.replace('Rascunho para leitura — v0.1', 'Revisão interna concluída — v1.0'))
line_change('book/modulo-3/README.md', '| 16 | ', lambda _: '| 16 | [Processos, serviços, logs e persistência de estado](capitulo-16/README.md) | Rascunho para leitura — v0.1 |')
line_change('book/modulo-3/README.md', 'Os capítulos 11 a 15 estão disponíveis', lambda _: 'Os capítulos 11 a 16 estão disponíveis neste módulo. Os capítulos 11 a 15 têm revisão interna concluída; o 16 está em primeira leitura. O capítulo 17 permanece planejado no [sumário mestre](../../editorial/master-outline.md). A numeração e a ordem continuam globais, sem reorganização.')
replace('book/modulo-3/README.md', '**[Continuar no Capítulo 15 →](capitulo-15/README.md)**', '**[Continuar no Capítulo 16 →](capitulo-16/README.md)**')

# Bibliography and coverage retain historical records.
section_transform('book/bibliografia.md', '## Capítulo 15', lambda part: part.replace('DRAFT 0.1', 'VALIDATED 1.0, com leitura aprovada e limites de revisão independente preservados').replace('Primeira entrega VALIDATED', 'Versão editorial VALIDATED'))
bib = '\n## Capítulo 16 — Processos, serviços, logs e persistência de estado\n\nAs [44 referências](modulo-3/capitulo-16/referencias.md) relacionam documentação Linux, systemd, procps-ng, Cronie, logrotate, Microsoft, Python, SQLite e OWASP. As reproduções de manuais são identificadas; não se confunde versão documental com ambiente executado.\n\nOs [dois exemplos próprios](modulo-3/capitulo-16/exemplos/README.md) e os [14 testes](../scripts/tests/test_chapter16_examples.py) separam inicialização, término, diagnóstico, efeito confirmado e resposta ausente. O exemplo SQLite usa apenas um banco temporário e interrupções de processo em dois pontos conhecidos, sem simular falha de energia ou sistema distribuído. O capítulo permanece DRAFT 0.1; [registro editorial](../editorial/reviews/capitulo-16.md) e [auditoria](../editorial/audits/2026-09-29-capitulo-16.md) delimitam fontes, execuções e revisão.\n'
replace('book/bibliografia.md', '\n## Política de referências', bib + '\n## Política de referências')
p = 'editorial/coverage-matrix.md'
lines = read(p).splitlines()
lines = [line.replace('DRAFT', 'revisão interna 1.0') if 'capitulo-15/' in line and 'DRAFT' in line else line for line in lines]
write(p, '\n'.join(lines))
coverage = '\n### Capítulo 16 — Ciclo de vida e continuidade\n\n| Seção | Teoria | Aplicação e verificação | Limites |\n| --- | --- | --- | --- |\n'
coverage_rows = [
 ('Ciclo de vida', 'Filho próprio, inicialização, espera, saídas e término.', 'Sem manipular processos externos ou criar zumbis deliberadamente.'),
 ('Serviços e supervisão', 'Tipos, prontidão, watchdog e contratos SCM/systemd.', 'Pesquisa documental; nenhum serviço foi instalado.'),
 ('Configuração e reinício', 'Reload, restart, dependências, contexto e recuperação.', 'Nenhum comando de alteração foi aplicado ao host.'),
 ('Agendamento', 'Cron, timers e Agendador de Tarefas; sobreposição.', 'Modelos de tempo fictícios; nenhuma tarefa registrada.'),
 ('Logs e tempo', 'Origem, correlação, retenção, rotação e relógios.', 'Somente teste JSON sintético; sem extrair logs reais.'),
 ('Estado e confirmação', 'SQLite, transação local, repetição e resposta ausente.', 'Interrupções do processo; sem energia, corrupção física ou concorrência testada.'),
 ('Investigação', 'Linha do tempo, hipótese, confirmação e limites de autoridade.', 'Caso Aurora fictício; sem diagnóstico de incidente real.')]
for i, (pfile, row) in enumerate(zip(sections, coverage_rows), 1):
    topic, application, limit = row
    coverage += f'| 16.{i} | [{topic}](../{pfile.as_posix()}) | {application} | {limit} |\n'
section_transform('editorial/coverage-matrix.md', '## Módulo III', lambda part: part.rstrip() + '\n' + coverage)

# Durable editorial state, not unreported study metrics.
status = 'editorial/publication-status.md'
line_change(status, '| 15 | ', lambda _: '| 15 | VALIDATED — versão editorial 1.0; leitura aprovada e ciclo interno concluído em 29/09/2026 | Manuscrito, 47 referências, quatorze respostas e nove testes preservados. Validação anterior e nova regressão identificadas; revisão independente pendente. [Registro](reviews/capitulo-15.md). |\n| 16 | DRAFT 0.1 — primeira entrega de leitura | Sete seções, quatorze respostas, 44 referências, dois exemplos e 14 testes próprios. Serviços e consultas Windows por documentação; sem laboratório de administração. Leitura e revisão independente pendentes. [Registro](reviews/capitulo-16.md). |')
replace(status, 'As aprovações dos capítulos 4 a 14', 'As aprovações dos capítulos 4 a 15')
line_change(status, 'O [Módulo III]', lambda _: 'O [Módulo III](../book/modulo-3/README.md) possui os capítulos 11 a 15 com ciclos internos concluídos e o [Capítulo 16](../book/modulo-3/capitulo-16/README.md) em primeira entrega. O capítulo 17 permanece planejado, na ordem original. O módulo continua em produção; a aprovação editorial não atribui domínio prático ao leitor.')
line_change(status, '1. Receber a leitura do Capítulo 15', lambda _: '1. Receber a leitura do Capítulo 16, acompanhando ciclo de vida, supervisão, logs e retomada do estado confirmado.')
line_change(status, '3. A comunicação de fechamento do Módulo II', lambda _: '3. A comunicação de fechamento do Módulo II foi preparada; não presumir publicação. Depois da leitura do capítulo 16, prosseguir para o Capítulo 17 — Virtualização e isolamento, mantendo glossário, fontes e navegação na mesma entrega.')
write('editorial/README.md', read('editorial/README.md') + '\n### Entrega do capítulo 16\n\n[Registro editorial](reviews/capitulo-16.md) · [Auditoria](audits/2026-09-29-capitulo-16.md). Aprovação do capítulo 15 preservada, capítulo 16 em primeira leitura e ordem original mantida.\n')

# Glossary: preserve definitions and footer; add only witnessed terms.
def normalized(text):
    return ''.join(c for c in unicodedata.normalize('NFD', text.casefold()) if not unicodedata.combining(c))

p = 'book/glossario.md'
original = read(p)
marker = '\n---\n\nAs definições metodológicas'
if original.count(marker) != 1:
    raise RuntimeError('Unknown glossary footer.')
body, footer = original.split(marker)
start = body.index('\n## A')
intro, body = body[:start], body[start:]
entries = {m.group(1).strip(): m.group(2).strip() for m in re.finditer(r'^### ([^\n]+)\n(.*?)(?=^### |^## |\Z)', body, re.M | re.S)}
if len(entries) != 554:
    raise RuntimeError(f'Expected 554 existing entries; found {len(entries)}')
preserved = dict(entries)
lookup = {normalized(key): key for key in entries}
added, extended = [], []
for term, definition, number in json.loads(read('editorial/updates/capitulo-16-glossario.json')):
    source = section_by_number[number]
    if normalized(term) not in normalized(read(source)):
        raise RuntimeError('Term without occurrence: ' + term)
    link = f'[Conceito: {number}](modulo-3/capitulo-16/{source.name}).'
    key = lookup.get(normalized(term))
    if key:
        entries[key] += '\n\n' + definition + ' ' + link
        extended.append(key)
    else:
        entries[term] = definition + ' ' + link
        lookup[normalized(term)] = term
        added.append(term)
letters = set(re.findall(r'^## ([A-Z])$', body, re.M))
letters.update(normalized(k)[0].upper() for k in entries)
new = intro.rstrip() + '\n'
for letter in sorted(letters):
    new += '\n## ' + letter + '\n'
    for term in sorted((k for k in entries if normalized(k)[0].upper() == letter), key=normalized):
        new += '\n### ' + term + '\n\n' + entries[term] + '\n'
new += marker + footer
for key, definition in preserved.items():
    if not entries[key].startswith(definition):
        raise RuntimeError('Previous definition changed: ' + key)
write(p, new)

# Metadata exists before traversal; it must not pretend that checks already ran.
write(AUDIT, '# Auditoria do Capítulo 16\n\nPreparação em execução; resultados ainda não confirmados.\n')
write(CHECKS, '{}')
review = 'editorial/reviews/capitulo-16.md'
write(review, read(review) + '\n## Verificação de conjunto\n\nOs resultados executados constam na [auditoria desta entrega](../audits/2026-09-29-capitulo-16.md) e no [registro de verificações](../updates/capitulo-16-checks.json). A integração em main e a checagem posterior são etapas distintas.\n')

# The staging-only workflow is excluded from the publishable tree.
for temp in ('.editorial_prepare16.py', '.github/workflows/prepare-chapter16.yml'):
    Path(temp).unlink()
    changed.add(temp)

suite = unittest.defaultTestLoader.discover('scripts/tests')
result = unittest.TextTestRunner(verbosity=1).run(suite)
tests = {'total':result.testsRun, 'passed':result.testsRun-len(result.failures)-len(result.errors)-len(result.skipped), 'failures':len(result.failures), 'errors':len(result.errors), 'skipped':len(result.skipped)}
if not result.wasSuccessful() or result.skipped or result.testsRun != 113:
    raise RuntimeError('Regression failed or did not execute all 113 tests: ' + json.dumps(tests))

urls = sorted(set(re.findall(r'^https://\S+', refs, re.M)))
if len(urls) != 44:
    raise RuntimeError('Unexpected source URL count: ' + str(len(urls)))

def check_external(url):
    request = urllib.request.Request(url, headers={'User-Agent':'inside-hacking-editorial-link-check/1.0'})
    try:
        with urllib.request.urlopen(request, timeout=12) as response:
            response.read(1024)
            return {'url':url,'status':response.status,'final_url':response.geturl(),'result':'accessible'}
    except urllib.error.HTTPError as exc:
        return {'url':url,'status':exc.code,'result':'restricted' if exc.code in (401,403,429) else 'unavailable' if exc.code in (404,410) else 'inconclusive'}
    except Exception as exc:
        return {'url':url,'status':None,'result':'inconclusive','error_type':type(exc).__name__}

with ThreadPoolExecutor(max_workers=8) as pool:
    external = list(pool.map(check_external, urls))
if any(r['result'] == 'unavailable' for r in external):
    print('EXTERNAL_RESULTS=' + json.dumps(external), flush=True)
    raise RuntimeError('Source returned 404 or 410; review it before publication.')


def docs_check():
    process = subprocess.run([sys.executable,'scripts/check_docs.py'], capture_output=True,text=True,timeout=60)
    print('DOCS_CHECK=' + process.stdout, flush=True)
    if process.returncode:
        raise RuntimeError('Documentation verification failed: ' + process.stderr)
    value = json.loads(process.stdout)
    if value['internal_errors']:
        raise RuntimeError('Internal navigation errors remain.')
    return value

first = docs_check()
versions = {'python':platform.python_version(),'os':platform.platform(),'sqlite':sqlite3.sqlite_version,'euid':os.geteuid()}
glossary = {'before':len(preserved),'after':len(entries),'added':added,'extended':extended,'preserved_previous_definitions':len(preserved)}
run_url = 'https://github.com/' + REPO + '/actions/runs/' + os.environ['GITHUB_RUN_ID']
counts = dict(Counter(item['result'] for item in external))
report = f'''# Auditoria de entrega — Capítulo 16

**Data:** 29/09/2026. **Base:** `{BASE}`. **Tipo:** revisão interna.

[Estado editorial](../publication-status.md) · [Capítulo](../../book/modulo-3/capitulo-16/README.md) · [Execução de preparação]({run_url})

## Continuidade

A leitura do capítulo 15 foi aprovada pelo pedido de avanço. Manuscrito, fontes e validações anteriores foram preservados, com atualização dos estados e da navegação. O capítulo 16 contém sete seções, quatorze respostas e 44 referências. A próxima unidade continua sendo 17 — Virtualização e isolamento.

## Exemplos e regressão

Foram executados **{tests['total']} testes**, com **{tests['passed']} aprovados**, **{tests['skipped']} skips**, **{tests['failures']} falhas** e **{tests['errors']} erros**. São 99 testes anteriores e 14 novos. Os exemplos usam somente processos filhos conhecidos e bancos temporários próprios.

```json
{json.dumps(versions,ensure_ascii=False,indent=2)}
```

O teste de ciclo de vida distingue inicialização, espera e término. O exemplo SQLite distingue encerramento antes do commit, encerramento após o commit sem resposta, repetição equivalente e conflito de conteúdo. Não houve corte de energia, simulação de corrupção de setores ou teste de concorrência. Os controles systemd e Windows foram pesquisados por documentação; não foram instalados serviços nem agendamentos.

## Documentação e glossário

README principal, índice geral, índice do Módulo III, bibliografia, matriz de cobertura e registros editoriais foram sincronizados. O glossário passou de **{len(preserved)} para {len(entries)} verbetes**, com **{len(added)} novos** e **{len(extended)} complementados**. As {len(preserved)} definições anteriores e o rodapé de referências foram preservados; cada termo incluído possui ocorrência na seção indicada.

A primeira passagem conferiu **{first['markdown_files']} Markdown** e **{first['internal_links']} destinos internos**, sem erros. A segunda passagem, depois de gravar esta auditoria, está no [registro de verificações](../updates/capitulo-16-checks.json).

## Referências externas

Foram consultadas **{len(urls)} URLs** por HTTP. Resultado: `{json.dumps(counts,ensure_ascii=False)}`. Bloqueio automatizado ou falha de rede é registrado como restrição ou resultado inconclusivo, não como ausência da fonte. A disponibilidade HTTP não comprova a correção integral do texto. A relação entre mecanismos e referências foi revista durante a escrita.

## Limites

Revisão assistida por IA não é revisão técnica independente. O capítulo 16 permanece DRAFT para primeira leitura. Aprovação do capítulo 15 não atribui horas, execução de laboratórios ou domínio prático ao leitor. O Módulo III continua em produção; a pendência do capítulo 1 e o fechamento interno do Módulo II não foram alterados.

Não houve alvo real de teste, leitura de dados privados, publicação no LinkedIn ou geração de PDF. Esta auditoria registra preparação. O commit em main e a verificação após integração são confirmados separadamente no histórico do GitHub.
'''
write(AUDIT, report)
record = {'base':BASE,'run_url':run_url,'tests':tests,'versions':versions,'glossary':glossary,'first_docs':first,'external_urls':external}
write(CHECKS,json.dumps(record,ensure_ascii=False,indent=2))
second = docs_check()
record['second_docs'] = second
write(CHECKS,json.dumps(record,ensure_ascii=False,indent=2))

# Do not touch any branch/ref; return one candidate tree for explicit integration.
base_tree = subprocess.check_output(['git','rev-parse','HEAD^{tree}'],text=True).strip()
elements = []
for path in sorted(changed):
    if Path(path).exists():
        elements.append({'path':path,'mode':'100644','type':'blob','content':read(path)})
    else:
        elements.append({'path':path,'mode':'100644','type':'blob','sha':None})
payload = json.dumps({'base_tree':base_tree,'tree':elements}).encode()
request = urllib.request.Request('https://api.github.com/repos/' + REPO + '/git/trees', data=payload, method='POST', headers={'Authorization':'Bearer '+os.environ['GH_TOKEN'],'Accept':'application/vnd.github+json','Content-Type':'application/json','User-Agent':'inside-hacking-editorial'})
with urllib.request.urlopen(request,timeout=45) as response:
    tree = json.load(response)['sha']
if re.fullmatch('[0-9a-f]{40}',tree) is None:
    raise RuntimeError('Invalid returned tree identifier.')
print('TEST_SUMMARY=' + json.dumps(tests), flush=True)
print('GLOSSARY=' + json.dumps(glossary,ensure_ascii=False), flush=True)
print('FINAL_DOCS=' + json.dumps(second,ensure_ascii=False), flush=True)
print('EXTERNAL_SUMMARY=' + json.dumps(counts), flush=True)
print('CANDIDATE_TREE=' + tree, flush=True)
print('NO_BRANCH_OR_REF_UPDATED', flush=True)
