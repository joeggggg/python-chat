# #from multiprocessing import process
# import litellm
# from litellm import completion
# import os
# from dotenv import load_dotenv
# import streamlit as st
# from st_pages import Page, Section, show_pages, add_page_title

# #init
# load_dotenv()  
# os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')
# prompt_text = "Help me create a web application in Python with Streamlit and supported packages such as pandas, psycopg2. The purpose of the web app is enabling can allow user to upload document such as .csv, .docx, .pdf and perform a chat. While uploaded document chunks, conversation history shall be saved to Postgres database"
#  # Stores conversation history 
# conversation = [] 


# def chat_openai(prompt_input, conversation):
#     messages = [
#     {
#         "role": "user",
#         "content": [
#             {
#                 "type": "text",
#                 "text": prompt_input
#             }
#         ]
#     }
#     ]   
#     response = completion(
#             model="gpt-3.5-turbo", 
#             messages=messages,
#             temperature=0.9,
#             stream=True
#             )
    
#     output_text = ""
#     for part in response:
#         output_text += part.choices[0].delta.content or ""
#     conversation.append(prompt_input)
#     conversation.append(output_text)
#     return output_text

# # chat_openai(prompt_text, conversation)      
# # execute
# conversation = chat_openai(prompt_text, conversation)


# st.title("Chat with ChatGPT")

# # prompt_text = st.text_input("Enter your prompt:")
# prompt_text = st.text_input(prompt_text)

# if prompt_text:
#   response_text = chat_openai(prompt_text, conversation)
#   st.write("**🐸 Your Prompt:**")
#   st.write(conversation[0])
#   st.write("**🤖 ChatGPT's Response:**")
#   st.markdown(response_text)

#   # Display Chat History (Optional)
#   # Uncomment the following block to display the entire conversation history
#   st.write("**Conversation History:**")
#   for i in range(0, len(conversation), 2):
#     st.write(f"You: {conversation[i]}")
#     st.write(f"Gemini: {conversation[i+1]}")
