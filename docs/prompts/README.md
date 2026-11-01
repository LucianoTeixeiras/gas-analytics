# Catálogo de Prompts Canônicos — GasAnalytics

Este catálogo documenta e versiona formalmente todos os **Prompts de Arquitetura (Épicos)** e **Ordens de Serviço (Tasks-as-a-Prompt)** executados pelos agentes da frota (`Hermes Agent`, `Antigravity`, etc.) sob a governança de **Luciano Teixeira**.

Cada documento espelha fielmente a respectiva issue do Jira Cloud no projeto **`GAS`** (ID 10287), garantindo paridade total entre o board de governança e os arquivos físicos no Git.

---

## 🏛️ Épicos (Prompts de Arquitetura & Visão de Negócio)

| Chave | Status | Arquivo Canônico | Resumo |
|---|---|---|---|
| **GAS-1** | Em Andamento | [`epicos/GAS-1_ep1-infraestrutura-analitica-ingestao.md`](epicos/GAS-1_ep1-infraestrutura-analitica-ingestao.md) | EP1 — Infraestrutura Analítica & Ingestão de Séries Temporais (ANP / Bacen / Yahoo) |
| **GAS-2** | Backlog | [`epicos/GAS-2_ep2-modelagem-econometrica-ciclos-eleitorais.md`](epicos/GAS-2_ep2-modelagem-econometrica-ciclos-eleitorais.md) | EP2 — Modelagem Econométrica: Ciclos Eleitorais x Defasagem de Combustíveis |
| **GAS-3** | Backlog | [`epicos/GAS-3_ep3-matriz-impacto-agro-safra-2027.md`](epicos/GAS-3_ep3-matriz-impacto-agro-safra-2027.md) | EP3 — Matriz de Impacto Agro: Custo Operacional, Frete & Safra 2027 |
| **GAS-4** | Backlog | [`epicos/GAS-4_ep4-complexo-sucroalcooleiro-paridade-etanol.md`](epicos/GAS-4_ep4-complexo-sucroalcooleiro-paridade-etanol.md) | EP4 — Complexo Sucroalcooleiro & Paridade Etanol x Gasolina |
| **GAS-5** | Backlog | [`epicos/GAS-5_ep5-camada-publicacao-data-app-laudo.md`](epicos/GAS-5_ep5-camada-publicacao-data-app-laudo.md) | EP5 — Camada de Publicação: Data App & Laudo Executivo de Sensibilidade |

---

## 📋 Tasks & Histórias (Tasks-as-a-Prompt & Ordens de Execução)

| Chave | Status | Precedência / Vínculo | Arquivo Canônico | Resumo |
|---|---|---|---|---|
| **GAS-6** | Feito | **Fundação do Projeto** | [`tasks/GAS-6_setup-repositorio-uv-duckdb.md`](tasks/GAS-6_setup-repositorio-uv-duckdb.md) | Setup do Repositório gas-analytics com uv, DuckDB e PyProject |
| **GAS-17** | Feito | **Governança Agêntica** | [`tasks/GAS-17_estruturacao-catalogo-prompts-governanca.md`](tasks/GAS-17_estruturacao-catalogo-prompts-governanca.md) | Estruturação do Catálogo de Prompts Canônico e Governança Agêntica (Padrão Tá na Lista) |
| **GAS-7** | Backlog | Depende da GAS-6 | [`tasks/GAS-7_extrator-series-historicas-anp.md`](tasks/GAS-7_extrator-series-historicas-anp.md) | Extrator de Séries Históricas da ANP (Gasolina C e Diesel S10) |
| **GAS-8** | Backlog | Depende da GAS-6 | [`tasks/GAS-8_conector-series-macro-bacen-yahoo.md`](tasks/GAS-8_conector-series-macro-bacen-yahoo.md) | Conector de Séries Macroeconômicas (Bacen SGS, Câmbio USD/BRL e Brent/WTI) |
| **GAS-9** | Backlog | Depende de GAS-7 e GAS-8 | [`tasks/GAS-9_motor-alinhamento-temporal-janelas-eleitorais.md`](tasks/GAS-9_motor-alinhamento-temporal-janelas-eleitorais.md) | Motor de Alinhamento Temporal: Marcação de Janelas Pré e Pós-Eleitorais |
| **GAS-10** | Backlog | Depende de GAS-8 e GAS-9 | [`tasks/GAS-10_calculo-curva-defasagem-ppi.md`](tasks/GAS-10_calculo-curva-defasagem-ppi.md) | Cálculo da Curva de Defasagem PPI (Preço de Paridade de Importação) |
| **GAS-11** | Backlog | Depende de GAS-10 | [`tasks/GAS-11_matriz-elasticidade-diesel-frete-graos.md`](tasks/GAS-11_matriz-elasticidade-diesel-frete-graos.md) | Matriz de Elasticidade: Custo do Diesel x Frete de Grãos (MT/GO/RS para Portos) |
| **GAS-12** | Backlog | Depende de GAS-11 | [`tasks/GAS-12_projecao-sensibilidade-margem-safra-2027.md`](tasks/GAS-12_projecao-sensibilidade-margem-safra-2027.md) | Projeção de Sensibilidade e Margem Operacional da Safra 2026/2027 |
| **GAS-13** | Backlog | Depende de GAS-7 | [`tasks/GAS-13_analise-paridade-70-etanol-gasolina.md`](tasks/GAS-13_analise-paridade-70-etanol-gasolina.md) | Análise da Paridade dos 70% Etanol x Gasolina nos Estados Produtores |
| **GAS-14** | Backlog | Depende de GAS-13 | [`tasks/GAS-14_simulacao-mix-moagem-usinas-acucar-etanol.md`](tasks/GAS-14_simulacao-mix-moagem-usinas-acucar-etanol.md) | Simulação de Mix de Moagem das Usinas (Açúcar x Etanol) para a Safra 2027 |
| **GAS-15** | Backlog | Depende de EP1 a EP4 | [`tasks/GAS-15_data-app-interativo-streamlit-duckdb.md`](tasks/GAS-15_data-app-interativo-streamlit-duckdb.md) | Construção do Data App Interativo GasAnalytics (Streamlit + DuckDB) |
| **GAS-16** | Backlog | Depende de EP3 e EP5 | [`tasks/GAS-16_gerador-laudo-econometrico-executivo-pdf.md`](tasks/GAS-16_gerador-laudo-econometrico-executivo-pdf.md) | Gerador de Laudo Econométrico Executivo em PDF Corporativo |

---

## 🛡️ Padrão de Engenharia Agêntica (Core Rules Embarcadas)

Todas as tarefas ativas e futuras seguem compulsoriamente:
1. **Ritual de Início de Turno:** Sensoriamento de branch ativa, Imersão prévia no código e Runner oficial `uv run`.
2. **FinOps & Dados Abertos:** Zero custo de APIs proprietárias, ingestão eficiente de dados públicos (ANP, Banco Central SGS, Yahoo Finance / Fed FRED) gravados em Parquet Snappy particionado.
3. **Arquitetura Medallion Local:** Ingestão desacoplada (raw), limpeza e normalização (processed), e fatos agregados analíticos no DuckDB (gold).
4. **Governança de Commits:** Commits atômicos carimbados obrigatoriamente com a chave Jira `[GAS-XX]`.
