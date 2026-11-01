# GAS-9 — Motor de Alinhamento Temporal: Marcação de Janelas Pré e Pós-Eleitorais

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
Vamos implementar o motor econométrico de marcação temporal dos ciclos eleitorais brasileiros.

### 🛡️ RITUAL OBRIGATÓRIO DE INÍCIO DE TURNO
1. **Verificação de Idempotência:** `git log --grep="GAS-9"`.
2. **Confirme a branch de trabalho:** `git switch -c feat/GAS-9-janelas-eleitorais`.
3. **Execução estrita via `uv run`.**

### 📋 ESCOPO DE IMPLEMENTAÇÃO (GAS-9)
Em `src/gas_analytics/models/election_cycles.py`:
1. Mapear o calendário canônico das eleições presidenciais brasileiras:
   - 2014: 1º Turno (05/10/2014), 2º Turno (26/10/2014), Posse (01/01/2015).
   - 2018: 1º Turno (07/10/2018), 2º Turno (28/10/2018), Posse (01/01/2019).
   - 2022: 1º Turno (02/10/2022), 2º Turno (30/10/2022), Posse (01/01/2023).
   - 2026 (Projetado): 1º Turno (04/10/2026), 2º Turno (25/10/2026), Posse (01/01/2027).
2. Criar função de marcação temporal de flags:
   - `flg_pre_eleitoral_180d`, `flg_pre_eleitoral_90d`, `flg_pre_eleitoral_30d`.
   - `flg_pos_eleitoral_30d`, `flg_pos_eleitoral_90d`, `flg_pos_eleitoral_180d`.
3. Calcular métricas estatísticas agregadas por ciclo eleitoral (médias móveis de preços, volatilidade diária e deltas pré x pós).
4. Materializar a tabela analítica no DuckDB `gold.fct_ciclos_eleitorais_combustiveis`.

### 🧪 DEFINITION OF DONE (DoD) & COMANDOS DE TERMINAL
- Testes unitários em `tests/test_election_cycles.py` cobrindo todos os ciclos de 2014 a 2026.
- `uv run pytest tests/test_election_cycles.py` 100% aprovado.

### 📦 CONVENÇÃO DE COMMIT
`feat(models): motor de alinhamento temporal e marcacao de janelas eleitorais [GAS-9]`
```

---

## 2. Histórico de Versões do Prompt
* **v1 (01/11/2026):** Definição canônica de datas e janelas D-180 a D+180.
