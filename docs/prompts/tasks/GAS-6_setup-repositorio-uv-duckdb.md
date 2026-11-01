# GAS-6 — Setup do Repositório gas-analytics com uv, DuckDB e PyProject

**Tipo:** Tarefa  
**Status no Jira:** Feito  
**Projeto:** GAS (GasAnalytics — Petróleo, Combustíveis & Safra 2027)  
**Épico Pai:** GAS-1 (EP1: Infraestrutura Analítica & Ingestão de Séries Temporais)  
**Papéis:** Executor: `Hermes Agent` | Auditor Técnico: `Hermes Agent` | Validador de Negócio: **Luciano Teixeira**  
**Data:** 2026-11-01  

---

## 1. Prompt Executivo Disparado ao Agente

```markdown
@workspace Atuando sob as Core Rules e Governança da Frota.
Vamos executar a configuração e bootstrap do repositório `gas-analytics`.

### 🛡️ RITUAL OBRIGATÓRIO DE INÍCIO DE TURNO
1. **Verificação de Idempotência:** Antes de alterar código, verifique se a tarefa já foi concluída:
   `git log --grep="GAS-6"`
   Se a entrega já estiver no histórico e os testes estiverem passando, aborte informando: `[IDEMPOTÊNCIA] Tarefa GAS-6 já executada anteriormente`.
2. **Confirme a branch ativa:** `git branch --show-current`.
3. **Execução estrita via `uv run`.**

### 📋 ESCOPO DE EXECUÇÃO (GAS-6)
1. Configurar `pyproject.toml` com gerenciador `hatchling`, versão do Python `>=3.11,<3.13`, dependências (`duckdb`, `polars`, `pyarrow`, `requests`, `pydantic`, `pydantic-settings`, `pyyaml`, `rich`, `typer`) e grupo dev (`pytest`, `pytest-cov`, `ruff`).
2. Configurar `pythonpath = ["src"]` no `[tool.pytest.ini_options]`.
3. Estruturar diretórios canônicos:
   - `src/gas_analytics/` (`config.py`, `db.py`, `extractors/`, `models/`, `analysis/`).
   - `data/` (`raw/`, `processed/`, `gold/`) com `.gitkeep` e `.gitignore` apropriado.
   - `tests/` com testes unitários para `config` e `db` (DuckDB schemas raw/processed/gold).
4. Executar sincronização de pacotes via `uv sync` e suíte de testes via `uv run pytest`.

### 🧪 DEFINITION OF DONE (DoD) & COMANDOS DE TERMINAL
- `uv sync` executa com sucesso instalando os pacotes.
- `uv run pytest` executa 100% verde (pelo menos 3 testes aprovados).
- `git status` reflete estrutura limpa e pronta para versionamento.

### 📦 CONVENÇÃO DE COMMIT
`chore(scaffold): setup do repositorio com uv, duckdb e suite de testes [GAS-6]`
```

---

## 2. Histórico de Versões do Prompt
* **v1 (01/11/2026 — Concluído):** Scaffold inicial com uv, DuckDB Lakehouse Medallion e suíte pytest.
