"""Demonstra dois mapeamentos próprios em Linux; não acessa outros processos."""
# SPDX-License-Identifier: MIT
import mmap
import os
import sys


def main() -> int:
    if not sys.platform.startswith("linux") or not hasattr(os, "fork"):
        print("Este exemplo requer Linux com fork e mmap.", file=sys.stderr)
        return 2
    try:
        with mmap.mmap(-1, mmap.PAGESIZE,
                       flags=mmap.MAP_PRIVATE | mmap.MAP_ANONYMOUS,
                       prot=mmap.PROT_READ | mmap.PROT_WRITE) as privado, \
             mmap.mmap(-1, mmap.PAGESIZE,
                       flags=mmap.MAP_SHARED | mmap.MAP_ANONYMOUS,
                       prot=mmap.PROT_READ | mmap.PROT_WRITE) as compartilhado:
            privado[0] = compartilhado[0] = 5
            filho = os.fork()
            if filho == 0:
                # O filho só altera bytes próprios e herdados pelo exemplo.
                try:
                    privado[0] = 9
                    compartilhado[0] = 9
                except Exception:
                    os._exit(3)
                os._exit(0)
            _, estado = os.waitpid(filho, 0)
            if os.waitstatus_to_exitcode(estado) != 0:
                print("O filho não concluiu normalmente.", file=sys.stderr)
                return 3
            print(f"privado={privado[0]}")
            print(f"compartilhado={compartilhado[0]}")
            return 0 if (privado[0], compartilhado[0]) == (5, 9) else 1
    except (OSError, ValueError) as erro:
        print(f"Não foi possível concluir o exemplo: {erro}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
