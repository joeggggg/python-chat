import litellm
from litellm import completion
import os
from dotenv import load_dotenv
# import pytest
import streamlit as st

load_dotenv()  
os.environ["GEMINI_API_KEY"] = os.getenv('GEMINI_API_KEY')


# prompt_vision = 'Describe the image in a few sentences.'
# Note: You can pass here the URL or Path of image directly.
image_url = 'https://storage.googleapis.com/github-repo/img/gemini/intro/landmark3.jpg'

# Create the messages payload according to the documentation
messages_vision = [
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": prompt_vision
            },
            {
                "type": "image_url",
                "image_url": {"url": image_url}
            }
        ]
    }
]


#  Make the API call to Gemini model
response = litellm.completion(
    model="gemini/gemini-pro-vision",
    messages=messages_vision,
)

