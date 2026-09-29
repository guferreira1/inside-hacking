"""Prepare and verify an editorial snapshot; publish only an unattached Git tree."""
from pathlib import Path
import hashlib, json, os, platform, re, shutil, subprocess, unicodedata, unittest, urllib.request
TEMP={'.editorial_glossary13.psv','.editorial_glossary14.psv','.editorial_prepare14.py','.github/workflows/prepare-chapter14.yml'}
RUN=f'https://github.com/{os.environ["GITHUB_REPOSITORY"]}/actions/runs/{os.environ["GITHUB_RUN_ID"]}'
AUDIT='editorial/audits/2026-09-29-capitulos-12-14.md'
def read(p):return Path(p).read_text(encoding='utf-8')
def write(p,s):
    p=Path(p);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(s.rstrip()+'\n',encoding='utf-8')
def run(*a):return subprocess.run(a,text=True,encoding='utf-8',capture_output=True,check=True).stdout
def norm(s):return ''.join(c for c in unicodedata.normalize('NFKD',s) if not unicodedata.combining(c)).casefold()

manifest=json.loads(read('editorial/updates/capitulo-13-source-checksums.json'))
for p,d in manifest.items():
    if hashlib.sha256(read(p).rstrip().encode()).hexdigest()!=d:raise RuntimeError('Approved manuscript differs: '+p)
print('CH13_APPROVED_SOURCE_MATCH',len(manifest))
for n in (13,14):
    mapping={p.name.split('-')[0]:p.name for p in Path(f'book/modulo-3/capitulo-{n}').glob(f'{n}.*.md')}
    data=[]
    for line in read(f'.editorial_glossary{n}.psv').splitlines():
        if not line.strip():continue
        term,definition,section,source=line.split('|')
        data.append(dict(term=term,definition=definition,section=section,file=mapping[section],source=source))
    write(f'editorial/updates/capitulo-{n}-glossario.json',json.dumps(data,ensure_ascii=False,indent=2))
refs=json.loads(read('editorial/updates/capitulo-14-fontes.json'))
assert [x['id'] for x in refs]==[f'S{i}' for i in range(1,50)]
parts=['# Capítulo 14 — Referências e limites de verificação\n\n[Abertura](README.md) · [Respostas comentadas](solucoes.md)\n\n**Consulta:** 29/09/2026. **Versão editorial:** DRAFT 0.1.\n\nA pesquisa usa documentação primária do GNU, do projeto Linux man-pages, da Microsoft e do Python. O texto é autoral: os links fundamentam e delimitam os mecanismos, não substituem sua explicação.\n\nA documentação PowerShell consultada está identificada como 7.5; detalhes sobre mudanças em 7.3 e 7.4 foram delimitados. Os exemplos não alegam compatibilidade universal com Windows PowerShell 5.1, cmd.exe ou qualquer interpretador chamado sh. A versão da documentação e a versão realmente executada são informações distintas.\n\nParte das páginas GNU apresentou demora no acesso direto. Nesses casos, foi consultado o conteúdo oficial indexado nas páginas indicadas. Isso não equivale a uma auditoria HTTP independente de disponibilidade de todas as referências.\n\nA reprodução usa strings, argumentos, objetos sintéticos e arquivos temporários próprios. Não houve teste contra sistemas de terceiros nem alterações de permissões, contas, serviços ou execution policies. Ambiente, resultados e testes não executados ficam no [registro editorial](../../../editorial/reviews/capitulo-14.md).\n']
for x in refs:
    parts.append(f'<a id="{x["id"].lower()}"></a>\n\n## {x["id"]} — {x["title"]}\n\n**{x["author"]}.** [{x["title"]}]({x["url"]}).\n\n**Recorte:** {x["use"]}\n')
    for i,url in enumerate(x.get('related_urls',[]),1):parts.append(f'Complemento documental: [página relacionada {i}]({url}).\n')
write('book/modulo-3/capitulo-14/referencias.md','\n'.join(parts))
p='book/modulo-3/capitulo-14/14.6-automacao-e-fronteiras-de-confianca.md'
write(p,read(p).replace('Nos dois casos existe um argumento, mas seu papel mudou.','Nos dois casos o conteúdo chega como um argumento, mas seu papel mudou.'))

for n in (12,13):
    p=f'book/modulo-3/capitulo-{n}/README.md';s=read(p)
    s=re.sub(r'^> \*\*Status:\*\*.*$',f'> **Status:** VALIDATED — versão editorial 1.0; leitura aprovada e ciclo interno concluído em 29/09/2026. Fontes e limites no [registro editorial](../../../editorial/reviews/capitulo-{n}.md). Revisão técnica independente pendente.',s,flags=re.M)
    s=s.replace(f'[← Capítulo {n-1}](../capitulo-{n-1}/README.md)',f'[← Capítulo {n-1}](../capitulo-{n-1}/README.md) · [Capítulo {n+1} →](../capitulo-{n+1}/README.md)',1);write(p,s)
    p=f'book/modulo-3/capitulo-{n}/referencias.md';s=read(p).replace('**Versão:** DRAFT 0.1.','**Versão editorial:** VALIDATED 1.0 — fechamento interno em 29/09/2026; revisão independente pendente.');write(p,s)
    p=f'editorial/reviews/capitulo-{n}.md';s=read(p)
    s += '\n\n## Aprovação e integração de 29/09/2026\n\nA leitura foi aprovada antes do avanço. O ciclo interno da versão editorial 1.0 está concluído, com os limites de fontes e reprodução preservados. A integração recupera a entrega anterior sem reorganizar capítulos. A [auditoria desta entrega](../audits/2026-09-29-capitulos-12-14.md) registra os testes e a navegação efetivamente executados. Revisão independente permanece pendente.\n'
    s=s.replace('**Estado:** leitura aprovada; integração e checagem global nesta entrega do capítulo 14.','**Estado:** VALIDATED — versão editorial 1.0; revisão interna concluída. Integração e checagem global nesta entrega do capítulo 14.')
    if n==12:s=s.replace('**Estado:** DRAFT 0.1.','**Estado atual:** VALIDATED — versão editorial 1.0.',1)
    write(p,s)
    last=sorted(Path(f'book/modulo-3/capitulo-{n}').glob(f'{n}.*.md'))[-1]
    write(last,read(last)+f'\n\n[Continuar no Capítulo {n+1} →](../capitulo-{n+1}/README.md)\n')

titles={12:'Linux por dentro',13:'Windows por dentro',14:'Terminal, shells e automação'}
states={12:'Revisão interna concluída — v1.0',13:'Revisão interna concluída — v1.0',14:'Rascunho para leitura — v0.1'}
for p,prefix,root in [('README.md','book/modulo-3/',True),('book/README.md','modulo-3/',False)]:
    out=[];found=False
    for line in read(p).splitlines():
        if line.startswith('|') and f'{prefix}capitulo-12/README.md' in line:
            found=True;out.append(line.replace('Rascunho para leitura — v0.1',states[12]))
            for n in (13,14):
                if root:
                    desc='Organização, caminhos, executáveis, tokens, Registro e serviços.' if n==13 else 'Argumentos, aspas, fluxos, pipelines, status e automação em Bash e PowerShell.'
                    out.append(f'| [{n} · {titles[n]}]({prefix}capitulo-{n}/README.md) | {desc} | {states[n]} |')
                else:out.append(f'| {n} | [{titles[n]}]({prefix}capitulo-{n}/README.md) | {states[n]} |')
        else:out.append(line)
    if not found:raise RuntimeError('No chapter12 table row in '+p)
    s='\n'.join(out).replace('Os capítulos 1 a 12 estão disponíveis. No Módulo III, o capítulo 11 concluiu seu ciclo interno e o capítulo 12 está em primeira entrega de leitura.','Os capítulos 1 a 14 estão disponíveis. No Módulo III, os capítulos 11 a 13 concluíram seus ciclos internos, e o capítulo 14 está em primeira entrega de leitura.')
    write(p,s)
p='book/modulo-3/README.md';s=read(p)
for n in (12,13,14):s=re.sub(rf'^\| {n} \|.*$',f'| {n} | [{titles[n]}](capitulo-{n}/README.md) | {states[n]} |',s,flags=re.M)
s=s.replace('Os capítulos 11 e 12 estão disponíveis neste módulo. O 11 tem revisão interna concluída; o 12 está em primeira leitura.','Os capítulos 11 a 14 estão disponíveis neste módulo. Os capítulos 11 a 13 têm revisão interna concluída; o 14 está em primeira leitura.')
s=s.replace('**[Continuar no Capítulo 12 →](capitulo-12/README.md)**','**[Continuar no Capítulo 14 →](capitulo-14/README.md)**');write(p,s)
p='book/README.md';s=read(p);sections=[]
for n in (13,14):
    sections.append(f'### Dentro do Capítulo {n}\n')
    for f in sorted(Path(f'book/modulo-3/capitulo-{n}').glob(f'{n}.*.md')):
        title=read(f).splitlines()[0].removeprefix('# ').replace(' — ',' · ',1)
        sections.append(f'- [{title}](modulo-3/capitulo-{n}/{f.name})')
    if n==14:sections.append('- [Exemplos opcionais Bash e PowerShell](modulo-3/capitulo-14/exemplos/README.md).')
    sections.append(f'- [Respostas comentadas](modulo-3/capitulo-{n}/solucoes.md) e [referências](modulo-3/capitulo-{n}/referencias.md).\n')
assert '\n## Como navegar' in s
s=s.replace('\n## Como navegar','\n'+'\n'.join(sections)+'\n## Como navegar')
s=re.sub(r'^\| (\[III .*?\]) \|[^\n]+$',r'| \1 | Capítulos 11 a 17 | Capítulos 11–13 com revisão interna concluída; 14 em primeira leitura |',s,flags=re.M);write(p,s)

p='book/glossario.md';old=read(p);head,rest=old.split('\n## A\n',1);body,foot=rest.split('\n---\n',1);body='\n## A\n'+body
entries={}
for m in re.finditer(r'^### (.+)\n\n(.*?)(?=^### |^## [A-Z]\s*$|\Z)',body,flags=re.M|re.S):
    name,text=m.group(1).strip(),m.group(2).strip();key=norm(name)
    if key in entries:raise RuntimeError('Duplicate original glossary entry')
    entries[key]=[name,text]
if len(entries)!=401:raise RuntimeError(f'Unexpected base glossary count {len(entries)}')
original={k:v.copy() for k,v in entries.items()};added=[];extended=[]
for n in (13,14):
    for x in json.loads(read(f'editorial/updates/capitulo-{n}-glossario.json')):
        f=Path(f'book/modulo-3/capitulo-{n}')/x['file']
        if not f.exists():raise RuntimeError('Missing glossary occurrence '+str(f))
        link=f'[Conceito: {x["section"]}](modulo-3/capitulo-{n}/{x["file"]}).';text=x['definition']+' '+link;key=norm(x['term'])
        if key in entries:
            if link not in entries[key][1]:entries[key][1]+=f'\n\nNo contexto do capítulo {n}: '+text;extended.append(x['term'])
        else:entries[key]=[x['term'],text];added.append(x['term'])
letters=sorted({norm(v[0])[0].upper() for v in entries.values()})
head=re.sub(r'\*\*Consulta:\*\*.*','**Consulta:** '+' · '.join(f'[{a}](#{a.lower()})' for a in letters)+'.',head);chunks=[head.rstrip()]
for letter in letters:
    chunks.append(f'## {letter}')
    for key,(name,text) in sorted(entries.items()):
        if norm(name)[0].upper()==letter:chunks.append(f'### {name}\n\n{text}')
new='\n\n'.join(chunks)+'\n\n---\n'+foot
for k,(name,text) in original.items():
    if text not in new:raise RuntimeError('Definition lost: '+name)
write(p,new);print('GLOSSARY',json.dumps({'before':401,'after':len(entries),'added':added,'extended':sorted(set(extended))},ensure_ascii=False))

p='book/bibliografia.md';s=read(p)
s=s.replace('O capítulo está em DRAFT 0.1, conforme seu [registro editorial](../editorial/reviews/capitulo-12.md).','O capítulo tem leitura aprovada e revisão interna 1.0 concluída, conforme seu [registro editorial](../editorial/reviews/capitulo-12.md).')
s=s.replace('Revisão técnica independente e primeira leitura permanecem pendentes.','Revisão técnica independente permanece pendente.')
new='''## Capítulo 13 — Windows por dentro

As [44 referências do capítulo](modulo-3/capitulo-13/referencias.md) usam documentação primária da Microsoft para arquitetura, objetos, caminhos, PE/DLL, contas e tokens, Registro, serviços e eventos. A narrativa é fictícia; não houve reprodução de kernel, UAC, Registro ou SCM. Leitura aprovada e ciclo interno da versão 1.0 concluído, com [limites registrados](../editorial/reviews/capitulo-13.md).

## Capítulo 14 — Terminal, shells e automação

As [49 referências numeradas](modulo-3/capitulo-14/referencias.md) usam documentação GNU, Linux man-pages, Microsoft e Python. [Quatro scripts próprios](modulo-3/capitulo-14/exemplos/README.md) e os testes associados examinam argumentos, expansão, fluxos, status, escopos e validação. [O registro editorial](../editorial/reviews/capitulo-14.md) separa documentação consultada, execuções reais e limitações de plataforma. Primeira entrega DRAFT 0.1.

'''
assert '## Política de referências' in s;s=s.replace('## Política de referências',new+'## Política de referências');write(p,s)
p='editorial/coverage-matrix.md';s=read(p).replace('atualização em 28/09/2026','atualização em 29/09/2026').replace('Fundamentos, DRAFT; [fontes S1–S19]','Fundamentos, revisão interna 1.0; [fontes S1–S19]');rows=[];index=11
for n in (13,14):
    for f in sorted(Path(f'book/modulo-3/capitulo-{n}').glob(f'{n}.*.md')):
        title=read(f).splitlines()[0].removeprefix('# ')
        applied='Narrativa fictícia, perguntas e soluções; sem laboratório Windows.' if n==13 else 'Exemplos pequenos, dados sintéticos, scripts e testes delimitados; separação entre dados, código e autorização.'
        level='Revisão interna 1.0; revisão independente pendente.' if n==13 else 'Fundamentos desenvolvidos, DRAFT 0.1; não é um catálogo completo dos shells ou automação de exploração.'
        rows.append(f'| M03-{index:02d} | [{title}](../{f.as_posix()}) | {applied} | {level} |');index+=1
assert '\n## Cobertura ainda planejada' in s
s=s.replace('\n## Cobertura ainda planejada','\n'+'\n'.join(rows)+'\n\n## Cobertura ainda planejada');write(p,s)
p='editorial/publication-status.md';s=read(p)
s=re.sub(r'^\| 12 \|.*$','| 12 | VALIDATED — versão editorial 1.0; leitura aprovada e ciclo interno concluído em 29/09/2026 | Manuscrito recuperado sem reorganização. Exemplo de descritor próprio e quatro testes preservados; revisão independente pendente. [Registro](reviews/capitulo-12.md). |\n| 13 | VALIDATED — versão editorial 1.0; leitura aprovada e ciclo interno concluído em 29/09/2026 | Seis seções, doze respostas e 44 referências Microsoft preservadas da entrega local. Sem laboratório Windows de kernel, Registro ou UAC; revisão independente pendente. [Registro](reviews/capitulo-13.md). |\n| 14 | DRAFT 0.1 — primeira entrega de leitura | Seis seções, doze respostas, 49 referências, quatro scripts e testes Bash/PowerShell com ambientes delimitados. Leitura e revisão independente pendentes. [Registro](reviews/capitulo-14.md). |',s,flags=re.M)
s=s.replace('As aprovações dos capítulos 4 a 11','As aprovações dos capítulos 4 a 13')
s=re.sub(r'^O \[Módulo III\].*$','O [Módulo III](../book/modulo-3/README.md) possui os capítulos 11 a 13 com ciclos internos concluídos e o [Capítulo 14](../book/modulo-3/capitulo-14/README.md) em primeira entrega. Os capítulos 15 a 17 continuam planejados, na ordem original. O módulo permanece em produção; a aprovação editorial não atribui domínio prático ao leitor.',s,flags=re.M)
s=s.replace('1. Receber a leitura do Capítulo 12, com atenção às diferenças entre kernel, instalação, visão de montagens e interfaces de estado.','1. Receber a leitura do Capítulo 14, acompanhando argumentos efetivos, fluxos, status e fronteiras de interpretação.')
s=s.replace('Depois da leitura do capítulo 12, prosseguir para o Capítulo 13 — Windows por dentro','Depois da leitura do capítulo 14, prosseguir para o Capítulo 15 — Usuários, grupos, permissões e privilégios');write(p,s)
p='editorial/README.md';write(p,read(p)+'\n\nContinuidade: [revisão do capítulo 13](reviews/capitulo-13.md), [entrega do capítulo 14](reviews/capitulo-14.md) e [auditoria de integração dos capítulos 12–14](audits/2026-09-29-capitulos-12-14.md).')

suite=unittest.defaultTestLoader.discover('scripts/tests');r=unittest.TextTestRunner(verbosity=2).run(suite)
if not r.wasSuccessful():raise RuntimeError('Regression failed')
summary={'total':r.testsRun,'passed':r.testsRun-len(r.skipped),'skipped':len(r.skipped)}
versions={'python':platform.python_version(),'os':platform.platform(),'bash':run('bash','--version').splitlines()[0],'windows_powershell':os.environ['WINDOWS_POWERSHELL'],'windows_os':os.environ['WINDOWS_OS']}
if shutil.which('pwsh'):versions['linux_powershell']=run('pwsh','-NoProfile','-Command','$PSVersionTable.PSVersion.ToString()').strip()
questions=read('book/modulo-3/capitulo-14/14.6-automacao-e-fronteiras-de-confianca.md').split('## Para conferir a compreensão\n',1)[1]
assert len(re.findall(r'^\d+\. ',questions,re.M))==12
assert len(re.findall(r'^## \d+ — ',read('book/modulo-3/capitulo-14/solucoes.md'),re.M))==12
def docs():
    d=json.loads(run('python3','scripts/check_docs.py','--inventory'))
    if d['internal_errors']:raise RuntimeError(d['internal_errors'])
    return {k:d[k] for k in ('markdown_files','internal_links','internal_errors','glossary_entries')}
write(AUDIT,'# Auditoria de integração — Capítulos 12 a 14\n\nEm preparação nesta execução; só é publicado se todas as verificações passarem.')
d=docs()
report=f'''# Auditoria de integração — Capítulos 12 a 14

**Data:** 29/09/2026. **Tipo:** revisão interna e verificação técnica delimitada.

[Estado editorial](../publication-status.md) · [Módulo III](../../book/modulo-3/README.md)

## Origem e continuidade

A main de partida era `9ace0862c456f01b3d8b03e8857349448f086215`. A árvore preparada do capítulo 12 foi recuperada no commit `0da3c29cc4d4a9d143c96dce8c7ccdc459826cd9`. Os nove arquivos do manuscrito Windows foram comparados por SHA-256 com o pacote aprovado: todos coincidiram antes da atualização de estados e navegação.

O capítulo 13 não foi recriado com outro conteúdo. A redação nova corresponde ao capítulo 14. A ordem original foi mantida. A aprovação dos capítulos 12 e 13 é editorial, não domínio prático nem revisão independente.

## Reprodução

A [execução de preparação]({RUN}) executou a suíte e a verificação documental. No runner Linux: **{summary['total']} testes descobertos; {summary['passed']} aprovados; {summary['skipped']} skips; zero falhas**. A etapa Windows executou os **nove testes PowerShell** do capítulo 14, sem skips ou falhas, como pré-condição desta etapa.

Ambientes registrados:

```json
{json.dumps(versions,ensure_ascii=False,indent=2)}
```

A execução local anterior tinha 17 testes Bash aprovados e nove PowerShell não executados por ausência de pwsh. Isso não foi transformado retroativamente em execução Windows. A reprodução em Windows verifica scripts e cmdlets do capítulo 14; não comprova os mecanismos de UAC, kernel, Registro ou serviços apresentados documentalmente no capítulo 13.

## Documentação

Foram sincronizados README principal, índice geral, índice do Módulo III, bibliografia, glossário, cobertura, estados e registros dos capítulos. As {len(original)} definições originais do glossário e suas referências foram preservadas; o conjunto passou a {len(entries)} verbetes. Novas ocorrências e distinções de plataforma complementam verbetes existentes, em vez de apagar seus sentidos anteriores.

A primeira travessia interna desta preparação registrou {d['markdown_files']} Markdown, {d['internal_links']} destinos e zero erros. Uma segunda travessia é realizada depois de gravar este relatório. A checagem de caminhos e âncoras não é auditoria independente de todas as afirmações técnicas ou da disponibilidade de todas as URLs externas.

## Limites e estado

Os exemplos usam dados sintéticos e arquivos temporários próprios. Não houve acesso a alvos, credenciais, serviços da Aurora ou alterações de políticas. O capítulo 1 conserva sua pendência; o Módulo II conserva o fechamento interno; o III permanece em produção. Não houve publicação no LinkedIn nem geração de PDF.

Este relatório registra a preparação verificada. A confirmação do commit na main e da checagem pós-integração é uma etapa distinta, consultável no histórico de commits e Actions.
'''
write(AUDIT,report)
p='editorial/reviews/capitulo-14.md';write(p,read(p)+f'\n\n## Verificação em runners\n\nA [execução]({RUN}) concluiu os nove testes PowerShell em Windows sem skips ou falhas. No runner Linux, a suíte completa encontrou {summary["total"]} testes, com {summary["passed"]} aprovados e {summary["skipped"]} skips. Ambientes e limites constam na [auditoria](../audits/2026-09-29-capitulos-12-14.md). A segunda checagem de links é obrigatória após estas atualizações.\n')
changed=run('git','diff','--name-only').splitlines()+run('git','ls-files','--others','--exclude-standard').splitlines()
for p in changed:
    if p.endswith('.md') and Path(p).is_file():write(p,'\n'.join(l.rstrip() for l in read(p).splitlines()))
final_docs=docs();run('git','diff','--check')
write('editorial/updates/capitulo-14-checks.json',json.dumps({'run':RUN,'tests_linux':summary,'windows_powershell_tests':{'total':9,'passed':9,'skipped':0},'versions':versions,'documentation':final_docs,'new_glossary_entries':added,'extended_glossary_entries':sorted(set(extended))},ensure_ascii=False,indent=2))
print('TEST_SUMMARY',json.dumps(summary));print('FINAL_DOCS',json.dumps(final_docs));print('VERSIONS',json.dumps(versions))
changed=set(run('git','diff','--name-only').splitlines()+run('git','ls-files','--others','--exclude-standard').splitlines())-TEMP
items=[]
for p in sorted(changed):
    if '__pycache__' in p or p.endswith('.pyc'):continue
    if not p.startswith(('README.md','book/','editorial/','scripts/tests/','.github/workflows/')):raise RuntimeError('Unexpected modified path '+p)
    items.append({'path':p,'mode':'100644','type':'blob','content':read(p)})
tracked=set(run('git','ls-files').splitlines())
for p in sorted(TEMP & tracked):items.append({'path':p,'mode':'100644','type':'blob','sha':None})
base=run('git','rev-parse','HEAD^{tree}').strip()
req=urllib.request.Request(f'https://api.github.com/repos/{os.environ["GITHUB_REPOSITORY"]}/git/trees',data=json.dumps({'base_tree':base,'tree':items}).encode(),method='POST',headers={'Authorization':'Bearer '+os.environ['GH_TOKEN'],'Accept':'application/vnd.github+json','Content-Type':'application/json','X-GitHub-Api-Version':'2022-11-28'})
with urllib.request.urlopen(req,timeout=60) as response:tree=json.load(response)
if not re.fullmatch('[0-9a-f]{40}',tree['sha']):raise RuntimeError('Invalid tree')
print('CANDIDATE_TREE='+tree['sha']);print('NO_BRANCH_OR_REF_UPDATED')
