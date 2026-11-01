# GAS-17 — Estruturação do Catálogo de Prompts Canônico e Governança Agêntica (Padrão Tá na Lista)

**Tipo:** Tarefa  
**Status no Jira:** Concluído  
**Projeto:** GAS (GasAnalytics — Petróleo, Combustíveis & Safra 2027)  
**Épico Pai:** GAS-1 (EP1: Infraestrutura Analítica & Ingestão de Séries Temporais)  
**Papéis:** Arquiteto: **Luciano Teixeira** | Executor: `Hermes Agent` | Revisor: **Luciano Teixeira**  
**Data:** 2026-11-01  

---

## 1. Prompt Executivo Disparado ao Agente

```markdown
@workspace Atuando sob as Core Rules e Governança da Frota.
Vamos estruturar o Catálogo de Prompts Canônico do GasAnalytics, adotando paridade total com o padrão de maturidade do projeto Tá na Lista (SAGIDCFB).

### 🛡️ RITUAL OBRIGATÓRIO DE INÍCIO DE TURNO
1. **Verificação de Idempotência:** `git log --grep="GAS-17"`. Se já existir no histórico, aborte com aviso de idempotência.
2. **Confirme a branch ativa:** Trabalhe em branch dedicada `feat/GAS-17-catalogo-prompts-governanca`.
3. **Execução estrita via `uv run`.**

### 📋 ESCOPO DE IMPLEMENTAÇÃO (GAS-17)
1. **Estrutura Canônica:**
   - Criar `docs/prompts/README.md` como matriz central de rastreabilidade do projeto.
   - Criar `docs/prompts/epicos/` contendo os 5 Épicos (GAS-1 a GAS-5) com contexto, limites de arquitetura e diagramas Mermaid em fundo claro (#FFFFFF).
   - Criar `docs/prompts/tasks/` contendo as ordens de serviço executáveis de todas as tarefas (GAS-6 a GAS-16 e GAS-17).
2. **Padrão Issue-as-a-Prompt:**
   - Cada tarefa deve conter: Ritual de Início de Turno, Idempotência com `git log`, contratos de schema/dados factuais, comandos de validação CLI no DoD e formato estrito de commit com `[KEY]`.
3. **Proteção Física de Branches:**
   - Instalar scripts `.git/hooks/pre-commit` e `.git/hooks/pre-push` impedindo mutações diretas na branch `main`.

### 🧪 DEFINITION OF DONE (DoD) & COMANDOS DE TERMINAL
- Matriz `docs/prompts/README.md` catalogando 100% dos épicos e tasks.
- 5 arquivos de épicos em `docs/prompts/epicos/`.
- 12 arquivos de tarefas em `docs/prompts/tasks/`.
- Hooks de proteção de branch ativos e executáveis.
- Issue GAS-17 criada, vinculada ao Épico GAS-1 e concluída no Jira.

### 📦 CONVENÇÃO DE COMMIT
`docs(prompts): catalogo de prompts canonico e governanca agentica [GAS-17]`
```

---

## 2. Histórico de Versões do Prompt
* **v1 (01/11/2026 — Concluído):** Criação inicial e padronização com base no projeto Tá na Lista.
