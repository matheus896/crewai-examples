# créditos: https://github.com/crewAIInc/crewAI-examples/tree/main/surprise_trip/src/surprise_travel

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Importando módulos necessários
import sys
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from litellm import completion
from pydantic import BaseModel, Field
from typing import List, Optional
from dotenv import load_dotenv

load_dotenv()

llm = LLM (
    model = 'cerebras/llama3.1-70b',
    temperature=0.2
    )

# Definindo classes para organizar os dados das atividades e itinerário
class Activity(BaseModel):
    name: str = Field(..., description="Nome da atividade")
    location: str = Field(..., description="Localização da atividade")
    description: str = Field(..., description="Descrição da atividade")
    date: str = Field(..., description="Data da atividade")
    cuisine: str = Field(..., description="Culinária do restaurante")
    why_its_suitable: str = Field(..., description="Por que é adequado para o viajante")
    reviews: Optional[List[str]] = Field(..., description="Lista de avaliações")
    rating: Optional[float] = Field(..., description="Avaliação da atividade")

class DayPlan(BaseModel):
    date: str = Field(..., description="Data do dia")
    activities: List[Activity] = Field(..., description="Lista de atividades")
    restaurants: List[str] = Field(..., description="Lista de restaurantes")
    flight: Optional[str] = Field(None, description="Informação do voo")

class Itinerary(BaseModel):
    name: str = Field(..., description="Nome do itinerário, algo divertido")
    day_plans: List[DayPlan] = Field(..., description="Lista de planos diários")
    hotel: str = Field(..., description="Informação do hotel")

# Classe principal para o crew de viagem surpresa
@CrewBase
class SurpriseTravelCrew():
    """SurpriseTravel crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def personalized_activity_planner(self) -> Agent:
        return Agent(
            config=self.agents_config['personalized_activity_planner'],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            verbose=True,
            allow_delegation=False,
            llm=llm,
        )

    @agent
    def restaurant_scout(self) -> Agent:
        return Agent(
            config=self.agents_config['restaurant_scout'],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            verbose=True,
            allow_delegation=False,
            llm=llm,
        )

    @agent
    def itinerary_compiler(self) -> Agent:
        return Agent(
            config=self.agents_config['itinerary_compiler'],
            tools=[SerperDevTool()],
            verbose=True,
            allow_delegation=False,
            llm=llm,
        )

    @task
    def personalized_activity_planning_task(self) -> Task:
        return Task(
            config=self.tasks_config['personalized_activity_planning_task'],
            agent=self.personalized_activity_planner()
        )

    @task
    def restaurant_scenic_location_scout_task(self) -> Task:
        return Task(
            config=self.tasks_config['restaurant_scenic_location_scout_task'],
            agent=self.restaurant_scout()
        )

    @task
    def itinerary_compilation_task(self) -> Task:
        return Task(
            config=self.tasks_config['itinerary_compilation_task'],
            agent=self.itinerary_compiler(),
            output_json=Itinerary
        )

    @crew
    def crew(self) -> Crew:
        """Cria a crew do SurpriseTravel"""
        return Crew(
            agents=self.agents,  # Criado automaticamente pelo decorador @agent
            tasks=self.tasks,  # Criado automaticamente pelo decorador @task
            process=Process.sequential,
            verbose=True,
        )

# Função principal que executa o script
def run():
    # Substitua pelos seus inputs, eles serão interpolados automaticamente nas informações de tarefas e agentes
    inputs = {
        'origin': 'São Paulo, GRU',  # Origem da viagem
        'destination': 'New York, JFK',  # Destino da viagem
        'age': 25,  # Idade do viajante
        'hotel_location': 'Brooklyn',  # Localização do hotel
        'flight_information': 'LATAM 1234, leaving at november 30th, 2024, 10:00',  # Informações do voo
        'trip_duration': '14 days'  # Duração da viagem
    }
    
    # Inicializa a tripulação e executa o plano de ação com os inputs fornecidos
    result = SurpriseTravelCrew().crew().kickoff(inputs=inputs)
    print(result)  # Imprime o resultado obtido

# Função para treinar a tripulação com um determinado número de iterações
def train():
    """
    Treina a tripulação com um determinado número de iterações.
    """
    inputs = {
        'origin': 'São Paulo, GRU',
        'destination': 'New York, JFK',
        'age': 31,
        'hotel_location': 'Brooklyn',
        'flight_information': 'LATAM 1234, leaving at november 30th, 2024, 10:00',
        'trip_duration': '14 days'
    }
    try:
        # Tenta treinar a tripulação com um número de iterações fornecido por argumento
        SurpriseTravelCrew().crew().train(n_iterations=int(sys.argv[1]), inputs=inputs)
    except Exception as e:
        # Em caso de erro, levanta uma exceção com a mensagem de erro
        raise Exception(f"Ocorreu um erro durante o treinamento da tripulação: {e}")

# Bloco principal que define a execução com base nos argumentos passados
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'train':
        train()  # Executa o treinamento caso o argumento seja "train"
    else:
        run()  # Caso contrário, executa a função principal "run"
