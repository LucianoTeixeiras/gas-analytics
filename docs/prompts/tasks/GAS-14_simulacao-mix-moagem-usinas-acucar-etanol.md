# GAS-14 — Simulação de Mix de Moagem das Usinas (Açúcar x Etanol) para a Safra 2027

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
Vamos simular as decisões de arbitragem das usinas entre moagem para Açúcar ou Etanol na Safra 2026/2027.

### 🛡️ RITUAL OBRIGATÓRIO DE INÍCIO DE TURNO
1. **Verificação de Idempotência:** `git log --grep="GAS-14"`.
2. **Confirme a branch de trabalho:** `git switch -c feat/GAS-14-mix-moagem-usinas`.
3. **Execução estrita via `uv run`.**

### 📋 ESCOPO DE IMPLEMENTAÇÃO (GAS-14)
Em `src/gas_analytics/analysis/sugar_ethanol_mix.py`:
1. Modelar a equivalência técnica de ATR (Açúcar Total Recuperável):
   - 1 tonelada de cana -> ATR médio de 135 a 140 kg.
   - Rendimento teórico: 1 kg de ATR gera aproximadamente 0,595 L de etanol hidratado ou 0,95 kg de açúcar.
2. Calcular o ponto de indiferença financeira entre exportar açúcar (cotação NY #11) e produzir etanol combustível (mercado interno).
3. Projetar o direcionamento do mix de moagem para a safra 2026/2027 em cenários de gasolina represada vs. desregulada.
4. Materializar no DuckDB `gold.fct_simulacao_mix_usinas_2027`.

### 🧪 DEFINITION OF DONE (DoD) & COMANDOS DE TERMINAL
- Testes de consistência do balanço de massa e receita de ATR em `tests/test_sugar_ethanol_mix.py`.
- `uv run pytest tests/test_sugar_ethanol_mix.py` verde.

### 📦 CONVENÇÃO DE COMMIT
`feat(analysis): simulacao de mix de moagem de usinas acucar x etanol safra 2027 [GAS-14]`
```

---

## 2. Histórico de Versões do Prompt
* **v1 (01/11/2026):** Modelo econômico de equivalência de ATR e arbitragem de usinas.
