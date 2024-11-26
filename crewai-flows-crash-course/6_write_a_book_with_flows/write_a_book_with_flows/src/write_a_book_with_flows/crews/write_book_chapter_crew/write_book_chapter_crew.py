from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from write_a_book_with_flows.types import Chapter
from dotenv import load_dotenv
from datetime import datetime , timedelta

# Dicionário para rastrear as últimas consultas de cada termo
ultima_consulta_busca = {}
search_tool = SerperDevTool()

# Fun ção de cache personalizada
def funcao_cache(args, resultado):
    termo = args [0] # Primeiro argumento é o termo de busca
    agora = datetime.now ()
    # Verifica se o termo foi consultado nos ú ltimos 60 minutos
    if termo in ultima_consulta_busca :
        ultima_hora_consulta = ultima_consulta_busca [termo]
    if agora - ultima_hora_consulta < timedelta ( hours =1) :
        return True # cache se a ú ltima consulta foi menos de 1h
    ultima_consulta_busca [termo] = agora # ú ltima consulta
    return False # Não armazena em cache se passou mais de 1 hora

# Associa a função de cache à ferramenta SerperDevTool
search_tool.cache_function = funcao_cache

load_dotenv()

llm = LLM (
    model = 'gemini/gemini-1.5-flash-002',
    temperature=0.2
    )


@CrewBase
class WriteBookChapterCrew:
    """Write Book Chapter Crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def researcher(self) -> Agent:
        search_tool = SerperDevTool()
        return Agent(
            config=self.agents_config["researcher"],
            tools=[search_tool],
            llm=llm,
            verbose=True,
        )

    @agent
    def writer(self) -> Agent:
        return Agent(
            config=self.agents_config["writer"],
            llm=llm,
            verbose=True
        )

    @task
    def research_chapter(self) -> Task:
        return Task(
            config=self.tasks_config["research_chapter"],
        )

    @task
    def write_chapter(self) -> Task:
        return Task(config=self.tasks_config["write_chapter"], output_pydantic=Chapter)

    @crew
    def crew(self) -> Crew:
        """Creates the Write Book Chapter Crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
)

