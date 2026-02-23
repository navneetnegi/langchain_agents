

from typing import List
from pydantic import BaseModel, Field

from dotenv import load_dotenv
load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai.chat_models import ChatOpenAI
from langchain_tavily import TavilySearch
from tavily import TavilyClient

class Source(BaseModel):
    """
    Schema for the source used by agent
    """
    url: str = Field(description = "The URL of the source")

class AgentResponse(BaseModel):
    """
    Schema for the agent response
    """
    answer: str = Field(description = "The response of the agent")
    sources: List[Source] = Field(default_factory=list, description = "The list of sources used by the agent to generate the response")


# tavily = TavilyClient()  # Initialize the Tavily client

llm = ChatOpenAI(model="gpt-4")
tools = [TavilySearch()]  # Use the TavilySearch tool for searching over the internet
agent = create_agent(model=llm, tools=tools, response_format=AgentResponse)

content = "Search for 3 job listing for AI Engineer in New Delhi/NCR region on LinkedIn with experience in Python, Machine Learning, and Deep Learning. Provide the job title, company name, location, and a brief description of the job requirements."
def main():
    print("Hello from agents!")
    result = agent.invoke(
        {"messages":HumanMessage(
            content=content
            )
        }
    )
    print(result)

if __name__ == "__main__":
    main()