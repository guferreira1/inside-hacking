"""Contas didáticas e um exemplo Linux limitado do capítulo 9."""
# SPDX-License-Identifier: MIT
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[2]


class Chapter9Examples(unittest.TestCase):
    def test_translation_in_two_contexts(self):
        page, offset = divmod(0x1234, 256)
        self.assertEqual((page, offset), (0x12, 0x34))
        self.assertEqual(0xA7 * 256 + offset, 0xA734)
        self.assertEqual(0x38 * 256 + offset, 0x3834)

    def test_page_boundary(self):
        self.assertEqual(divmod(0x12FF, 256), (0x12, 0xFF))
        self.assertEqual(divmod(0x1300, 256), (0x13, 0))

    def test_half_open_region(self):
        start, end = 0x4000, 0x5000
        self.assertEqual(end - start, 4096)
        self.assertTrue(start <= 0x4FFF < end)
        self.assertFalse(start <= 0x5000 < end)

    def test_virtual_resident_and_proportional_sizes(self):
        self.assertEqual(16 * 4096, 65536)
        self.assertEqual(4 * 4096, 16384)
        shared, private_a, private_b = 8192, 4096, 4096
        self.assertEqual((private_a + shared) + (private_b + shared), 24576)
        self.assertEqual(private_a + private_b + shared, 16384)
        self.assertEqual(private_a + shared / 2, 8192)

    def test_bounds_and_page_are_distinct(self):
        start, length, index = 0x4100, 16, 16
        address = start + index
        self.assertEqual(address, 0x4110)
        self.assertFalse(0 <= index < length)
        self.assertTrue(0x4000 <= address < 0x5000)

    def test_lost_update_is_an_explicit_model(self):
        # Simulação sequencial; não provoca uma data race em C ou Python.
        total = 5
        read_a = total
        read_b = total
        total = read_a + 1
        total = read_b + 1
        self.assertEqual(total, 6)
        self.assertEqual(5 + 1 + 1, 7)

    @unittest.skipUnless(sys.platform.startswith("linux"), "Exemplo requer Linux")
    def test_private_and_shared_mappings(self):
        script = ROOT / "book/modulo-2/capitulo-9/exemplos/privado_e_compartilhado.py"
        result = subprocess.run(
            [sys.executable, "-I", "-S", str(script)], capture_output=True, text=True,
            timeout=10, check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.splitlines(), ["privado=5", "compartilhado=9"])


if __name__ == "__main__":
    unittest.main()
