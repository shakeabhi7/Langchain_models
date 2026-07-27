from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import TextLoader
load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"

)

prompt = PromptTemplate(
    template="Write a summary for the following poem - \n {poem}",
    input_variables=['poem']
)

parser = StrOutputParser()

loader = TextLoader('cricket.txt',encoding='utf-8')

docs = loader.load()

print(type(docs))
print(len(docs))
print(docs[0].metadata)

chain = prompt | llm | parser

print(chain.invoke({'poem':docs[0].page_content}))