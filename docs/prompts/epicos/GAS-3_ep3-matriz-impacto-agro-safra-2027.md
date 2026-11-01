# GAS-3 — EP3: Matriz de Impacto Agro: Custo Operacional, Frete & Safra 2027

**Tipo:** Épico  
**Status no Jira:** Backlog  
**Projeto:** GAS (GasAnalytics — Petróleo, Combustíveis & Safra 2027)  
**Papéis:** Arquiteto / Revisor: **Luciano Teixeira** | Orquestrador: `Hermes Agent` | Executores: `Antigravity` / `Hermes`  
**Data:** 2026-11-01  

---

## 1. Contexto & Visão de Negócio
O **EP3** modela como as variações e defasagens do preço do Óleo Diesel S10 impactam diretamente o agronegócio brasileiro, especificamente o custo do frete rodoviário de grãos (soja e milho) das regiões produtoras (Mato Grosso, Goiás, Paraná e Rio Grande do Sul) até os portos exportadores (Santos, Paranaguá, Rio Grande e Barcarena), projetando os reflexos de margem na **Safra 2026/2027**.

## 2. Fronteiras de Arquitetura & Stack
- **Modelagem de Custo de Frete:** Elasticidade diesel x frete rodoviário (participação do combustível estimada entre 35% e 48% do frete spot).
- **Simulação da Safra 2027:** Cenários de estresse de diesel (reajustes de +10%, +20%, +35% pós-eleição) e o impacto em R$/saca de 60kg e na margem líquida por hectare.

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'darkMode': false, 'background': '#FFFFFF', 'mainBkg': '#FFFFFF', 'primaryColor': '#F1F5F9', 'primaryTextColor': '#0F172A', 'lineColor': '#1E3A8A'}}}%%
graph LR
    Diesel[Variação Preço Diesel S10] --> Elasticidade[Matriz de Elasticidade]
    Elasticidade --> Frete[Custo Frete por Rota / Tonelada]
    Frete --> MargemAgro[Margem do Produtor Safra 2027 R$/saca]
```

## 3. Tarefas Subordinadas
1. **GAS-11:** Matriz de Elasticidade: Custo do Diesel x Frete de Grãos (MT/GO/RS para Portos).
2. **GAS-12:** Projeção de Sensibilidade e Margem Operacional da Safra 2026/2027.
