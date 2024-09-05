#part 3 

from crewai import Task
from tools import tool
from agents import news_researcher, news_writer, llm

research_task = Task(
    description="""
    Conduct a comprehensive research analysis on the topic of {topic}.
    Gather relevant data, perform data analysis, and provide a detailed report on the topic.
    The report should include a summary of the findings, any significant findings, and recommendations for further investigation.
    """,
    expected_output="A comprehensive 3 para long research report on the topic.",
    tools=[tool],
    agent=news_researcher,
)

#write task with language model configuration
write_task = Task(
    description="""
    Write an engaging tech news article on {topic} based on the research report provided.
    The article should be well-structured, informative, and visually appealing.
    """,
    expected_output="A 4-5 para long tech news article on the topic.",
    tools=[tool],
    agent=news_writer,
    async_execution=False, #optional
    output_file="news_article.txt", #optional
)