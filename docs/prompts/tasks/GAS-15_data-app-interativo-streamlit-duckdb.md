# GAS-15 — Construção do Data App Interativo GasAnalytics (Streamlit + DuckDB)

**Tipo:** Tarefa  
**Status no Jira:** Backlog  
**Projeto:** GAS (GasAnalytics — Petróleo, Combustíveis & Safra 2027)  
**Épico Pai:** GAS-5 (EP5: Camada de Publicação: Data App & Laudo Executivo)  
**Papéis:** Executor: `Antigravity` / `Hermes` | Auditor Técnico: `Hermes Agent` | Validador de Negócio: **Luciano Teixeira**  
**Data:** 2026-11-01  

---

## 1. Prompt Executivo Disparado ao Agente

```markdown
@workspace Atuando sob as Core Rules e Governança da Frota.
Vamos construir o Data App analítico interativo do GasAnalytics.

### 🛡️ RITUAL OBRIGATÓRIO DE INÍCIO DE TURNO
1. **Verificação de Idempotência:** `git log --grep="GAS-15"`.
2. **Confirme a branch de trabalho:** `git switch -c feat/GAS-15-data-app-interativo`.
3. **Execução estrita via `uv run`.**

### 📋 ESCOPO DE IMPLEMENTAÇÃO (GAS-15)
Em `src/gas_analytics/app/`:
1. Construir interface em Streamlit conectando diretamente às views `gold` do DuckDB local.
2. Módulos do Data App:
   - **Visão Geral Macro:** Painel de indicadores em tempo real (Brent, Câmbio USD/BRL, Gasolina e Diesel).
   - **Ciclos Eleitorais & Defasagem PPI:** Gráficos interativos com marcação visual de eleições e janelas pré/pós.
   - **Simulador de Frete & Safra 2027:** Sliders interativos de variação de diesel e visualização imediata do custo de frete por rota e impacto na margem líquida por saca.
   - **Paridade Etanol 70%:** Mapa de calor de competitividade por estado.
3. Design corporativo profissional, tema claro de alto contraste e performance sub-segundo graças ao DuckDB.

### 🧪 DEFINITION OF DONE (DoD) & COMANDOS DE TERMINAL
- Inicialização do app em modo headless para validação: `uv run streamlit run src/gas_analytics/app/main.py --server.headless=true`.
- Testes unitários das queries de agregação em `tests/test_app_queries.py`.
- `uv run pytest tests/test_app_queries.py` verde.

### 📦 CONVENÇÃO DE COMMIT
`feat(app): data app interativo streamlit integrado ao duckdb gold [GAS-15]`
```

---

## 2. Histórico de Versões do Prompt
* **v1 (01/11/2026):** Especificação do Data App interativo e simulador de safra.
