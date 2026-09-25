"""Conferências delimitadas de formato, transformação e arquivos; licença MIT."""
import base64
import csv
import gzip
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import struct
import sys
import tempfile
import unicodedata
import unittest
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[2]
ARQUIVO = ROOT / "book/modulo-2/capitulo-10/exemplos/registro.py"
SPEC = importlib.util.spec_from_file_location("chapter10_registro", ARQUIVO)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("exemplo do capítulo 10 não localizado")
MOD = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MOD
SPEC.loader.exec_module(MOD)


class Chapter10Formats(unittest.TestCase):
    def setUp(self):
        self.registro = MOD.Registro("Livro", 3)
        self.dados = bytes.fromhex("41 55 52 01 00 05 00 03 4C 69 76 72 6F")

    def test_exact_binary_layout(self):
        self.assertEqual(MOD.CABECALHO.size, 8)
        self.assertEqual(MOD.codificar_binario(self.registro), self.dados)
        self.assertEqual(len(self.dados), 13)
        self.assertEqual(MOD.decodificar_binario(self.dados), self.registro)

    def test_title_length_is_utf8_bytes(self):
        registro = MOD.Registro("é", 3)
        dados = MOD.codificar_binario(registro)
        self.assertEqual(dados[4:6], b"\x00\x02")
        self.assertEqual(dados[8:], b"\xc3\xa9")
        self.assertEqual(MOD.decodificar_binario(dados), registro)

    def test_all_truncated_prefixes_are_rejected(self):
        for tamanho in range(len(self.dados)):
            with self.subTest(tamanho=tamanho), self.assertRaises(MOD.FormatoInvalido):
                MOD.decodificar_binario(self.dados[:tamanho])

    def test_extra_bytes_are_not_silently_ignored(self):
        with self.assertRaises(MOD.FormatoInvalido):
            MOD.decodificar_binario(self.dados + b"\x00")

    def test_signature_and_version_are_checked(self):
        for dados in (b"XYZ" + self.dados[3:], self.dados[:3] + b"\x02" + self.dados[4:]):
            with self.assertRaises(MOD.FormatoInvalido):
                MOD.decodificar_binario(dados)

    def test_declared_length_is_not_trusted(self):
        for tamanho in (0, 4, 6, 81, 65535):
            dados = self.dados[:4] + struct.pack(">H", tamanho) + self.dados[6:]
            with self.subTest(tamanho=tamanho), self.assertRaises(MOD.FormatoInvalido):
                MOD.decodificar_binario(dados)

    def test_invalid_utf8_is_not_repaired(self):
        dados = MOD.CABECALHO.pack(b"AUR", 1, 1, 3) + b"\xff"
        with self.assertRaises(MOD.FormatoInvalido):
            MOD.decodificar_binario(dados)

    def test_title_boundaries(self):
        for titulo in ("a", "a" * 80, "é" * 40):
            registro = MOD.Registro(titulo, 3)
            self.assertEqual(MOD.decodificar_binario(MOD.codificar_binario(registro)), registro)
        for titulo in ("", "a" * 81, "é" * 41, "\ud800", None):
            with self.assertRaises(MOD.FormatoInvalido):
                MOD.codificar_binario(MOD.Registro(titulo, 3))

    def test_quantity_domain_and_type(self):
        for quantidade in (0, 1000):
            registro = MOD.Registro("Livro", quantidade)
            self.assertEqual(MOD.decodificar_binario(MOD.codificar_binario(registro)), registro)
        for quantidade in (-1, 1001, True, 3.0, "3", None):
            with self.assertRaises(MOD.FormatoInvalido):
                MOD.codificar_binario(MOD.Registro("Livro", quantidade))
        dados = MOD.CABECALHO.pack(b"AUR", 1, 5, 1001) + b"Livro"
        with self.assertRaises(MOD.FormatoInvalido):
            MOD.decodificar_binario(dados)

    def test_json_round_trip_and_literal_output(self):
        self.assertEqual(MOD.codificar_json(self.registro), b'{"titulo":"Livro","quantidade":3}')
        for registro in (self.registro, MOD.Registro("Aé🔒", 10)):
            self.assertEqual(MOD.decodificar_json(MOD.codificar_json(registro)), registro)

    def test_json_duplicate_names_including_escape(self):
        casos = [b'{"titulo":"Livro","quantidade":3,"quantidade":7}',
                 br'{"titulo":"Livro","quantidade":3,"\u0071uantidade":7}']
        for dados in casos:
            with self.assertRaises(MOD.FormatoInvalido):
                MOD.decodificar_json(dados)

    def test_json_shape_types_and_trailing_data(self):
        casos = [b'null', b'[]', b'{"titulo":"Livro"}',
                 b'{"titulo":"Livro","quantidade":3,"extra":0}',
                 b'{"titulo":"Livro","quantidade":true}',
                 b'{"titulo":"Livro","quantidade":"3"}',
                 b'{"titulo":"Livro","quantidade":3.0}',
                 b'{"titulo":"Livro","quantidade":3e0}',
                 b'{"titulo":null,"quantidade":3}',
                 b'{"titulo":"Livro","quantidade":3} {}']
        for dados in casos:
            with self.subTest(dados=dados), self.assertRaises(MOD.FormatoInvalido):
                MOD.decodificar_json(dados)

    def test_json_constants_unicode_and_size(self):
        for numero in (b'NaN', b'Infinity', b'-Infinity'):
            with self.assertRaises(MOD.FormatoInvalido):
                MOD.decodificar_json(b'{"titulo":"Livro","quantidade":' + numero + b'}')
        for dados in (b'\xff', b' ' * 4097, br'{"titulo":"\ud800","quantidade":3}',
                      b'\xef\xbb\xbf' + MOD.codificar_json(self.registro)):
            with self.assertRaises(MOD.FormatoInvalido):
                MOD.decodificar_json(dados)

    def test_wrong_api_inputs_are_rejected(self):
        for entrada in ("Livro", bytearray(self.dados), None):
            for funcao in (MOD.decodificar_binario, MOD.decodificar_json):
                with self.assertRaises(MOD.FormatoInvalido):
                    funcao(entrada)


class Chapter10Transformations(unittest.TestCase):
    def test_base64_groups_padding_and_round_trip(self):
        self.assertEqual(base64.b64encode(b"ABC"), b"QUJD")
        self.assertEqual(base64.b64encode(b"Livro"), b"TGl2cm8=")
        for n in range(10):
            dados = b"a" * n
            codificado = base64.b64encode(dados)
            self.assertEqual(len(codificado), 4 * ((n + 2) // 3))
            self.assertEqual(base64.b64decode(codificado, validate=True), dados)

    def test_percent_decoding_layers_differ(self):
        uma = unquote("A%2520B")
        self.assertEqual(uma, "A%20B")
        self.assertEqual(unquote(uma), "A B")

    def test_unicode_equivalence_is_not_byte_identity(self):
        a, b = "é", "e\u0301"
        self.assertNotEqual(a.encode("utf-8"), b.encode("utf-8"))
        self.assertEqual(unicodedata.normalize("NFC", a), unicodedata.normalize("NFC", b))

    def test_text_io_can_translate_line_endings(self):
        dados = b"A\r\nB\n"
        with io.TextIOWrapper(io.BytesIO(dados), encoding="utf-8", newline=None) as texto:
            self.assertEqual(texto.read(), "A\nB\n")
        self.assertEqual(len(dados), 5)

    def test_json_equivalent_values_can_have_different_bytes(self):
        a = b'{"titulo":"Livro","quantidade":3}'
        b = b'{ "quantidade": 3, "titulo": "Livro" }'
        self.assertEqual(json.loads(a), json.loads(b))
        self.assertNotEqual(a, b)
        self.assertNotEqual(hashlib.sha256(a).digest(), hashlib.sha256(b).digest())

    def test_default_json_policy_differs_from_our_profile(self):
        dados = b'{"titulo":"Livro","quantidade":3,"quantidade":7}'
        self.assertEqual(json.loads(dados)["quantidade"], 7)
        with self.assertRaises(MOD.FormatoInvalido):
            MOD.decodificar_json(dados)

    def test_csv_quotes_protect_a_delimiter(self):
        texto = 'titulo,quantidade\r\n"Redes, sistemas",3\r\n'
        linhas = list(csv.reader(io.StringIO(texto, newline="")))
        self.assertEqual(linhas, [["titulo", "quantidade"], ["Redes, sistemas", "3"]])
        self.assertEqual(len(texto.splitlines()[1].split(",")), 3)

    def test_gzip_round_trip_uses_only_small_known_data(self):
        dados = b"Livro\n" * 20
        self.assertEqual(gzip.decompress(gzip.compress(dados, mtime=0)), dados)


@unittest.skipUnless(sys.platform.startswith("linux"), "semântica de arquivos conferida no Linux")
class Chapter10Files(unittest.TestCase):
    def test_two_names_and_an_open_file_after_unlink(self):
        with tempfile.TemporaryDirectory() as diretorio:
            a = Path(diretorio) / "catalogo.txt"
            b = Path(diretorio) / "segundo-nome.bin"
            a.write_bytes(b"Livro")
            os.link(a, b)
            self.assertEqual((a.stat().st_dev, a.stat().st_ino),
                             (b.stat().st_dev, b.stat().st_ino))
            with a.open("rb", buffering=0) as aberto:
                a.unlink()
                b.unlink()
                self.assertFalse(a.exists())
                self.assertFalse(b.exists())
                self.assertEqual(aberto.read(), b"Livro")


if __name__ == "__main__":
    unittest.main()
