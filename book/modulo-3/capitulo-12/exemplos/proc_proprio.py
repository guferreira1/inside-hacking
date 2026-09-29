"""Observe somente um descritor do próprio processo; código sob MIT."""
from __future__ import annotations

import os
from pathlib import Path
import stat
import sys
from tempfile import TemporaryDirectory


class AmbienteIndisponivel(RuntimeError):
    """O ambiente não oferece o recorte Linux/procfs exigido pelo exemplo."""


def examinar(diretorio_base: Path | None = None) -> dict[str, object]:
    if sys.platform != "linux" or not Path("/proc/self/fd").is_dir():
        raise AmbienteIndisponivel("Linux com /proc/self/fd acessível é necessário.")
    conteudo = b"Livro\n"
    with TemporaryDirectory(prefix="inside-hacking-c12-", dir=diretorio_base) as pasta:
        arquivo = Path(pasta) / "catalogo.bin"
        arquivo.write_bytes(conteudo)
        with arquivo.open("rb") as aberto:
            referencia = Path(f"/proc/self/fd/{aberto.fileno()}")
            try:
                entrada = referencia.lstat()
                destino = referencia.stat()
                original = os.fstat(aberto.fileno())
                with referencia.open("rb") as outra_abertura:
                    recebido = outra_abertura.read(len(conteudo) + 1)
            except OSError as erro:
                raise AmbienteIndisponivel("A consulta ao descritor próprio foi recusada.") from erro
            mesmo = (destino.st_dev, destino.st_ino) == (original.st_dev, original.st_ino)
            if recebido != conteudo or not mesmo or not stat.S_ISREG(destino.st_mode):
                raise RuntimeError("O comportamento observado diverge do contrato do exemplo.")
            return {
                "entrada_link": stat.S_ISLNK(entrada.st_mode),
                "mesmo_arquivo_regular": mesmo and stat.S_ISREG(destino.st_mode),
                "conteudo": recebido,
                "bytes_lidos": len(recebido),
            }


def main() -> int:
    try:
        resultado = examinar()
    except AmbienteIndisponivel as erro:
        print(f"EXEMPLO_NAO_EXECUTADO: {erro}", file=sys.stderr)
        return 2
    print("entrada_em_proc=" + ("link" if resultado["entrada_link"] else "outro_tipo"))
    print("destino=" + ("mesmo_arquivo_regular" if resultado["mesmo_arquivo_regular"] else "diferente"))
    print("leitura=" + resultado["conteudo"].decode("ascii").rstrip("\n"))
    print(f"bytes_lidos={resultado['bytes_lidos']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
