# 🤖 Agente de IA: Seu Mentor de Carreira em Tech

Repositório da live **"Crie um Agente de IA para Ser Seu Mentor de Carreira em Tech"**, onde usamos um agente de IA (OpenCode) para construir outro agente de IA (um mentor de carreira), tudo sem custo.

> Você não precisa saber programar para acompanhar. Esse é justamente o ponto.

## Pré-requisitos

- [OpenCode](https://opencode.ai) instalado (terminal ou desktop)
- [Ollama](https://ollama.com) instalado (opcional, apenas se quiser rodar IA localmente)
- [Python 3.12+](https://www.python.org/downloads/) instalado

> Em cada link acima você encontra as instruções de instalação para o seu sistema operacional (Windows, macOS ou Linux).

> Todo o código gerado durante a live está disponível neste repositório pra você consultar depois.

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

### Ollama (IA rodando 100% local)

O [Ollama](https://ollama.com) permite rodar modelos de IA direto na sua máquina. Sem internet, sem conta, sem cartão de crédito. É mais lento que um modelo na nuvem (especialmente sem GPU), mas o custo é zero pra sempre.

Depois de instalar o app, basta buscar e baixar um modelo. Na live usamos o `qwen3:4b`, que é leve e funciona bem mesmo em computadores mais modestos.

Para conectar o OpenCode ao Ollama, o próprio Ollama faz a configuração automaticamente. No app do Ollama, basta buscar por **OpenCode** nas integrações. Pelo terminal, o comando é:

```bash
ollama launch opencode
```

Depois é só abrir o OpenCode, rodar `/models` e selecionar o modelo local.

---

## 3. Construindo o Agente Mentor (com OpenCode)

Aqui começa a parte mais interessante. Em vez de escrever código manualmente, descrevemos o que queremos pro OpenCode e deixamos ele trabalhar. Esse é o poder de usar um agente como intermediário: ele desbloqueia a barreira técnica e permite que qualquer pessoa curiosa consiga transformar uma ideia em algo funcional.

### Por que CrewAI? Por que Python?

Existem várias formas de criar agentes de IA, mas o **CrewAI** se destaca por ser intuitivo. Ele organiza cada agente como se fosse uma pessoa de verdade: com um papel, um objetivo, uma história e ferramentas que pode usar. Isso torna o código gerado fácil de entender, mesmo pra quem nunca programou.

E o **Python** é a linguagem mais usada no mundo da IA, então praticamente tudo que você encontrar sobre o tema vai estar nessa linguagem. É o caminho natural.

Quando mencionamos essas escolhas no prompt, não estamos exigindo conhecimento técnico de quem está assistindo. Estamos sendo específicos com o agente (OpenCode) pra que ele gere o melhor resultado possível. É como pedir um prato num restaurante: quanto mais detalhes você dá, melhor sai.

### O prompt

Dentro do OpenCode, descrevemos o que queremos:

```
Crie um agente de IA com Python e o framework CrewAI que funcione como um mentor de carreira em tecnologia.

Esse agente precisa acessar a página https://www.dio.me/#careers para conhecer as carreiras disponíveis na plataforma DIO e,
com base nessas informações, orientar alunos que estão começando ou migrando para a área de tecnologia.

Regras:
- Use uma ferramenta nativa do CrewAI para acessar a página da DIO
- O código deve ser SUPER simples e didático (não exagere em comentários e/ou prompts)
- Todos os atributos do agente, bem como comentários importantes, devem estar em português do Brasil
- O agente deve rodar usando o Ollama como LLM local (modelo qwen3:8b)
- Gere APENAS dois arquivos: agent.py e requirements.txt
- Use o mínimo de dependências possível e sempre as mais recentes
- Não modifique nenhum outro arquivo do repositório
```

### Resultado: modelo gratuito (nuvem)

> _Espaço reservado para o resultado gerado durante a live usando um modelo gratuito do OpenCode._

```
TODO: colar aqui o output do OpenCode usando modelo gratuito
```

### Resultado: modelo local (Ollama)

> _Espaço reservado para o resultado gerado durante a live usando o Ollama localmente._

```
TODO: colar aqui o output do OpenCode usando Ollama
```

### Entendendo o código gerado

Independente do modelo usado, o código gerado pelo OpenCode segue a estrutura do CrewAI. Mesmo sem saber programar, dá pra entender o que está acontecendo:

- **role** = qual o papel do agente (ex: "Mentor de Carreira em Tecnologia")
- **goal** = o que ele busca alcançar
- **backstory** = o contexto que guia suas respostas
- **tools** = o que ele pode acessar (nesse caso, o site da DIO)

Essa clareza é proposital. O CrewAI foi pensado pra que a estrutura de um agente faça sentido até pra quem não programa.

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
