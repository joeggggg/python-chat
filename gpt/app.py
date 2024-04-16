import os
# from apikey import apikey
from dotenv import load_dotenv
import streamlit as st
from langchain_openai import OpenAI
# from langchain.globals import set_verbose, get_verbose
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.memory import ConversationBufferMemory
import time

#init
load_dotenv() 
user = os.getlogin().upper()
os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')

api_key = os.environ["OPENAI_API_KEY"]

def stream(text):
    result = ""
    container = st.empty()
    for chunk in text:
        time.sleep(0.005)
        result += chunk
        container.write(result, unsafe_allow_html=True)


st.title('🦜⛓️ Langchain Conversation')
prompt = st.text_input(f'🤖 : Hi __{user}__, what is your prompt?')

# prompt templates, to give context to the init prompt 
title_template = PromptTemplate(
    input_variables=['topic'],
    template='Can you write down a short explanation about this {topic}'
)

script_template = PromptTemplate(
    input_variables=['title'],
    template='highlight top 10 most important concepts I need to know about this topic TOPIC : {title} , each concept should come with sample code example, make sure you wrap code blocks with ``` ``` so that it can be formatted in markdown'
    
)
# memory 
memory = ConversationBufferMemory(input_key='topic', memory_key='chat_history')

llm = OpenAI(temperature=0.9)

title_chain = LLMChain(llm=llm,prompt=title_template, verbose=True,
    output_key='title', memory=memory) 
script_chain = LLMChain(llm=llm,prompt=script_template, verbose=True,
    output_key='script', memory=memory) 
sequential_chain = SequentialChain(chains=[title_chain, script_chain], 
    input_variables=['topic'], output_variables=['title','script'], verbose=True)  
conversation = [] 
if prompt:
    # from langchain_core.prompts import ChatPromptTemplate
    # prompt = ChatPromptTemplate.from_messages([
    #     ("system", "You are world class technical documentation writer."),
    #     ("user", "{input}")
    # ])
    
    # response = llm.invoke(prompt)
    # response = title_chain.run(topic = prompt)
    response = sequential_chain({'topic': prompt})
    # st.write("**🐸 Your Prompt:**")
#   st.write(conversation[0])
    #st.write("**🐸 :**")
    st.write("**🤖 typing... :**")
    with st.spinner("responding..."):
        # write_stream(stream=get_stream(text))
        stream(response['title'])
    # st.markdown(response['title'])
    with st.spinner("responding..."):
        # write_stream(stream=get_stream(text))
        stream(response['script'])
    # st.markdown(response['script'])
    with st.expander('Conversation History'):
        st.info(memory.buffer)

# langchain
# llm.invoke("how can langsmith help with testing?")

# We can also guide its response with a prompt template. Prompt templates convert raw user input to better input to the LLM.

# from langchain_core.prompts import ChatPromptTemplate
# prompt = ChatPromptTemplate.from_messages([
#     ("system", "You are world class technical documentation writer."),
#     ("user", "{input}")
# ])