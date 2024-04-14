#from multiprocessing import process
import os
from openai import OpenAI
from dotenv import load_dotenv

client = OpenAI(
  api_key=os.getenv("OPENAI_API_KEY"),
 )

#  async client
stream = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    messages=[{"role": "user", 
             "content": "Help me create a web application in Python with Streamlit, OpenAI API, to perform a chat, and save the conversation to Postgres database"
            }
               ],
    stream=True,
)
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content.format)

# client = OpenAI(
#   # api_key=os.environ.get("OPENAI_API_KEY"),
#   api_key=os.getenv("OPENAI_API_KEY")
#  )


# chat_completion = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", 
#      "content": "You act as a successful aesthetic."},
#     {"role": "user", 
#      "content": "Help me to create a healthy meal plan x 30 days."
#      }
#   ]
# )


# print(chat_completion.choices[0].message)