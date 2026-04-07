# 🤖 Agente de IA: Seu Mentor de Carreira em Tech

Repositório da live **"Crie um Agente de IA para Ser Seu Mentor de Carreira em Tech"**, onde usamos um agente de IA (OpenCode) para construir outro agente de IA (um mentor de carreira), tudo rodando 100% local e gratuito com Ollama.

> Você não precisa saber programar para acompanhar. Esse é justamente o ponto.

## O que vamos construir?

Um agente de IA que funciona como mentor de carreira personalizado. Você pergunta algo como _"Quero migrar pra área de dados, por onde começo?"_ e o agente responde com orientações práticas baseadas nas carreiras da [DIO](https://dio.me).

O diferencial: quem vai escrever o código do agente não somos nós, é outro agente de IA.

---

## 1. Entendendo Agentes de IA

Antes de qualquer coisa, vale organizar o vocabulário. Esses termos aparecem o tempo todo e muita gente confunde:

| Conceito | O que faz | Exemplo |
|---|---|---|
| **Chatbot** | Responde perguntas com base em um modelo | ChatGPT respondendo "qual a capital da França" |
| **Assistente** | Chatbot com acesso a contexto pessoal | GitHub Copilot sugerindo código no seu projeto |
| **Copilot** | Assistente integrado a um fluxo de trabalho | Microsoft Copilot dentro do Excel |
| **Agente** | Toma decisões, usa ferramentas e age de forma autônoma | Um agente que pesquisa vagas, cruza com seu perfil e monta um plano de estudos |

A diferença central é o **grau de autonomia**. Um chatbot responde. Um agente *age*: ele analisa o problema, decide qual ferramenta usar, executa e avalia o resultado.

Na prática, vamos ver dois exemplos concretos disso hoje:

1. O **OpenCode**, um agente que sabe escrever código (ele decide quais arquivos criar, quais comandos rodar, e faz tudo sozinho)
2. O **agente mentor** que vamos construir com CrewAI, que sabe consultar as carreiras da DIO e orientar alunos

---

## 2. Configurando o Ambiente Local

Tudo que usamos hoje roda na sua máquina. Sem conta, sem cartão de crédito, sem enviar dados pra ninguém.

### 2.1 Ollama (o cérebro)

O [Ollama](https://ollama.com) é quem roda o modelo de IA localmente.

```bash
# Instalação (macOS / Linux)
curl -fsSL https://ollama.com/install.sh | sh

# Windows: baixe em https://ollama.com/download
```

Depois de instalar, baixe um modelo. Na live vamos testar qual se sai melhor, mas um bom ponto de partida:

```bash
ollama pull qwen3:8b
```

> **Sobre hardware:** com 32GB de RAM roda tranquilo via CPU. Com 16GB funciona, mas modelos menores (como o `qwen3:4b`) são mais indicados. O Ollama gerencia tudo automaticamente.

### 2.2 OpenCode (o agente de código)

O [OpenCode](https://opencode.ai) é um agente de IA open source para codificação. Ele roda no terminal, entende o contexto do seu projeto, cria e edita arquivos, e executa comandos. Pense nele como um desenvolvedor que trabalha pra você.

```bash
# Instalação
curl -fsSL https://opencode.ai/install | bash
```

### 2.3 Conectando OpenCode ao Ollama

Para que o OpenCode use o modelo local em vez de uma API na nuvem, crie (ou edite) o arquivo de configuração:

```bash
mkdir -p ~/.config/opencode
```

Crie o arquivo `~/.config/opencode/opencode.json`:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "ollama": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Ollama (local)",
      "options": {
        "baseURL": "http://localhost:11434/v1"
      },
      "models": {
        "qwen3:8b": {
          "name": "Qwen3 8B"
        }
      }
    }
  }
}
```

> **Dica:** o Ollama usa por padrão uma janela de contexto de 4K tokens, que pode ser pouco para o OpenCode. Para aumentar, rode: `ollama run qwen3:8b`, depois `/set parameter num_ctx 16384`, e por fim `/save qwen3:8b`. Isso garante que o agente tenha contexto suficiente para trabalhar.

Agora é só abrir o OpenCode e selecionar o modelo local:

```bash
opencode
# Dentro do OpenCode, use /models e selecione o Qwen3 8B
```

---

## 3. Construindo o Agente Mentor (com OpenCode)

Aqui está a parte mais legal: vamos pedir ao OpenCode para criar o agente mentor por nós. Ele vai gerar os arquivos Python, instalar as dependências, e montar tudo.

### O prompt

Dentro do OpenCode, digitamos algo como:

```
Crie um agente de IA usando CrewAI que funcione como mentor de carreira
em tecnologia. O agente deve:

1. Usar o Ollama como LLM (modelo local, sem API key)
2. Ter uma tool que faz scraping da página https://www.dio.me/#careers
   para consultar as carreiras disponíveis na DIO
3. Receber uma pergunta do usuário e responder com orientações
   personalizadas sobre qual carreira seguir

Use o ScrapeWebsiteTool do crewai-tools para simplificar o scraping.
Crie um arquivo agent.py com tudo pronto para rodar.
Crie também um requirements.txt com as dependências.
```

O OpenCode vai:
1. Criar o arquivo `requirements.txt`
2. Criar o arquivo `agent.py` com o agente configurado
3. Possivelmente rodar `pip install` e testar

### O que esperamos que o OpenCode gere

O código final deve ficar parecido com isso (o OpenCode pode gerar variações, e tudo bem):

```python
# agent.py
from crewai import Agent, Task, Crew
from crewai_tools import ScrapeWebsiteTool

# Ferramenta: consulta as carreiras direto do site da DIO
consultar_carreiras = ScrapeWebsiteTool(
    website_url="https://www.dio.me/#careers",
    name="Consultar Carreiras DIO",
    description="Consulta as carreiras e trilhas educacionais disponíveis na DIO (dio.me)."
)

# Definindo o Agente
mentor = Agent(
    role="Mentor de Carreira em Tecnologia",
    goal="Orientar pessoas que estão começando ou migrando para a área de tecnologia, "
         "recomendando trilhas de estudo da DIO de forma personalizada.",
    backstory="Você é um mentor experiente que conhece profundamente as carreiras em "
              "tecnologia e as trilhas educacionais da DIO. Você conversa de forma "
              "acessível, sem jargão desnecessário, e sempre considera o momento "
              "atual e os interesses de quem te procura.",
    tools=[consultar_carreiras],
    llm="ollama/qwen3:8b",
    verbose=True
)

# Definindo a Tarefa
tarefa = Task(
    description="O aluno disse: '{pergunta}'. "
                "Com base nas carreiras da DIO, oriente esse aluno de forma prática. "
                "Considere o nível de experiência, interesses e objetivos mencionados.",
    expected_output="Uma orientação clara com recomendação de trilha, tecnologias "
                    "iniciais e próximos passos concretos.",
    agent=mentor
)

# Montando a Crew e executando
crew = Crew(agents=[mentor], tasks=[tarefa], verbose=True)

resultado = crew.kickoff(inputs={
    "pergunta": "Trabalho com suporte técnico e quero migrar pra desenvolvimento. "
                "Gosto de lógica mas nunca programei profissionalmente."
})

print("\n===== RESPOSTA DO MENTOR =====\n")
print(resultado)
```

### Executando o agente

```bash
# Certifique-se de que o Ollama está rodando
ollama serve

# Em outro terminal, execute o agente
pip install -r requirements.txt
python agent.py
```

O `verbose=True` mostra na tela todo o raciocínio do agente: o que ele está "pensando", qual ferramenta decidiu usar, e o resultado de cada passo. É isso que diferencia um agente de um chatbot simples.

---

## 4. O Panorama: de Código a Assistentes Pessoais

O que fizemos hoje foi usar um agente (OpenCode) para construir outro agente (mentor de carreira). Isso já demonstra o poder do conceito, mas é só o começo.

O [OpenClaw](https://openclaw.ai) leva essa ideia para outro nível. Enquanto o OpenCode é um agente especializado em código, o OpenClaw é um agente pessoal completo: ele roda na sua máquina, se conecta com WhatsApp, Telegram, e-mail, calendário, e pode aprender novas habilidades (chamadas de *skills*) sob demanda.

O interessante é que a base é a mesma: um modelo de IA (que pode ser local via Ollama), ferramentas que o agente pode usar, e autonomia para decidir como agir. A diferença está no escopo: o OpenCode age no seu código, o agente mentor age nas carreiras da DIO, e o OpenClaw age na sua vida digital inteira.

Todos eles compartilham essa integração simples com o Ollama, o que significa que você pode experimentar tudo isso sem custo e com total privacidade dos seus dados.

---

## Recapitulando

1. **Agentes não são chatbots sofisticados.** A diferença está na autonomia: agentes decidem, usam ferramentas e agem.
2. **Rodar IA local é viável e gratuito.** Com Ollama e um computador com RAM razoável, você já prototipar sem depender de serviços pagos.
3. **Você não precisa saber programar para criar um agente.** Usando o OpenCode como intermediário, a construção do agente fica acessível para qualquer pessoa.
4. **O ecossistema está evoluindo rápido.** Do OpenCode (agente de código) ao OpenClaw (agente pessoal), as possibilidades só crescem.

## Links Úteis

- [DIO](https://dio.me)
- [Ollama](https://ollama.com)
- [OpenCode](https://opencode.ai)
- [OpenClaw](https://openclaw.ai)
- [CrewAI Docs](https://docs.crewai.com)
