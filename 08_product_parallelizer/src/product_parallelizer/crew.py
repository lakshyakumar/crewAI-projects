from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool, ScrapeWebsiteTool, FileWriterTool
from dotenv import load_dotenv
load_dotenv()

# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class ProductParallelizer():
	"""ProductParallelizer crew"""

	# Learn more about YAML configuration files here:
	# Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
	# Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	# If you would like to add tools to your agents, you can learn more about it here:
	# https://docs.crewai.com/concepts/agents#agent-tools
	@agent
	def retrieve_product(self) -> Agent:
		return Agent(
			config=self.agents_config['retrieve_product'],
			tools=[SerperDevTool()],
			verbose=True
		)

	@agent
	def website_scraper(self) -> Agent:
		return Agent(
			config=self.agents_config['website_scraper'],
   			tools=[ScrapeWebsiteTool()],
			verbose=True
		)
  
	@agent
	def product_analyzer_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['product_analyzer_agent'],
			verbose=True
		)
  
	@agent
	def tech_analyzer_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['tech_analyzer_agent'],
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
	def retrieve_product_task(self) -> Task:
		return Task(
			config=self.tasks_config['retrieve_product_task'],
		)

	@task
	def website_scraper_task(self) -> Task:
		return Task(
			config=self.tasks_config['website_scraper_task'],
		)
  
	@task
	def product_analyzer_task(self) -> Task:
		return Task(
			config=self.tasks_config['product_analyzer_task'],
		)
  
	@task
	def tech_analyzer_task(self) -> Task:
		return Task(
			config=self.tasks_config['tech_analyzer_task'],
		)
  
	@task
	def file_writer_task(self) -> Task:
		return Task(
			config=self.tasks_config['file_writer_task'],
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the ProductParallelizer crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
