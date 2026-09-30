import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
EX = ROOT / 'book/modulo-3/capitulo-16/exemplos'


def load(name):
    spec = importlib.util.spec_from_file_location(name, EX / (name + '.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


state = load('estado_proprio')
life = load('ciclo_proprio')


class Chapter16Lifecycle(unittest.TestCase):
    def test_ready_does_not_mean_finished(self):
        self.assertEqual(life.observar(), {'pronto':'pronto', 'ativo_antes_do_pedido':True,
                         'saida_final':'concluido', 'diagnostico':'', 'codigo':0})
    def test_child_error_is_not_hidden(self):
        result = life.observar('invalido\n')
        self.assertEqual(result['codigo'], 7)
        self.assertEqual(result['saida_final'], '')
        self.assertEqual(result['diagnostico'], 'pedido invalido')
    def test_lifecycle_cli(self):
        p = subprocess.run([sys.executable, '-I', str(EX/'ciclo_proprio.py')],
                           capture_output=True, text=True, timeout=20, check=True)
        self.assertTrue(json.loads(p.stdout)['ativo_antes_do_pedido'])
    def test_structured_log_preserves_a_newline_as_data(self):
        text = json.dumps({'mensagem':'primeira\nsegunda'}, ensure_ascii=False)
        self.assertEqual(len(text.splitlines()), 1)
        self.assertEqual(json.loads(text)['mensagem'], 'primeira\nsegunda')


class Chapter16State(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='test-cap16-')
        self.addCleanup(self.temp.cleanup)
        self.db = Path(self.temp.name) / 'estado.sqlite3'
        state.inicializar(self.db)
    def test_configuration_and_initial_state(self):
        con = state.conectar(self.db)
        try:
            self.assertEqual(con.execute('PRAGMA journal_mode').fetchone()[0], 'delete')
            self.assertEqual(con.execute('PRAGMA synchronous').fetchone()[0], 2)
        finally: con.close()
        self.assertEqual(state.consultar(self.db), {'total':0, 'aplicados':[]})
    def test_apply_once(self):
        self.assertEqual(state.aplicar(self.db,'lote-1',3), 'aplicado')
        self.assertEqual(state.consultar(self.db), {'total':3,'aplicados':[['lote-1',3]]})
    def test_repeat_is_idempotent_within_this_database(self):
        state.aplicar(self.db,'lote-1',3)
        self.assertEqual(state.aplicar(self.db,'lote-1',3), 'ja_aplicado')
        self.assertEqual(state.consultar(self.db)['total'], 3)
    def test_same_id_other_content_is_rejected(self):
        state.aplicar(self.db,'lote-1',3)
        with self.assertRaises(ValueError): state.aplicar(self.db,'lote-1',4)
        self.assertEqual(state.consultar(self.db)['total'],3)
    def test_two_distinct_jobs_are_not_duplicates(self):
        state.aplicar(self.db,'lote-1',3)
        state.aplicar(self.db,'lote-2',3)
        self.assertEqual(state.consultar(self.db)['total'],6)
    def test_invalid_inputs_leave_state_unchanged(self):
        for job, qty in [('bad',3),('lote-1',True),('lote-1',0),('lote-1',1001)]:
            with self.subTest(job=job,qty=qty), self.assertRaises(ValueError):
                state.aplicar(self.db,job,qty)
        self.assertEqual(state.consultar(self.db), {'total':0,'aplicados':[]})
    def test_process_dies_before_commit(self):
        p = state.tentativa(self.db,'lote-1',3,'antes')
        self.assertEqual(p.returncode,31)
        self.assertEqual(p.stdout,'')
        self.assertEqual(state.consultar(self.db), {'total':0,'aplicados':[]})
        self.assertEqual(state.aplicar(self.db,'lote-1',3), 'aplicado')
    def test_process_dies_after_commit_before_response(self):
        p = state.tentativa(self.db,'lote-1',3,'depois')
        self.assertEqual(p.returncode,32)
        self.assertEqual(p.stdout,'')
        self.assertEqual(state.consultar(self.db)['total'],3)
        self.assertEqual(state.aplicar(self.db,'lote-1',3), 'ja_aplicado')
        self.assertEqual(state.consultar(self.db)['total'],3)
    def test_demo_cli(self):
        p = subprocess.run([sys.executable,'-I',str(EX/'estado_proprio.py')],
                           capture_output=True,text=True,timeout=30,check=True)
        d = json.loads(p.stdout)
        self.assertEqual(d['antes_do_commit']['total'],0)
        self.assertEqual(d['depois_do_commit_sem_resposta']['total'],5)
        self.assertEqual(d['depois_da_repeticao'],d['depois_do_commit_sem_resposta'])
    def test_temporary_database_is_removed(self):
        with tempfile.TemporaryDirectory(prefix='cap16-clean-') as folder:
            p = Path(folder)/'estado.sqlite3'
            state.inicializar(p)
            state.aplicar(p,'lote-1',1)
        self.assertFalse(Path(folder).exists())


if __name__ == '__main__': unittest.main()
