from dotenv import load_dotenv

load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai.chat_models import ChatOpenAI
from tavily import TavilyClient
from langchain_tavily import TavilySearch

tavily = TavilyClient()  # Initialize the Tavily client
@tool
def search(query: str) -> str:
    """
    Tool that searches over the internet
    Args:
        query: The query to search for
    Returns:
        The search results
    """
    print(f"Searching for: {query}")
    return tavily.search(query)  # Use the Tavily client to perform the search

llm = ChatOpenAI(model="gpt-4")
# tools = [TavilySearch()]
tools = [search]  # Use the custom search tool instead of TavilySearch
agent = create_agent(model=llm, tools=tools)

content = "Search for LinkedIn job listing for AI Engineer in New Delhi/NCR region with experience in Python, Machine Learning, and Deep Learning. Provide the job title, company name, location, and a brief description of the job requirements."

def main():
    print("Hello from agents!")
    result = agent.invoke({"messages":HumanMessage(content=content)})
    print(result)

if __name__ == "__main__":
    main()
