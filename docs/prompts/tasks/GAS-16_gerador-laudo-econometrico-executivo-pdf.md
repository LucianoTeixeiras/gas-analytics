# GAS-16 — Gerador de Laudo Econométrico Executivo em PDF Corporativo

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
Vamos criar o pipeline automatizado de geração de Laudos Executivos em PDF para cooperativas e investidores agro.

### 🛡️ RITUAL OBRIGATÓRIO DE INÍCIO DE TURNO
1. **Verificação de Idempotência:** `git log --grep="GAS-16"`.
2. **Confirme a branch de trabalho:** `git switch -c feat/GAS-16-gerador-laudo-pdf`.
3. **Execução estrita via `uv run`.**

### 📋 ESCOPO DE IMPLEMENTAÇÃO (GAS-16)
Em `src/gas_analytics/reports/`:
1. Estruturar template HTML/CSS corporativo em conformidade com as diretrizes do portfólio de Luciano Teixeira:
   - Fundo 100% branco, tipografia sem serifa profissional, tabelas executivas com linhas suaves e sem caixas escuras.
   - Cards de indicadores e matriz de sensibilidade dos 3 cenários de estresse da Safra 2027.
2. Automatizar geração de PDF via Edge Headless:
   `msedge --headless --disable-gpu --print-to-pdf=<saida.pdf> <relatorio.html>`
3. Salvar laudos gerados em `docs/reports/YYYYMM/DD/LAUDO_EXECUTIVO_GASANALYTICS_SAFRA_2027.pdf`.

### 🧪 DEFINITION OF DONE (DoD) & COMANDOS DE TERMINAL
- Script de geração executável: `uv run python -m gas_analytics.reports.generate --output docs/reports/laudo_teste.pdf`.
- Arquivo PDF gerado e validado visualmente.
- Testes em `tests/test_report_generator.py` verdes.

### 📦 CONVENÇÃO DE COMMIT
`feat(reports): gerador automatizado de laudo econometrico executivo em pdf [GAS-16]`
```

---

## 2. Histórico de Versões do Prompt
* **v1 (01/11/2026):** Template corporativo e motor de compilação PDF via Edge Headless.
