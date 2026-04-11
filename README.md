# 🤖 Agente de IA: Seu Mentor de Carreira em Tech

Repositório da live **"Crie um Agente de IA para Ser Seu Mentor de Carreira em Tech"**, onde usamos um agente de IA (OpenCode) para construir outro agente de IA (um mentor de carreira), tudo sem custo.

> Você não precisa saber programar para acompanhar. Esse é justamente o ponto.

## Pré-requisitos

- [OpenCode](https://opencode.ai) instalado (terminal ou desktop)
- [Ollama](https://ollama.com) instalado (opcional, apenas se quiser rodar IA localmente)
- [Python 3.12+](https://www.python.org/downloads/) instalado

> Em cada link acima você encontra as instruções de instalação para o seu sistema operacional (Windows, macOS ou Linux).

> Todo o código gerado durante a live está disponível neste repositório. Os arquivos `agent.py` e `requirements.txt` já estão prontos pra você baixar e experimentar.

---

## 1. Entendendo Agentes de IA

Esses termos aparecem o tempo todo e muita gente confunde:

| Conceito | O que faz | Exemplo |
|---|---|---|
| **Chatbot** | Responde perguntas com base em um modelo | ChatGPT respondendo "qual a capital da França" |
| **Assistente** | Chatbot com acesso a contexto pessoal | GitHub Copilot sugerindo código no seu projeto |
| **Copilot** | Assistente integrado a um fluxo de trabalho | Microsoft Copilot dentro do Excel |
| **Agente** | Toma decisões, usa ferramentas e age de forma autônoma | Um agente que pesquisa vagas, cruza com seu perfil e monta um plano de estudos |

A diferença central é o **grau de autonomia**. Um chatbot responde. Um agente *age*: ele analisa o problema, decide qual ferramenta usar, executa e avalia o resultado.

Hoje vimos isso acontecer duas vezes:

1. O **OpenCode**, um agente especializado em escrever código. Ele decidiu quais arquivos criar, quais comandos rodar, e fez tudo sozinho. Nós só descrevemos o que queríamos.
2. O **agente mentor**, que sabe consultar as carreiras da DIO e orientar alunos de forma personalizada.

---

## 2. Ferramentas Utilizadas

### OpenCode (o agente que codou pra gente)

O [OpenCode](https://opencode.ai) é um agente de IA open source para codificação. Ele entende o contexto do seu projeto, cria e edita arquivos, e executa comandos. Pense nele como um desenvolvedor que trabalha pra você.

O OpenCode oferece alguns **modelos gratuitos por tempo limitado**, o que é ótimo pra quem quer experimentar sem gastar nada. Basta abrir o OpenCode e rodar `/models` para ver as opções disponíveis.

### Ollama (IA local ou na nuvem, sem custo)

O [Ollama](https://ollama.com) permite rodar modelos de IA direto na sua máquina ou usar modelos gratuitos na nuvem. Na live usamos o `glm-5:cloud` (gratuito no Ollama Cloud) por ser mais rápido, mas se você tiver uma máquina com GPU ou não se importar com um tempo de resposta maior, modelos locais como o `qwen3:8b` funcionam bem pra experimentar no seu ritmo em casa.

Para conectar o OpenCode ao Ollama, o próprio Ollama faz a configuração automaticamente. No app do Ollama, basta buscar por **OpenCode** nas integrações. Pelo terminal, o comando é:

```bash
ollama launch opencode
```

Depois é só abrir o OpenCode, rodar `/models` e selecionar o modelo.

---

## 3. Construindo o Agente Mentor (com OpenCode)

Em vez de escrever código do zero, já deixamos a estrutura do agente pronta no arquivo `agent.py`. O que falta preencher são justamente as partes mais importantes: a identidade do agente e a tarefa que ele vai executar. E quem vai preencher isso pra gente é o OpenCode.

### Por que CrewAI? Por que Python?

Existem várias formas de criar agentes de IA, mas o **CrewAI** se destaca por ser intuitivo. Ele organiza cada agente como se fosse uma pessoa de verdade: com um papel, um objetivo, uma história e ferramentas que pode usar. Isso torna o código fácil de entender, mesmo pra quem nunca programou.

E o **Python** é a linguagem mais usada no mundo da IA, então praticamente tudo que você encontrar sobre o tema vai estar nessa linguagem. É o caminho natural.

### A estrutura do agente

O arquivo `agent.py` já tem toda a parte técnica configurada (LLM, ferramenta, execução). O que deixamos em aberto são os campos que definem *quem* o agente é:

```python
mentor = Agent(
    role="",       # Qual o papel desse agente?
    goal="",       # Qual o objetivo principal dele?
    backstory="",  # Qual a história por trás dele?
    tools=[ferramenta_dio],
    llm=llm,
    verbose=True
)

tarefa = Task(
    description="",       # O que o agente deve fazer?
    expected_output="",   # O que esperamos como resultado?
    agent=mentor
)
```

Esses campos são o coração de qualquer agente no CrewAI:

- **role** = qual o papel do agente (ex: "Mentor de Carreira em Tecnologia")
- **goal** = o que ele busca alcançar
- **backstory** = o contexto que guia suas respostas
- **description** = o que ele deve fazer nesta tarefa
- **expected_output** = o que esperamos como resultado

### Preenchendo com OpenCode

Dentro do OpenCode (usando um modelo gratuito pra ter mais agilidade), pedimos pra ele preencher os TODOs:

```
Preencha os campos vazios (role, goal, backstory, description e
expected_output) do arquivo agent.py.

O agente deve atuar como um mentor de carreira em tecnologia, orientando
alunos que estão começando ou migrando para a área de tecnologia com
base nas carreiras disponíveis na DIO (dio.me).

Mantenha os textos em português do Brasil, simples e diretos.
Não altere nada além dos campos vazios.
```

> Os resultados da live estão registrados em [`RESULT.md`](RESULT.md).

### Executando o agente

```bash
# Se estiver usando o Ollama via terminal (o app já faz isso automaticamente)
ollama serve

# Instalar dependências e rodar
pip install -r requirements.txt
python agent.py
```

### Versionando com OpenCode

O OpenCode também pode nos ajudar a versionar e publicar o código. Como o repositório já existe no GitHub, basta pedir:

```
Faça o commit de todos os arquivos e publique no repositório
digitalinnovationone/live-ai-agent-career-mentor no GitHub.
```

> Repositório: [github.com/digitalinnovationone/live-ai-agent-career-mentor](https://github.com/digitalinnovationone/live-ai-agent-career-mentor)

---

## 4. O Panorama: de Código a Assistentes Pessoais

O que fizemos hoje foi usar um agente (OpenCode) para construir outro agente (mentor de carreira). Isso já demonstra o poder do conceito, mas é só o começo.

O [OpenClaw](https://openclaw.ai) leva essa ideia para outro nível. Enquanto o OpenCode é um agente especializado em código, o OpenClaw é um agente pessoal completo: ele roda na sua máquina, se conecta com WhatsApp, Telegram, e-mail, calendário, e pode aprender novas habilidades sob demanda.

A base é a mesma: um modelo de IA (que pode ser local via Ollama), ferramentas que o agente pode usar, e autonomia para decidir como agir. A diferença está no escopo: o OpenCode age no seu código, o agente mentor age nas carreiras da DIO, e o OpenClaw age na sua vida digital inteira.

---

## Recapitulando

1. **Agentes não são chatbots sofisticados.** A diferença está na autonomia: agentes decidem, usam ferramentas e agem.
2. **Rodar IA sem custo é possível.** Seja com modelos gratuitos na nuvem ou rodando local com Ollama.
3. **Você não precisa saber programar para criar um agente.** O OpenCode desbloqueia a barreira técnica, e o CrewAI gera código legível o suficiente pra você entender cada pedaço.
4. **O ecossistema está evoluindo rápido.** Do OpenCode (agente de código) ao OpenClaw (agente pessoal), as possibilidades só crescem.

## Links Úteis

- [DIO](https://dio.me)
- [Ollama](https://ollama.com)
- [OpenCode](https://opencode.ai)
- [OpenClaw](https://openclaw.ai)
- [CrewAI Docs](https://docs.crewai.com)
