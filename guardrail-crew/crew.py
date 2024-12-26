from crewai import Agent, Task, Crew, Process, LLM
from crewai_tools import SerperDevTool
from dotenv import load_dotenv
from custom_tool import validate_summary # Custom Tool Guardrail AI
from pydantic import BaseModel

# Modelo Pydantic para a saída esperada
class SummaryOutput(BaseModel):
    summary: str

# Carregando variáveis de ambiente
load_dotenv()

llm = LLM(model="cerebras/llama3.1-70b")

# Criando o agente Pesquisador Web
web_researcher = Agent(
    role="Pesquisador Web",
    goal="Realizar pesquisas na web para encontrar informações confiáveis sobre {topic}.",
    verbose=True,
    backstory="Você é um pesquisador experiente, especializado em encontrar informações precisas rapidamente.",
    tools=[SerperDevTool()],
    llm=llm
)

# Criando o agente Redator de Resumos
summary_writer = Agent(
    role="Redator de Resumos",
    goal="Escrever um resumo informativo e coerente sobre {topic} com base nas informações fornecidas.",
    verbose=True,
    llm=llm,
    backstory="Você é um redator especializado em transformar informações complexas em resumos simples e envolventes."
)

# Criando o agente Validador de Resumos
summary_validator = Agent(
    role="Validador de Resumos",
    goal="Validar se o resumo atende aos critérios de qualidade (informativo, coerente, conciso e envolvente).",
    verbose=True,
    llm=llm,
    backstory="Você é um especialista em garantir a qualidade e conformidade dos resumos com os padrões exigidos.",
    tools=[validate_summary]
)

# Tarefa 1: Pesquisa Web
web_research_task = Task(
    description=(
        "Realizar uma pesquisa na web sobre o tópico: {topic}. "
        "Reúna informações confiáveis e relevantes para serem usadas em um resumo."
    ),
    expected_output="Um conjunto de informações relevantes sobre o tópico.",
    agent=web_researcher
)

# Tarefa 2: Escrever Resumo
write_summary_task = Task(
    description=(
        "Baseado nas informações fornecidas, escreva um resumo informativo e envolvente sobre o tópico: {topic}."
    ),
    expected_output="Um resumo claro e conciso sobre o tópico.",
    agent=summary_writer
)

# Ajustando a tarefa de validação
validate_summary_task = Task(
    description=(
        "Valide o resumo gerado utilizando critérios de qualidade. "
        "Certifique-se de que ele é informativo, coerente, conciso e envolvente."
    ),
    expected_output="Uma mensagem clara indicando sucesso ou falha na validação.",
    agent=summary_validator,
    output_json=SummaryOutput  # Configurando o modelo Pydantic
)

# Configuração do Workflow
crew = Crew(
    agents=[web_researcher, summary_writer, summary_validator],
    tasks=[web_research_task, write_summary_task, validate_summary_task],
    verbose=True,
    process=Process.sequential  # Execução sequencial
)

# Executando a Crew
inputs = {
    "topic": "impacto da inteligencia artificial nas mudanças climáticas"
}
result = crew.kickoff(inputs=inputs)

print(result)

