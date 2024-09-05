#part 2 tools
#install crewai_tools

import os
from dotenv import load_dotenv
load_dotenv()

os.environ["SERPER_API_KEY"]= os.getenv("SERPER_API_KEY")

from crewai_tools import SerperDevTool

# Initialize the tool for internet searching capabilities
tool = SerperDevTool()