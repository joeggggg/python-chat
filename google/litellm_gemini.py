import os
import time
# import litellm
# from litellm import embedding
from litellm import completion
from dotenv import load_dotenv
import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title
# from langchain_community.utilities import WikipediaAPIWrapper
#init

load_dotenv()  
os.environ["GEMINI_API_KEY"] = os.getenv('GEMINI_API_KEY')
os.environ['HUGGINGFACE_API_KEY'] = os.getenv('HUGGINGFACEHUB_API_TOKEN')
# wiki = WikipediaAPIWrapper()

#utilities
def stream(text):
    result = ""
    container = st.empty()
    for chunk in text:
        time.sleep(0.005)
        result += chunk
        container.write(result, unsafe_allow_html=True)

 # Stores conversation history 
prompt_conversation = [] 
response_conversation = [] 

#.env looks like this,
# OPENAI_API_KEY=sk-56734684978
# HUGGINGFACEHUB_API_TOKEN = hf_45375437
# GEMINI_API_KEY = 5683835738
# - To learn how to set the environment variable refer to readme.md

#test
# prompt_init = 'RAG'
# wiki_research = wiki.run(prompt_init) 



# response = embedding(
#     model='huggingface/microsoft/codebert-base', 
#     input=["good morning from litellm"]
# )

def chat_gemini(prompt_init,  prompt_conversation, response_conversation):
    
    # wiki_research = wiki.run(prompt_init) 
    messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "Can you please create comprehensive topic TOPIC of " + prompt_init +
                "? I would like the response to be structured in a clear and organized manner, incorporating headings, sections, and visual elements like emojis. "
                +"Please ensure that the response maintain the order and organization of ideas from the original TOPIC. "
                +"Additionally, highlight key terms, code examples, , and any other relevant details to make the response as informative as possible. "
                +"Feel free to utilize bolding, italics, underlining, numbering, markdown and other text modifications to enhance readability."
            }
        ]
    }
    ]   
    
    #to access attributes value in dictionary
    last_prompt_formatted = messages[0]["content"][0]["text"]
    response = completion(
            model="gemini/gemini-1.5-pro-latest", 
            messages=messages,
            temperature=0.9,
            stream=True
            )
    
    output_text = ""
    for part in response:
        output_text += part.choices[0].delta.content or ""
    # prompt_conversation.append(prompt_input)
    prompt_conversation.append(last_prompt_formatted)
    response_conversation.append(output_text)
    return output_text

## Streamlit App
def main():
    with st.sidebar:
        st.page_link("gemini.py", label="Gemini Chat", icon="🤖")
        
    st.write("### 🐸 Chat with Gemini 🤖")
    # prompt_text = st.text_area(label="Enter your prompt", value= "", height=300)
    prompt_init = st.text_input("__Enter your prompt:__")

    if prompt_init:
        response_text = chat_gemini(prompt_init, prompt_conversation, response_conversation)
        st.write("**🐸 Your Prompt:**")
        st.write(prompt_conversation[0])
        st.write("**🤖 Gemini's Response:**")
        # st.markdown(response_text)
        with st.spinner("**thinking... :**"):
            stream(response_text)
  # Display Chat History 

        st.markdown("""---""")
        st.write("### Conversation History:")
        # for i in range(0, len(conversation), 2):
        for i in range(0, len(prompt_conversation), 1):
            # st.write(f"__🐸 Your Prompt:__")
            # st.markdown(conversation[i])
            # st.write(f"__🤖 Gemini's Response:__")
            # st.markdown(conversation[i+1])
            with st.expander('Topic History'):
                st.info(prompt_conversation[i])
                st.info(response_conversation[i])
    
if __name__ == "__main__":
    main()