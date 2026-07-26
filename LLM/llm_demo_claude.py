from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

llm = ChatAnthropic(model = 'claude-sonnet-4-6')

result = llm.invoke("What is Capital of India?")

print(result)