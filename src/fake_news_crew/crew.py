from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class FakeNewsCrew():
    
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    def __init__(self):
        self.llm = LLM(
            model="ollama/llama3.2",
            base_url="http://localhost:11434",
            temperature=0.1
        )

    @agent
    def jurnalist(self) -> Agent:
        return Agent(
            config=self.agents_config['jurnalist'], 
            llm=self.llm,
            allow_delegation=False,
            verbose=True
        )
    
    @agent
    def fact_checker(self) -> Agent:
        return Agent(
            config=self.agents_config['fact_checker'], 
            llm=self.llm,
            allow_delegation=False,
            verbose=True
        )
    
    @agent
    def redactor(self) -> Agent:
        return Agent(
            config=self.agents_config['redactor'],
            llm=self.llm,
            allow_delegation=False,
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