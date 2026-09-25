"""Formato didático AUR v1 e perfil JSON do capítulo 10; licença MIT.

A API recebe bytes já adquiridos: quem lê arquivos/rede deve limitar a entrada
antes de construí-los. Não é um parser universal nem uma sandbox.
"""
from dataclasses import dataclass
import json
import struct

CABECALHO = struct.Struct(">3sBHH")
MAGIA = b"AUR"
VERSAO = 1
MAX_TITULO = 80  # bytes UTF-8, não caracteres percebidos
MAX_QUANTIDADE = 1000
MAX_JSON = 4096


class FormatoInvalido(ValueError):
    """Entrada incompatível com o contrato didático."""


@dataclass(frozen=True)
class Registro:
    titulo: str
    quantidade: int


def validar(registro: Registro) -> bytes:
    if not isinstance(registro, Registro):
        raise FormatoInvalido("esperado um Registro")
    if type(registro.titulo) is not str:
        raise FormatoInvalido("titulo deve ser texto")
    try:
        titulo = registro.titulo.encode("utf-8", errors="strict")
    except UnicodeEncodeError as erro:
        raise FormatoInvalido("titulo não codificável em UTF-8") from erro
    if not 1 <= len(titulo) <= MAX_TITULO:
        raise FormatoInvalido("titulo deve ocupar de 1 a 80 bytes UTF-8")
    if type(registro.quantidade) is not int:
        raise FormatoInvalido("quantidade deve ser inteiro, não booleano")
    if not 0 <= registro.quantidade <= MAX_QUANTIDADE:
        raise FormatoInvalido("quantidade fora de 0 a 1000")
    return titulo


def codificar_binario(registro: Registro) -> bytes:
    titulo = validar(registro)
    return CABECALHO.pack(MAGIA, VERSAO, len(titulo), registro.quantidade) + titulo


def decodificar_binario(dados: bytes) -> Registro:
    if type(dados) is not bytes:
        raise FormatoInvalido("esperada uma sequência bytes")
    if not CABECALHO.size <= len(dados) <= CABECALHO.size + MAX_TITULO:
        raise FormatoInvalido("tamanho total incompatível")
    magia, versao, tamanho, quantidade = CABECALHO.unpack_from(dados)
    if magia != MAGIA or versao != VERSAO:
        raise FormatoInvalido("assinatura ou versão não reconhecida")
    if not 1 <= tamanho <= MAX_TITULO:
        raise FormatoInvalido("comprimento declarado fora do limite")
    if len(dados) != CABECALHO.size + tamanho:
        raise FormatoInvalido("conteúdo truncado ou bytes excedentes")
    try:
        titulo = dados[CABECALHO.size:].decode("utf-8", errors="strict")
    except UnicodeDecodeError as erro:
        raise FormatoInvalido("titulo não é UTF-8 válido") from erro
    registro = Registro(titulo, quantidade)
    validar(registro)
    return registro


def _pares_unicos(pares: list[tuple[str, object]]) -> dict[str, object]:
    objeto: dict[str, object] = {}
    for chave, valor in pares:
        if chave in objeto:
            raise FormatoInvalido("nome duplicado no objeto JSON")
        objeto[chave] = valor
    return objeto


def _rejeitar_constante(valor: str) -> None:
    raise FormatoInvalido("constante numérica fora do perfil JSON")


def codificar_json(registro: Registro) -> bytes:
    validar(registro)
    objeto = {"titulo": registro.titulo, "quantidade": registro.quantidade}
    texto = json.dumps(objeto, ensure_ascii=False, allow_nan=False, separators=(",", ":"))
    return texto.encode("utf-8")


def decodificar_json(dados: bytes) -> Registro:
    if type(dados) is not bytes or not 1 <= len(dados) <= MAX_JSON:
        raise FormatoInvalido("esperados de 1 a 4096 bytes JSON")
    try:
        texto = dados.decode("utf-8", errors="strict")
        objeto = json.loads(texto, object_pairs_hook=_pares_unicos,
                            parse_constant=_rejeitar_constante)
    except (UnicodeDecodeError, json.JSONDecodeError, RecursionError) as erro:
        raise FormatoInvalido("texto ou estrutura JSON inválida") from erro
    if type(objeto) is not dict or set(objeto) != {"titulo", "quantidade"}:
        raise FormatoInvalido("esperado objeto com titulo e quantidade, sem outros campos")
    registro = Registro(objeto["titulo"], objeto["quantidade"])
    validar(registro)
    return registro


def main() -> None:
    registro = Registro("Livro", 3)
    dados = codificar_binario(registro)
    print("binario:", dados.hex(" ").upper())
    print("json:", codificar_json(registro).decode("utf-8"))
    print("retorno:", decodificar_binario(dados))


if __name__ == "__main__":
    main()
