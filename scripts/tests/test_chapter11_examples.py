"""Conferências delimitadas do capítulo 11; não simulam um kernel."""
import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
EXAMPLE = ROOT / "book/modulo-3/capitulo-11/exemplos/pedidos.py"
spec = importlib.util.spec_from_file_location("chapter11_pedidos", EXAMPLE)
assert spec is not None and spec.loader is not None
pedidos = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pedidos)


@unittest.skipUnless(sys.platform.startswith("linux"), "Exemplo delimitado ao Linux")
class Chapter11Interfaces(unittest.TestCase):
    def test_resultados_das_operacoes_reais(self):
        self.assertEqual(pedidos.observar(), {
            "leitura": "Livro", "fim_da_leitura": 0,
            "escrita": "EBADF", "ausente": "ENOENT",
            "conteudo_preservado": "sim",
        })

    def test_execucao_independente_com_saida_literal(self):
        result = subprocess.run(
            [sys.executable, "-I", "-S", str(EXAMPLE)],
            capture_output=True, text=True, timeout=10, check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stderr, "")
        self.assertEqual(result.stdout,
            "leitura=Livro\nfim_da_leitura=0\nescrita=EBADF\n"
            "ausente=ENOENT\nconteudo_preservado=sim\n")

    def test_limpeza_da_pasta_temporaria(self):
        criadas = []
        original = tempfile.TemporaryDirectory
        with original(prefix="inside-hacking-c11-teste-") as base:
            def criar(**kwargs):
                obj = original(dir=base, **kwargs)
                criadas.append(Path(obj.name))
                return obj
            with patch.object(pedidos.tempfile, "TemporaryDirectory", side_effect=criar):
                pedidos.observar()
            self.assertEqual(len(criadas), 1)
            self.assertFalse(criadas[0].exists())
            self.assertEqual(list(Path(base).iterdir()), [])


class Chapter11Modelos(unittest.TestCase):
    def test_tempo_de_parede_nao_e_so_cpu(self):
        # Linha do tempo fictícia de 11.3, sem sobreposição de etapas.
        cpu = 4 + 3
        espera = 20
        fila = 5
        self.assertEqual(cpu + espera + fila, 32)
        self.assertEqual(cpu, 7)

    def test_abertura_no_so_e_autorizacao_do_leitor_sao_distintas(self):
        # Política inventada da narrativa; não consulta permissões reais.
        leituras_do_servico = {"historico-A", "historico-B"}
        permitido_ao_leitor = {"A": {"historico-A"}, "B": {"historico-B"}}
        self.assertIn("historico-B", leituras_do_servico)
        self.assertNotIn("historico-B", permitido_ao_leitor["A"])

    def test_espera_circular_do_modelo(self):
        # Duas tarefas mantêm recursos distintos e esperam sem liberar.
        detentor = {"catalogo": "A", "relatorio": "B"}
        espera_por = {"A": "relatorio", "B": "catalogo"}
        dependencia = {tarefa: detentor[recurso]
                       for tarefa, recurso in espera_por.items()}
        self.assertEqual(dependencia, {"A": "B", "B": "A"})


if __name__ == "__main__":
    unittest.main()
