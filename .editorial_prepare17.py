"""One-time editorial preparation. Creates a tree only; never updates refs."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import collections
import hashlib
import importlib.util
import json
import os
import platform
import re
import subprocess
import sys
import time
import unicodedata
import unittest
import urllib.error
import urllib.request

ROOT = Path.cwd()
REPO = 'guferreira1/inside-hacking'
BASE = '5b812f65e9eef87f1bf8b968481a7c290dc2370d'
DATE = '29/09/2026'
CH = 'book/modulo-3/capitulo-17'
AUDIT = 'editorial/audits/2026-09-29-capitulo-17.md'
CHECKS = 'editorial/updates/capitulo-17-checks.json'
changed = set()

def read(path):
    return Path(path).read_text(encoding='utf-8')

def write(path, content):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding='utf-8')
    changed.add(path)

def replace(path, old, new, count=1):
    text = read(path)
    if text.count(old) != count:
        raise RuntimeError(f'Unexpected replacement count in {path}: {old[:100]!r}')
    write(path, text.replace(old, new))

def replace_row(path, marker, transform):
    lines = read(path).splitlines(keepends=True)
    hits = [i for i, line in enumerate(lines) if line.startswith('| ') and marker in line]
    if len(hits) != 1:
        raise RuntimeError(f'Row not unique in {path}: {marker}')
    i = hits[0]
    lines[i] = transform(lines[i])
    write(path, ''.join(lines))

def norm(value):
    return ''.join(c for c in unicodedata.normalize('NFKD', value.casefold()) if not unicodedata.combining(c))

# Final terminology refinements; no changes to the chapter order.
replace(CH + '/17.2-maquinas-virtuais-e-hipervisores.md',
        'do TCG, mecanismo de tradução usado para emulação de CPUs.',
        'do TCG (*Tiny Code Generator*), mecanismo de tradução usado para emulação de CPUs.')
replace(CH + '/17.3-containers-namespaces-e-recursos.md',
        '| UTS | Nome do host e nome de domínio NIS. |',
        '| UTS | Nome do host; a categoria é identificada como `uts`. |')
replace(CH + '/17.3-containers-namespaces-e-recursos.md',
        '| IPC | Determinados mecanismos de comunicação entre processos. |',
        '| IPC | Interprocess Communication: determinados mecanismos de comunicação entre processos. |')
replace(CH + '/17.3-containers-namespaces-e-recursos.md',
        ' O significado de domínio NIS também não deve ser confundido com o domínio de um site.', '')

sections = sorted(Path(CH).glob('17.*.md'), key=lambda p: int(p.name.split('-')[0].split('.')[1]))
assert len(sections) == 7
section_names = {int(p.name.split('-')[0].split('.')[1]): p.name for p in sections}
titles = {n: read(CH + '/' + name).splitlines()[0].split(' — ', 1)[1] for n, name in section_names.items()}
reftext = read(CH + '/referencias.md')
source_ids = re.findall(r'<a id="s(\d+)"></a>', reftext)
assert sorted(map(int, source_ids)) == list(range(1, 39))
for p in sections:
    for sid in re.findall(r'referencias\.md#s(\d+)', p.read_text(encoding='utf-8')):
        assert sid in source_ids, (p, sid)
questions = read(CH + '/' + section_names[7]).split('## Para conferir a compreensão', 1)[1]
assert len(re.findall(r'^\d+\. ', questions, re.M)) == 14
assert len(re.findall(r'^## \d+\.', read(CH + '/solucoes.md'), re.M)) == 14

# Approve only the preceding chapter, preserving historical execution records.
previous = 'book/modulo-3/capitulo-16'
replace(previous + '/README.md',
        '> **Status:** DRAFT 0.1 — primeira entrega de leitura. Fontes, execuções e limites no [registro editorial](../../../editorial/reviews/capitulo-16.md). Revisão técnica independente pendente.',
        '> **Status:** VALIDATED — versão editorial 1.0; leitura aprovada e ciclo interno concluído em 29/09/2026. Fontes, execuções e limites no [registro editorial](../../../editorial/reviews/capitulo-16.md). Revisão técnica independente pendente.')
text = read(previous + '/referencias.md')
assert text.count('DRAFT 0.1') == 1
write(previous + '/referencias.md', text.replace('DRAFT 0.1', 'VALIDATED 1.0 — fechamento interno em 29/09/2026; revisão independente pendente'))
replace(previous + '/16.7-investigacao-e-verificacao.md',
        'A próxima unidade permanece **17 — Virtualização e isolamento**, na ordem original do módulo.',
        'Continue no [Capítulo 17 — Virtualização e isolamento](../capitulo-17/README.md), na ordem original do módulo.')
replace('editorial/reviews/capitulo-16.md',
        '**Data:** 29/09/2026. **Estado:** DRAFT 0.1. **Módulo:** III.',
        '**Primeira entrega:** 29/09/2026. **Estado atual:** VALIDATED — versão editorial 1.0; ciclo interno concluído em 29/09/2026. **Módulo:** III.')
write('editorial/reviews/capitulo-16.md', read('editorial/reviews/capitulo-16.md') + '\n## Aprovação e reconferência interna\n\nO pedido de continuidade confirma a aprovação da leitura. As sete seções e quatorze respostas foram relidas, preservando o conteúdo e os limites dos experimentos. Fontes e execuções da entrega anterior não são apresentadas como novas execuções; a regressão desta rodada está na [auditoria do capítulo 17](../audits/2026-09-29-capitulo-17.md). Não foram atribuídas horas ou competência prática não relatadas. Revisão técnica independente permanece pendente.\n')

# Reader indexes.
replace_row('README.md', '[16 · ', lambda line: line.replace('Rascunho para leitura — v0.1', 'Revisão interna concluída — v1.0') + '| [17 · Virtualização e isolamento](book/modulo-3/capitulo-17/README.md) | VMs, containers, fronteiras, compartilhamentos, conectividade e recuperação. | Rascunho para leitura — v0.1 |\n')
replace('README.md',
        'Os capítulos 1 a 16 estão disponíveis. No Módulo III, os capítulos 11 a 15 concluíram seus ciclos internos, e o capítulo 16 está em primeira entrega de leitura.',
        'Os capítulos 1 a 17 estão disponíveis. No Módulo III, os capítulos 11 a 16 concluíram seus ciclos internos, e o capítulo 17 está em primeira entrega de leitura. Todos os textos previstos deste módulo foram escritos; o fechamento interno depende da leitura do 17 e da revisão de conjunto.')
replace_row('book/README.md', '| 16 | [', lambda line: line.replace('Rascunho para leitura — v0.1', 'Revisão interna concluída — v1.0') + '| 17 | [Virtualização e isolamento](modulo-3/capitulo-17/README.md) | Rascunho para leitura — v0.1 |\n')
replace('book/README.md', 'Capítulos 11 a 16 disponíveis; 17 planejado', 'Todos os textos disponíveis; capítulo 17 em primeira leitura')
index17 = '\n### Dentro do Capítulo 17\n\n' + ''.join(f'- [17.{n} · {titles[n]}](modulo-3/capitulo-17/{section_names[n]})\n' for n in range(1, 8))
index17 += '- [Exemplo opcional de namespaces próprios](modulo-3/capitulo-17/exemplos/README.md).\n- [Respostas comentadas](modulo-3/capitulo-17/solucoes.md) e [referências](modulo-3/capitulo-17/referencias.md).\n\n'
replace('book/README.md', '## Como navegar', index17 + '## Como navegar')
replace_row('book/modulo-3/README.md', '| 16 | [', lambda line: line.replace('Rascunho para leitura — v0.1', 'Revisão interna concluída — v1.0'))
replace('book/modulo-3/README.md', '| 17 | Virtualização e isolamento | Planejado |', '| 17 | [Virtualização e isolamento](capitulo-17/README.md) | Rascunho para leitura — v0.1 |')
replace('book/modulo-3/README.md',
        'Os capítulos 11 a 16 estão disponíveis neste módulo. Os capítulos 11 a 15 têm revisão interna concluída; o 16 está em primeira leitura. O capítulo 17 permanece planejado no [sumário mestre](../../editorial/master-outline.md). A numeração e a ordem continuam globais, sem reorganização.',
        'Todos os capítulos previstos deste módulo, do 11 ao 17, estão disponíveis. Os capítulos 11 a 16 têm revisão interna concluída; o 17 está em primeira leitura. O fechamento interno do módulo depende dessa leitura e da revisão de conjunto. A sequência do [sumário mestre](../../editorial/master-outline.md) permanece inalterada; o próximo módulo começa no capítulo 18.')
replace('book/modulo-3/README.md', '**[Continuar no Capítulo 16 →](capitulo-16/README.md)**', '**[Continuar no Capítulo 17 →](capitulo-17/README.md)**')

# Bibliography, coverage and publication records.
replace('book/bibliografia.md', 'O capítulo permanece DRAFT 0.1; [registro editorial](../editorial/reviews/capitulo-16.md)', 'A leitura foi aprovada e o ciclo interno 1.0 foi concluído; [registro editorial](../editorial/reviews/capitulo-16.md)')
replace('book/bibliografia.md', '## Política de referências', '## Capítulo 17 — Virtualização e isolamento\n\nAs [38 referências numeradas](modulo-3/capitulo-17/referencias.md) relacionam 39 URLs de documentação primária Linux, QEMU, Oracle, Docker, Microsoft e Python. O percurso separa representação, restrição, kernel compartilhado, recursos concedidos, conectividade e alcance de restauração. As configurações de VM, containers e Windows Sandbox são documentais, não reproduções alegadas.\n\nO [exemplo próprio](modulo-3/capitulo-17/exemplos/README.md) e os [nove testes](../scripts/tests/test_chapter17_examples.py) comparam namespaces de pai e filho e verificam contratos e limpeza. Não criam isolamento nem avaliam escapes. O capítulo permanece DRAFT 0.1 para leitura; seu [registro editorial](../editorial/reviews/capitulo-17.md) e a [auditoria](../editorial/audits/2026-09-29-capitulo-17.md) distinguem pesquisa, execução local e runner.\n\n## Política de referências')
coverage = '\n### Capítulo 17 — Fronteiras entre ambientes\n\n| Seção | Teoria | Aplicação e verificação | Limites |\n| --- | --- | --- | --- |\n'
applications = [
    'Requisito de proteção e base de confiança; venv e chroot como recortes.',
    'Modelo de máquina, acelerador, memória e dispositivos.',
    'Visões, identidade, kernel compartilhado e orçamento de recursos.',
    'Origens de arquivos, integrações, administração e filtragem.',
    'Entrada e saída, topologia e opções de conectividade.',
    'Estado incluído, efeito externo e identificação de artefatos.',
    'Caso Aurora e comparação real de namespaces de pai e filho.'
]
for n in range(1, 8):
    limit = 'Fundamento documental; sem configurar VM, container ou host.' if n < 7 else 'Nove testes delimitados; não comprova isolamento externo nem resistência a escapes.'
    coverage += f'| 17.{n} | [{titles[n]}](../book/modulo-3/capitulo-17/{section_names[n]}) | {applications[n-1]} | {limit} |\n'
coverage += '\nCapítulo 17 em primeira leitura; [fontes](../book/modulo-3/capitulo-17/referencias.md) e [registro](reviews/capitulo-17.md). O capítulo 16 concluiu o ciclo interno 1.0 com limites preservados.\n\n'
replace('editorial/coverage-matrix.md', '## Cobertura ainda planejada', coverage + '## Cobertura ainda planejada')
replace('editorial/coverage-matrix.md',
        'Os capítulos a partir do 13 não recebem linhas de cobertura efetiva antes da produção dos textos. Os capítulos 11 e 12 não substituem o aprofundamento futuro de Windows, administração, permissões ou isolamento.',
        'Os capítulos a partir do 18 não recebem linhas de cobertura efetiva antes da produção dos textos. Os fundamentos dos capítulos 11 a 17 não substituem as unidades futuras de administração aplicada, segurança de plataformas ou pós-exploração.')

new16 = '| 16 | VALIDATED — versão editorial 1.0; leitura aprovada e ciclo interno concluído em 29/09/2026 | Sete seções, quatorze respostas, 44 referências e dois exemplos preservados. Regressão identificada separadamente; revisão independente pendente. [Registro](reviews/capitulo-16.md). |\n'
new17 = '| 17 | DRAFT 0.1 — primeira entrega de leitura | Sete seções, quatorze respostas, 38 referências e nove testes próprios. Comparação Linux de namespaces; plataformas de virtualização por documentação, sem administração executada. Leitura e revisão independente pendentes. [Registro](reviews/capitulo-17.md). |\n'
replace_row('editorial/publication-status.md', '| 16 | ', lambda _: new16 + new17)
replace('editorial/publication-status.md', 'As aprovações dos capítulos 4 a 15', 'As aprovações dos capítulos 4 a 16')
replace('editorial/publication-status.md',
        'O [Módulo III](../book/modulo-3/README.md) possui os capítulos 11 a 15 com ciclos internos concluídos e o [Capítulo 16](../book/modulo-3/capitulo-16/README.md) em primeira entrega. O capítulo 17 permanece planejado, na ordem original. O módulo continua em produção; a aprovação editorial não atribui domínio prático ao leitor.',
        'O [Módulo III](../book/modulo-3/README.md) possui todos os textos previstos. Os capítulos 11 a 16 têm ciclos internos concluídos e o [Capítulo 17](../book/modulo-3/capitulo-17/README.md) está em primeira leitura. Depois dessa aprovação, falta a revisão de conjunto para o fechamento interno e o marco de divulgação no LinkedIn, antes de iniciar o Módulo IV. A sequência permanece original; aprovação editorial não atribui domínio prático ao leitor.')
status = read('editorial/publication-status.md')
lines = status.splitlines()
for i, line in enumerate(lines):
    if line.startswith('1. Receber a leitura do Capítulo 16'):
        lines[i] = '1. Receber a leitura do Capítulo 17 e revisar o conjunto do Módulo III, sem presumir aprovação antecipada ou revisão técnica independente.'
    if line.startswith('3. A comunicação de fechamento do Módulo II'):
        lines[i] = '3. Concluir internamente o Módulo III após leitura e revisão de conjunto, preparar sua publicação de marco no LinkedIn e então iniciar o Capítulo 18 — Como computadores se comunicam. Não presumir postagem nem criar automação.'
write('editorial/publication-status.md', '\n'.join(lines) + '\n')
write('editorial/README.md', read('editorial/README.md').rstrip() + '\n\n- [Entrega do capítulo 17 e aprovação do 16](audits/2026-09-29-capitulo-17.md).\n')

# Preserve every existing glossary definition and reference.
glossary = read('book/glossario.md')
marker = '\n---\n\nAs definições metodológicas'
assert glossary.count(marker) == 1
body, footer_rest = glossary.split(marker, 1)
footer = marker + footer_rest
first_letter = re.search(r'^## [A-Z]\s*$', body, re.M)
assert first_letter
intro = body[:first_letter.start()]
entry_pattern = r'^### ([^\n]+)\n\n(.*?)(?=^### |^## [A-Z]\s*$|\Z)'
old_entries = {name: definition.strip() for name, definition in re.findall(entry_pattern, body, re.M | re.S)}
assert len(old_entries) == 588, len(old_entries)
assert len({norm(k) for k in old_entries}) == len(old_entries)
entries = dict(old_entries)
lookup = {norm(k): k for k in entries}
additions = json.loads(read('editorial/updates/capitulo-17-glossario.json'))
added, extended = [], []
for item in additions:
    term, n = item['term'], item['section']
    content = read(CH + '/' + section_names[n]).replace('**', '').replace('`', '')
    if norm(item.get('occurrence', term)) not in norm(content):
        raise RuntimeError('Glossary term without occurrence: ' + term)
    definition = item['definition'] + f' [Conceito: 17.{n}](modulo-3/capitulo-17/{section_names[n]}).'
    key = lookup.get(norm(term))
    if key is not None:
        entries[key] += '\n\n' + definition
        extended.append(key)
    else:
        entries[term] = definition
        lookup[norm(term)] = term
        added.append(term)
for name, original in old_entries.items():
    assert original in entries[name], name
letters = sorted({norm(name)[0].upper() for name in entries})
nav = '**Consulta:** ' + ' · '.join(f'[{x}](#{x.lower()})' for x in letters) + '.'
intro, replacements = re.subn(r'^\*\*Consulta:\*\*[^\n]*', nav, intro, flags=re.M)
assert replacements == 1
rendered = intro.rstrip() + '\n\n'
for letter in letters:
    rendered += '## ' + letter + '\n\n'
    for name in sorted((k for k in entries if norm(k).startswith(letter.lower())), key=norm):
        rendered += '### ' + name + '\n\n' + entries[name] + '\n\n'
write('book/glossario.md', rendered.rstrip() + '\n' + footer)
assert footer in read('book/glossario.md')
glossary_result = {'before': len(old_entries), 'after': len(entries), 'added': added, 'extended': extended, 'preserved_previous_definitions': len(old_entries)}

# Create referenced records before invoking the link checker.
write(AUDIT, '# Auditoria de entrega — Capítulo 17\n\nVerificação em andamento nesta árvore de preparação; sem conclusão antecipada.\n')
write(CHECKS, '{}\n')

# Run all tests, keeping skips distinct from successes.
suite = unittest.defaultTestLoader.discover('scripts/tests')
result = unittest.TextTestRunner(verbosity=1).run(suite)
test_summary = {'total': result.testsRun, 'passed': result.testsRun - len(result.failures) - len(result.errors) - len(result.skipped), 'failures': len(result.failures), 'errors': len(result.errors), 'skipped': len(result.skipped)}
if not result.wasSuccessful() or result.testsRun != 122 or result.skipped:
    raise RuntimeError('Incomplete or failed regression: ' + json.dumps(test_summary))
observation = json.loads(subprocess.check_output([sys.executable, '-I', '-S', CH + '/exemplos/namespaces_proprios.py'], text=True, timeout=10))
assert observation['processos_distintos'] and observation['namespaces_comparados'] == 6
assert all(observation['mesmo_namespace'].values())
environment = {'python': platform.python_version(), 'os': platform.platform(), 'euid': os.geteuid(), 'bash': subprocess.check_output(['bash', '--version'], text=True).splitlines()[0]}

# Check only the exact primary-source URLs in this chapter.
urls = sorted(set(re.findall(r'^https?://\S+', reftext, re.M)))
assert len(urls) == 39, len(urls)
def check_url(url):
    for attempt in range(2):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'inside-hacking-editorial-link-check/1.0', 'Accept': 'text/html,application/xhtml+xml,*/*'})
            with urllib.request.urlopen(req, timeout=18) as response:
                response.read(1024)
                return {'url': url, 'status': response.status, 'final_url': response.geturl(), 'result': 'accessible'}
        except urllib.error.HTTPError as exc:
            kind = 'broken' if exc.code in (404, 410) else 'restricted' if exc.code in (401, 403, 429) else 'inconclusive'
            record = {'url': url, 'status': exc.code, 'result': kind}
            if kind in ('broken', 'restricted'):
                return record
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            record = {'url': url, 'status': None, 'result': 'inconclusive', 'error_type': type(exc).__name__}
        if attempt == 0:
            time.sleep(1)
    return record
with ThreadPoolExecutor(max_workers=8) as pool:
    external = list(pool.map(check_url, urls))
external_summary = dict(collections.Counter(x['result'] for x in external))
if external_summary.get('broken', 0):
    print(json.dumps(external, ensure_ascii=False, indent=2))
    raise RuntimeError('Primary reference returned 404/410')

# Remove preparation-only files before the final inventory.
for temporary in ('.editorial_prepare17.py', '.github/workflows/prepare-chapter17.yml'):
    Path(temporary).unlink()
    changed.add(temporary)

def docs_check():
    proc = subprocess.run([sys.executable, 'scripts/check_docs.py'], capture_output=True, text=True, timeout=60)
    print('DOCS_CHECK=' + proc.stdout, flush=True)
    if proc.returncode != 0:
        print(proc.stderr, flush=True)
        raise RuntimeError('Documentation checker failed')
    data = json.loads(proc.stdout)
    if data['internal_errors']:
        raise RuntimeError('Internal link errors')
    return data
first = docs_check()
report = f'''# Auditoria de entrega — Capítulo 17

**Data:** {DATE}. **Base:** `{BASE}`. **Tipo:** revisão interna.

[Estado editorial](../publication-status.md) · [Capítulo](../../book/modulo-3/capitulo-17/README.md) · [Execução de preparação](https://github.com/{REPO}/actions/runs/{os.environ['GITHUB_RUN_ID']})

## Continuidade e recorte

A leitura do capítulo 16 foi aprovada pelo pedido de avanço. Suas sete seções e quatorze respostas foram relidas; exemplos e limites anteriores permanecem identificados. O capítulo 17 tem sete seções, quatorze respostas e 38 referências numeradas, com 39 URLs primárias. A ordem do sumário não foi alterada.

## Reprodução

A regressão executou **{test_summary['total']} testes**, com **{test_summary['passed']} aprovados**, zero falhas, erros ou skips. São 113 testes anteriores e nove novos. O exemplo independente confirmou processos distintos e igualdade nos seis namespaces comparados entre pai e filho.

```json
{json.dumps(environment, ensure_ascii=False, indent=2)}
```

O experimento não cria namespaces, VMs ou containers, não muda privilégios, montagens, rede ou políticas. Não identifica a fronteira externa de um ambiente nem valida resistência a escapes. Falhas injetadas verificam contratos e fechamento de descritores, não incidentes reais. As observações locais anteriores permanecem distintas desta execução no runner.

## Documentação e glossário

Foram atualizados READMEs, índices, bibliografia, matriz de cobertura, navegação e registros editoriais. A nota final de cobertura que ainda tratava capítulos já escritos como futuros foi sincronizada. O glossário passou de **{glossary_result['before']} para {glossary_result['after']} verbetes**, com **{len(added)} novos** e **{len(extended)} complementados**. Todas as {len(old_entries)} definições anteriores e o rodapé de referências foram preservados; os termos novos têm ocorrência conferida.

A primeira passagem examinou **{first['markdown_files']} Markdown** e **{first['internal_links']} destinos internos**, sem erros. A segunda, posterior à gravação deste relatório, está no [registro de verificações](../updates/capitulo-17-checks.json). Checagem de links não substitui revisão factual independente.

## Referências externas

Foram consultadas 39 URLs primárias por HTTP. Resultado: `{json.dumps(external_summary, ensure_ascii=False)}`. Respostas restritas ou inconclusivas não são apresentadas como acessíveis nem como links mortos. Os resultados individuais constam no registro de verificações. Disponibilidade não comprova integralmente as afirmações técnicas.

## Estado e limites

O capítulo 17 permanece DRAFT para leitura. Todos os textos previstos do Módulo III foram escritos, mas seu fechamento interno requer a aprovação desta leitura e a revisão de conjunto. A publicação de marco no LinkedIn é a próxima etapa editorial desse fechamento, antes do capítulo 18. Não houve postagem ou criação de automação.

Revisão assistida por IA não é revisão técnica independente. Não foram atribuídos horas, laboratórios ou domínio prático ao leitor. A pendência do capítulo 1 e o fechamento interno do Módulo II foram preservados. Esta auditoria registra preparação; o commit na main e o CI posterior são confirmados separadamente.
'''
write(AUDIT, report)
write('editorial/reviews/capitulo-17.md', read('editorial/reviews/capitulo-17.md').rstrip() + f'\n\n## Verificação no runner\n\nA [execução de preparação](https://github.com/{REPO}/actions/runs/{os.environ["GITHUB_RUN_ID"]}) concluiu {test_summary["passed"]} testes sem falhas ou skips. A auditoria registra ambientes, observação independente do exemplo, preservação do glossário, consultas HTTP e checagens documentais. A confirmação de integração em main é separada.\n')
checks = {'base_commit': BASE, 'preparation_commit': os.environ['GITHUB_SHA'], 'run_id': os.environ['GITHUB_RUN_ID'], 'tests': test_summary, 'environment': environment, 'observation': observation, 'glossary': glossary_result, 'first_docs': first, 'external_summary': external_summary, 'external_urls': external}
write(CHECKS, json.dumps(checks, ensure_ascii=False, indent=2) + '\n')
second = docs_check()
checks['second_docs'] = second
write(CHECKS, json.dumps(checks, ensure_ascii=False, indent=2) + '\n')

# Do not include a changed master outline or any unrelated deletion.
assert 'editorial/master-outline.md' not in changed
assert all(Path(p).exists() or p in ('.editorial_prepare17.py', '.github/workflows/prepare-chapter17.yml') for p in changed)
head_tree = subprocess.check_output(['git', 'rev-parse', 'HEAD^{tree}'], text=True).strip()
assert re.fullmatch(r'[0-9a-f]{40}', head_tree)
items = []
for path in sorted(changed):
    if Path(path).exists():
        items.append({'path': path, 'mode': '100644', 'type': 'blob', 'content': read(path)})
    else:
        items.append({'path': path, 'mode': '100644', 'type': 'blob', 'sha': None})
request = urllib.request.Request(
    f'https://api.github.com/repos/{REPO}/git/trees',
    data=json.dumps({'base_tree': head_tree, 'tree': items}).encode('utf-8'),
    headers={'Authorization': 'Bearer ' + os.environ['GH_TOKEN'], 'Accept': 'application/vnd.github+json', 'Content-Type': 'application/json', 'User-Agent': 'inside-hacking-editorial-preparation'},
    method='POST',
)
with urllib.request.urlopen(request, timeout=60) as response:
    tree = json.load(response)['sha']
assert re.fullmatch(r'[0-9a-f]{40}', tree)
print('TEST_SUMMARY=' + json.dumps(test_summary))
print('GLOSSARY=' + json.dumps(glossary_result, ensure_ascii=False))
print('FINAL_DOCS=' + json.dumps(second, ensure_ascii=False))
print('EXTERNAL_SUMMARY=' + json.dumps(external_summary))
print('CANDIDATE_TREE=' + tree)
print('NO_BRANCH_OR_REF_UPDATED')
