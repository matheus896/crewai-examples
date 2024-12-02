from crewai import Agent, Crew, Process, Task, LLM
from crewai_tools import PDFSearchTool
from dotenv import load_dotenv
from langchain_ollama import OllamaEmbeddings

embeddings = OllamaEmbeddings(model="nomic-embed-text:latest", base_url="http://localhost:11434")


load_dotenv()

llm = LLM (
    model = "cerebras/llama3.1-70b",
    temperature=0.1
    )

# --- Tools ---
pdf_search_tool = PDFSearchTool(
    pdf="./example_home_inspection.pdf",
    config=dict(
        embedder=dict(provider="ollama", config=dict(model="nomic-embed-text:latest")))
)

# --- Agents ---
research_agent = Agent(
    role="Agente de Pesquisa",
    goal="Pesquisar no PDF para encontrar respostas relevantes",
    allow_delegation=False,
    verbose=True,
    backstory=(
        """
        O agente de pesquisa é especialista em buscar e extrair dados de documentos,
        garantindo respostas precisas e rápidas.
        """
    ),
    tools=[pdf_search_tool],
    llm = llm
)

professional_writer_agent = Agent(
    role="Escritor Profissional",
    goal="Escrever e-mails profissionais com base nas descobertas do agente de pesquisa",
    allow_delegation=False,
    verbose=True,
    backstory=(
        """
        O agente escritor profissional possui excelentes habilidades de escrita e é capaz de
        criar e-mails claros e concisos com base nas informações fornecidas.
        """
    ),
    tools=[],
    llm = llm
)

# --- Tasks ---
answer_customer_question_task = Task(
    description=(
        """
        Responda às perguntas do cliente com base no PDF da inspeção domiciliar.
        O agente de pesquisa pesquisará no PDF para encontrar as respostas relevantes.
        Sua resposta final DEVE ser clara e precisa, com base no conteúdo do PDF da inspeção domiciliar.

        Aqui está a pergunta do cliente:
        {customer_question}
        """
    ),
    expected_output="""
        Forneça respostas claras e precisas às perguntas do cliente com base no conteúdo do PDF da inspeção domiciliar.
        """,
    tools=[pdf_search_tool],
    agent=research_agent,
)

write_email_task = Task(
    description=(
        """
        Escreva um e-mail profissional para um empreiteiro com base nas descobertas do agente de pesquisa.
        O e-mail deve declarar claramente os problemas encontrados na seção especificada do relatório e solicitar
        um orçamento ou plano de ação para corrigir esses problemas.

        Certifique-se de que o e-mail seja assinado com os seguintes detalhes:

        Atenciosamente,

        Brandon Hancock,
        Hancock Realty
        """
    ),
    expected_output="""
        Escreva um e-mail claro e conciso que possa ser enviado a um empreiteiro para abordar os problemas encontrados
        no relatório de inspeção domiciliar.
        """,
    tools=[],
    agent=professional_writer_agent,
)


# --- Crew ---
crew = Crew(
    tasks=[answer_customer_question_task, write_email_task],
    agents=[research_agent, professional_writer_agent],
    process=Process.sequential,
)

customer_question = input(
    "Para qual seção do relatório você gostaria de gerar uma ordem de serviço?\n"
)
result = crew.kickoff(inputs={"customer_question": customer_question})
print(result)
