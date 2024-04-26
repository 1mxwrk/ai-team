from crewai import Agent, Task, Process, Crew
from crewai.project import CrewBase, agent, crew, task
from langchain_groq import ChatGroq
import financial_analyst_crew.utils as utils

@CrewBase
class FinancialAnalystCrew():
    """Financial Analyst Crew"""
    agent_config = utils.get_config('src/financial_analyst_crew/config/agents.yaml')
    task_config = utils.get_config('src/financial_analyst_crew/config/tasks.yaml')

    # agent_config = 'config/agents.yaml'
    # task_config = 'config/tasks.yaml'

    def __init__(self) -> None:
        self.groq_llm = ChatGroq(temperature=0, model_name='mixtral-8x7b-32768')

    @agent
    def company_researcher(self) -> Agent:
        return Agent(
            config = self.agent_config['company_researcher'],
            llm = self.groq_llm
        )

    @agent
    def company_analyst(self) -> Agent:
        return Agent(
            config = self.agent_config['company_analyst'],
            llm = self.groq_llm
        )
    
    @task
    def research_company_task(self) -> Task:
        return Task(
            config = self.task_config['research_company_task'],
            agent = self.company_researcher()
        )
    
    @task
    def analyze_company_task(self) -> Task:
        return Task(
            config = self.task_config['analyse_company_task'],
            agent = self.company_analyst()
        )
    
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents = self.agents,
            tasks = self.tasks,
            process = Process.sequential,
            verbose = 2        
        )