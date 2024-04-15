import os
# from apikey import apikey
from dotenv import load_dotenv
import streamlit as st
from langchain_openai import OpenAI
# from langchain.globals import set_verbose, get_verbose
#init
load_dotenv() 

os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')

api_key = os.environ["OPENAI_API_KEY"]


llm = OpenAI(temperature=0.9)
# llm.globals.set_verbose() 
# llm.globals.get_verbose()
# hit error when init ChatOpenAI
# llm = ChatOpenAI(api_key) 

#streamlit page

st.title('hello')
prompt = st.text_input('what is your prompt')


if prompt:
    # from langchain_core.prompts import ChatPromptTemplate
    # prompt = ChatPromptTemplate.from_messages([
    #     ("system", "You are world class technical documentation writer."),
    #     ("user", "{input}")
    # ])
    
    response = llm.invoke(prompt)
    st.write("**🐸 Your Prompt:**")
#   st.write(conversation[0])
    st.write("**🤖 ChatGPT's Response:**")
    st.write(response)

# langchain
# llm.invoke("how can langsmith help with testing?")

# We can also guide its response with a prompt template. Prompt templates convert raw user input to better input to the LLM.

# from langchain_core.prompts import ChatPromptTemplate
# prompt = ChatPromptTemplate.from_messages([
#     ("system", "You are world class technical documentation writer."),
#     ("user", "{input}")
# ])