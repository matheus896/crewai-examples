from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import FirecrawlScrapeWebsiteTool, SerperDevTool
from dotenv import load_dotenv
from noob_research_crew.tools.tavily_search_tool import TavilySearchTool
from noob_research_crew.tools.youtube_search_tool import (
    YoutubeVideoSearchAndDetailsTool,
)


# Carregando variáveis de ambiente
load_dotenv()

llm = LLM(model="gemini/gemini-1.5-pro")


@CrewBase
class NoobResearchCrew:
    """NoobResearchCrew crew"""

    # YAML Configurations
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["researcher"],
            tools=[
                SerperDevTool(),
                TavilySearchTool(),
                FirecrawlScrapeWebsiteTool(),
                YoutubeVideoSearchAndDetailsTool(),
            ],
            verbose=True,
            llm=llm,
        )

    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(config=self.agents_config["reporting_analyst"], verbose=True, llm=llm,)

    @task
    def research_task(self) -> Task:
        return Task(config=self.tasks_config["research_task"])

    @task
    def reporting_task(self) -> Task:
        return Task(config=self.tasks_config["reporting_task"], output_file="report.md")

    @crew
    def crew(self) -> Crew:
        """Creates the NoobResearchCrew crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
