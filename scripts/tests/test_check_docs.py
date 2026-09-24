"""Synthetic fixtures for the supported Markdown/link subset; no network."""
import importlib.util
import tempfile
import unittest
from pathlib import Path

SPEC = importlib.util.spec_from_file_location('check_docs', Path(__file__).resolve().parents[1] / 'check_docs.py')
CHECK = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECK)


class DocumentationChecks(unittest.TestCase):
    def run_fixture(self, files):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for path, text in files.items():
                dest = root / path
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_text(text, encoding='utf-8')
            return CHECK.audit(root)

    def test_relative_and_explicit_anchors(self):
        result = self.run_fixture({'README.md': '[x](book/a.md#alvo)', 'book/a.md': '<a id="alvo"></a>\n# Título\n[voltar](../README.md)'})
        self.assertEqual(result['internal_errors'], [])

    def test_missing_target_and_anchor(self):
        result = self.run_fixture({'README.md': '[x](ausente.md)\n[y](#ausente)\n# Presente'})
        self.assertEqual({e['problem'] for e in result['internal_errors']}, {'missing target', 'missing anchor'})

    def test_fences_and_inline_code_are_not_navigation(self):
        result = self.run_fixture({'README.md': '```md\n[x](ausente.md)\n```\n`[y](ausente2.md)`\n<!-- [z](ausente3.md) -->'})
        self.assertEqual(result['internal_links'], 0)
        self.assertEqual(result['internal_errors'], [])

    def test_html_reference_and_duplicate_headings(self):
        result = self.run_fixture({'README.md': '<a href="a.md#seção-1">ir</a>\n[x][ref]\n[ref]: a.md#seção', 'a.md': '# Seção\n# Seção'})
        self.assertEqual(result['internal_errors'], [])

    def test_external_urls_are_inventory_only(self):
        result = self.run_fixture({'README.md': '[x](https://example.invalid/source)\nhttps://example.invalid/other'})
        self.assertEqual(len(result['external_urls']), 2)
        self.assertEqual(result['internal_errors'], [])

    def test_repository_escape_and_undefined_reference(self):
        result = self.run_fixture({'README.md': '[x](../fora.md)\n[y][faltou]'})
        self.assertEqual({e['problem'] for e in result['internal_errors']}, {'escapes repository', 'undefined reference'})


if __name__ == '__main__':
    unittest.main()
