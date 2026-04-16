# 🤖 AI Agent: Your Tech Career Mentor

Repository for the live session **"Create an AI Agent to Be Your Tech Career Mentor"**, where we use an AI agent (OpenCode) to build another AI agent (a career mentor), all at no cost.

> You don't need to know how to code to follow along. That's exactly the point.

## Prerequisites

- [OpenCode](https://opencode.ai) installed (terminal or desktop)
- [Ollama](https://ollama.com) installed (optional, only if you want to run AI locally)
- [Python 3.12+](https://www.python.org/downloads/) installed

> Each link above contains installation instructions for your operating system (Windows, macOS, or Linux).

> All code generated during the live session is available in this repository. The `agent.py` and `requirements.txt` files are ready for you to download and experiment with.

---

## 1. Understanding AI Agents

These terms appear all the time and many people confuse them:

| Concept | What it does | Example |
|---|---|---|
| **Chatbot** | Answers questions based on a model | ChatGPT answering "what is the capital of France" |
| **Assistant** | Chatbot with access to personal context | GitHub Copilot suggesting code in your project |
| **Copilot** | Assistant integrated into a workflow | Microsoft Copilot inside Excel |
| **Agent** | Makes decisions, uses tools, and acts autonomously | An agent that researches job openings, cross-references with your profile, and creates a study plan |

The central difference is the **degree of autonomy**. A chatbot responds. An agent *acts*: it analyzes the problem, decides which tool to use, executes, and evaluates the result.

Today we saw this happen twice:

1. **OpenCode**, an agent specialized in writing code. It decided which files to create, which commands to run, and did everything by itself. We just described what we wanted.
2. The **mentor agent**, which knows how to query DIO careers and guide students in a personalized way.

---

## 2. Tools Used

### OpenCode (the agent that coded for us)

[OpenCode](https://opencode.ai) is an open source AI agent for coding. It understands your project context, creates and edits files, and executes commands. Think of it as a developer working for you.

OpenCode offers some **free models for a limited time**, which is great for those who want to experiment without spending anything. Just open OpenCode and run `/models` to see the available options.

### Ollama (local or cloud AI, at no cost)

[Ollama](https://ollama.com) allows you to run AI models directly on your machine or use free cloud models. In the live session, we used `glm-5:cloud` (free on Ollama Cloud) because it's faster, but if you have a machine with a GPU or don't mind longer response times, local models like `qwen3:8b` work well for experimenting at your own pace at home.

To connect OpenCode to Ollama, Ollama handles the configuration automatically. In the Ollama app, just search for **OpenCode** in the integrations. From the terminal, the command is:

```bash
ollama launch opencode
```

Then just open OpenCode, run `/models` and select the model.

---

## 3. Building the Mentor Agent (with OpenCode)

Instead of writing code from scratch, we've already prepared the agent structure in the `agent.py` file. What's missing are exactly the most important parts: the agent's identity and the task it will execute. And OpenCode will fill that in for us.

### Why CrewAI? Why Python?

There are several ways to create AI agents, but **CrewAI** stands out for being intuitive. It organizes each agent as if it were a real person: with a role, a goal, a backstory, and tools it can use. This makes the code easy to understand, even for those who have never programmed.

And **Python** is the most used language in the AI world, so practically everything you find on the subject will be in this language. It's the natural path.

### The agent structure

The `agent.py` file already has all the technical configuration (LLM, tool, execution). What we left open are the fields that define *who* the agent is:

```python
mentor = Agent(
    role="",       # What is this agent's role?
    goal="",       # What is its main objective?
    backstory="",  # What is the story behind it?
    tools=[ferramenta_dio],
    llm=llm,
    verbose=True
)

tarefa = Task(
    description="",       # What should the agent do?
    expected_output="",   # What do we expect as a result?
    agent=mentor
)
```

These fields are the heart of any agent in CrewAI:

- **role** = what is the agent's role (e.g., "Tech Career Mentor")
- **goal** = what it seeks to achieve
- **backstory** = the context that guides its responses
- **description** = what it should do in this task
- **expected_output** = what we expect as a result

### Filling in with OpenCode

Inside OpenCode (using a free model for more agility), we asked it to fill in the TODOs:

```
Fill in the empty fields (role, goal, backstory, description and
expected_output) in the agent.py file.

The agent should act as a technology career mentor, guiding
students who are starting or transitioning to the technology field
based on the careers available at DIO (dio.me).

Keep the texts in English, simple and direct.
Do not change anything other than the empty fields.
```

> The results from the live session are recorded in [`RESULT.md`](RESULT.md).

### Running the agent

```bash
# If using Ollama via terminal (the app does this automatically)
ollama serve

# Install dependencies and run
pip install -r requirements.txt
python agent.py
```

### Versioning with OpenCode

OpenCode can also help us version and publish the code. Since the repository already exists on GitHub, just ask:

```
Commit all files and publish to the repository
digitalinnovationone/live-ai-agent-career-mentor on GitHub.
```

> Repository: [github.com/digitalinnovationone/live-ai-agent-career-mentor](https://github.com/digitalinnovationone/live-ai-agent-career-mentor)

---

## 4. The Big Picture: From Code to Personal Assistants

What we did today was use an agent (OpenCode) to build another agent (career mentor). This already demonstrates the power of the concept, but it's just the beginning.

[OpenClaw](https://openclaw.ai) takes this idea to another level. While OpenCode is an agent specialized in code, OpenClaw is a complete personal agent: it runs on your machine, connects with WhatsApp, Telegram, email, calendar, and can learn new skills on demand.

The foundation is the same: an AI model (which can be local via Ollama), tools the agent can use, and autonomy to decide how to act. The difference is in the scope: OpenCode acts on your code, the mentor agent acts on DIO careers, and OpenClaw acts on your entire digital life.

---

## Recap

1. **Agents are not sophisticated chatbots.** The difference is in autonomy: agents decide, use tools, and act.
2. **Running AI at no cost is possible.** Whether with free cloud models or running locally with Ollama.
3. **You don't need to know how to program to create an agent.** OpenCode unlocks the technical barrier, and CrewAI generates readable enough code for you to understand each piece.
4. **The ecosystem is evolving fast.** From OpenCode (code agent) to OpenClaw (personal agent), the possibilities only grow.

## Useful Links

- [DIO](https://dio.me)
- [Ollama](https://ollama.com)
- [OpenCode](https://opencode.ai)
- [OpenClaw](https://openclaw.ai)
- [CrewAI Docs](https://docs.crewai.com)