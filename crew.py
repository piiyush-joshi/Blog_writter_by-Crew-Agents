#part 4

from crewai import Crew, Process
from agents import news_researcher, news_writer
from tasks import research_task, write_task

crew = Crew(
    agents=[news_researcher, news_writer],
    tasks=[research_task, write_task],
    verbose=True,
    process=Process.sequential,
)


#starting the task wxcution process with enchanced feedback


result = crew.kickoff(inputs = {"topic":"Gen AI in Marketing."})

print("Crew execution result:", result)