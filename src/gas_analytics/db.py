"""Gerenciador de conexão e schemas DuckDB do GasAnalytics."""

from pathlib import Path

import duckdb

from gas_analytics.config import settings


class DatabaseManager:
    """Gerencia conexões in-memory ou persistentes ao DuckDB."""

    def __init__(self, db_path: Path | None = None):
        self.db_path = db_path or settings.duckdb_path
        self._conn: duckdb.DuckDBPyConnection | None = None

    def get_connection(self, read_only: bool = False) -> duckdb.DuckDBPyConnection:
        """Retorna uma conexão ativa ao banco DuckDB."""
        if str(self.db_path) == ":memory:":
            if self._conn is None:
                self._conn = duckdb.connect(database=":memory:")
            return self._conn

        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        return duckdb.connect(database=str(self.db_path), read_only=read_only)

    def init_medallion_schemas(self, conn: duckdb.DuckDBPyConnection | None = None) -> None:
        """Inicializa os schemas canônicos da arquitetura Medalhão."""
        c = conn or self.get_connection()
        c.execute("CREATE SCHEMA IF NOT EXISTS raw;")
        c.execute("CREATE SCHEMA IF NOT EXISTS processed;")
        c.execute("CREATE SCHEMA IF NOT EXISTS gold;")


def get_db(db_path: Path | None = None) -> duckdb.DuckDBPyConnection:
    """Factory helper para obter conexão configurada."""
    manager = DatabaseManager(db_path=db_path)
    conn = manager.get_connection()
    manager.init_medallion_schemas(conn)
    return conn
