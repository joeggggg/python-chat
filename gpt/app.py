import os
import time

from dotenv import load_dotenv
import streamlit as st
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain_community.utilities import WikipediaAPIWrapper

#init
load_dotenv() 
user = os.getlogin().upper()
os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')
wiki = WikipediaAPIWrapper()
llm = OpenAI(temperature=0.9)

#utilities
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
    input_variables=['title','wikipedia_research'],
    template='Now, you will highlight top 10 most important concepts I need to know about {title} while leveraging this wikipedia research {wikipedia_research}.'
    
)
# memory 
# title_memory = ConversationBufferMemory(input_key='topic', memory_key='chat_history')
title_memory = ConversationBufferMemory(input_key='topic', memory_key='chat_history')
script_memory = ConversationBufferMemory(input_key='title', memory_key='chat_history')


title_chain = LLMChain(llm=llm,prompt=title_template, verbose=True,
    output_key='title', memory=title_memory) 
script_chain = LLMChain(llm=llm,prompt=script_template, verbose=True,
    output_key='script', memory=script_memory) 
# sequential_chain = SequentialChain(chains=[title_chain, script_chain], 
#     input_variables=['topic'], output_variables=['title','script'], verbose=True)  

#conversation = [] 
if prompt:
    title = title_chain.run(prompt)
    wiki_research = wiki.run(prompt) 
    script = script_chain.run(title=title, wikipedia_research=wiki_research)

    # response = sequential_chain({'topic': prompt})
    # st.write(response['title'])
    st.write(title) 
    with st.spinner("**🤖 typing... :**"):
        # stream(response['script'])
        stream(script)
    with st.expander('Topic History'):
        st.info(title_memory.buffer)
    with st.expander('Response History'):
        st.info(script_memory.buffer)
    with st.expander('Wiki Research'):
        st.info(wiki_research)
