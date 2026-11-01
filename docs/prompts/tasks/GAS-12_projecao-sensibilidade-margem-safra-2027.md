# GAS-12 — Projeção de Sensibilidade e Margem Operacional da Safra 2026/2027

**Tipo:** Tarefa  
**Status no Jira:** Backlog  
**Projeto:** GAS (GasAnalytics — Petróleo, Combustíveis & Safra 2027)  
**Épico Pai:** GAS-3 (EP3: Matriz de Impacto Agro: Custo Operacional, Frete & Safra 2027)  
**Papéis:** Executor: `Antigravity` / `Hermes` | Auditor Técnico: `Hermes Agent` | Validador de Negócio: **Luciano Teixeira**  
**Data:** 2026-11-01  

---

## 1. Prompt Executivo Disparado ao Agente

```markdown
@workspace Atuando sob as Core Rules e Governança da Frota.
Vamos projetar a margem operacional da Safra 2026/2027 sob diferentes cenários de recomposição do diesel pós-eleição.

### 🛡️ RITUAL OBRIGATÓRIO DE INÍCIO DE TURNO
1. **Verificação de Idempotência:** `git log --grep="GAS-12"`.
2. **Confirme a branch de trabalho:** `git switch -c feat/GAS-12-sensibilidade-safra-2027`.
3. **Execução estrita via `uv run`.**

### 📋 ESCOPO DE IMPLEMENTAÇÃO (GAS-12)
Em `src/gas_analytics/analysis/crop_margin.py`:
1. Definir os 3 cenários de estresse de combustível pós-eleição 2026:
   - Cenário Otimista: Reajuste brando de +8% (estabilidade do barril de petróleo a $75 USD).
   - Cenário Base: Recomposição integral do PPI de +18% (barril a $85 USD, USD/BRL a 5,50).
   - Cenário Estresse: Choque geopolítico + fiscal com reajuste de +32% (barril a $100 USD, USD/BRL a 6,00).
2. Calcular o impacto financeiro direto:
   - Custo operacional de máquinas agrícolas (tratores e colheitadeiras: ~60 a 80 L/ha de diesel).
   - Custo de escoamento rodoviário por saca de soja (60kg).
   - Margem líquida residual do produtor (R$/ha e % de lucro sobre a receita bruta).
3. Materializar no DuckDB `gold.fct_simulacao_margem_safra_2027`.

### 🧪 DEFINITION OF DONE (DoD) & COMANDOS DE TERMINAL
- Testes de integridade matemática dos 3 cenários em `tests/test_crop_margin.py`.
- `uv run pytest tests/test_crop_margin.py` verde.

### 📦 CONVENÇÃO DE COMMIT
`feat(analysis): projecao e simulacao de margem operacional da safra 2026 2027 [GAS-12]`
```

---

## 2. Histórico de Versões do Prompt
* **v1 (01/11/2026):** Modelagem dos 3 cenários de estresse e impacto por hectare/saca.
