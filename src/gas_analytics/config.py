"""Configuração centralizada do GasAnalytics."""

from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Parâmetros e caminhos canônicos do projeto."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    environment: str = "development"
    log_level: str = "INFO"

    # Raiz do projeto
    project_root: Path = Path(__file__).resolve().parent.parent.parent

    # Caminhos Medallion
    data_raw: Path = project_root / "data" / "raw"
    data_processed: Path = project_root / "data" / "processed"
    data_gold: Path = project_root / "data" / "gold"

    # DuckDB
    duckdb_path: Path = data_gold / "gas_analytics.duckdb"

    # Parâmetros de Modelagem Econométrica
    janela_pre_eleitoral_dias: int = 180
    janela_pos_eleitoral_dias: int = 180
    paridade_etanol_gasolina_ref: float = 0.70


settings = Settings()
