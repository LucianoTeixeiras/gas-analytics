# GAS-10 — Cálculo da Curva de Defasagem PPI (Preço de Paridade de Importação)

**Tipo:** Tarefa  
**Status no Jira:** Backlog  
**Projeto:** GAS (GasAnalytics — Petróleo, Combustíveis & Safra 2027)  
**Épico Pai:** GAS-2 (EP2: Modelagem Econométrica: Ciclos Eleitorais x Defasagem)  
**Papéis:** Executor: `Antigravity` / `Hermes` | Auditor Técnico: `Hermes Agent` | Validador de Negócio: **Luciano Teixeira**  
**Data:** 2026-11-01  

---

## 1. Prompt Executivo Disparado ao Agente

```markdown
@workspace Atuando sob as Core Rules e Governança da Frota.
Vamos implementar o algoritmo econométrico de cálculo da defasagem frente ao PPI internacional.

### 🛡️ RITUAL OBRIGATÓRIO DE INÍCIO DE TURNO
1. **Verificação de Idempotência:** `git log --grep="GAS-10"`.
2. **Confirme a branch de trabalho:** `git switch -c feat/GAS-10-calculo-ppi`.
3. **Execução estrita via `uv run`.**

### 📋 ESCOPO DE IMPLEMENTAÇÃO (GAS-10)
Em `src/gas_analytics/models/ppi_calculator.py`:
1. Estruturar a fórmula teórica de paridade de importação para Gasolina C e Diesel S10:
   - Preço de referência do Golfo dos EUA (USGC) ou Brent FOB convertido para R$/Litro via cotação USD/BRL.
   - Adição de custos de internação, frete marítimo, seguro internacional, taxas portuárias e margem de distribuição.
2. Comparar diariamente o preço realizado nas refinarias e bombas com o preço PPI teórico.
3. Calcular a curva de defasagem nominal (R$/litro) e percentual (%):
   `defasagem_pct = ((preco_realizado / preco_ppi_teorico) - 1) * 100`
4. Avaliar se nos períodos marcados como pré-eleitorais a defasagem atinge picos estatisticamente relevantes (> 15% a 25%).
5. Materializar a tabela no DuckDB `gold.fct_defasagem_ppi_historica`.

### 🧪 DEFINITION OF DONE (DoD) & COMANDOS DE TERMINAL
- Testes unitários com dados sintéticos conhecidos em `tests/test_ppi_calculator.py`.
- `uv run pytest tests/test_ppi_calculator.py` verde.

### 📦 CONVENÇÃO DE COMMIT
`feat(models): calculo econometrico da curva de defasagem ppi refinaria e bomba [GAS-10]`
```

---

## 2. Histórico de Versões do Prompt
* **v1 (01/11/2026):** Equação de paridade de importação e métricas de defasagem.
