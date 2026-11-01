# GAS-7 — Extrator de Séries Históricas da ANP (Gasolina C e Diesel S10)

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
Vamos implementar o extrator automatizado das séries históricas de preços de combustíveis da ANP.

### 🛡️ RITUAL OBRIGATÓRIO DE INÍCIO DE TURNO
1. **Verificação de Idempotência:** `git log --grep="GAS-7"`. Se já existir, aborte com aviso de idempotência.
2. **Confirme a branch de trabalho:** Crie e mude para `feat/GAS-7-extrator-anp`.
3. **Execução estrita via `uv run`.**

### 📋 ESCOPO DE IMPLEMENTAÇÃO (GAS-7)
Em `src/gas_analytics/extractors/anp.py`:
1. Implementar `ANPExtractor` para baixar os arquivos semestrais/mensais de preços de combustíveis automotivos disponibilizados pelo portal de dados abertos da ANP:
   - URL base: `https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/shpc/dsas/ca/`
   - Séries alvo: Gasolina Comum (C), Óleo Diesel S10 e Etanol Hidratado.
   - Período histórico: de 2014 a 2026.
2. Armazenar arquivos brutos baixados em `data/raw/anp/{combustivel}/`.
3. Normalizar dados em Polars (`src/gas_analytics/extractors/anp_transformer.py`):
   - Colunas padronizadas: `data_coleta (date)`, `regiao`, `estado_sigla`, `municipio`, `produto`, `preco_venda_litro (float)`, `bandeira`.
   - Gravar Parquet Snappy em `data/processed/anp/precos_combustiveis.parquet`.
4. Ingerir no DuckDB na tabela `processed.anp_precos_semanais`.

### 🧪 DEFINITION OF DONE (DoD) & COMANDOS DE TERMINAL
- Script de extração CLI: `uv run python -m gas_analytics.extractors.anp --sample` executa sem erros e baixa amostra.
- Testes unitários em `tests/test_anp_extractor.py` validando parsing e tipos.
- Execução: `uv run pytest tests/test_anp_extractor.py` verde.

### 📦 CONVENÇÃO DE COMMIT
`feat(extractors): extrator de series historicas da anp gasolina diesel etanol [GAS-7]`
```

---

## 2. Histórico de Versões do Prompt
* **v1 (01/11/2026):** Especificação inicial com contratos ANP e normalização Polars/Parquet.
