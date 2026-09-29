"""Exemplo do capítulo 11. Opera apenas em arquivos temporários próprios."""
from __future__ import annotations

import errno
import os
from pathlib import Path
import sys
import tempfile


def observar() -> dict[str, str | int]:
    """Compare leitura, fim de arquivo e duas recusas distintas no Linux."""
    if not sys.platform.startswith("linux"):
        raise RuntimeError("Este exemplo foi delimitado ao Linux.")

    with tempfile.TemporaryDirectory(prefix="inside-hacking-c11-") as pasta:
        caminho = Path(pasta) / "catalogo.txt"
        caminho.write_bytes(b"Livro")
        descritor = os.open(caminho, os.O_RDONLY)
        try:
            # Leituras podem ser parciais; o laço tem tamanho e número limitados.
            partes: list[bytes] = []
            for _ in range(6):
                trecho = os.read(descritor, 5)
                if not trecho:
                    break
                partes.append(trecho)
            else:
                raise RuntimeError("Fim do arquivo próprio não observado.")
            conteudo = b"".join(partes)
            if conteudo != b"Livro":
                raise RuntimeError("O arquivo próprio apresentou conteúdo inesperado.")

            try:
                os.write(descritor, b"X")
            except OSError as erro:
                if erro.errno != errno.EBADF:
                    raise
                escrita = errno.errorcode[erro.errno]
            else:
                raise RuntimeError("A escrita não foi recusada como previsto.")
        finally:
            os.close(descritor)

        try:
            outro = os.open(Path(pasta) / "ausente.txt", os.O_RDONLY)
        except OSError as erro:
            if erro.errno != errno.ENOENT:
                raise
            ausente = errno.errorcode[erro.errno]
        else:
            os.close(outro)
            raise RuntimeError("O nome reservado ao exemplo de ausência existe.")

        preservado = caminho.read_bytes() == b"Livro"
        if not preservado:
            raise RuntimeError("O conteúdo do arquivo foi alterado.")
        return {
            "leitura": conteudo.decode("ascii"),
            "fim_da_leitura": 0,
            "escrita": escrita,
            "ausente": ausente,
            "conteudo_preservado": "sim",
        }


def main() -> int:
    try:
        resultado = observar()
    except (OSError, RuntimeError) as erro:
        print(f"Exemplo não concluído: {erro}", file=sys.stderr)
        return 1
    for nome, valor in resultado.items():
        print(f"{nome}={valor}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
