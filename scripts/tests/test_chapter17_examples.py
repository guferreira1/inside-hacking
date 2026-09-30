"""Observações reais limitadas a processos próprios; sem teste de escape ou VM."""
from contextlib import redirect_stdout, redirect_stderr
import importlib.util
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import unittest
from unittest import mock

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / 'book/modulo-3/capitulo-17/exemplos/namespaces_proprios.py'
spec = importlib.util.spec_from_file_location('ch17_namespaces', SCRIPT)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


class Chapter17Contracts(unittest.TestCase):
    def test_platform_is_checked_before_opening(self):
        with mock.patch.object(m.sys, 'platform', 'unsupported'), mock.patch.object(m.os, 'open') as op:
            with self.assertRaises(m.ObservationUnavailable):
                with m.pinned_snapshot():
                    self.fail('must not yield')
            op.assert_not_called()

    def test_incomplete_or_invalid_payload_is_rejected(self):
        good = {'pid': 12, 'namespaces': {k: [4, 20] for k in m.KINDS}}
        self.assertEqual(m.validate_snapshot(good), good)
        for bad in ({}, {'pid': True, 'namespaces': good['namespaces']},
                    {'pid': 12, 'namespaces': {}},
                    {'pid': 12, 'namespaces': {k: [4, 0] for k in m.KINDS}}):
            with self.subTest(bad=bad), self.assertRaises(m.ObservationUnavailable):
                m.validate_snapshot(bad)

    def test_failure_has_no_success_output(self):
        out, err = io.StringIO(), io.StringIO()
        with mock.patch.object(m, 'observe', side_effect=PermissionError), redirect_stdout(out), redirect_stderr(err):
            status = m.main([])
        self.assertEqual(status, 2)
        self.assertEqual(out.getvalue(), '')
        self.assertIn('indisponível', err.getvalue())

    def test_external_arguments_are_not_accepted(self):
        with mock.patch.object(m, 'observe') as obs, redirect_stderr(io.StringIO()):
            self.assertEqual(m.main(['/outro/processo']), 2)
        obs.assert_not_called()


@unittest.skipUnless(sys.platform == 'linux', 'observação requer Linux')
class Chapter17Linux(unittest.TestCase):
    def track_opens(self):
        opened = []
        real_open = os.open
        def tracked(*args, **kwargs):
            fd = real_open(*args, **kwargs)
            opened.append(fd)
            return fd
        return opened, tracked

    def assert_closed(self, fds):
        for fd in fds:
            with self.assertRaises(OSError):
                os.fstat(fd)

    def test_handles_remain_open_until_snapshot_ends(self):
        opened, tracked = self.track_opens()
        with mock.patch.object(m.os, 'open', side_effect=tracked):
            with m.pinned_snapshot() as snap:
                self.assertEqual(snap['pid'], os.getpid())
                self.assertEqual(len(opened), len(m.KINDS))
                for fd in opened:
                    self.assertGreater(os.fstat(fd).st_ino, 0)
            self.assert_closed(opened)

    def test_partial_open_failure_releases_previous_handles(self):
        opened, tracked = self.track_opens()
        def failing(path, flags):
            if path.endswith('/user'):
                raise PermissionError('falha injetada somente no teste')
            return tracked(path, flags)
        with mock.patch.object(m.os, 'open', side_effect=failing):
            with self.assertRaises(PermissionError):
                with m.pinned_snapshot():
                    self.fail('must not yield')
        self.assertEqual(len(opened), 2)
        self.assert_closed(opened)

    def test_real_child_is_distinct_and_shares_observed_namespaces(self):
        result = m.observe()
        self.assertTrue(result['processos_distintos'])
        self.assertEqual(result['namespaces_comparados'], 6)
        self.assertEqual(result['mesmo_namespace'], {k: True for k in m.KINDS})

    def test_independent_cli_emits_only_the_bounded_comparison(self):
        proc = subprocess.run([sys.executable, '-I', '-S', str(SCRIPT)], capture_output=True, text=True, timeout=10)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        value = json.loads(proc.stdout)
        self.assertEqual(set(value), {'processos_distintos', 'namespaces_comparados', 'mesmo_namespace'})
        self.assertTrue(value['processos_distintos'])
        self.assertTrue(all(value['mesmo_namespace'].values()))
        self.assertEqual(proc.stderr, '')

    def test_timeout_closes_parent_handles(self):
        opened, tracked = self.track_opens()
        with mock.patch.object(m.os, 'open', side_effect=tracked), mock.patch.object(m.subprocess, 'run', side_effect=subprocess.TimeoutExpired('filho', 5)):
            with self.assertRaises(subprocess.TimeoutExpired):
                m.observe()
        self.assertEqual(len(opened), 6)
        self.assert_closed(opened)


if __name__ == '__main__':
    unittest.main()
