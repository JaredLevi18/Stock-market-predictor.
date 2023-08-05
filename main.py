from parts_of_the_program import tools
from langchain.agents import AgentType, initialize_agent
from langchain.chat_models import ChatOpenAI
import os

os.environ["OPENAI_API_KEY"] = "" # Your API key here.

llm = ChatOpenAI(temperature=0.2)

agent = initialize_agent(
    tools=tools, llm=llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)

command = input("Enter the name of the company you'd like to know its stock price: ")
agent.run(command)
