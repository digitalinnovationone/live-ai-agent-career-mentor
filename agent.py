from crewai import Agent, Task, Crew, LLM
from crewai_tools import ScrapeWebsiteTool

# Configuração do LLM via Ollama
# Na live usamos "ollama/glm-5:cloud" (gratuito no Ollama Cloud)
# Para rodar local, troque para "ollama/qwen3:8b" ou outro modelo disponível
llm = LLM(
    model="ollama/glm-5:cloud",
    base_url="http://localhost:11434"
)

# Ferramenta para acessar a página de carreiras da DIO
ferramenta_dio = ScrapeWebsiteTool(
    website_url="https://www.dio.me/#careers"
)

# TODO: Defina o Agente Mentor de Carreira em Tecnologia
mentor = Agent(
    role="",       # Qual o papel desse agente?
    goal="",       # Qual o objetivo principal dele?
    backstory="",  # Qual a história por trás dele?
    tools=[ferramenta_dio],
    llm=llm,
    verbose=True
)

# TODO: Defina a Tarefa do agente
tarefa = Task(
    description="",       # O que o agente deve fazer?
    expected_output="",   # O que esperamos como resultado?
    agent=mentor
)

# Execução
crew = Crew(agents=[mentor], tasks=[tarefa])
resultado = crew.kickoff()
print("\n=== Resultado ===\n")
print(resultado)
