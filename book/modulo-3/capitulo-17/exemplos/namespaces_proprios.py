#!/usr/bin/env python3
"""Compare namespaces do processo atual e de um filho próprio, sem alterá-los."""
from contextlib import ExitStack, contextmanager
import json
import os
from pathlib import Path
import subprocess
import sys

KINDS = ('mnt', 'pid', 'user', 'net', 'uts', 'ipc')

class ObservationUnavailable(RuntimeError):
    """A observação não pôde ser concluída; não representa isolamento provado."""


def validate_snapshot(value):
    if not isinstance(value, dict) or set(value) != {'pid', 'namespaces'}:
        raise ObservationUnavailable('resposta interna com estrutura inesperada')
    if type(value['pid']) is not int or value['pid'] <= 0:
        raise ObservationUnavailable('identificador de processo inválido')
    spaces = value['namespaces']
    if not isinstance(spaces, dict) or set(spaces) != set(KINDS):
        raise ObservationUnavailable('conjunto de namespaces incompleto')
    for pair in spaces.values():
        if not isinstance(pair, (list, tuple)) or len(pair) != 2:
            raise ObservationUnavailable('identificação de namespace inválida')
        if any(type(n) is not int for n in pair) or pair[0] < 0 or pair[1] <= 0:
            raise ObservationUnavailable('metadados de namespace inválidos')
    return value


@contextmanager
def pinned_snapshot():
    if sys.platform != 'linux':
        raise ObservationUnavailable('este exemplo requer Linux e procfs acessível')
    with ExitStack() as stack:
        spaces = {}
        for kind in KINDS:
            # Seguir o link de procfs é deliberado: o descritor referencia o namespace.
            fd = os.open('/proc/self/ns/' + kind, os.O_RDONLY | os.O_CLOEXEC)
            stack.callback(os.close, fd)
            info = os.fstat(fd)
            spaces[kind] = [info.st_dev, info.st_ino]
        yield validate_snapshot({'pid': os.getpid(), 'namespaces': spaces})


def observe():
    with pinned_snapshot() as parent:
        # Mantém as referências do pai abertas durante a observação do filho.
        result = subprocess.run(
            [sys.executable, '-I', '-S', str(Path(__file__).resolve()), '--filho'],
            stdin=subprocess.DEVNULL, capture_output=True, text=True,
            encoding='utf-8', timeout=5, check=False, shell=False,
        )
        if result.returncode != 0:
            raise ObservationUnavailable('o filho não concluiu sua observação')
        child = validate_snapshot(json.loads(result.stdout))
        return {
            'processos_distintos': parent['pid'] != child['pid'],
            'namespaces_comparados': len(KINDS),
            'mesmo_namespace': {
                kind: parent['namespaces'][kind] == child['namespaces'][kind]
                for kind in KINDS
            },
        }


def main(argv=None):
    args = sys.argv[1:] if argv is None else argv
    try:
        if args == ['--filho']:
            with pinned_snapshot() as value:
                print(json.dumps(value, ensure_ascii=True))
        elif not args:
            print(json.dumps(observe(), ensure_ascii=True, sort_keys=True, indent=2))
        else:
            raise ObservationUnavailable('o exemplo não recebe caminhos nem alvos')
    except (ObservationUnavailable, OSError, ValueError, subprocess.SubprocessError):
        print('Observação indisponível: confira plataforma, acesso a procfs e execução do filho.', file=sys.stderr)
        return 2
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
