"""One-use preparation: no branch/ref updates; creates a verified Git tree only."""
from pathlib import Path
import collections
import concurrent.futures
import importlib.util
import json
import os
import platform
import re
import subprocess
import sys
import unicodedata
import unittest
import urllib.error
import urllib.request

ROOT = Path.cwd()
REPO = 'guferreira1/inside-hacking'
BASE = '089792c1facff1b625d609c50e319dab44ffb2bd'
TITLE = 'Usuários, grupos, permissões e privilégios'
CH = 'book/modulo-3/capitulo-15'
AUDIT = 'editorial/audits/2026-09-29-capitulo-15.md'
RUN = 'https://github.com/' + REPO + '/actions/runs/' + os.environ['GITHUB_RUN_ID']
changed = set()


def read(path):
    return Path(path).read_text(encoding='utf-8')


def write(path, text):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text.rstrip() + '\n', encoding='utf-8')
    changed.add(path)


def replace(path, old, new, count=1):
    text = read(path)
    if text.count(old) != count:
        raise RuntimeError(f'Replacement mismatch {path}: {old[:100]!r}; found {text.count(old)}')
    write(path, text.replace(old, new))


def validate_row(path):
    lines = read(path).splitlines()
    hits = [i for i, line in enumerate(lines)
            if 'capitulo-14/README.md' in line and line.startswith('|')
            and 'Rascunho para leitura — v0.1' in line]
    if len(hits) != 1:
        raise RuntimeError(f'Expected one chapter 14 reader row in {path}: {hits}')
    lines[hits[0]] = lines[hits[0]].replace('Rascunho para leitura — v0.1',
                                         'Revisão interna concluída — v1.0')
    write(path, '\n'.join(lines))
    return lines, hits[0]


# Reading approval and navigation, preserving the chapter 14 manuscript.
replace('book/modulo-3/capitulo-14/README.md',
        '> **Status:** DRAFT 0.1 — primeira entrega de leitura.',
        '> **Status:** VALIDATED — versão editorial 1.0; leitura aprovada e ciclo interno concluído em 29/09/2026.')
replace('book/modulo-3/capitulo-14/README.md',
        '[← Capítulo 13](../capitulo-13/README.md) ·',
        '[← Capítulo 13](../capitulo-13/README.md) · [Capítulo 15 →](../capitulo-15/README.md) ·')
replace('book/modulo-3/capitulo-14/referencias.md',
        '**Versão editorial:** DRAFT 0.1.',
        '**Versão editorial:** VALIDATED 1.0 — fechamento interno em 29/09/2026; revisão independente pendente.')
replace('book/modulo-3/capitulo-14/14.6-automacao-e-fronteiras-de-confianca.md',
        '**15 — Usuários, grupos, permissões e privilégios**',
        '**[15 — Usuários, grupos, permissões e privilégios](../capitulo-15/README.md)**')

path = 'editorial/reviews/capitulo-14.md'
replace(path, '# Primeira entrega editorial — Capítulo 14', '# Revisão editorial — Capítulo 14')
replace(path, '**Estado:** DRAFT 0.1.', '**Estado atual:** VALIDATED — versão editorial 1.0.')
replace(path, 'O capítulo 14 permanece em primeira leitura; revisão técnica independente pendente.',
        'Na primeira entrega, o capítulo 14 ficou em primeira leitura. O estado atual é registrado no fechamento abaixo; revisão técnica independente permanece pendente.')
write(path, read(path) + '\n\n## Fechamento interno de 29/09/2026\n\n'
      'O pedido do mantenedor de seguir ao próximo capítulo registra sua aprovação de leitura. '
      'A revisão de continuidade preservou as seis seções, exemplos e respostas, atualizando apenas '
      'estado e navegação. Os testes existentes participam novamente da regressão da entrega do capítulo 15; '
      'seus resultados estão na [auditoria](../audits/2026-09-29-capitulo-15.md). '
      'O ciclo interno da versão 1.0 está concluído. Não foram presumidos tempo de estudo, '
      'execução pelo leitor ou revisão técnica independente.\n')

# Reader indexes.
lines, at = validate_row('README.md')
lines.insert(at + 1, '| [15 · ' + TITLE + '](' + CH + '/README.md) | Identidades, permissões por operação, ACLs, privilégios e menor privilégio em Linux e Windows. | Rascunho para leitura — v0.1 |')
write('README.md', '\n'.join(lines))
replace('README.md',
        'Os capítulos 1 a 14 estão disponíveis. No Módulo III, os capítulos 11 a 13 concluíram seus ciclos internos, e o capítulo 14 está em primeira entrega de leitura.',
        'Os capítulos 1 a 15 estão disponíveis. No Módulo III, os capítulos 11 a 14 concluíram seus ciclos internos, e o capítulo 15 está em primeira entrega de leitura.')

lines, at = validate_row('book/README.md')
lines.insert(at + 1, '| 15 | [' + TITLE + '](modulo-3/capitulo-15/README.md) | Rascunho para leitura — v0.1 |')
write('book/README.md', '\n'.join(lines))
replace('book/README.md', 'Capítulos 11 e 12 disponíveis; demais planejados',
        'Capítulos 11 a 15 disponíveis; 16 e 17 planejados')
sections = sorted(Path(CH).glob('15.*.md'), key=lambda p: int(p.name.split('.')[1].split('-')[0]))
assert len(sections) == 7
section_map = {p.name.split('-')[0]: p.name for p in sections}
section_titles = {key: read(CH + '/' + value).splitlines()[0].split(' — ', 1)[1]
                  for key, value in section_map.items()}
nav = '### Dentro do Capítulo 15\n\n'
for number, filename in section_map.items():
    nav += f'- [{number} · {section_titles[number]}](modulo-3/capitulo-15/{filename})\n'
nav += '- [Observações opcionais de permissões](modulo-3/capitulo-15/exemplos/README.md).\n'
nav += '- [Respostas comentadas](modulo-3/capitulo-15/solucoes.md) e [referências](modulo-3/capitulo-15/referencias.md).\n\n'
replace('book/README.md', '## Como navegar', nav + '## Como navegar')

validate_row('book/modulo-3/README.md')
replace('book/modulo-3/README.md', '| 15 | ' + TITLE + ' | Planejado |',
        '| 15 | [' + TITLE + '](capitulo-15/README.md) | Rascunho para leitura — v0.1 |')
replace('book/modulo-3/README.md',
        'Os capítulos 11 a 14 estão disponíveis neste módulo. Os capítulos 11 a 13 têm revisão interna concluída; o 14 está em primeira leitura.',
        'Os capítulos 11 a 15 estão disponíveis neste módulo. Os capítulos 11 a 14 têm revisão interna concluída; o 15 está em primeira leitura.')
replace('book/modulo-3/README.md', '[Continuar no Capítulo 14 →](capitulo-14/README.md)',
        '[Continuar no Capítulo 15 →](capitulo-15/README.md)')

# Publication state; no unrelated chapter or module promotion.
p = 'editorial/publication-status.md'
text = read(p)
old_row = next(line for line in text.splitlines() if line.startswith('| 14 |'))
new_row = '| 14 | VALIDATED — versão editorial 1.0; leitura aprovada e ciclo interno concluído em 29/09/2026 | Seis seções, doze respostas, 49 referências e quatro scripts preservados. Regressão reconferida; revisão independente pendente. [Registro](reviews/capitulo-14.md). |'
row15 = '| 15 | DRAFT 0.1 — primeira entrega de leitura | Sete seções, quatorze respostas, 47 referências e nove testes próprios delimitados. Observações Linux em arquivos próprios; controles Windows por documentação, sem execução. Leitura e revisão independente pendentes. [Registro](reviews/capitulo-15.md). |'
replace(p, old_row, new_row + '\n' + row15)
replace(p, 'As aprovações dos capítulos 4 a 13', 'As aprovações dos capítulos 4 a 14')
replace(p,
        'possui os capítulos 11 a 13 com ciclos internos concluídos e o [Capítulo 14](../book/modulo-3/capitulo-14/README.md) em primeira entrega. Os capítulos 15 a 17 continuam planejados, na ordem original.',
        'possui os capítulos 11 a 14 com ciclos internos concluídos e o [Capítulo 15](../book/modulo-3/capitulo-15/README.md) em primeira entrega. Os capítulos 16 e 17 continuam planejados, na ordem original.')
replace(p,
        'Receber a leitura do Capítulo 14, acompanhando argumentos efetivos, fluxos, status e fronteiras de interpretação.',
        'Receber a leitura do Capítulo 15, acompanhando identidade da execução, operação solicitada, política e limites da concessão.')
replace(p,
        'Depois da leitura do capítulo 14, prosseguir para o Capítulo 15 — Usuários, grupos, permissões e privilégios',
        'Depois da leitura do capítulo 15, prosseguir para o Capítulo 16 — Processos, serviços, logs e persistência de estado')

# Bibliography and coverage.
p = 'book/bibliografia.md'
replace(p, 'Primeira entrega DRAFT 0.1.',
        'Leitura aprovada e ciclo interno da versão editorial 1.0 concluído; revisão independente pendente.')
new_bib = ('## Capítulo 15 — ' + TITLE + '\n\n'
    'As [47 referências numeradas](modulo-3/capitulo-15/referencias.md) relacionam documentação '
    'Linux man-pages, Linux ACL, GNU, shadow-utils, util-linux, sudo, kernel, Microsoft, Python e OWASP. '
    'Sete seções desenvolvem identidades, operações, criação e ACLs, tokens e direitos Windows, '
    'delegação, camadas, revogação e investigação. Os modelos de acesso Linux e Windows são distinguidos.\n\n'
    'O [exemplo opcional](modulo-3/capitulo-15/exemplos/README.md) observa somente arquivos temporários '
    'do próprio usuário comum em Linux. Os nove testes separam três verificações de modelo/guarda '
    'e seis de operações reais e limpeza. Não houve administração de contas, ACLs ou privilégios, '
    'nem execução dos controles Windows. O [registro editorial](../editorial/reviews/capitulo-15.md) '
    'preserva ambientes, resultados e limites; o capítulo está em DRAFT 0.1.\n\n')
replace(p, '## Política de referências', new_bib + '## Política de referências')
p = 'editorial/coverage-matrix.md'
lines = read(p).splitlines()
ids = [(i, int(m.group(1))) for i, line in enumerate(lines)
       if (m := re.match(r'\| M03-(\d+) \|', line))]
assert ids
last = max(number for _, number in ids)
at = max(i for i, _ in ids) + 1
limits = [
    'UID/GID/NSS e SID/token; cadastro não atualiza todas as execuções. Sem criação de contas.',
    'rwx, classes, caminhos e unlink. Observações somente do proprietário de arquivos temporários.',
    'Criação, umask, setgid e ACL POSIX. Contas de bits não equivalem a testar ACLs reais.',
    'Direitos solicitados, ACEs, ordem e herança. Modelo didático e fontes Microsoft; sem AccessCheck executado.',
    'Capabilities, sudo, setuid, UAC e impersonação por documentação. Nenhuma autoridade elevada ou configurada.',
    'DAC, controles adicionais e revogação. Descritor Linux observado não generaliza recursos Windows/remotos.',
    'Consultas por documentação; quatro observações Linux e nove testes delimitados. Sem matriz de contas ou alvos externos.'
]
rows = []
for offset, (number, filename) in enumerate(section_map.items(), 1):
    rows.append(f'| M03-{last + offset:02d} | [{section_titles[number]}](../{CH}/{filename}) | {limits[offset - 1]} | Fundamentos desenvolvidos, DRAFT; [fontes](../{CH}/referencias.md) e [registro](reviews/capitulo-15.md). Revisão independente pendente. |')
lines[at:at] = rows
for i, line in enumerate(lines):
    if line.startswith('| M03-') and '/capitulo-14/' in line:
        lines[i] = line.replace('DRAFT', 'revisão interna 1.0')
write(p, '\n'.join(lines))

# Add the precise primary source for deny-only SID attributes.
p = CH + '/15.4-tokens-e-acls-no-windows.md'
replace(p, 'O mesmo nome de usuário em dois processos não garante tokens com a mesma capacidade efetiva. [S8](referencias.md#s8) [S21](referencias.md#s21)',
        'O mesmo nome de usuário em dois processos não garante tokens com a mesma capacidade efetiva. [S8](referencias.md#s8) [S21](referencias.md#s21) [S47](referencias.md#s47)')

# Glossary: preserve every existing definition and the reference footer.
p = 'book/glossario.md'
old = read(p)
marker = '\n---\n\nAs definições metodológicas'
assert old.count(marker) == 1
body, tail = old.split(marker, 1)
footer = marker + tail
letters = list(re.finditer(r'^## ([A-Z])\s*$', body, re.M))
assert letters
prefix = body[:letters[0].start()]
entries = {}
for i, match in enumerate(letters):
    block = body[match.end():letters[i + 1].start() if i + 1 < len(letters) else len(body)]
    for item in re.finditer(r'^### ([^\n]+)\n(.*?)(?=^### |\Z)', block, re.M | re.S):
        term = item.group(1).strip()
        key = term.casefold()
        if key in entries:
            raise RuntimeError('Duplicate glossary term: ' + term)
        entries[key] = (term, item.group(2).strip())
assert len(entries) == 510, len(entries)
before = dict(entries)
added, extended = [], []
upserts = json.loads(read('editorial/updates/capitulo-15-glossario.json'))
for item in upserts:
    term, section, definition = item['term'], item['section'], item['definition']
    filename = section_map[section]
    if term.casefold() not in read(CH + '/' + filename).casefold():
        raise RuntimeError('Glossary term without occurrence: ' + term)
    key = term.casefold()
    link = f'[Conceito: {section}](modulo-3/capitulo-15/{filename}).'
    if key in entries:
        old_term, old_definition = entries[key]
        entries[key] = (old_term, old_definition + '\n\n' + definition + ' ' + link)
        extended.append(old_term)
    else:
        entries[key] = (term, definition + ' ' + link)
        added.append(term)

def sort_key(term):
    return ''.join(c for c in unicodedata.normalize('NFKD', term.casefold()) if not unicodedata.combining(c))

buckets = collections.defaultdict(list)
for term, definition in entries.values():
    buckets[sort_key(term)[0].upper()].append((term, definition))
parts = [prefix.rstrip()]
for letter in sorted(buckets):
    parts.append('\n## ' + letter + '\n')
    for term, definition in sorted(buckets[letter], key=lambda item: sort_key(item[0])):
        parts.append('### ' + term + '\n\n' + definition + '\n')
new = '\n'.join(parts).rstrip() + '\n' + footer
for key, (term, definition) in before.items():
    assert entries[key][1].startswith(definition), term
assert new.endswith(footer)
write(p, new)
glossary_result = {'before': len(before), 'after': len(entries), 'added': added, 'extended': extended,
                   'preserved_previous_definitions': len(before)}

# Make current records point to the same audit before counting links.
p = 'editorial/README.md'
write(p, read(p) + '\n\nA [auditoria da entrega do capítulo 15](audits/2026-09-29-capitulo-15.md) '
      'registra continuidade, glossário, testes e limites de validação.\n')
p = 'editorial/reviews/capitulo-15.md'
write(p, read(p) + '\n\n## Verificação no runner\n\n'
      'Os resultados da regressão e da segunda passagem documental estão na '
      '[auditoria desta entrega](../audits/2026-09-29-capitulo-15.md), '
      'separados da execução local descrita acima.\n')

# The temporary workflow and this helper are not part of the final tree.
for path in ('.github/workflows/prepare-chapter15.yml', '.editorial_prepare15.py'):
    Path(path).unlink()
    changed.add(path)

# Run the full existing suite plus the nine new tests, requiring actual execution.
if sys.platform != 'linux' or os.geteuid() == 0:
    raise RuntimeError('This preparation requires an unprivileged Linux runner.')
suite = unittest.defaultTestLoader.discover('scripts/tests')
result = unittest.TextTestRunner(verbosity=2).run(suite)
checks = {'total': result.testsRun, 'failures': len(result.failures), 'errors': len(result.errors),
          'skipped': len(result.skipped), 'passed': result.testsRun - len(result.failures) - len(result.errors) - len(result.skipped)}
if not result.wasSuccessful() or result.skipped or result.testsRun != 99:
    raise RuntimeError('Incomplete regression: ' + json.dumps(checks))

# Probe public primary-source URLs once. An inaccessible URL is not called dead.
urls = sorted(set(re.findall(r'^https?://\S+$', read(CH + '/referencias.md'), re.M)))
def probe(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'inside-hacking-editorial-check/1.0'})
    try:
        with urllib.request.urlopen(req, timeout=18) as response:
            return {'url': url, 'status': response.status, 'final_url': response.geturl(), 'classification': 'accessible'}
    except urllib.error.HTTPError as exc:
        return {'url': url, 'status': exc.code, 'classification': 'missing' if exc.code in (404, 410) else 'inconclusive'}
    except Exception as exc:
        return {'url': url, 'status': None, 'classification': 'inconclusive', 'error': type(exc).__name__}
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
    external = list(pool.map(probe, urls))
external_counts = dict(collections.Counter(item['classification'] for item in external))

versions = {'python': platform.python_version(), 'os': platform.platform(), 'euid': os.geteuid(),
            'bash': subprocess.check_output(['bash', '--version'], text=True).splitlines()[0]}
try:
    versions['powershell'] = subprocess.check_output(['pwsh', '-NoLogo', '-NoProfile', '-Command', '$PSVersionTable.PSVersion.ToString()'], text=True, timeout=10).strip()
except (OSError, subprocess.SubprocessError):
    versions['powershell'] = 'not determined'

report = ('# Auditoria de entrega — Capítulo 15\n\n'
    '**Data:** 29/09/2026. **Base:** `' + BASE + '`. **Tipo:** revisão interna.\n\n'
    '[Estado editorial](../publication-status.md) · [Capítulo](../../' + CH + '/README.md) · '
    '[Execução de preparação](' + RUN + ')\n\n'
    '## Continuidade\n\nA aprovação da leitura do capítulo 14 foi registrada pelo pedido de avançar. '
    'Seu conteúdo, exemplos e limitações foram preservados, com atualização de estado e navegação. '
    'O capítulo 15 tem sete seções, quatorze respostas e 47 referências. A sequência original '
    'permanece inalterada; o próximo é o capítulo 16. Nenhum outro capítulo foi promovido automaticamente.\n\n'
    '## Reprodução\n\nA regressão no runner encontrou **' + str(checks['total']) + ' testes**, '
    'com **' + str(checks['passed']) + ' aprovados e zero skips, erros ou falhas**. '
    'São 90 testes anteriores e nove novos. Os testes próprios separam modelos/guarda de ambiente '
    'de operações reais sobre arquivos temporários do próprio usuário em Linux. '
    'O programa recusa root ou capabilities efetivas; não houve administração de contas.\n\n'
    '```json\n' + json.dumps(versions, ensure_ascii=False, indent=2) + '\n```\n\n'
    'A execução local anterior e sua redução de privilégios apenas no subprocesso permanecem '
    'identificadas no registro do capítulo. A regressão de PowerShell existente não comprova '
    'ACLs Windows, UAC, impersonação ou outros mecanismos apresentados por documentação neste capítulo.\n\n'
    '## Documentação e glossário\n\nREADMEs, índices, bibliografia, cobertura e estados foram sincronizados. '
    'Também foi corrigida a tabela superior do índice geral, que ainda listava apenas os capítulos 11 e 12 '
    'como disponíveis no Módulo III. O glossário passou de **510 para ' + str(len(entries)) + ' verbetes**, '
    'com ' + str(len(added)) + ' entradas novas e ' + str(len(extended)) + ' complementadas. '
    'As 510 definições anteriores e o rodapé de referências foram preservados. Cada termo novo possui ocorrência no capítulo.\n\n'
    'CHECK_COUNTS\n\n'
    '## Referências externas\n\nForam consultadas por HTTP ' + str(len(urls)) + ' URLs únicas da lista de referências. '
    'Resultado: `' + json.dumps(external_counts, ensure_ascii=False, sort_keys=True) + '`. '
    'Uma resposta inconclusiva não é declarada link morto. Os detalhes estão no '
    '[registro de verificações](../updates/capitulo-15-checks.json). A disponibilidade HTTP '
    'não substitui revisão das afirmações sustentadas por cada fonte.\n\n'
    '## Limites\n\nRevisão assistida por IA não é revisão técnica independente. O capítulo 15 permanece '
    'DRAFT 0.1 para leitura; o Módulo III continua em produção. A pendência do capítulo 1 e o fechamento '
    'interno do Módulo II foram preservados. Não houve alvo externo de teste, publicação no LinkedIn '
    'ou geração de edição PDF. Este relatório registra preparação; o commit e a verificação na main '
    'são confirmados separadamente antes da entrega.\n')
write(AUDIT, report)

def docs_check():
    out = subprocess.check_output([sys.executable, 'scripts/check_docs.py'], text=True)
    value = json.loads(out)
    if value['internal_errors']:
        raise RuntimeError('Invalid internal links: ' + out)
    return value

first = docs_check()
counts = ('A primeira e a segunda passagens internas conferiram **' + str(first['markdown_files']) +
    ' Markdown** e **' + str(first['internal_links']) + ' destinos internos**, com **zero erros de caminho ou âncora**. '
    'A checagem automatizada não substitui revisão factual independente.')
replace(AUDIT, 'CHECK_COUNTS', counts)
second = docs_check()
assert (first['markdown_files'], first['internal_links']) == (second['markdown_files'], second['internal_links'])
assert second['glossary_entries'] == len(entries)
record = {'base': BASE, 'preparation_run': RUN, 'tests': checks, 'versions': versions,
          'glossary': glossary_result, 'documentation': second, 'external_urls': external,
          'independent_review': False, 'windows_access_control_executed': False}
write('editorial/updates/capitulo-15-checks.json', json.dumps(record, ensure_ascii=False, indent=2))

# Scope assertion: only named chapter/index/editorial paths were touched.
allowed = {'README.md', 'book/README.md', 'book/bibliografia.md', 'book/glossario.md',
           'book/modulo-3/README.md', 'editorial/README.md', 'editorial/coverage-matrix.md',
           'editorial/publication-status.md', 'editorial/reviews/capitulo-14.md',
           'editorial/reviews/capitulo-15.md', AUDIT, 'editorial/updates/capitulo-15-checks.json',
           '.editorial_prepare15.py', '.github/workflows/prepare-chapter15.yml'}
for path in changed:
    if path not in allowed and not path.startswith('book/modulo-3/capitulo-14/') and not path.startswith(CH + '/'):
        raise RuntimeError('Unexpected mutation: ' + path)

base_tree = subprocess.check_output(['git', 'rev-parse', 'HEAD^{tree}'], text=True).strip()
elements = []
for path in sorted(changed):
    if Path(path).exists():
        elements.append({'path': path, 'mode': '100644', 'type': 'blob', 'content': read(path)})
    else:
        elements.append({'path': path, 'mode': '100644', 'type': 'blob', 'sha': None})
payload = json.dumps({'base_tree': base_tree, 'tree': elements}, ensure_ascii=False).encode('utf-8')
req = urllib.request.Request('https://api.github.com/repos/' + REPO + '/git/trees', data=payload,
    headers={'Authorization': 'Bearer ' + os.environ['GH_TOKEN'], 'Accept': 'application/vnd.github+json',
             'Content-Type': 'application/json', 'X-GitHub-Api-Version': '2022-11-28'}, method='POST')
with urllib.request.urlopen(req, timeout=60) as response:
    tree = json.load(response)['sha']
assert re.fullmatch(r'[0-9a-f]{40}', tree)
print('GLOSSARY=' + json.dumps(glossary_result, ensure_ascii=False))
print('TEST_SUMMARY=' + json.dumps(checks))
print('FINAL_DOCS=' + json.dumps(second, ensure_ascii=False))
print('EXTERNAL_SUMMARY=' + json.dumps(external_counts))
print('CANDIDATE_TREE=' + tree)
print('NO_BRANCH_OR_REF_UPDATED')
