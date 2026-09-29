"""Examples from chapter 14: own strings and disposable local files only.

Bash is exercised on Linux. PowerShell tests require an actual pwsh 7 runtime.
An absent runtime is reported as SKIP, never as a successful reproduction.
"""
from __future__ import annotations
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
EXAMPLES = ROOT / 'book/modulo-3/capitulo-14/exemplos'
BASH = shutil.which('bash') if sys.platform.startswith('linux') else None
PWSH = shutil.which('pwsh')

class Workspace(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='inside-hacking-ch14-')
        self.addCleanup(self.temp.cleanup)
        self.cwd = Path(self.temp.name)

    def run_bash(self, code: str, *args: str):
        environment = {'PATH': os.defpath, 'HOME': str(self.cwd), 'LC_ALL': 'C.UTF-8'}
        return subprocess.run([BASH, '--noprofile', '--norc', '-c', code, 'chapter14', *args],
                              cwd=self.cwd, env=environment, capture_output=True,
                              text=True, encoding='utf-8', timeout=10, check=False)

    def run_ps(self, code: str, *, values=None):
        environment = os.environ.copy()
        environment['CH14_EXAMPLES'] = str(EXAMPLES)
        environment['CH14_WORKSPACE'] = str(self.cwd)
        environment['CH14_VALUES'] = json.dumps(values if values is not None else [])
        return subprocess.run([PWSH, '-NoLogo', '-NoProfile', '-NonInteractive', '-Command', code],
                              cwd=self.cwd, env=environment, capture_output=True,
                              text=True, encoding='utf-8', timeout=30, check=False)

@unittest.skipUnless(BASH, 'Requires Bash on Linux; not a Windows Bash compatibility claim.')
class Chapter14Bash(Workspace):
    def test_argument_boundaries_and_empty_argument(self):
        script = str(EXAMPLES / 'argumentos.bash')
        r = self.run_bash('arquivo="catalogo de teste.txt"; bash "$1" $arquivo; bash "$1" "$arquivo"; bash "$1" ""', script)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(r.stdout, 'quantidade=3\n<catalogo>\n<de>\n<teste.txt>\nquantidade=1\n<catalogo de teste.txt>\nquantidade=1\n<>\n')

    def test_single_and_double_quotes(self):
        r = self.run_bash('arquivo=Aurora; printf "%s\\n" \'$arquivo\' "$arquivo"')
        self.assertEqual(r.stdout, '$arquivo\nAurora\n')

    def test_glob_and_literal_are_distinct(self):
        (self.cwd / 'a.txt').write_text('own fixture')
        (self.cwd / 'b.txt').write_text('own fixture')
        r = self.run_bash('bash "$1" *.txt; bash "$1" \'*.txt\'', str(EXAMPLES / 'argumentos.bash'))
        self.assertEqual(r.stdout, 'quantidade=2\n<a.txt>\n<b.txt>\nquantidade=1\n<*.txt>\n')

    def test_expanded_data_is_not_reparsed_as_shell_code(self):
        r = self.run_bash('rotulo=\'Aurora; revisao\'; printf "%s\\n" "$rotulo"')
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(r.stdout, 'Aurora; revisao\n')
        self.assertEqual(r.stderr, '')

    def test_array_keeps_each_argument(self):
        r = self.run_bash('argumentos=("catalogo de teste.txt" "*.txt"); bash "$1" "${argumentos[@]}"', str(EXAMPLES / 'argumentos.bash'))
        self.assertEqual(r.stdout, 'quantidade=2\n<catalogo de teste.txt>\n<*.txt>\n')

    def test_redirection_order(self):
        r = self.run_bash('emitir() { printf "registro\\n"; printf "aviso\\n" >&2; }; emitir > conjunto.txt 2>&1; emitir 2>&1 > apenas-saida.txt')
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual((self.cwd/'conjunto.txt').read_text(), 'registro\naviso\n')
        self.assertEqual((self.cwd/'apenas-saida.txt').read_text(), 'registro\n')
        self.assertEqual(r.stdout, 'aviso\n')
        self.assertEqual(r.stderr, '')

    def test_redirection_can_truncate_before_failure(self):
        p = self.cwd/'own.txt'
        p.write_text('own temporary content')
        r = self.run_bash('false > own.txt')
        self.assertNotEqual(r.returncode, 0)
        self.assertEqual(p.read_bytes(), b'')

    def test_pipeline_and_component_statuses(self):
        r = self.run_bash('set +o pipefail; false | true; printf "%s\\n" "$?"; set -o pipefail; false | true; printf "%s:%s:%s\\n" "$?" "${PIPESTATUS[0]}" "${PIPESTATUS[1]}"')
        self.assertEqual(r.stdout, '0\n1:1:0\n')

    def test_capture_status_before_new_command(self):
        r = self.run_bash('false; estado=$?; printf "estado=%s\\n" "$estado"')
        self.assertEqual(r.stdout, 'estado=1\n')
        self.assertEqual(r.returncode, 0)

    def test_explicit_if_checks_its_write(self):
        r = self.run_bash('if printf "%s\\n" Aurora > resultado.txt; then printf "%s\\n" "escrita concluida"; else estado=$?; printf "falha de escrita: %s\\n" "$estado" >&2; fi')
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(r.stdout, 'escrita concluida\n')
        self.assertEqual((self.cwd/'resultado.txt').read_text(), 'Aurora\n')

    def test_errexit_does_not_replace_condition_logic(self):
        r = self.run_bash('set -e; if false; then printf "nao\\n"; else printf "tratado\\n"; fi; printf "continua\\n"')
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(r.stdout, 'tratado\ncontinua\n')

    def test_command_substitution_removes_trailing_newlines(self):
        r = self.run_bash('nome=$(printf "Aurora\\n\\n"); printf "<%s>\\n" "$nome"')
        self.assertEqual(r.stdout, '<Aurora>\n')

    def test_child_and_source_have_different_scope(self):
        (self.cwd/'contexto.bash').write_text('rotulo=filho\n')
        r = self.run_bash('rotulo=pai; bash ./contexto.bash; printf "%s\\n" "$rotulo"; . ./contexto.bash; printf "%s\\n" "$rotulo"')
        self.assertEqual(r.stdout, 'pai\nfilho\n')

    def test_only_exported_variable_is_inherited(self):
        r = self.run_bash('rotulo=Aurora; bash -c \'printf "<%s>\\n" "${rotulo-nao_exportado}"\'; export rotulo; bash -c \'printf "<%s>\\n" "$rotulo"\'')
        self.assertEqual(r.stdout, '<nao_exportado>\n<Aurora>\n')

    def test_summary_valid_and_limit(self):
        script = str(EXAMPLES/'resumo-estados.bash')
        r = self.run_bash('bash "$1" "${@:2}"', script, 'disponivel','emprestado','disponivel')
        self.assertEqual(r.stdout, 'disponiveis=2\nemprestados=1\n')
        self.assertEqual(r.returncode, 0, r.stderr)
        r = self.run_bash('bash "$1" "${@:2}"', script, *(['disponivel']*256))
        self.assertEqual(r.stdout, 'disponiveis=256\nemprestados=0\n')
        self.assertEqual(r.returncode, 0, r.stderr)

    def test_summary_rejects_without_partial_output(self):
        script = str(EXAMPLES/'resumo-estados.bash')
        for values in [[], ['DISPONIVEL'], [''], ['disponivel', 'em revisao'], ['disponivel']*257]:
            with self.subTest(size=len(values),first=values[:2]):
                r = self.run_bash('bash "$1" "${@:2}"', script, *values)
                self.assertEqual(r.returncode, 2)
                self.assertEqual(r.stdout, '')
                self.assertTrue(r.stderr)

    def test_script_syntax(self):
        for p in EXAMPLES.glob('*.bash'):
            r = self.run_bash('bash -n "$1"',str(p))
            self.assertEqual(r.returncode, 0, r.stderr)

@unittest.skipUnless(PWSH, 'Requires an actual PowerShell 7 runtime (pwsh).')
class Chapter14PowerShell(Workspace):
    def test_argument_collection_preserves_literals(self):
        r = self.run_ps("$a = & (Join-Path $env:CH14_EXAMPLES Argumentos.ps1) -Valores @('catalogo de teste.txt','*.txt',''); $a | ConvertTo-Json -Compress")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(json.loads(r.stdout), {'Quantidade':3,'Valores':['catalogo de teste.txt','*.txt','']})

    def test_literal_and_interpolated_strings(self):
        r = self.run_ps("$arquivo='Aurora'; @('$arquivo',\"$arquivo\") | ConvertTo-Json -Compress")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(json.loads(r.stdout), ['$arquivo','Aurora'])

    def test_object_pipeline_uses_properties(self):
        r = self.run_ps("$livros=@([pscustomobject]@{Titulo='Redes';Paginas=120};[pscustomobject]@{Titulo='Sistemas';Paginas=240}); $livros | Where-Object {$_.Paginas -ge 200} | Select-Object Titulo,Paginas | ConvertTo-Json -Compress")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(json.loads(r.stdout), {'Titulo':'Sistemas','Paginas':240})

    def test_error_action_stop_enters_catch(self):
        r = self.run_ps("try {Get-Item -LiteralPath (Join-Path $env:CH14_WORKSPACE ausente) -ErrorAction Stop; 'nao'} catch {'tratado'}")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(r.stdout.strip(), 'tratado')

    def test_summary_valid_and_limit(self):
        code = "$v=@(ConvertFrom-Json $env:CH14_VALUES); & (Join-Path $env:CH14_EXAMPLES Resumo-Estados.ps1) -Estados $v | ConvertTo-Json -Compress"
        for values, expected in [(['disponivel','emprestado','disponivel'],{'Disponiveis':2,'Emprestados':1}), (['disponivel']*256,{'Disponiveis':256,'Emprestados':0})]:
            with self.subTest(size=len(values)):
                r = self.run_ps(code,values=values)
                self.assertEqual(r.returncode, 0, r.stderr)
                self.assertEqual(json.loads(r.stdout), expected)

    def test_invalid_summary_raises_no_partial_object(self):
        code = "$v=@(ConvertFrom-Json $env:CH14_VALUES); try {& (Join-Path $env:CH14_EXAMPLES Resumo-Estados.ps1) -Estados $v | ConvertTo-Json -Compress; exit 0} catch {[Console]::Error.WriteLine('rejeitado'); exit 2}"
        for values in [[],['DISPONIVEL'],[''],['disponivel','em revisao'],['disponivel']*257]:
            with self.subTest(size=len(values),first=values[:2]):
                r = self.run_ps(code,values=values)
                self.assertEqual(r.returncode, 2, r.stderr)
                self.assertEqual(r.stdout, '')
                self.assertIn('rejeitado',r.stderr)

    def test_literal_path_with_brackets(self):
        (self.cwd/'[a].txt').write_text('own fixture',encoding='utf-8')
        r = self.run_ps("Get-Content -LiteralPath (Join-Path $env:CH14_WORKSPACE '[a].txt') -Raw -ErrorAction Stop")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(r.stdout.strip(),'own fixture')

    def test_dot_sourcing_scope(self):
        (self.cwd/'scope.ps1').write_text("$rotulo='filho'\n",encoding='utf-8')
        r = self.run_ps("$rotulo='pai'; & (Join-Path $env:CH14_WORKSPACE scope.ps1); $antes=$rotulo; . (Join-Path $env:CH14_WORKSPACE scope.ps1); @($antes,$rotulo) | ConvertTo-Json -Compress")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(json.loads(r.stdout),['pai','filho'])

    def test_native_parser_accepts_scripts(self):
        r = self.run_ps("$falhas=0; Get-ChildItem -LiteralPath $env:CH14_EXAMPLES -Filter '*.ps1' | ForEach-Object {$t=$null;$e=$null;[void][System.Management.Automation.Language.Parser]::ParseFile($_.FullName,[ref]$t,[ref]$e);$falhas+=$e.Count}; if($falhas -gt 0){throw 'syntax errors'}; 'ok'")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(r.stdout.strip(),'ok')

if __name__ == '__main__':
    unittest.main()
