"""One-time supporting-document update, confined to a temporary branch."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys

BASES = {
    'README.md': '4eb9d0cdf5ab6f4ea3d8f812b9249e83ae4f4eac',
    'book/README.md': '85aae31d60c2c70035c54aa38a95cb264cc4f107',
    'book/bibliografia.md': 'a3804416d69260e056b56f08fdfa1b985e36d0c3',
    'book/modulo-2/README.md': '9efe985e01a9d9c28138e0400055a89e08b3e20e',
    'book/modulo-2/capitulo-10/README.md': '25e3b9965857da2be0ae2eb217a7374e5043ff7e',
    'book/modulo-2/capitulo-10/10.6-integridade-e-fronteiras.md': '7bed181c3e27b4f6798c6201025a62b9f454d0f0',
    'editorial/coverage-matrix.md': 'b1417545172fea273f332647d5593a9f250bb4da',
    'editorial/publication-status.md': 'bae7f50f9e745f6aa9424b61ad5f71c6d0bfbefa',
}
ALLOWED = set(BASES) | {'book/glossario.md'}
if sys.argv[1:] == ['--verify-diff']:
    names = subprocess.check_output(['git', 'diff', '--name-only', '-z']).decode().split('\0')
    changed = {name for name in names if name}
    if changed != ALLOWED:
        raise SystemExit(f'Unexpected modified paths: {sorted(changed ^ ALLOWED)}')
    print(json.dumps({'approved_modified_paths': sorted(changed)}, ensure_ascii=False))
    raise SystemExit(0)
if sys.argv[1:]:
    raise SystemExit('Unsupported arguments.')

texts = {}
for name, expected in BASES.items():
    raw = Path(name).read_bytes()
    actual = hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
    if actual != expected:
        raise SystemExit(f'Unexpected base for {name}: {actual}')
    texts[name] = raw.decode('utf-8')

def replace(name, old, new):
    assert texts[name].count(old) == 1, (name, old)
    texts[name] = texts[name].replace(old, new, 1)

root_module = '''**[Módulo III — Sistemas operacionais](book/modulo-3/README.md)**

| Leitura | O que você encontrará | Estado |
| --- | --- | --- |
| [11 · O papel de um sistema operacional](book/modulo-3/capitulo-11/README.md) | Abstrações, interfaces do kernel, recursos, identidades e ciclo de vida de serviços. | Rascunho para leitura — v0.1 |

'''
replace('README.md', '**[Abrir o índice de leitura →](book/README.md)**', root_module + '**[Abrir o índice de leitura →](book/README.md)**')
replace('README.md', 'Os capítulos 1 a 10 estão disponíveis.', 'Os capítulos 1 a 11 estão disponíveis. O Módulo III começa com o capítulo 11 em primeira entrega de leitura.')
replace('README.md', '| [`editorial/`](editorial/README.md)', '| [`book/modulo-3/`](book/modulo-3/README.md) | Papel do sistema operacional e progressão para Linux, Windows e isolamento. |\n| [`editorial/`](editorial/README.md)')

replace('book/README.md', '| [II · Computadores por dentro](modulo-2/README.md) | Capítulos 6 a 10 | Todos os textos disponíveis; capítulo 10 em primeira leitura |', '| [II · Computadores por dentro](modulo-2/README.md) | Capítulos 6 a 10 | Todos os textos disponíveis; capítulo 10 em primeira leitura |\n| [III · Sistemas operacionais](modulo-3/README.md) | Capítulos 11 a 17 | Capítulo 11 disponível; demais planejados |')
replace('book/README.md', 'No planejamento atual, o Módulo III começa no capítulo 11.', 'O Módulo III começa no capítulo 11; o Módulo IV, ainda planejado, começa no capítulo 18.')
new_index = '''## Capítulos disponíveis no Módulo III

| Capítulo | Leitura | Estado |
| --- | --- | --- |
| 11 | [O papel de um sistema operacional](modulo-3/capitulo-11/README.md) | Rascunho para leitura — v0.1 |

### Dentro do Capítulo 11

- [11.1 · Um equipamento, muitas promessas](modulo-3/capitulo-11/11.1-abstracoes-e-responsabilidades.md)
- [11.2 · O pedido atravessa uma fronteira](modulo-3/capitulo-11/11.2-interfaces-e-chamadas-de-sistema.md)
- [11.3 · Executar também é esperar](modulo-3/capitulo-11/11.3-recursos-espera-e-coordenacao.md)
- [11.4 · Quem pede faz parte da operação](modulo-3/capitulo-11/11.4-identidades-e-limites.md)
- [11.5 · Ligar a máquina não é concluir o serviço](modulo-3/capitulo-11/11.5-inicializacao-servicos-e-investigacao.md)
- [Exemplo opcional de operações sobre arquivos próprios](modulo-3/capitulo-11/exemplos/README.md).
- [Respostas comentadas](modulo-3/capitulo-11/solucoes.md) e [referências](modulo-3/capitulo-11/referencias.md).

'''
replace('book/README.md', '## Como navegar', new_index + '## Como navegar')

replace('book/modulo-2/README.md', 'O percurso seguinte planejado é o Módulo III — Sistemas operacionais, começando pelo capítulo 11. Essa indicação ainda não representa um manuscrito publicado.', 'O percurso seguinte já começou no [Módulo III — Sistemas operacionais](../modulo-3/README.md), com o [Capítulo 11 — O papel de um sistema operacional](../modulo-3/capitulo-11/README.md). A abertura desse módulo não encerra as revisões pendentes deste.')
texts['book/modulo-2/README.md'] = texts['book/modulo-2/README.md'].rstrip() + '\n\n**[Seguir para o Módulo III →](../modulo-3/README.md)**\n'
texts['book/modulo-2/capitulo-10/README.md'] = texts['book/modulo-2/capitulo-10/README.md'].rstrip() + '\n\n**[Próximo capítulo: 11 — O papel de um sistema operacional →](../../modulo-3/capitulo-11/README.md)**\n'
replace('book/modulo-2/capitulo-10/10.6-integridade-e-fronteiras.md', '[Conferir as respostas](solucoes.md) · [Voltar ao Módulo II](../README.md)', '[Conferir as respostas](solucoes.md) · [Voltar ao Módulo II](../README.md) · [Seguir para o Capítulo 11 →](../../modulo-3/capitulo-11/README.md)')

replace('book/bibliografia.md', '**Data desta revisão bibliográfica:** 24 de setembro de 2026.', '**Data desta revisão bibliográfica:** 28 de setembro de 2026.')
new_biblio = '''## Capítulo 11 — O papel de um sistema operacional

As [fontes S1–S14](modulo-3/capitulo-11/referencias.md) relacionam documentação Debian, Linux, Microsoft, seL4, Python, systemd e OWASP. O percurso distingue abstrações, núcleo e espaço de usuário, chamadas de sistema, espera, recursos, contexto de segurança e ciclo de vida de serviços.

As páginas systemd efetivamente consultadas são reproduções identificadas de sua documentação no man7. A comparação de microkernel é introdutória; não houve instalação de seL4, Windows ou configuração de isolamento. O caso Aurora e os modelos de duração e dependência são autorais e fictícios.

O [exemplo opcional](modulo-3/capitulo-11/exemplos/README.md) usa somente arquivos temporários próprios para distinguir leitura, fim de arquivo e erros de operação. Os [seis testes](../scripts/tests/test_chapter11_examples.py) incluem três verificações desse exemplo e três de modelos conceituais. Não demonstram política entre contas nem medem chamadas de sistema ou desempenho. O capítulo permanece DRAFT 0.1, conforme seu [registro editorial](../editorial/reviews/capitulo-11.md); a abertura do Módulo III não encerra revisões anteriores.

'''
replace('book/bibliografia.md', '## Política de referências', new_biblio + '## Política de referências')

replace('editorial/coverage-matrix.md', 'atualização em 24/09/2026.', 'atualização em 28/09/2026.')
new_coverage = '''## Módulo III — Sistemas operacionais

Pré-requisitos: representações, recursos, processos e arquivos apresentados nos capítulos 6 a 10. O capítulo 11 conecta essas peças às responsabilidades do sistema operacional, sem exigir administração prévia ou execução de comandos. Seu estado é DRAFT 0.1; [fontes S1–S14](../book/modulo-3/capitulo-11/referencias.md) e [registro da entrega](reviews/capitulo-11.md) delimitam a validação.

| ID | Tema / teoria disponível | Aplicação e defesa | Profundidade / fonte e limite |
| --- | --- | --- | --- |
| M03-01 | [Abstrações e responsabilidades](../book/modulo-3/capitulo-11/11.1-abstracoes-e-responsabilidades.md) | VFS, mecanismo/política, kernel, espaço de usuário e composição da instalação. | Introdução funcional. Microkernel é comparação documental, não sistema instalado ou garantia universal. |
| M03-02 | [Interfaces e chamadas de sistema](../book/modulo-3/capitulo-11/11.2-interfaces-e-chamadas-de-sistema.md) | Exemplo Linux próprio de leitura, fim de arquivo, EBADF e ENOENT. | Fundamentos aplicados; sem rastreamento de syscalls ou teste de acesso entre identidades. |
| M03-03 | [Recursos, espera e coordenação](../book/modulo-3/capitulo-11/11.3-recursos-espera-e-coordenacao.md) | Linha do tempo, limites, cgroups e dependência circular. | Modelos explicados e testados, não benchmark, exaustão, deadlock real ou configuração de controladores. |
| M03-04 | [Identidade e limites](../book/modulo-3/capitulo-11/11.4-identidades-e-limites.md) | Distingue identidade do serviço/cliente, permissions do sistema e autorização da aplicação; menor privilégio. | UID/GID, token Windows, capabilities, LSM, namespaces e containers apenas introduzidos. Nenhuma mudança de credenciais ou avaliação de isolamento. |
| M03-05 | [Inicialização e serviços](../book/modulo-3/capitulo-11/11.5-inicializacao-servicos-e-investigacao.md) | Caso fictício de diagnóstico por contexto, prontidão, saúde, registros e reteste. | Percurso Linux/systemd e comparação documental Windows. Nenhum serviço ou sistema de boot alterado. |

'''.replace('permissions do sistema', 'permissões do sistema')
replace('editorial/coverage-matrix.md', '## Cobertura ainda planejada', new_coverage + '## Cobertura ainda planejada')
replace('editorial/coverage-matrix.md', 'Os capítulos a partir do 11 não recebem linhas de cobertura efetiva antes da produção dos textos.', 'Os capítulos a partir do 12 não recebem linhas de cobertura efetiva antes da produção dos textos. As introduções a Linux, Windows e isolamento no capítulo 11 não substituem essas unidades futuras.')

replace('editorial/publication-status.md', '**Atualização:** 24 de setembro de 2026.', '**Atualização:** 28 de setembro de 2026.')
row10 = '| 10 | DRAFT 0.1 — primeira entrega de leitura | Seis seções, doze questões e soluções, fontes S1–S18, codec AUR/JSON e 23 testes locais. Leitura do mantenedor e revisão independente pendentes. [Registro](reviews/capitulo-10.md). |'
row11 = '| 11 | DRAFT 0.1 — primeira entrega de leitura | Cinco seções, dez questões e soluções, fontes S1–S14 e seis testes delimitados. Exemplo Linux próprio de operações e erros; leitura e revisão independente pendentes. [Registro](reviews/capitulo-11.md). |'
replace('editorial/publication-status.md', row10, row10 + '\n' + row11)
replace('editorial/publication-status.md', 'O capítulo 11, previsto como abertura do Módulo III, continua planejado, sem manuscrito nesta entrega.', 'O pedido de continuidade desta rodada não contém avaliação explícita da leitura do capítulo 10; seu estado foi preservado.\n\nO [Módulo III](../book/modulo-3/README.md) começa com o [Capítulo 11](../book/modulo-3/capitulo-11/README.md) em primeira entrega. Os capítulos 12 a 17 continuam planejados. A abertura do módulo não equivale a encerrar os anteriores ou a atribuir domínio prático ao leitor.')
replace('editorial/publication-status.md', '1. Receber a primeira leitura do Capítulo 10, com atenção às camadas de representação e validação, e revisar o conjunto do Módulo II antes de encerrá-lo.', '1. Receber a leitura do Capítulo 11, com atenção à relação entre operação, identidade, recurso e contexto. Registrar também o retorno ainda pendente do capítulo 10 e revisar o conjunto do Módulo II antes de encerrá-lo.')
replace('editorial/publication-status.md', '3. Prosseguir para o Capítulo 11 — O papel de um sistema operacional, abertura do Módulo III, após a unidade atual.', '3. Prosseguir para o Capítulo 12 — Linux por dentro, mantendo glossário, fontes e navegação na mesma entrega.')

for name, text in texts.items():
    assert text != Path(name).read_text(encoding='utf-8'), name
    Path(name).write_text(text.rstrip() + '\n', encoding='utf-8')
print(json.dumps({'updated_documents': list(texts), 'chapter10_status': 'DRAFT 0.1 preserved'}, ensure_ascii=False))
