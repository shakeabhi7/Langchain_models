from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

from pydantic import BaseModel, Field
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser


load_dotenv()
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

class Person(BaseModel):
    name:str = Field(description='Name of the person')
    age:int = Field(description="Age of the person")
    city:str = Field(description="Name of the city the person belongs to")

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template = 'Generate the name, age and city of famous Cricketer {place} person \n {format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}

)

chain = template | llm | parser

final_result = chain.invoke({'place':'Nepal'})

print(final_result)
