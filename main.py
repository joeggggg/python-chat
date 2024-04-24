import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title

show_pages(
    [
     
        Page("google/litellm_gemini.py","Gemini", "✌️"),
   
        Page("openai/chatgpt_wiki.py", "ChatGPT", "👌"),
        Page("openai/chatgpt_stream.py", "ChatGPT", "👌"),
      
      
    ]
)