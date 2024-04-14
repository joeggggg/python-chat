import litellm
from litellm import completion
import os
from dotenv import load_dotenv
import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title

# Optional -- adds the title and icon to the current page




# Specify what pages should be shown in the sidebar, and what their titles and icons
# should be

load_dotenv()  
os.environ["GEMINI_API_KEY"] = os.getenv('GEMINI_API_KEY')

# prompt_text = 'You act as an professional Olympic athlete, help me to create a healthy meal plan x 07 days. Here is my preference: My estimated TDEE or body weight maintenance energy requirement is 2,307 Calories/ per day, mild weight loss is 2057 Calories/ per day , please use Asian food,. The response should be in markdown format, with 3 columns, Day, Meal, Macro'

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

conversation = []  # Stores conversation history 

# chat_gemini(prompt_text, conversation)      
# execute
# conversation = chat_gemini(prompt_text, conversation)



# Streamlit App



st.title("Chat with Gemini")

prompt_text = st.text_input("Enter your prompt:")

if prompt_text:
  response_text = chat_gemini(prompt_text, conversation)
  st.write("**🐸 Your Prompt:**")
  st.write(conversation[0])
  st.write("**🤖 Gemini's Response:**")
  st.markdown(response_text)

  # Display Chat History (Optional)
  # Uncomment the following block to display the entire conversation history
  st.write("**Conversation History:**")
  for i in range(0, len(conversation), 2):
    st.write(f"You: {conversation[i]}")
    st.write(f"Gemini: {conversation[i+1]}")


# Display the conversation history
# st.header("Chat Conversation")
# for message in conversation:
#   st.write(message)
  
# st.title("Chat with Gemini")
# prompt = st.text_area("Enter your prompt here:")

# submit_button = st.button("Submit")
# if submit_button and prompt:
#   for response in chat_gemini(prompt, conversation):
#     st.write("Gemini:", response)
#     conversation.append(response)


    
# def main():
    # st.title("My LLM API Playground")
#     st.subheader("Powered by [LiteLLM](https://github.com/BerriAI/litellm/)")

#     # Sidebar for user input
    # st.header("User Input")
#     prompt_input = st.text_area("Enter your prompt here:")
#     submit_button = st.button("Submit")
    
#     # Main content area to display model outputs
#     # st.header("Powered by")  
    
#     # List of models to test
#     model = ["gemini/gemini-1.5-pro-latest"]  # Add your model names here
    
#     # cols = st.columns(len(model_names))  # Create columns
#     outputs = [""]   # Initialize outputs list with empty strings
#     if submit_button and prompt_input:
#         for  part in chat_gemini(prompt_input):
#             st.write(part )           

#     # Display text areas and fill with outputs if available
#         # chat_gemini(prompt_input)  #
#         # text_area(label=f"{model}", value= chat_gemini(prompt_input), height=300)

# if __name__ == "__main__":
#     main()