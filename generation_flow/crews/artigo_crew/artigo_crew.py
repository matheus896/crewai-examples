from crewai import Agent, Crew, Process, Task, LLM
from crewai_tools import SerperDevTool
from crewai.project import CrewBase, agent, crew, task
from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

llm = LLM(model='cerebras/llama3.1-70b')

search_tool = SerperDevTool()

@CrewBase
class ArtigoCrew():
    """Artigo Crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def pesquisador(self) -> Agent:
        return Agent(
            config=self.agents_config['pesquisador'],
            tools=[search_tool],
            llm=llm
        )
    
    @agent
    def escritor(self) -> Agent:
        return Agent(
            config=self.agents_config['escritor'],
            tools=[search_tool],
            llm=llm
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],
        )
    
    @task
    def write_task(self) -> Task:
        return Task(
            config=self.tasks_config['write_task'],
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            memory=True,
            embedder={
                "provider": "google",
                "config": {
                    "api_key": GOOGLE_API_KEY,
                    "model": "models/text-embedding-004"
                }
            }
        )
