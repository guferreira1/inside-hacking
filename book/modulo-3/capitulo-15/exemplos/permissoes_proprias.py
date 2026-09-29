#!/usr/bin/env python3
"""Quatro observações Linux sobre arquivos temporários do próprio usuário.

Não administra contas, não recebe caminhos externos e não eleva privilégios.
Execute como usuário comum, sem capabilities efetivas. Não é auditor de host.
"""
from __future__ import annotations

import json
import os
from pathlib import Path
import sys
import tempfile
from collections.abc import Callable

DATA = b"Aurora\n"


def unsupported_reason() -> str | None:
    if sys.platform != "linux":
        return "Este exemplo requer Linux."
    if os.geteuid() == 0:
        return "Execute como usuário comum; UID efetivo zero invalida o exemplo."
    try:
        status = Path("/proc/self/status").read_text(encoding="ascii")
        caps = next(line.split()[1] for line in status.splitlines()
                    if line.startswith("CapEff:"))
        if int(caps, 16):
            return "O exemplo requer ausência de capabilities efetivas."
    except (OSError, StopIteration, ValueError):
        return "Não foi possível conferir o contexto do próprio processo."
    return None


def require_environment() -> None:
    reason = unsupported_reason()
    if reason is not None:
        raise RuntimeError(reason)


def require_denied(operation: Callable[[], object]) -> None:
    try:
        operation()
    except PermissionError:
        return
    raise AssertionError("A recusa esperada não ocorreu neste ambiente.")


def readonly_name() -> dict[str, bool]:
    require_environment()
    with tempfile.TemporaryDirectory(prefix="aurora-perm-") as folder:
        root = Path(folder)
        root.chmod(0o700)
        item = root / "catalogo.txt"
        item.write_bytes(DATA)
        item.chmod(0o400)
        require_denied(lambda: item.write_bytes(b"alteracao"))
        if item.read_bytes() != DATA:
            raise AssertionError("Conteúdo original inesperado.")
        item.unlink()
        return {"escrita_recusada": True, "nome_removido": not item.exists()}


def open_before_change() -> dict[str, bool]:
    require_environment()
    with tempfile.TemporaryDirectory(prefix="aurora-perm-") as folder:
        root = Path(folder)
        root.chmod(0o700)
        item = root / "catalogo.txt"
        item.write_bytes(DATA)
        item.chmod(0o600)
        try:
            with item.open("rb", buffering=0) as opened:
                item.chmod(0o000)
                require_denied(item.read_bytes)
                content = opened.read(len(DATA) + 1)
                if content != DATA:
                    raise AssertionError("Leitura pelo descritor divergiu.")
                return {"nova_abertura_recusada": True,
                        "descritor_anterior_leu": True}
        finally:
            item.chmod(0o600)


def directory_access(mode: int) -> dict[str, bool]:
    require_environment()
    if mode not in (0o100, 0o400):
        raise ValueError("O exemplo admite somente os modos 100 e 400.")
    with tempfile.TemporaryDirectory(prefix="aurora-perm-") as folder:
        root = Path(folder)
        root.chmod(0o700)
        child = root / "entrada"
        child.mkdir(mode=0o700)
        item = child / "catalogo.txt"
        item.write_bytes(DATA)
        item.chmod(0o400)
        try:
            child.chmod(mode)
            if mode == 0o100:
                require_denied(lambda: os.listdir(child))
                if item.read_bytes() != DATA:
                    raise AssertionError("Arquivo conhecido não foi lido.")
                return {"listagem_recusada": True, "nome_conhecido_lido": True}
            names = os.listdir(child)
            if names != ["catalogo.txt"]:
                raise AssertionError("Listagem própria inesperada.")
            require_denied(item.read_bytes)
            return {"nome_listado": True, "abertura_sem_busca_recusada": True}
        finally:
            child.chmod(0o700)


def run_checks() -> dict[str, dict[str, bool]]:
    return {"arquivo_somente_leitura": readonly_name(),
            "descritor_aberto": open_before_change(),
            "diretorio_busca": directory_access(0o100),
            "diretorio_leitura": directory_access(0o400)}


def main() -> int:
    if len(sys.argv) != 1:
        print("Este exemplo não recebe caminhos ou argumentos.", file=sys.stderr)
        return 2
    try:
        result = run_checks()
    except (OSError, ValueError, RuntimeError, AssertionError) as exc:
        print(f"Exemplo interrompido: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
