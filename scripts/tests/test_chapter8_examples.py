"""Conferência de exemplos autorais do capítulo 8, sem alvos externos.

Requisitos para a parte C: Linux, GCC e biblioteca C de desenvolvimento.
São executados somente programas presentes no próprio capítulo, em temporários.
"""
# SPDX-License-Identifier: MIT
from __future__ import annotations

import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import types
import unittest

ROOT = Path(__file__).resolve().parents[2]
SOURCES = ROOT / "book/modulo-2/capitulo-8/exemplos"
GCC = shutil.which("gcc")


def run(args: list[str], cwd: Path, *, check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, cwd=cwd, capture_output=True, text=True,
                          timeout=30, check=check, env={**os.environ, "LC_ALL": "C"})


def elf_type(path: Path) -> int:
    data = path.read_bytes()
    if len(data) < 18 or data[:4] != b"\x7fELF" or data[5] not in (1, 2):
        raise ValueError(f"Cabeçalho ELF não reconhecido: {path.name}")
    order = "little" if data[5] == 1 else "big"
    return int.from_bytes(data[16:18], order)


@unittest.skipUnless(sys.platform.startswith("linux") and GCC, "Requer Linux e GCC")
class Chapter8NativeExamples(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.temp = tempfile.TemporaryDirectory(prefix="hacking-ch8-")
        cls.addClassCleanup(cls.temp.cleanup)
        cls.work = Path(cls.temp.name)
        for name in ("principal.c", "acervo.c", "acervo.h"):
            shutil.copyfile(SOURCES / name, cls.work / name)
        cls.flags = [str(GCC), "-std=c17", "-Wall", "-Wextra", "-Werror"]
        run(cls.flags + ["-E", "principal.c", "-o", "principal.i"], cls.work)
        run(cls.flags + ["-S", "principal.c", "-o", "principal.s"], cls.work)
        run(cls.flags + ["-c", "principal.c", "-o", "principal.o"], cls.work)
        run(cls.flags + ["-c", "acervo.c", "-o", "acervo.o"], cls.work)
        run([str(GCC), "principal.o", "acervo.o", "-o", "catalogo"], cls.work)

    def test_preprocessing_and_assembly_are_distinct_artifacts(self) -> None:
        preprocessed = (self.work / "principal.i").read_text()
        self.assertIn("total_exemplares", preprocessed)
        self.assertNotIn('#include "acervo.h"', preprocessed)
        self.assertGreater((self.work / "principal.s").stat().st_size, 0)
        self.assertFalse((self.work / "principal.s").read_bytes().startswith(b"\x7fELF"))

    def test_relocatable_object_and_executable_have_different_roles(self) -> None:
        self.assertEqual(elf_type(self.work / "principal.o"), 1)  # ET_REL
        self.assertIn(elf_type(self.work / "catalogo"), (2, 3))  # ET_EXEC ou PIE/ET_DYN

    def test_missing_definition_fails_at_link_time(self) -> None:
        result = run([str(GCC), "principal.o", "-o", "incompleto"], self.work, check=False)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("total_exemplares", result.stderr)

    def test_output_is_not_the_exit_status(self) -> None:
        result = run([str(self.work / "catalogo")], self.work)
        self.assertEqual(result.stdout, "Exemplares: 5\n")
        self.assertEqual(result.stderr, "")
        self.assertEqual(result.returncode, 0)

    def test_source_edit_requires_a_new_build(self) -> None:
        with tempfile.TemporaryDirectory(dir=self.work) as directory:
            changed = Path(directory)
            for name in ("principal.c", "acervo.c", "acervo.h", "catalogo"):
                shutil.copy2(self.work / name, changed / name)
            path = changed / "acervo.c"
            path.write_text(path.read_text().replace("2 + 3", "2 + 7"))
            self.assertEqual(run([str(changed / "catalogo")], changed).stdout,
                             "Exemplares: 5\n")
            run(self.flags + ["principal.c", "acervo.c", "-o", "catalogo"], changed)
            self.assertEqual(run([str(changed / "catalogo")], changed).stdout,
                             "Exemplares: 9\n")

    def test_filename_suffix_does_not_rewrite_the_binary(self) -> None:
        renamed = self.work / "catalogo.txt"
        shutil.copy2(self.work / "catalogo", renamed)
        self.assertEqual(renamed.read_bytes(), (self.work / "catalogo").read_bytes())
        self.assertEqual(run([str(renamed)], self.work).stdout, "Exemplares: 5\n")


class Chapter8RuntimeExamples(unittest.TestCase):
    def test_compilation_does_not_execute_the_assignment(self) -> None:
        scope: dict[str, object] = {}
        code = compile("total = 2 + 3", "<exemplo-autoral>", "exec")
        self.assertIsInstance(code, types.CodeType)
        self.assertNotIn("total", scope)
        exec(code, scope)  # Somente a string constante acima; nunca entrada externa.
        self.assertEqual(scope["total"], 5)

    def test_same_code_can_operate_on_distinct_state(self) -> None:
        code = compile("contador = contador + 1", "<estado-autoral>", "exec")
        first: dict[str, object] = {"contador": 4}
        second: dict[str, object] = {"contador": 4}
        exec(code, first)
        exec(code, second)
        exec(code, first)
        self.assertEqual((first["contador"], second["contador"]), (6, 5))
        # Namespaces separados não simulam nem comprovam isolamento de processos.

    def test_arguments_environment_and_working_directory_are_inputs(self) -> None:
        code = ('import json, os, sys; '
                'print(json.dumps([sys.argv[1], os.environ["CH8_MODO"], os.getcwd()]))')
        with tempfile.TemporaryDirectory(prefix="hacking-context-") as directory:
            result = subprocess.run(
                [sys.executable, "-I", "-c", code, "resumo"],
                cwd=directory, env={**os.environ, "CH8_MODO": "estudo"},
                capture_output=True, text=True, check=True, timeout=15)
            mode, environment, cwd = json.loads(result.stdout)
            self.assertEqual((mode, environment), ("resumo", "estudo"))
            self.assertEqual(Path(cwd).resolve(), Path(directory).resolve())


if __name__ == "__main__":
    unittest.main()
