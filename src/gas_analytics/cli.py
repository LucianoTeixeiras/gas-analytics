"""Interface de linha de comando (CLI) do GasAnalytics."""

import typer
from rich.console import Console

app = typer.Typer(
    name="gas-analytics",
    help="GasAnalytics — Petróleo, Combustíveis & Safra 2027",
    no_args_is_help=True,
    add_completion=False,
)
console = Console()


@app.command()
def version():
    """Exibe a versão do GasAnalytics."""
    from gas_analytics import __version__

    console.print(f"[bold green]GasAnalytics[/bold green] v{__version__}")


@app.command()
def info():
    """Exibe informações sobre o ambiente e status da base DuckDB."""
    from gas_analytics.config import settings
    from gas_analytics.db import DatabaseManager

    console.print("[bold green]GasAnalytics[/bold green] v0.1.0")
    console.print(f"Ambiente: [cyan]{settings.environment}[/cyan]")
    console.print(f"DuckDB Path: [yellow]{settings.duckdb_path}[/yellow]")

    manager = DatabaseManager()
    conn = manager.get_connection(read_only=True) if settings.duckdb_path.exists() else None
    if conn:
        tables = conn.execute(
            "SELECT table_schema, table_name FROM information_schema.tables WHERE table_schema IN ('raw', 'processed', 'gold')"
        ).fetchall()
        console.print(f"Tabelas materializadas: {len(tables)}")
    else:
        console.print("[dim]Banco DuckDB ainda não inicializado em disco.[/dim]")


def main():
    app()


if __name__ == "__main__":
    main()
