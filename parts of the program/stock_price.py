from langchain.agents import AgentType, initialize_agent
from langchain.tools import Tool
from langchain.tools import DuckDuckGoSearchRun

search_stock = DuckDuckGoSearchRun()

tools = [
    Tool.from_function(
        func=search_stock.run,
        name="Search Stock price",
        description="Useful for when you need to know a stock's price on the internet",
    ),
]
