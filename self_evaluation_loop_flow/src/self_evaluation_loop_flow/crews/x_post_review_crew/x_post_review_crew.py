from typing import Optional

from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from pydantic import BaseModel
from dotenv import load_dotenv

from self_evaluation_loop_flow.tools.CharacterCounterTool import CharacterCounterTool

# Uncomment the following line to use an example of a custom tool
# from x_post_review_crew.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

load_dotenv()

llm = LLM (
    model = 'gemini/gemini-1.5-flash-002',
    temperature=0.2
    )


class XPostVerification(BaseModel):
    valid: bool
    feedback: Optional[str]


@CrewBase
class XPostReviewCrew:
    """XPostReviewCrew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def x_post_verifier(self) -> Agent:
        return Agent(
            config=self.agents_config["x_post_verifier"],
            tools=[CharacterCounterTool()],
            llm = llm
        )

    @task
    def verify_x_post(self) -> Task:
        return Task(
            config=self.tasks_config["verify_x_post"],
            output_pydantic=XPostVerification,
        )

    @crew
    def crew(self) -> Crew:
        """Creates the XPostReviewCrew crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
