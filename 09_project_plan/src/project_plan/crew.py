from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import FileWriterTool
from dotenv import load_dotenv
load_dotenv()

# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class ProjectPlan():
	"""ProjectPlan crew"""

	# Learn more about YAML configuration files here:
	# Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
	# Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	# If you would like to add tools to your agents, you can learn more about it here:
	# https://docs.crewai.com/concepts/agents#agent-tools
	@agent
	def project_planning_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['project_planning_agent'],
			verbose=True
		)

	@agent
	def estimation_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['estimation_agent'],
			verbose=True
		)

	@agent
	def resource_allocation_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['resource_allocation_agent'],
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
	def task_breakdown(self) -> Task:
		return Task(
			config=self.tasks_config['task_breakdown'],
		)
  
	@task
	def time_resource_estimation(self) -> Task:
		return Task(
			config=self.tasks_config['time_resource_estimation'],
		)

	@task
	def resource_allocation(self) -> Task:
		return Task(
			config=self.tasks_config['resource_allocation'],
			output_file='report.md'
		)
  
	@task
	def file_writer_task(self) -> Task:
		return Task(
			config=self.tasks_config['file_writer_task'],
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the ProjectPlan crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
