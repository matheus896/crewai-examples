from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from dotenv import load_dotenv

from self_evaluation_loop_flow.tools.CharacterCounterTool import CharacterCounterTool

load_dotenv()

llm = LLM (
    model = 'gemini/gemini-1.5-flash-002',
    temperature=0.2
    )


@CrewBase
class ShakespeareCrew:
    """ShakespeareCrew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def shakespearean_bard(self) -> Agent:
        return Agent(
            config=self.agents_config["shakespearean_bard"],
            tools=[CharacterCounterTool()],
            llm = llm,
        )

    @task
    def write_x_post(self) -> Task:
        return Task(
            config=self.tasks_config["write_x_post"],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the ShakespeareCrew crew"""
        return Crew(
            agents=self.agents,  # Automaticamente criado por @agent decorator
            tasks=self.tasks,  # Automaticamente criado por @task decorator
            process=Process.sequential,
            verbose=True,
        )
