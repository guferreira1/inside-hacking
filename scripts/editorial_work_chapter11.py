"""One-time editorial edit on a temporary branch; excluded from main delivery."""
from pathlib import Path
import hashlib
import json
import re
import unicodedata

path = Path('book/glossario.md')
raw = path.read_bytes()
expected = '876329776ccf5ebf5f29ec8dc663752024b09aa0'
actual = hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
if actual != expected:
    raise SystemExit('Unexpected glossary base; refusing to edit.')
text = raw.decode('utf-8')
original_entries = re.findall(r'(?ms)^### [^\n]+\n.*?(?=^### |^## |^---|\Z)', text)
assert len(original_entries) == 340, len(original_entries)

entries = {
'Abstração': ('Apresentação de operações e garantias que permite trabalhar sem administrar todos os detalhes internos. Não elimina as condições de existência, acesso, custo ou falha do recurso.', '11.1', 'c111'),
'Capabilities (Linux)': ('Divisão de parte dos privilégios tradicionalmente associados ao superusuário em capacidades específicas do contexto de execução. Não equivale a todo modelo de segurança baseado em capabilities.', '11.4', 'c114'),
'Cgroup': ('Control group. Organização hierárquica de processos para administrar recursos no Linux segundo controladores e configurações. Peso relativo de distribuição e teto de consumo não são a mesma garantia.', '11.3', 'c113'),
'Container': ('Organização de execução e isolamento por uma combinação de mecanismos e configurações. No percurso Linux usual, compartilha o kernel; a separação de uma visão não certifica todos os limites do ambiente.', '11.4', 'c114'),
'Daemon': ('Processo de serviço em segundo plano no vocabulário Unix apresentado. Serviço lógico, processo e unidade de um gerenciador não precisam ter correspondência de um para um.', '11.5', 'c115'),
'Deadlock': ('Impasse sem progresso sob condições como as do modelo: tarefas mantêm recursos exclusivos e esperam recursos umas das outras sem liberar nem dispor de recuperação. O exemplo do livro é uma dependência desenhada, não um travamento executado.', '11.3', 'c113'),
'Distribuição Linux': ('Integração do kernel Linux com ferramentas, bibliotecas, pacotes, configurações e manutenção. Compartilhar o kernel não implica que duas instalações ofereçam as mesmas condições de execução.', '11.1', 'c111'),
'EACCES': ('Nome simbólico de erro associado a recusa de acesso nas interfaces discutidas. Não identifica sozinho qual componente do caminho ou política ocasionou a recusa.', '11.2', 'c112'),
'EBADF': ('Nome simbólico de erro que pode indicar descritor inválido ou incompatível com a operação. Uma abertura válida somente para leitura pode produzir esse erro quando usada para escrita.', '11.2', 'c112'),
'ENOENT': ('Nome simbólico de erro associado à ausência de componente necessário à resolução de um caminho. No exemplo, aparece ao tentar abrir um nome não criado, não ao consumir o fim do arquivo existente.', '11.2', 'c112'),
'errno': ('Informação de erro utilizada em interfaces C sob o contrato da função. Deve ser consultada quando a operação indica falha; um valor antigo não comprova erro numa chamada bem-sucedida. Python conserva códigos correspondentes em exceções OSError.', '11.2', 'c112'),
'Espaço de usuário': ('Userspace. Ambiente de execução de aplicações e componentes fora do kernel. Pode incluir serviços com permissões relevantes; não significa que todo programa ali execute sob uma conta sem privilégios.', '11.1', 'c111'),
'Gerenciador de serviços': ('Componente que organiza ciclo de vida e contexto de serviços conforme sua configuração. Iniciar ou reiniciar um processo não demonstra que todas as funções do serviço estejam saudáveis.', '11.5', 'c115'),
'GID': ('Group identifier, identificador de grupo. Participa do contexto de credenciais das interfaces Unix/Linux; grupos e variantes de identificadores possuem papéis que precisam ser distinguidos.', '11.4', 'c114'),
'initramfs': ('Ambiente inicial de sistemas de arquivos em memória que pode participar da preparação antes de alcançar o sistema de arquivos raiz pretendido no percurso Linux. Sua utilização depende da inicialização configurada.', '11.5', 'c115'),
'LSM': ('Linux Security Modules. Arcabouço do kernel para participação de mecanismos adicionais de segurança. Sua presença não informa sozinha quais políticas estão ativas ou quais operações serão permitidas.', '11.4', 'c114'),
'Mecanismo': ('No vocabulário de análise do livro, meio utilizado para realizar uma decisão, como a verificação de uma permissão. A política define o critério; possuir o mecanismo não garante uma política adequada.', '11.1', 'c111'),
'Menor privilégio': ('Princípio de conceder a cada componente ou identidade somente as capacidades necessárias às suas responsabilidades. Limitar o serviço não substitui a autorização dos registros que ele entrega a seus clientes.', '11.4', 'c114'),
'Microkernel': ('Organização que concentra um conjunto reduzido de mecanismos no núcleo e deixa diversos serviços em componentes externos. A comparação com seL4 não certifica a segurança de qualquer sistema montado dessa maneira.', '11.1', 'c111'),
'Namespace': ('No Linux, visão particular de uma classe de recursos apresentada a um conjunto de processos. O tipo de namespace determina o que se separa; não equivale automaticamente a um limite de consumo.', '11.4', 'c114'),
'Operação bloqueante': ('Operação que pode manter o fluxo à espera de condições para prosseguir. A espera por E/S não se resolve necessariamente com maior prioridade de CPU.', '11.3', 'c113'),
'Operação não bloqueante': ('Operação que retorna sem aguardar determinada condição e pode informar que ainda não é possível prosseguir. Não significa que o trabalho já terminou; as garantias dependem da interface e do recurso.', '11.3', 'c113'),
'Política': ('Critério que orienta decisões de uso, distribuição ou acesso a recursos. Um mecanismo pode aplicar corretamente uma política inadequada ou deixar de aplicar a política pretendida.', '11.1', 'c111'),
'Preempção': ('Interrupção da ocupação da CPU por um fluxo para permitir encaminhar outro segundo as regras de escalonamento. Não garante divisão igual ou atendimento imediato de qualquer tarefa.', '11.3', 'c113'),
'Prontidão': ('Condição de preparação para uma operação ou estágio do ciclo de vida, conforme um contrato. No serviço, uma indicação de inicialização concluída não é garantia permanente de funcionamento de todas as capacidades.', '11.5', 'c115'),
'Reteste': ('Nova verificação após uma alteração, voltada ao comportamento que deveria ser corrigido e às propriedades que deveriam permanecer. No exemplo de acesso, inclui o uso legítimo e a preservação das recusas necessárias.', '11.5', 'c115'),
'Service Control Manager': ('Componente Windows que inicia e controla serviços e mantém sua base de configuração. É um exemplo de gerenciador, não o mesmo programa que systemd.', '11.5', 'c115'),
'Serviço': ('Capacidade oferecida por um componente em execução, frequentemente administrado sem interação constante. Pode envolver vários processos; existir um processo não demonstra que a capacidade oferecida está funcionando.', '11.5', 'c115'),
'systemd': ('Conjunto de componentes que inclui um gerenciador de sistema e serviços. No papel de gerenciador de sistema descrito, executa como PID 1 e coordena unidades. Não é o kernel nem um componente obrigatório de toda distribuição.', '11.5', 'c115'),
'Token de acesso (Windows)': ('Objeto que descreve contexto de segurança de um processo ou thread, incluindo identidade, grupos e privilégios. Não é sinônimo de token de sessão Web nem da senha digitada por uma pessoa.', '11.4', 'c114'),
'UID': ('User identifier, identificador de usuário. Nas interfaces Unix/Linux há variantes com papéis distintos, como identidade real, efetiva e de sistema de arquivos; o nome mostrado numa tela não descreve todo o contexto.', '11.4', 'c114'),
'Verificação de saúde': ('Observação deliberada de uma capacidade definida de um serviço. Conferir apenas a existência do processo não demonstra que uma importação ou outra função esteja funcionando.', '11.5', 'c115'),
'VFS': ('Virtual File System. Camada do kernel Linux que fornece uma interface de sistemas de arquivos e permite coexistência de implementações. A abstração não garante que todo pedido seja permitido ou atendido pelo mesmo caminho físico.', '11.1', 'c111'),
}

def key(value):
    return ''.join(c for c in unicodedata.normalize('NFD', value.casefold())
                   if not unicodedata.combining(c))

existing = {key(x) for x in re.findall(r'(?m)^### (.+)$', text)}
added = []
skipped = []
for name, (definition, section, ref) in sorted(entries.items(), key=lambda item: key(item[0])):
    if key(name) in existing:
        skipped.append(name)
        continue
    letter = key(name)[0].upper()
    marker = f'## {letter}\n'
    assert text.count(marker) == 1, marker
    start = text.index(marker) + len(marker)
    ending = re.search(r'(?m)^## [A-Z]\s*$|^---\s*$', text[start:])
    assert ending, letter
    end = start + ending.start()
    position = end
    for heading in re.finditer(r'(?m)^### (.+)$', text[start:end]):
        if key(heading.group(1)) > key(name):
            position = start + heading.start()
            break
    block = f'### {name}\n\n{definition} [Conceito: {section}][{ref}].\n\n'
    text = text[:position] + block + text[position:]
    existing.add(key(name))
    added.append(name)

old_nav = '[Módulo II](modulo-2/README.md) · [Bibliografia]'
assert text.count(old_nav) == 1
text = text.replace(old_nav, '[Módulo II](modulo-2/README.md) · [Módulo III](modulo-3/README.md) · [Bibliografia]', 1)
refs = {
'c111': '11.1-abstracoes-e-responsabilidades.md',
'c112': '11.2-interfaces-e-chamadas-de-sistema.md',
'c113': '11.3-recursos-espera-e-coordenacao.md',
'c114': '11.4-identidades-e-limites.md',
'c115': '11.5-inicializacao-servicos-e-investigacao.md',
}
for ref, target in refs.items():
    assert f'[{ref}]:' not in text
    assert Path('book/modulo-3/capitulo-11', target).is_file()
    text += f'\n[{ref}]: modulo-3/capitulo-11/{target}'
text += '\n'
for block in original_entries:
    assert block in text, 'An original entry was modified or removed.'
assert len(re.findall(r'(?m)^### ', text)) == 340 + len(added)
path.write_text(text, encoding='utf-8')
print(json.dumps({'original_entries_preserved': 340, 'added': added,
                  'already_present': skipped, 'total': 340 + len(added)}, ensure_ascii=False))
