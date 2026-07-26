from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

from pydantic import BaseModel, Field
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

class Facts(BaseModel):
    fact_1 : str = Field(description="Fact 1 about the topic")
    fact_2 : str = Field(description="Fact 2 about the topic")
    fact_3 : str = Field(description="Fact 3 about the topic")

structured_llm = llm.with_structured_output(Facts)

template = PromptTemplate(template="Give 3 facts about {topic}",
                          input_variables=["topic"])


chain = template | structured_llm

result = chain.invoke({"topic":"black hole"})

print(result)