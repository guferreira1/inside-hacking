"""Exemplo didatico: efeito e identificador no MESMO banco e transacao.
O modo normal cria e remove seu proprio diretorio temporario.
Interrupcoes os._exit acontecem somente no worker filho de demonstracao.
"""
from __future__ import annotations
import json
import os
from pathlib import Path
import re
import sqlite3
import subprocess
import sys
import tempfile


def conectar(database: Path) -> sqlite3.Connection:
    con = sqlite3.connect(database, timeout=2, isolation_level=None)
    try:
        mode = con.execute('PRAGMA journal_mode=DELETE').fetchone()[0]
        con.execute('PRAGMA synchronous=FULL')
        if mode.lower() != 'delete' or con.execute('PRAGMA synchronous').fetchone()[0] != 2:
            raise RuntimeError('Configuracao SQLite inesperada.')
        return con
    except BaseException:
        con.close()
        raise


def inicializar(database: Path) -> None:
    con = conectar(database)
    try:
        con.executescript('''
            BEGIN IMMEDIATE;
            CREATE TABLE estoque (id INTEGER PRIMARY KEY CHECK(id=1), total INTEGER NOT NULL);
            INSERT INTO estoque VALUES (1, 0);
            CREATE TABLE aplicados (job TEXT PRIMARY KEY NOT NULL, quantidade INTEGER NOT NULL);
            COMMIT;
        ''')
    finally:
        con.close()


def aplicar(database: Path, job: str, quantity: int, crash: str = 'nenhum') -> str:
    if not isinstance(job, str) or re.fullmatch(r'lote-[0-9]{1,6}', job) is None:
        raise ValueError('Identificador fora do contrato.')
    if type(quantity) is not int or not 1 <= quantity <= 1000:
        raise ValueError('Quantidade fora do contrato.')
    if crash not in ('nenhum', 'antes', 'depois'):
        raise ValueError('Ponto de interrupcao invalido.')
    con = conectar(database)
    try:
        con.execute('BEGIN IMMEDIATE')
        previous = con.execute('SELECT quantidade FROM aplicados WHERE job=?', (job,)).fetchone()
        if previous is not None:
            if previous[0] != quantity:
                raise ValueError('Mesmo identificador com outro conteudo.')
            con.execute('COMMIT')
            return 'ja_aplicado'
        con.execute('UPDATE estoque SET total=total+? WHERE id=1', (quantity,))
        con.execute('INSERT INTO aplicados VALUES (?, ?)', (job, quantity))
        if crash == 'antes':
            os._exit(31)  # Worker conhecido; sem finally, COMMIT ou resposta.
        con.execute('COMMIT')
        if crash == 'depois':
            os._exit(32)  # COMMIT terminou, mas a resposta nao saiu.
        return 'aplicado'
    except BaseException:
        if con.in_transaction:
            con.execute('ROLLBACK')
        raise
    finally:
        con.close()


def consultar(database: Path) -> dict:
    con = conectar(database)
    try:
        con.execute('BEGIN')
        total = con.execute('SELECT total FROM estoque WHERE id=1').fetchone()[0]
        rows = con.execute('SELECT job, quantidade FROM aplicados ORDER BY job').fetchall()
        con.execute('COMMIT')
        return {'total': total, 'aplicados': [list(row) for row in rows]}
    finally:
        con.close()


def tentativa(database: Path, job: str, quantity: int, crash: str = 'nenhum') -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, '-I', str(Path(__file__).resolve()), '--worker', str(database),
         job, str(quantity), crash], capture_output=True, text=True, encoding='utf-8',
        timeout=15, shell=False,
    )


def demonstrar() -> dict:
    with tempfile.TemporaryDirectory(prefix='aurora-cap16-') as folder:
        database = Path(folder) / 'estado.sqlite3'
        inicializar(database)
        before = tentativa(database, 'lote-1', 3, 'antes')
        if before.returncode != 31 or before.stdout:
            raise RuntimeError('Interrupcao antes do COMMIT nao observada.')
        first = consultar(database)
        retry = tentativa(database, 'lote-1', 3)
        if retry.returncode != 0 or json.loads(retry.stdout)['resultado'] != 'aplicado':
            raise RuntimeError('Retomada do lote-1 falhou.')
        after = tentativa(database, 'lote-2', 2, 'depois')
        if after.returncode != 32 or after.stdout:
            raise RuntimeError('Interrupcao depois do COMMIT nao observada.')
        second = consultar(database)
        duplicate = tentativa(database, 'lote-2', 2)
        if duplicate.returncode != 0 or json.loads(duplicate.stdout)['resultado'] != 'ja_aplicado':
            raise RuntimeError('Repeticao nao foi reconhecida.')
        return {'antes_do_commit': first, 'depois_do_commit_sem_resposta': second,
                'depois_da_repeticao': consultar(database)}


if __name__ == '__main__':
    if len(sys.argv) == 6 and sys.argv[1] == '--worker':
        result = aplicar(Path(sys.argv[2]), sys.argv[3], int(sys.argv[4]), sys.argv[5])
        print(json.dumps({'resultado': result}), flush=True)
    elif len(sys.argv) == 1:
        print(json.dumps(demonstrar(), ensure_ascii=False, sort_keys=True))
    else:
        raise SystemExit('Execute sem argumentos; --worker e reservado ao exemplo.')
