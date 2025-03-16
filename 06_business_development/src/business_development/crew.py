from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool, FileWriterTool
from dotenv import load_dotenv
load_dotenv()

# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class BusinessDevelopment():
	"""BusinessDevelopment crew"""

	# Learn more about YAML configuration files here:
	# Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
	# Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	# If you would like to add tools to your agents, you can learn more about it here:
	# https://docs.crewai.com/concepts/agents#agent-tools
	@agent
	def market_research_analyst_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['market_research_analyst_agent'],
			tools=[SerperDevTool()],
			verbose=True
		)
  
	@agent
	def tech_expert_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['tech_expert_agent'],
			verbose=True
		)
  
	@agent
	def business_consultant_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['business_consultant_agent'],
			verbose=True
		)

	@agent
	def file_writer(self) -> Agent:
		return Agent(
			config=self.agents_config['file_writer'],
			tools=[FileWriterTool()],
		)

	# To learn more about structured task outputs, 
	# task dependencies, and task callbacks, check out the documentation:
	# https://docs.crewai.com/concepts/tasks#overview-of-a-task
	@task
	def market_research_analysis_task(self) -> Task:
		return Task(
			config=self.tasks_config['market_research_analysis_task'],
		)
  
	@task
	def tech_expert_task(self) -> Task:
		return Task(
			config=self.tasks_config['tech_expert_task'],
		)
  
	@task
	def business_consulting_task(self) -> Task:
		return Task(
			config=self.tasks_config['business_consulting_task'],
		)

	@task
	def file_writer_task(self) -> Task:
		return Task(
			config=self.tasks_config['file_writer_task'],
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the BusinessDevelopment crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
