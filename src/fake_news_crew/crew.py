import os
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun

ddg_search = DuckDuckGoSearchRun()

@tool("Cautare pe Internet")
def internet_search_tool(query: str) -> str:
    """Folosește această unealtă pentru a căuta informații pe internet despre un subiect."""
    return ddg_search.invoke(query)


@CrewBase
class FakeNewsCrew():
    
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    def __init__(self):
        self.llm = LLM(
            model="groq/llama-3.3-70b-versatile",
            api_key=os.environ.get("GROQ_API_KEY"),
            temperature=0.1
        )

    # --- AGENȚI ---
    @agent
    def jurnalist(self) -> Agent:
        return Agent(
            config=self.agents_config['jurnalist'], 
            tools=[internet_search_tool], 
            llm=self.llm,
            verbose=True
        )
    
    @agent
    def fact_checker(self) -> Agent:
        return Agent(
            config=self.agents_config['fact_checker'], 
            llm=self.llm,
            verbose=True
        )
    
    @agent
    def redactor(self) -> Agent:
        return Agent(
            config=self.agents_config['redactor'],
            llm=self.llm,
            verbose=True
        )
    
    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task']
        )

    @task
    def fact_check_task(self) -> Task:
        return Task(
            config=self.tasks_config['fact_check_task']
        )

    @task
    def reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config['reporting_task'], 
            output_file='raport_final.md'
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
    