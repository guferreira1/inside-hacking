"""Observe somente um filho criado aqui; sem shell, rede ou PID externo."""
from __future__ import annotations
import json
import queue
import subprocess
import sys
import threading

CHILD = """import sys
print('pronto', flush=True)
command = sys.stdin.readline()
if command != 'terminar\\n':
    print('pedido invalido', file=sys.stderr, flush=True)
    raise SystemExit(7)
print('concluido', flush=True)
"""


def observar(command: str = 'terminar\n') -> dict:
    process = subprocess.Popen(
        [sys.executable, '-I', '-u', '-c', CHILD], stdin=subprocess.PIPE,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
        encoding='utf-8', shell=False,
    )
    messages: queue.Queue = queue.Queue(maxsize=1)
    reader = threading.Thread(target=lambda: messages.put(process.stdout.readline()), daemon=True)
    reader.start()
    try:
        ready = messages.get(timeout=10)
        reader.join(timeout=1)
        if ready != 'pronto\n':
            raise RuntimeError('O filho nao confirmou a inicializacao.')
        active = process.poll() is None
        output, diagnostics = process.communicate(input=command, timeout=10)
        return {'pronto': ready.strip(), 'ativo_antes_do_pedido': active,
                'saida_final': output.strip(), 'diagnostico': diagnostics.strip(),
                'codigo': process.returncode}
    finally:
        if process.poll() is None:
            process.kill()  # Somente o filho criado por este programa.
        process.wait(timeout=10)
        reader.join(timeout=1)
        for stream in (process.stdin, process.stdout, process.stderr):
            if stream is not None and not stream.closed:
                stream.close()


if __name__ == '__main__':
    print(json.dumps(observar(), ensure_ascii=False, sort_keys=True))
