from dotenv import load_dotenv

load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai.chat_models import ChatOpenAI
from tavily import TavilyClient

tavily = TavilyClient()  # Initialize the Tavily client

@tool
def search(query: str) -> str:
    """
    Tool that searches only sports activity related information over the internet
    Args:
        query: The query to search for Sport personlities and sports related information
    Returns:
        The search results
    """

    print(f"Searching for: {query}")
    return tavily.search(query)  # Use the Tavily client to perform the search

llm = ChatOpenAI(model="gpt-4")
tools = [search]  # Use the custom search tool instead of TavilySearch
agent = create_agent(model=llm, tools=tools)

# content = "Search for the latest news about Lionel Messi and Cristiano Ronaldo. Provide a brief summary of their recent performances, any injuries, and upcoming matches they are involved in."
content = "Search what is Donald Trump new tariff strategy after Supreme Court's decision"
def main():
    print("Welcome to Sport Search Agent!")
    response = agent.invoke({"messages":HumanMessage(content=content)})
    print(response)\
    
if __name__ == "__main__":
    main()