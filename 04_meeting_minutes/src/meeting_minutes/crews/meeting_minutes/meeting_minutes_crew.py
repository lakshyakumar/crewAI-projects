from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import FileWriterTool

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

file_writer_tool_summary = FileWriterTool(directory="meeting_minutes", filename="summary.txt")
file_writer_tool_action_items = FileWriterTool(directory="meeting_minutes", filename="action_items.txt")
file_writer_tool_sentiment = FileWriterTool(directory="meeting_minutes", filename="sentiment.txt")


@CrewBase
class MeetingMinutesCrew:
    """Meeting Minutes Crew"""

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    # If you would lik to add tools to your crew, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def meeting_minutes_summarizer(self) -> Agent:
        return Agent(
            config=self.agents_config["meeting_minutes_summarizer"],
            tools=[file_writer_tool_summary, file_writer_tool_action_items, file_writer_tool_sentiment],
        )
        
    @agent
    def meeting_minutes_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["meeting_minutes_writer"],
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def meeting_minutes_summarizer_task(self) -> Task:
        return Task(
            config=self.tasks_config["meeting_minutes_summarizer_task"],
        )
        
    @task
    def meeting_minutes_writer_task(self) -> Task:
        return Task(
            config=self.tasks_config["meeting_minutes_writer_task"],
        )
        
    

    @crew
    def crew(self) -> Crew:
        """Creates the Research Crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
