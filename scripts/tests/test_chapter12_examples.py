"""Verificações delimitadas de procfs; não alteram montagens ou serviços."""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
EXAMPLE = ROOT / "book/modulo-3/capitulo-12/exemplos/proc_proprio.py"
SPEC = spec_from_file_location("chapter12_proc_proprio", EXAMPLE)
assert SPEC is not None and SPEC.loader is not None
EX = module_from_spec(SPEC)
SPEC.loader.exec_module(EX)


class Chapter12Environment(unittest.TestCase):
    def test_platform_requirement_is_explicit(self):
        with patch.object(EX.sys, "platform", "not-linux"):
            with self.assertRaises(EX.AmbienteIndisponivel):
                EX.examinar()


@unittest.skipUnless(sys.platform == "linux" and Path("/proc/self/fd").is_dir(), "requires Linux/procfs")
class Chapter12Procfs(unittest.TestCase):
    def test_descriptor_view_and_cleanup(self):
        with TemporaryDirectory() as base:
            result = EX.examinar(Path(base))
            self.assertEqual(result, {
                "entrada_link": True,
                "mesmo_arquivo_regular": True,
                "conteudo": b"Livro\n",
                "bytes_lidos": 6,
            })
            self.assertEqual(list(Path(base).iterdir()), [])

    def test_cleanup_after_proc_access_failure(self):
        with TemporaryDirectory() as base:
            with patch.object(EX, "os") as sistema:
                sistema.fstat.side_effect = PermissionError("synthetic denial")
                with self.assertRaises(EX.AmbienteIndisponivel):
                    EX.examinar(Path(base))
            self.assertEqual(list(Path(base).iterdir()), [])

    def test_documented_output_in_separate_process(self):
        result = subprocess.run([sys.executable, "-I", "-S", str(EXAMPLE)],
                                capture_output=True, text=True, timeout=10, check=False)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stderr, "")
        self.assertEqual(result.stdout, "entrada_em_proc=link\ndestino=mesmo_arquivo_regular\nleitura=Livro\nbytes_lidos=6\n")


if __name__ == "__main__":
    unittest.main()
