# Roteiro da Live (~1h)

## Abertura (~5 min)
- Provocação: _"Vamos usar um agente de IA pra criar outro agente de IA, e você não precisa saber programar pra acompanhar"_
- Mostrar o repositório no GitHub
- Clonar o repo como workspace

## Bloco 1: O que são Agentes de IA? (~10 min)
- Tabela: chatbot → assistente → copilot → agente
- Palavra-chave: **autonomia** (_"Chatbot responde. Agente age."_)
- Apresentar os dois agentes do dia: OpenCode e o Agente Mentor

## Bloco 2: Ferramentas (~15 min)
- Abrir o OpenCode, mostrar modelos gratuitos disponíveis (`/models`)
- Ollama: abrir o app, mostrar o `glm-5:cloud` (gratuito)
- _"Na live vou usar modelos na nuvem pra ser mais rápido, mas em casa vocês podem rodar local com um modelo como o qwen3:8b"_

## Bloco 3: Construindo o Agente (~25 min)
- Abrir o `agent.py`, mostrar a estrutura e os TODOs
- Explicar cada campo: role, goal, backstory, description, expected_output
- Pedir pro OpenCode preencher os TODOs (modelo gratuito)
- Analisar o resultado juntos
- Rodar o agente: `pip install -r requirements.txt && python agent.py`
- Testar com pergunta do chat
- Versionar via OpenCode

## Fechamento (~5 min)
- Recapitular: autonomia, custo zero, sem precisar programar, ecossistema crescendo
- Paralelo rápido com OpenClaw (mesmo conceito, escopo maior)
- Compartilhar link do repositório

---

### Checklist pré-live
- [ ] Ollama app rodando + `glm-5:cloud` disponível
- [ ] OpenCode instalado + modelo gratuito configurado
- [ ] Ollama conectado ao OpenCode (`ollama launch opencode`)
- [ ] Python 3.12+ instalado
- [ ] Repositório clonado (`digitalinnovationone/live-ai-agent-career-mentor`)
- [ ] Terminal limpo, fontes grandes
