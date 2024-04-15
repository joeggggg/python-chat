import litellm
from litellm import completion
import os
from dotenv import load_dotenv
import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title

#init

load_dotenv()  
os.environ["GEMINI_API_KEY"] = os.getenv('GEMINI_API_KEY')
# prompt_text = 'You act as an professional Olympic athlete, help me to create a healthy meal plan x 07 days. Here is my preference: My estimated TDEE or body weight maintenance energy requirement is 2,307 Calories/ per day, mild weight loss is 2057 Calories/ per day , please use Asian food,. The response should be in markdown format, with 3 columns, Day, Meal, Macro'
# prompt_text = "Help me create a web application in Python with Streamlit and supported packages such as langchain, pandas, psycopg2. The purpose of the web app is enabling can allow user to upload document such as .csv, .docx, .pdf and perform a chat. While uploaded document chunks, conversation history shall be saved to Postgres database"

 # Stores conversation history 
conversation = [] 

#.env looks like this,
# OPENAI_API_KEY=sk-56734684978
# HUGGINGFACEHUB_API_TOKEN = hf_45375437
# GEMINI_API_KEY = 5683835738

# - To learn how to set the environment variable refer to readme.md

def chat_gemini(prompt_input,conversation):
    
    messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": prompt_input
            }
        ]
    }
    ]   
    response = completion(
            model="gemini/gemini-1.5-pro-latest", 
            messages=messages,
            temperature=0.9,
            stream=True
            )
    
    output_text = ""
    for part in response:
        output_text += part.choices[0].delta.content or ""
    conversation.append(prompt_input)
    conversation.append(output_text)
    return output_text

# chat_gemini(prompt_text, conversation)      
# execute
# conversation = chat_gemini(prompt_text, conversation)


## Streamlit App
def main():
    with st.sidebar:
        st.page_link("gemini.py", label="Gemini Chat", icon="🤖")
        
    st.title("🐸 Chat with Gemini 🤖")
    # prompt_text = st.text_area(label="Enter your prompt", value= "", height=300)
    prompt_text = st.text_input("__Enter your prompt:__")

    if prompt_text:
        response_text = chat_gemini(prompt_text, conversation)
        # st.write("**🐸 Your Prompt:**")
        # st.write(conversation[0])
        st.write("**🤖 Gemini's Response:**")
        st.markdown(response_text)

  # Display Chat History 

        st.markdown("""---""")
        st.write("## Conversation History:")
        for i in range(0, len(conversation), 2):
            st.write(f"__🐸 Your Prompt:__")
            st.markdown(conversation[i])
            st.write(f"__🤖 Gemini's Response:__")
            st.markdown(conversation[i+1])
    
if __name__ == "__main__":
    main()