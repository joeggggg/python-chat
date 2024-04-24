import time

import streamlit as st

text = 'A langchain, or language chain, is a sequence of related languages that have evolved from a common ancestral language. These languages share similar grammatical structures, vocabulary, and phonetics, but have developed their own unique characteristics over time. This can occur through natural linguistic evolution or through language contact and borrowing. Studying langchains can provide insights into the history and development of languages and can help linguists understand the relationships between different language families.'

def write_stream(stream):
    result = ""
    container = st.empty()
    for chunk in stream:
        result += chunk
        container.write(result, unsafe_allow_html=True)


def get_stream(text):
    
    for chunk in text:
        time.sleep(0.01)
        yield chunk

def stream(text):
    result = ""
    container = st.empty()
    for chunk in text:
        time.sleep(0.01)
        result += chunk
        container.write(result, unsafe_allow_html=True)
        
        
if st.button("Stream HTML text"):
    with st.spinner("responding..."):
        # write_stream(stream=get_stream(text))
        stream(text)
    st.success('Done!')