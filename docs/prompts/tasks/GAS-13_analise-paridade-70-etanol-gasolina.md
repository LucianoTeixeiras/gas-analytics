# GAS-13 — Análise da Paridade dos 70% Etanol x Gasolina nos Estados Produtores

**Tipo:** Tarefa  
**Status no Jira:** Backlog  
**Projeto:** GAS (GasAnalytics — Petróleo, Combustíveis & Safra 2027)  
**Épico Pai:** GAS-4 (EP4: Complexo Sucroalcooleiro & Paridade Etanol x Gasolina)  
**Papéis:** Executor: `Antigravity` / `Hermes` | Auditor Técnico: `Hermes Agent` | Validador de Negócio: **Luciano Teixeira**  
**Data:** 2026-11-01  

---

## 1. Prompt Executivo Disparado ao Agente

```markdown
@workspace Atuando sob as Core Rules e Governança da Frota.
Vamos implementar a análise quantitativa da paridade energética de 70% entre Etanol Hidratado e Gasolina C.

### 🛡️ RITUAL OBRIGATÓRIO DE INÍCIO DE TURNO
1. **Verificação de Idempotência:** `git log --grep="GAS-13"`.
2. **Confirme a branch de trabalho:** `git switch -c feat/GAS-13-paridade-etanol-gasolina`.
3. **Execução estrita via `uv run`.**

### 📋 ESCOPO DE IMPLEMENTAÇÃO (GAS-13)
Em `src/gas_analytics/analysis/ethanol_parity.py`:
1. Calcular a série histórica da razão de paridade nas bombas:
   `razao_paridade = preco_etanol_litro / preco_gasolina_litro`
2. Avaliar competitividade nos 5 estados líderes de consumo e produção (SP, MG, GO, MT, PR):
   - `flg_etanol_competitivo`: `razao_paridade <= 0.70` (ou limiar dinâmico por estado).
3. Analisar como o congelamento artificial do preço da gasolina em anos eleitorais prejudica a demanda por etanol e a rentabilidade do setor sucroenergético.
4. Materializar no DuckDB `gold.fct_paridade_etanol_gasolina_estados`.

### 🧪 DEFINITION OF DONE (DoD) & COMANDOS DE TERMINAL
- Testes unitários em `tests/test_ethanol_parity.py`.
- `uv run pytest tests/test_ethanol_parity.py` verde.

### 📦 CONVENÇÃO DE COMMIT
`feat(analysis): analise da curva de paridade 70 por cento etanol e gasolina [GAS-13]`
```

---

## 2. Histórico de Versões do Prompt
* **v1 (01/11/2026):** Modelagem de paridade e sensibilidade nos estados produtores.
