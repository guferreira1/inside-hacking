"""Modelos numéricos separados de operações reais em arquivos Linux próprios."""
from __future__ import annotations

import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "book/modulo-3/capitulo-15/exemplos/permissoes_proprias.py"
spec = importlib.util.spec_from_file_location("chapter15_permissions", SCRIPT)
assert spec is not None and spec.loader is not None
example = importlib.util.module_from_spec(spec)
spec.loader.exec_module(example)
REASON = example.unsupported_reason()


class Chapter15Models(unittest.TestCase):
    def test_creation_masks_are_bitwise_not_subtraction(self):
        for requested, mask, expected in [(0o666, 0o022, 0o644),
            (0o666, 0o077, 0o600), (0o666, 0o027, 0o640),
            (0o777, 0o027, 0o750), (0o600, 0o022, 0o600)]:
            with self.subTest(requested=requested, mask=mask):
                self.assertEqual(requested & (~mask & 0o777), expected)

    def test_owner_class_is_not_a_union_with_other(self):
        mode = 0o046
        owner = (mode >> 6) & 7
        others = mode & 7
        self.assertEqual(owner, 0)
        self.assertEqual(others, 6)
        self.assertFalse(owner & 2)
        self.assertTrue(others & 2)

    def test_environment_guard_rejects_root_and_capabilities(self):
        with patch.object(example.sys, "platform", "linux"):
            with patch.object(example.os, "geteuid", return_value=0, create=True):
                self.assertIn("zero", example.unsupported_reason())
            with patch.object(example.os, "geteuid", return_value=1000, create=True):
                with patch.object(Path, "read_text", return_value="CapEff:\t0001\n"):
                    self.assertIn("capabilities", example.unsupported_reason())


@unittest.skipIf(REASON is not None, REASON or "ambiente indisponível")
class Chapter15Linux(unittest.TestCase):
    def test_readonly_content_and_name_have_different_controls(self):
        self.assertEqual(example.readonly_name(),
            {"escrita_recusada": True, "nome_removido": True})

    def test_chmod_does_not_close_our_existing_descriptor(self):
        self.assertEqual(example.open_before_change(),
            {"nova_abertura_recusada": True, "descritor_anterior_leu": True})

    def test_search_without_listing(self):
        self.assertEqual(example.directory_access(0o100),
            {"listagem_recusada": True, "nome_conhecido_lido": True})

    def test_listing_without_search(self):
        self.assertEqual(example.directory_access(0o400),
            {"nome_listado": True, "abertura_sem_busca_recusada": True})

    def test_cli_reports_only_completed_observations(self):
        result = subprocess.run([sys.executable, "-I", "-S", str(SCRIPT)],
            capture_output=True, text=True, timeout=10, check=True)
        data = json.loads(result.stdout)
        self.assertEqual(len(data), 4)
        self.assertTrue(all(v is True for group in data.values() for v in group.values()))
        self.assertEqual(result.stderr, "")

    def test_cleanup_after_success_and_injected_failure(self):
        with tempfile.TemporaryDirectory(prefix="aurora-test-parent-") as parent:
            with patch.object(tempfile, "tempdir", parent):
                example.directory_access(0o100)
                self.assertEqual(os.listdir(parent), [])
                with patch.object(example, "require_denied", side_effect=RuntimeError("simulada")):
                    with self.assertRaisesRegex(RuntimeError, "simulada"):
                        example.directory_access(0o100)
                self.assertEqual(os.listdir(parent), [])


if __name__ == "__main__":
    unittest.main()
