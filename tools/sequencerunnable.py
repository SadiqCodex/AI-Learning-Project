from dotenv import load_dotenv
import os

load_dotenv()

from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


# 1. Prompt Template
prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in simple words"
)

# 2. Model
ollama_base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
ollama_model = os.getenv("OLLAMA_CHAT_MODEL", "phi3:latest")
model = ChatOllama(model=ollama_model, base_url=ollama_base_url, temperature=0)

# 3. Output Parser
parser = StrOutputParser()


chain = prompt | model | parser

result = chain.invoke("Machine Learning")
print(result)

