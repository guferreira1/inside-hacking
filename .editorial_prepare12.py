"""Auxiliar temporário: edita apenas documentação declarada e publica uma árvore, nunca refs."""
from pathlib import Path
import json
import os
import re
import subprocess
import sys
import unicodedata
import urllib.request

BASE = "9ace0862c456f01b3d8b03e8857349448f086215"
REPO = "guferreira1/inside-hacking"
TEMP = [".editorial_prepare12.py", ".github/workflows/chapter12-prep.yml"]
ALLOWED = {
    "README.md", "book/README.md", "book/bibliografia.md", "book/glossario.md",
    "book/modulo-3/README.md", "book/modulo-3/capitulo-11/README.md",
    "book/modulo-3/capitulo-11/referencias.md",
    "book/modulo-3/capitulo-11/11.5-inicializacao-servicos-e-investigacao.md",
    "editorial/reviews/capitulo-11.md", "editorial/reviews/capitulo-12.md",
    "editorial/publication-status.md", "editorial/coverage-matrix.md",
}

def run(*args):
    return subprocess.check_output(args, text=True)

def replace(path, before, after):
    p = Path(path)
    text = p.read_text()
    if text.count(before) != 1:
        raise RuntimeError(f"Replacement count {text.count(before)} in {path}: {before[:110]}")
    p.write_text(text.replace(before, after), encoding="utf-8")

def edit():
    if subprocess.run(["git", "merge-base", "--is-ancestor", BASE, "HEAD"], check=False).returncode != 0:
        raise RuntimeError("Preparation must retain declared baseline")
    replace("README.md", "| [11 · O papel de um sistema operacional](book/modulo-3/capitulo-11/README.md) | Abstrações, interfaces do kernel, recursos, identidades e ciclo de vida de serviços. | Rascunho para leitura — v0.1 |", "| [11 · O papel de um sistema operacional](book/modulo-3/capitulo-11/README.md) | Abstrações, interfaces do kernel, recursos, identidades e ciclo de vida de serviços. | Revisão interna concluída — v1.0 |\n| [12 · Linux por dentro](book/modulo-3/capitulo-12/README.md) | Distribuição, diretórios, montagens, interfaces de estado, dispositivos e pacotes. | Rascunho para leitura — v0.1 |")
    replace("README.md", "Os capítulos 1 a 11 estão disponíveis. O Módulo III começa com o capítulo 11 em primeira entrega de leitura.", "Os capítulos 1 a 12 estão disponíveis. No Módulo III, o capítulo 11 concluiu seu ciclo interno e o capítulo 12 está em primeira entrega de leitura.")
    replace("book/README.md", "| [III · Sistemas operacionais](modulo-3/README.md) | Capítulos 11 a 17 | Capítulo 11 disponível; demais planejados |", "| [III · Sistemas operacionais](modulo-3/README.md) | Capítulos 11 a 17 | Capítulos 11 e 12 disponíveis; demais planejados |")
    replace("book/README.md", "| 11 | [O papel de um sistema operacional](modulo-3/capitulo-11/README.md) | Rascunho para leitura — v0.1 |", "| 11 | [O papel de um sistema operacional](modulo-3/capitulo-11/README.md) | Revisão interna concluída — v1.0 |\n| 12 | [Linux por dentro](modulo-3/capitulo-12/README.md) | Rascunho para leitura — v0.1 |")
    sections = [
        ("12.1 · Linux é o núcleo de qual sistema?", "12.1-kernel-distribuicao-e-contexto.md"),
        ("12.2 · Uma árvore de nomes, várias origens", "12.2-diretorios-e-montagens.md"),
        ("12.3 · Arquivos que mostram o sistema em funcionamento", "12.3-proc-sys-e-dev.md"),
        ("12.4 · Do dispositivo ao serviço", "12.4-drivers-modulos-e-servicos.md"),
        ("12.5 · Instalar, atualizar e investigar sem adivinhar", "12.5-pacotes-atualizacoes-e-investigacao.md"),
    ]
    insert = "### Dentro do Capítulo 12\n\n" + "\n".join(f"- [{title}](modulo-3/capitulo-12/{file})" for title, file in sections)
    insert += "\n- [Exemplo opcional de descritor próprio](modulo-3/capitulo-12/exemplos/README.md).\n- [Respostas comentadas](modulo-3/capitulo-12/solucoes.md) e [referências](modulo-3/capitulo-12/referencias.md).\n\n"
    replace("book/README.md", "## Como navegar", insert + "## Como navegar")
    replace("book/modulo-3/README.md", "| 11 | [O papel de um sistema operacional](capitulo-11/README.md) | Rascunho para leitura — v0.1 |", "| 11 | [O papel de um sistema operacional](capitulo-11/README.md) | Revisão interna concluída — v1.0 |")
    replace("book/modulo-3/README.md", "| 12 | Linux por dentro | Planejado |", "| 12 | [Linux por dentro](capitulo-12/README.md) | Rascunho para leitura — v0.1 |")
    replace("book/modulo-3/README.md", "Somente o capítulo 11 está disponível neste módulo. Os demais títulos indicam a progressão do [sumário mestre](../../editorial/master-outline.md), não arquivos já produzidos. A numeração continua global.", "Os capítulos 11 e 12 estão disponíveis neste módulo. O 11 tem revisão interna concluída; o 12 está em primeira leitura. Os demais títulos indicam a progressão do [sumário mestre](../../editorial/master-outline.md), não arquivos já produzidos. A numeração continua global.")
    replace("book/modulo-3/README.md", "**[Começar pelo Capítulo 11 →](capitulo-11/README.md)**", "O capítulo 12 concretiza esse mapa em Linux, com diretórios, montagens, interfaces de estado e manutenção de pacotes. Seu exemplo consulta somente um descritor próprio; a leitura não exige operações administrativas.\n\n**[Começar pelo Capítulo 11 →](capitulo-11/README.md)** · **[Continuar no Capítulo 12 →](capitulo-12/README.md)**")
    replace("book/modulo-3/capitulo-11/README.md", "> **Status:** DRAFT 0.1 — primeira entrega de leitura. Fontes e verificações delimitadas no [registro editorial](../../../editorial/reviews/capitulo-11.md). Revisão técnica independente pendente.", "> **Status:** VALIDATED — versão editorial 1.0; leitura aprovada e revisão interna concluída em 29/09/2026. Fontes e verificações delimitadas no [registro editorial](../../../editorial/reviews/capitulo-11.md). Revisão técnica independente pendente.")
    replace("book/modulo-3/capitulo-11/README.md", "**[Começar pela seção 11.1 →](11.1-abstracoes-e-responsabilidades.md)**", "**[Começar pela seção 11.1 →](11.1-abstracoes-e-responsabilidades.md)** · **[Próximo capítulo: Linux por dentro →](../capitulo-12/README.md)**")
    replace("book/modulo-3/capitulo-11/11.5-inicializacao-servicos-e-investigacao.md", "[Conferir as respostas](solucoes.md) · [Voltar ao Módulo III](../README.md)", "[Conferir as respostas](solucoes.md) · [Voltar ao Módulo III](../README.md) · [Seguir para o Capítulo 12 →](../capitulo-12/README.md)")
    replace("book/modulo-3/capitulo-11/referencias.md", "**Consulta:** 28/09/2026. **Versão:** DRAFT 0.1.", "**Consulta inicial:** 28/09/2026. **Versão editorial:** VALIDATED 1.0 — fechamento interno em 29/09/2026; revisão independente pendente.")
    replace("book/modulo-3/capitulo-11/referencias.md", "Revisão técnica independente e leitura do capítulo 11 permanecem pendentes.", "A leitura foi aprovada e o ciclo interno da versão editorial 1.0 foi encerrado em 29/09/2026. Revisão técnica independente permanece pendente.")
    replace("book/bibliografia.md", "**Data desta revisão bibliográfica:** 28 de setembro de 2026.", "**Data desta revisão bibliográfica:** 29 de setembro de 2026.")
    replace("book/bibliografia.md", "O capítulo permanece DRAFT 0.1, conforme seu [registro editorial](../editorial/reviews/capitulo-11.md); a abertura do Módulo III não encerra revisões anteriores.", "A leitura foi aprovada e o ciclo interno da versão editorial 1.0 foi encerrado em 29/09/2026, conforme seu [registro editorial](../editorial/reviews/capitulo-11.md). Revisão independente permanece pendente.")
    bib = """## Capítulo 12 — Linux por dentro

As [fontes S1–S19](modulo-3/capitulo-12/referencias.md) relacionam documentação do kernel, Linux man-pages, Debian, FHS, systemd, kmod, util-linux e Python. Delimitam composição da instalação, árvore de nomes, montagens, interfaces de estado, dispositivos, módulos e pacotes. O percurso Debian/APT não é generalizado para todas as distribuições; convenções FHS e merged-/usr são identificadas por suas fontes.

O cenário de visibilidade do catálogo é fictício. O [exemplo opcional](modulo-3/capitulo-12/exemplos/README.md) consulta somente um descritor do próprio processo, sobre arquivo temporário próprio. Os [quatro testes](../scripts/tests/test_chapter12_examples.py) conferem plataforma, metadados/leitura, limpeza e saída documentada; não demonstram uma política entre identidades nem compartilhamento de posição entre aberturas.

O capítulo está em DRAFT 0.1, conforme seu [registro editorial](../editorial/reviews/capitulo-12.md). Não houve montagem, instalação, administração de serviços, carga de módulos ou leitura de processos alheios. Revisão técnica independente e primeira leitura permanecem pendentes.

"""
    replace("book/bibliografia.md", "## Política de referências", bib + "## Política de referências")
    replace("editorial/publication-status.md", "**Atualização:** 28 de setembro de 2026.", "**Atualização:** 29 de setembro de 2026.")
    replace("editorial/publication-status.md", "| 11 | DRAFT 0.1 — primeira entrega de leitura | Cinco seções, dez questões e soluções, fontes S1–S14 e seis testes delimitados. Exemplo Linux próprio de operações e erros; leitura e revisão independente pendentes. [Registro](reviews/capitulo-11.md). |", "| 11 | VALIDATED — versão editorial 1.0; leitura aprovada e revisão interna concluída em 29/09/2026 | Cinco seções, dez respostas e fontes S1–S14 relidas; seis testes delimitados preservados e reconferidos na regressão. Revisão independente pendente. [Registro](reviews/capitulo-11.md). |\n| 12 | DRAFT 0.1 — primeira entrega de leitura | Cinco seções, dez questões e respostas, fontes S1–S19 e quatro testes próprios delimitados. Exemplo de descritor próprio em procfs, sem administração da máquina. Leitura e revisão independente pendentes. [Registro](reviews/capitulo-12.md). |")
    replace("editorial/publication-status.md", "As aprovações dos capítulos 4 a 10", "As aprovações dos capítulos 4 a 11")
    replace("editorial/publication-status.md", "O [Módulo III](../book/modulo-3/README.md) começa com o [Capítulo 11](../book/modulo-3/capitulo-11/README.md) em primeira entrega. Os capítulos 12 a 17 continuam planejados. A abertura do módulo não equivale a encerrar os anteriores ou a atribuir domínio prático ao leitor.", "O [Módulo III](../book/modulo-3/README.md) possui o [Capítulo 11](../book/modulo-3/capitulo-11/README.md) com ciclo interno concluído e o [Capítulo 12](../book/modulo-3/capitulo-12/README.md) em primeira entrega. Os capítulos 13 a 17 continuam planejados. O módulo permanece em produção; a aprovação editorial não atribui domínio prático ao leitor.")
    replace("editorial/publication-status.md", "1. Receber a leitura do Capítulo 11, com atenção à relação entre operação, identidade, recurso e contexto.", "1. Receber a leitura do Capítulo 12, com atenção às diferenças entre kernel, instalação, visão de montagens e interfaces de estado.")
    replace("editorial/publication-status.md", "3. Preparar a comunicação pública do fechamento do Módulo II e, depois da leitura do capítulo 11, prosseguir para o Capítulo 12 — Linux por dentro, mantendo glossário, fontes e navegação na mesma entrega.", "3. A comunicação de fechamento do Módulo II foi preparada; não presumir publicação. Depois da leitura do capítulo 12, prosseguir para o Capítulo 13 — Windows por dentro, mantendo glossário, fontes e navegação na mesma entrega.")
    replace("editorial/coverage-matrix.md", "Seu estado é DRAFT 0.1; [fontes S1–S14]", "Seu ciclo interno da versão 1.0 foi concluído; [fontes S1–S14]")
    rows = """| M03-06 | [Kernel, distribuição e contexto](../book/modulo-3/capitulo-12/12.1-kernel-distribuicao-e-contexto.md) | Identificação de kernel versus instalação, composição e dependências. | Fundamentos, DRAFT; [fontes S1–S19](../book/modulo-3/capitulo-12/referencias.md). Sem diagnóstico universal por versão ou prova de container. |
| M03-07 | [Diretórios e montagens](../book/modulo-3/capitulo-12/12.2-diretorios-e-montagens.md) | FHS, merged-/usr, pontos de montagem e contexto da observação. | Explicação por modelo, sem montar dispositivos, alterar diretórios ou entrar em namespaces. |
| M03-08 | [Procfs, sysfs e dispositivos](../book/modulo-3/capitulo-12/12.3-proc-sys-e-dev.md) | Distingue documento e interface de estado; exemplo de descritor próprio e tmpfs. | Leitura local limitada; não lê processos alheios, não escreve em sysfs nem comprova isolamento. |
| M03-09 | [Drivers, módulos e serviços](../book/modulo-3/capitulo-12/12.4-drivers-modulos-e-servicos.md) | Instalado versus carregado, gerenciamento de dispositivos e condição de prontidão. | Introdução por documentação; sem carregar módulos, alterar firmware ou configurar serviços. |
| M03-10 | [Pacotes e manutenção](../book/modulo-3/capitulo-12/12.5-pacotes-atualizacoes-e-investigacao.md) | dpkg/APT, índices, cadeia de confiança, backports e diagnóstico da Aurora. | Percurso Debian identificado; não instala pacotes nem atesta correção de vulnerabilidade real. |

"""
    replace("editorial/coverage-matrix.md", "\n## Cobertura ainda planejada", "\n" + rows + "## Cobertura ainda planejada")
    replace("editorial/coverage-matrix.md", "Os capítulos a partir do 12 não recebem linhas de cobertura efetiva antes da produção dos textos.", "Os capítulos a partir do 13 não recebem linhas de cobertura efetiva antes da produção dos textos.")
    replace("editorial/coverage-matrix.md", "As introduções a Linux, Windows e isolamento no capítulo 11 não substituem essas unidades futuras.", "Os capítulos 11 e 12 não substituem o aprofundamento futuro de Windows, administração, permissões ou isolamento.")
    replace("editorial/reviews/capitulo-11.md", "# Primeira entrega editorial — Capítulo 11", "# Revisão editorial — Capítulo 11")
    replace("editorial/reviews/capitulo-11.md", "**Data:** 28/09/2026. **Estado:** DRAFT 0.1. **Módulo:** III.", "**Primeira entrega:** 28/09/2026. **Fechamento interno:** 29/09/2026. **Estado:** VALIDATED — versão editorial 1.0. **Módulo:** III.")
    old = "A solicitação desta rodada autoriza continuar a escrita. Não contém avaliação explícita da leitura do capítulo 10; seu estado anterior é preservado, sem inventar aprovação, horas ou prática. Também não foi concluída nesta entrega a revisão pendente do capítulo 1 ou a revisão de conjunto dos módulos anteriores. O capítulo 11 permanece em primeira leitura e com revisão independente pendente. Não houve geração de PDF nem publicação no LinkedIn."
    new = "Na primeira entrega, a interpretação de que o pedido de avanço não aprovava a leitura do capítulo 10 deixou uma pendência editorial indevida. Essa interpretação foi corrigida na auditoria do Módulo II: pedir o próximo capítulo registra aprovação de leitura do anterior. A solicitação atual aprova o capítulo 11 sob a mesma convenção. Não são inferidas horas, respostas a exercícios ou prática. O fechamento do Módulo II e a pendência do capítulo 1 são registros separados. Não houve geração de PDF nem publicação no LinkedIn nesta rodada."
    replace("editorial/reviews/capitulo-11.md", old, new)
    replace("editorial/reviews/capitulo-11.md", "**Próxima revisão:** conferir a clareza da passagem entre operação, identidade, recurso e contexto. Próximo capítulo planejado: **12 — Linux por dentro**.", "## Fechamento interno — 29/09/2026\n\nAs cinco seções, as dez respostas e os limites de fontes e exemplos foram relidos. Os seis testes originais são reconferidos na regressão da entrega do capítulo 12, sem transformar modelos em medições do kernel. A aprovação de leitura e essas verificações encerram o ciclo interno da versão editorial 1.0. Revisão técnica independente permanece pendente.\n\n**Próxima revisão:** revisão técnica independente e preparação de edição estável. A leitura continua no **Capítulo 12 — Linux por dentro**, em DRAFT 0.1.")
    glossary(sections)

def glossary(sections):
    p = Path("book/glossario.md")
    if run("git", "hash-object", str(p)).strip() != "444251500c540089ff661f800dd1c3d30701e0aa":
        raise RuntimeError("Unexpected glossary baseline")
    text = p.read_text()
    body, tail = text.split("\n---\n", 1)
    header, _ = body.split("\n## A\n", 1)
    entries = {}
    pattern = r"^### ([^\n]+)\n(.*?)(?=^### |^## |\Z)"
    for match in re.finditer(pattern, body, re.M | re.S):
        name = match.group(1)
        block = match.group(0).rstrip() + "\n\n"
        if name.casefold() in entries:
            raise RuntimeError("duplicate glossary heading")
        entries[name.casefold()] = (name, block)
    if len(entries) != 373:
        raise RuntimeError(f"Expected 373 original entries, got {len(entries)}")
    originals = dict(entries)
    additions = {
        "APT": ("Advanced Package Tool. Conjunto de ferramentas que trabalha com fontes e metadados de pacotes, resolução de dependências e operações de instalação. Atualizar índices não equivale a atualizar programas instalados.", "125"),
        "Arquivo de dispositivo": ("Objeto especial que oferece acesso a uma interface de dispositivo. Seu contrato não é necessariamente o de um arquivo regular que conserva todos os bytes escritos.", "123"),
        "Backport": ("Transporte seletivo de uma correção ou mudança para uma versão mantida anteriormente. Na segurança de pacotes, exige verificar a revisão completa e o aviso da distribuição; o termo não prova sozinho que uma instalação esteja corrigida.", "125"),
        "Bind mount": ("Montagem que torna uma árvore existente acessível por outro ponto. Não cria, por si só, uma cópia independente dos arquivos nem uma cópia de segurança.", "122"),
        "Dependência de software": ("Relação declarada entre componentes necessários à instalação ou ao funcionamento de software. Resolver dependências não demonstra toda a correção ou segurança da aplicação.", "125"),
        "Diretório raiz": ("Início da árvore usada para resolver caminhos absolutos, representado por /. Não é a conta root nem seu diretório pessoal /root; a raiz e a visão dependem do contexto do processo.", "122"),
        "Dispositivo de bloco": ("Tipo de interface de dispositivo que organiza acesso por blocos. É uma classificação da interface, não um formato de documento nem confirmação de que seu sistema de arquivos esteja montado.", "123"),
        "Dispositivo de caractere": ("Tipo de interface de dispositivo distinto do acesso por blocos. O nome não significa que o recurso armazene apenas texto; cada interface mantém suas próprias operações e garantias.", "123"),
        "dpkg": ("Ferramenta de administração de pacotes Debian e de seu estado local. Instalação pode envolver arquivos, metadados e scripts de manutenção, não apenas copiar um executável.", "125"),
        "dpkg-query": ("Ferramenta que consulta a base local de pacotes Debian, incluindo versões e caminhos registrados. Não é inventário universal de todos os arquivos criados fora desse mecanismo nem das versões em execução.", "125"),
        "FHS": ("Filesystem Hierarchy Standard. Documento de convenções para a organização de diretórios e suas funções. O capítulo usa a versão 3.0 como referência, sem presumir conformidade literal de toda instalação atual.", "122"),
        "findmnt": ("Utilitário do projeto util-linux para consultar informações de sistemas de arquivos montados. A interpretação depende das opções e da origem da consulta; a visão do terminal não é automaticamente a de outro serviço.", "122"),
        "Índice de pacotes": ("Metadados que descrevem pacotes anunciados por uma fonte. Buscar uma versão nova do índice não significa substituir o software já instalado.", "125"),
        "kmod": ("Conjunto de ferramentas para trabalhar com módulos de kernel Linux, incluindo modprobe. Consultar o estado de módulos e solicitar carga ou remoção são operações diferentes.", "124"),
        "Merged-/usr": ("Organização em que determinados caminhos tradicionais, como /bin, são links para equivalentes em /usr. A relação pode ser prevista pela distribuição e não demonstra, sozinha, corrupção da instalação.", "122"),
        "modprobe": ("Ferramenta do conjunto kmod que trata inclusão e remoção de módulos Linux considerando dependências. É citada para explicar seu papel, sem execução dessas alterações no capítulo.", "124"),
        "Módulo de kernel": ("Componente que pode ser carregado separadamente para acrescentar funcionalidade ao kernel, conforme a configuração. Não é um processo de usuário isolado; nem todo driver precisa ser fornecido como módulo carregável.", "124"),
        "Montagem": ("Associação que disponibiliza um sistema de arquivos ou uma árvore em um ponto de uma visão de nomes. Pode encobrir conteúdo anterior por aquele caminho sem apagá-lo.", "122"),
        "os-release": ("Arquivo de identificação da instalação, com campos como ID e PRETTY_NAME. Identifica uma camada diferente da release do kernel em execução e não certifica a integridade de todos os componentes.", "121"),
        "Pacote de software": ("Unidade de distribuição com arquivos e metadados para instalação e administração, podendo incluir dependências e ações de manutenção. Não se confunde com um pacote de rede.", "125"),
        "Ponto de montagem": ("Local de uma árvore de nomes em que uma montagem torna seu conteúdo acessível. O caminho não revela sozinho a origem dos dados nem a visão de todos os processos.", "122"),
        "Procfs": ("Sistema de arquivos normalmente montado em /proc que apresenta informações de processos e do sistema em funcionamento. Seus dados são dinâmicos; várias consultas não equivalem necessariamente a uma fotografia atômica do sistema.", "123"),
        "Repositório de pacotes": ("Fonte que disponibiliza pacotes e seus metadados para distribuição e manutenção. É distinto de um repositório Git de código; confiar numa nova fonte altera a cadeia de fornecimento do ambiente.", "125"),
        "root": ("Conta administrativa no contexto Linux do capítulo. Não é sinônimo de diretório raiz nem do caminho /root; suas capacidades efetivas continuam sujeitas aos mecanismos e políticas do ambiente.", "122"),
        "Sysfs": ("Sistema de arquivos normalmente montado em /sys que organiza objetos do kernel e atributos. Algumas escritas acionam operações de controle, não apenas alteram um documento persistente.", "123"),
        "Tmpfs": ("Sistema de arquivos que utiliza memória virtual e pode usar swap conforme a configuração. Não garante conservação após desmontagem ou reinicialização; o nome /tmp não prova que um diretório use tmpfs.", "123"),
        "udev": ("Componente de gerenciamento dinâmico de dispositivos que recebe eventos do kernel e aplica regras em espaço de usuário. Não é o driver nem uma garantia universal de automontagem.", "124"),
        "uname": ("Utilitário que apresenta informações do sistema; a opção -r identifica a release do kernel em execução. Não lista todas as imagens de kernel instaladas para uma próxima inicialização.", "121"),
        "Upstream": ("Projeto de origem em relação a quem integra ou distribui seu software. Sua versão e a revisão mantida por uma distribuição precisam ser distinguidas ao examinar correções.", "125"),
    }
    added = []
    for name, (definition, section) in additions.items():
        if name.casefold() in entries:
            continue
        block = f"### {name}\n\n{definition} [Conceito: {section[:2]}.{section[2:]}][c{section}].\n\n"
        entries[name.casefold()] = (name, block)
        added.append(name)
    def key(name):
        return unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode().casefold()
    groups = {}
    for name, block in entries.values():
        groups.setdefault(key(name)[0].upper(), []).append((name, block))
    newbody = header + "\n\n"
    for letter in sorted(groups):
        newbody += f"## {letter}\n\n"
        newbody += "".join(block for name, block in sorted(groups[letter], key=lambda it: key(it[0])))
    result = newbody.rstrip() + "\n\n---\n" + tail.rstrip() + "\n\n"
    for i, (_, file) in enumerate(sections, 1):
        label = f"[c12{i}]:"
        if label in text:
            raise RuntimeError("New label already exists")
        result += f"{label} modulo-3/capitulo-12/{file}\n"
    for name, block in originals.values():
        if block.rstrip() not in result:
            raise RuntimeError(f"Original glossary entry not preserved: {name}")
    p.write_text(result, encoding="utf-8")
    Path("/tmp/ch12_glossary.json").write_text(json.dumps({"before": 373, "after": len(entries), "added": added}, ensure_ascii=False))
    print("GLOSSARY", json.dumps({"before": 373, "after": len(entries), "added": added}, ensure_ascii=False))

def report():
    check = json.loads(run("python3", "scripts/check_docs.py"))
    if check["internal_errors"]:
        raise RuntimeError("Internal links failed")
    glossary = json.loads(Path("/tmp/ch12_glossary.json").read_text())
    result = json.loads(Path("/tmp/ch12_tests.json").read_text())
    if not result["successful"] or result["skipped"]:
        raise RuntimeError("Full execution without skip required for this preparation report")
    count = result["testsRun"]
    run_url = f"https://github.com/{REPO}/actions/runs/{os.environ['GITHUB_RUN_ID']}"
    note = f"""A preparação no [workflow de apoio]({run_url}) executou **{count} testes com sucesso**, incluindo os quatro novos. A checagem global percorreu **{check['markdown_files']} Markdown**, conferiu **{check['internal_links']} destinos internos** e não detectou erro de caminho ou âncora. Esse verificador inventaria URLs externas; não certifica sua disponibilidade por HTTP.

O glossário passou de **373 para {glossary['after']} verbetes**, com **{len(glossary['added'])} entradas novas** e preservação dos 373 blocos anteriores. As entradas têm ocorrência no capítulo, explicação delimitada e navegação para as respectivas seções. Nenhum assunto apenas planejado foi adicionado.

O workflow e o auxiliar usados apenas para preparar esta alteração são excluídos da árvore final. O workflow permanente permanece inalterado. A aprovação do commit final é conferida separadamente antes e depois da integração.
"""
    replace("editorial/reviews/capitulo-12.md", "<!-- RESULTADOS_C12 -->", note)
    finalcheck = json.loads(run("python3", "scripts/check_docs.py"))
    if finalcheck["internal_errors"]:
        raise RuntimeError("Post-report links failed")
    for field in ["markdown_files", "internal_links"]:
        if finalcheck[field] != check[field]:
            raise RuntimeError(f"Unstable check count: {field}")
    print("FINAL_DOCS", json.dumps(finalcheck, ensure_ascii=False))

def api(path, body=None):
    req = urllib.request.Request("https://api.github.com/repos/" + REPO + path,
        data=None if body is None else json.dumps(body).encode(),
        headers={"Authorization": "Bearer " + os.environ["GH_TOKEN"], "Accept": "application/vnd.github+json", "Content-Type": "application/json"},
        method="GET" if body is None else "POST")
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.load(response)

def publish():
    changed = set(run("git", "diff", "--name-only").splitlines())
    if not changed.issubset(ALLOWED) or not changed:
        raise RuntimeError("Unexpected edit set: " + repr(changed))
    if api("/git/ref/heads/main")["object"]["sha"] != BASE:
        raise RuntimeError("main advanced; reconcile before publishing")
    elements = [{"path": path, "mode": "100644", "type": "blob", "content": Path(path).read_text()} for path in sorted(changed)]
    elements += [{"path": path, "mode": "100644", "type": "blob", "sha": None} for path in TEMP]
    tree = api("/git/trees", {"base_tree": run("git", "rev-parse", "HEAD^{tree}").strip(), "tree": elements})
    print("CANDIDATE_TREE=" + tree["sha"])
    print("CHANGED_PATHS=" + json.dumps(sorted(changed)))
    print("No branch/ref/commit has been created or updated by this helper.")

if __name__ == "__main__":
    {"edit": edit, "report": report, "publish": publish}[sys.argv[1]]()
