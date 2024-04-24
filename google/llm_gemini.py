import os
# import time
# import getpass
from dotenv import load_dotenv
# import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain.prompts import PromptTemplate
# from langchain.chains import LLMChain
# from langchain.memory import ConversationBufferMemory
# from langchain_community.utilities import WikipediaAPIWrapper
from langchain_core.messages import HumanMessage, SystemMessage


load_dotenv() 

os.environ["GOOGLE_API_KEY"] = os.getenv('GOOGLE_API_KEY')

# test
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest", temperature=0.9)
# result = llm.invoke("Write a ballad about LangChain")
# print(result.content)

for chunk_result in llm.stream("Write a ballad about LangChain."):
    print(chunk_result.content)
    print("---")