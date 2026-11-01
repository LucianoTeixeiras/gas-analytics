# GAS-8 — Conector de Séries Macroeconômicas (Bacen SGS, Câmbio USD/BRL e Brent/WTI)

**Tipo:** Tarefa  
**Status no Jira:** Backlog  
**Projeto:** GAS (GasAnalytics — Petróleo, Combustíveis & Safra 2027)  
**Épico Pai:** GAS-1 (EP1: Infraestrutura Analítica & Ingestão de Séries Temporais)  
**Papéis:** Executor: `Antigravity` / `Hermes` | Auditor Técnico: `Hermes Agent` | Validador de Negócio: **Luciano Teixeira**  
**Data:** 2026-11-01  

---

## 1. Prompt Executivo Disparado ao Agente

```markdown
@workspace Atuando sob as Core Rules e Governança da Frota.
Vamos implementar os conectores macroeconômicos do Bacen SGS e cotações internacionais de petróleo.

### 🛡️ RITUAL OBRIGATÓRIO DE INÍCIO DE TURNO
1. **Verificação de Idempotência:** `git log --grep="GAS-8"`.
2. **Confirme a branch de trabalho:** `git switch -c feat/GAS-8-conector-macro`.
3. **Execução estrita via `uv run`.**

### 📋 ESCOPO DE IMPLEMENTAÇÃO (GAS-8)
Em `src/gas_analytics/extractors/macro.py`:
1. Conectar à API pública do Banco Central do Brasil (SGS):
   - Série 1 (Taxa de câmbio USD/BRL comercial venda diária).
   - Série 433 (IPCA variação mensal) e Série 10813 (Câmbio USD/BRL fim de período).
2. Conectar à extração de cotações de Petróleo Brent (`BZ=F`) e WTI (`CL=F`) via API REST pública ou Yahoo Finance / FRED:
   - Preço diário de fechamento em USD/barril.
3. Consolidar tabela diária macro em `data/processed/macro/indicadores_macro.parquet`:
   - Colunas: `data`, `usd_brl`, `brent_usd`, `wti_usd`, `brent_brl_barril` (calculado: `brent_usd * usd_brl`).
4. Ingerir no DuckDB na tabela `processed.indicadores_macro`.

### 🧪 DEFINITION OF DONE (DoD) & COMANDOS DE TERMINAL
- Testes unitários com mocks de HTTP em `tests/test_macro_extractor.py`.
- `uv run pytest tests/test_macro_extractor.py` verde.
- Amostra executável: `uv run python -m gas_analytics.extractors.macro --dias 30`.

### 📦 CONVENÇÃO DE COMMIT
`feat(extractors): conector de series bacen sgs cambio e petroleo brent wti [GAS-8]`
```

---

## 2. Histórico de Versões do Prompt
* **v1 (01/11/2026):** Especificação com séries Bacen SGS e cálculo de cotação em reais.
