from dotenv import load_dotenv
import os

load_dotenv()
from langchain_ollama import ChatOllama
from langchain.tools import tool 
from langchain_core.messages import HumanMessage
from rich import print 

#1 creating a tool 

@tool
def get_text_length(text: str) -> int:
    """Returns the number of character in a given text"""
    return len(text)

tools = {
    "get_text_length" : get_text_length
}
ollama_base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
ollama_model = os.getenv("OLLAMA_CHAT_MODEL", "phi3:latest")
llm = ChatOllama(model=ollama_model, base_url=ollama_base_url, temperature=0)

#tool binding 
llm_with_tool = llm.bind_tools([get_text_length])

message = []
prompt = input("You: ")
query = HumanMessage(prompt)
message.append(query)

result = llm_with_tool.invoke(message)

message.append(result)

if result.tool_calls:
    tool_name = result.tool_calls[0]["name"]
    tool_message = tools[tool_name].invoke(result.tool_calls[0])
    message.append(tool_message)
   

result = llm_with_tool.invoke(message)
print(result.content)