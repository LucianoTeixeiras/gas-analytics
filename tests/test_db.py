"""Testes do gerenciador DuckDB."""

from pathlib import Path

from gas_analytics.db import get_db


def test_duckdb_in_memory():
    db = get_db(db_path=Path(":memory:"))
    # Verifica schemas criados
    schemas = [
        row[0]
        for row in db.execute("SELECT schema_name FROM information_schema.schemata").fetchall()
    ]
    assert "raw" in schemas
    assert "processed" in schemas
    assert "gold" in schemas


def test_duckdb_query():
    db = get_db(db_path=Path(":memory:"))
    res = db.execute("SELECT 42 AS resposta").fetchall()
    assert res[0][0] == 42
