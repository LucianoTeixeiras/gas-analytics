# GAS-11 — Matriz de Elasticidade: Custo do Diesel x Frete de Grãos (MT/GO/RS para Portos)

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
Vamos desenvolver a matriz de elasticidade entre o preço do Óleo Diesel S10 e o frete rodoviário de grãos.

### 🛡️ RITUAL OBRIGATÓRIO DE INÍCIO DE TURNO
1. **Verificação de Idempotência:** `git log --grep="GAS-11"`.
2. **Confirme a branch de trabalho:** `git switch -c feat/GAS-11-elasticidade-frete`.
3. **Execução estrita via `uv run`.**

### 📋 ESCOPO DE IMPLEMENTAÇÃO (GAS-11)
Em `src/gas_analytics/analysis/freight_elasticity.py`:
1. Mapear as 5 rotas rodoviárias estratégicas de escoamento de grãos (soja e milho):
   - Rota 1: Sorriso (MT) -> Porto de Santos (SP) (~2.100 km).
   - Rota 2: Rio Verde (GO) -> Porto de Santos (SP) (~950 km).
   - Rota 3: Cascavel (PR) -> Porto de Paranaguá (PR) (~650 km).
   - Rota 4: Passo Fundo (RS) -> Porto de Rio Grande (RS) (~450 km).
   - Rota 5: Sinop (MT) -> Porto de Barcarena / Miritituba (PA) (~1.000 km arco norte).
2. Modelar o coeficiente de elasticidade do diesel no frete (peso do combustível = 38% a 45% do custo por tonelada).
3. Calcular a função:
   `delta_frete_tonelada = delta_diesel_pct * peso_diesel * frete_base_tonelada`
4. Materializar no DuckDB `gold.dim_rotas_frete_agro` e `gold.fct_elasticidade_frete_diesel`.

### 🧪 DEFINITION OF DONE (DoD) & COMANDOS DE TERMINAL
- Testes unitários validando cálculos de frete por rota em `tests/test_freight_elasticity.py`.
- `uv run pytest tests/test_freight_elasticity.py` verde.

### 📦 CONVENÇÃO DE COMMIT
`feat(analysis): matriz de elasticidade de frete rodoviario diesel rotas agro [GAS-11]`
```

---

## 2. Histórico de Versões do Prompt
* **v1 (01/11/2026):** Mapeamento das 5 rotas de escoamento e coeficientes de custo.
