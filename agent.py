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
    role="Mentor de Carreira em Tecnologia",       # Qual o papel desse agente?
    goal="Orientar alunos sobre carreiras em tecnologia disponíveis na DIO",       # Qual o objetivo principal dele?
    backstory="Você é um mentor experiente na área de tecnologia, com amplo conhecimento sobre o mercado de trabalho e as trilhas de carreiras oferecidas pela DIO. Ajudou dezenas de alunos a iniciarem ou migrarem para carreiras em tecnologia.",  # Qual a história por trás dele?
    tools=[ferramenta_dio],
    llm=llm,
    verbose=True
)

# Input do aluno
print("=== Mentor de Carreira em Tecnologia ===\n")
necessidade_aluno = input("Conte sobre sua situação atual e o que você busca na área de tecnologia:\n> ")

# TODO: Defina a Tarefa do agente
tarefa = Task(
    description=f"Analise as carreiras disponíveis na DIO e forneça orientações baseadas na seguinte necessidade do aluno: '{necessidade_aluno}'",       # O que o agente deve fazer?
    expected_output="Um texto orientativo e personalizado com recomendações de carreiras em tecnologia, explicando os benefícios de cada trilha e os próximos passos para o aluno.",   # O que esperamos como resultado?
    agent=mentor
)

# Execução
crew = Crew(agents=[mentor], tasks=[tarefa])
resultado = crew.kickoff()
print("\n=== Resultado ===\n")
print(resultado)
