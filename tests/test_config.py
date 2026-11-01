"""Testes de configuração e caminhos."""

from gas_analytics.config import settings


def test_settings_paths():
    assert settings.project_root.exists()
    assert settings.data_raw.name == "raw"
    assert settings.data_processed.name == "processed"
    assert settings.data_gold.name == "gold"
    assert settings.paridade_etanol_gasolina_ref == 0.70
