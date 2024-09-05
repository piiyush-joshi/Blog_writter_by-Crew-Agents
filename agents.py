from crewai import Agent
from tools import tool

import os
from dotenv import load_dotenv
load_dotenv()
os.environ["AZURE_OPENAI_ENDPOINT"] = "https://documentsummary.openai.azure.com/"
os.environ["AZURE_OPENAI_API_KEY"] = os.getenv("AZURE_OPENAI_API_KEY")
#call the azureopeanimodel
#setup llm model
from langchain_openai import AzureChatOpenAI

llm = AzureChatOpenAI(
    azure_deployment="gpt4o",
    api_version="2024-02-15-preview",
    verbose= True,
    temperature=0.4,
    api_key= os.getenv("AZURE_OPENAI_API_KEY")
)


#creating a reacher agent with memory and verbose mode

news_researcher = Agent(
    role='Senior Researcher',
    goal='Uncover ground breaking technologies in {topic}',
    verbose=True,
    memory=True,
    llm=llm,
    backstory="""You are a senior researcher with a passion for discovering new technologies.
    You have a knack for unraveling complex theories and designing innovative solutions.""",
    tools = [],
    allow_delegation=True #(this allows the agent to delegate tasks & interact to other agents)
)

#creating a writer agent with custom tools responsible in writing news blog

news_writer = Agent(
    role='Tech News Writer',
    goal='Craft compelling tech news stories about {topic}',
    verbose=True,
    memory=True,
    llm=llm,
    backstory="""You are a renowned Tech News Writer, known for your insightful and engaging articles.
    You have a deep understanding of technology and its impact on society.""",
    tools = [],
    allow_delegation=False
)