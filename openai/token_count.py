
import tiktoken
#import openai

#reference
#  https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb

prompt_input = "Help me create a web application in Python with Streamlit and supported packages such as pandas, psycopg2. The purpose of the web app is enabling can allow user to upload document such as .csv, .docx, .pdf and perform a chat. While uploaded document chunks, conversation history shall be saved to Postgres database"

# Load an encoding
encoding = tiktoken.get_encoding("cl100k_base")
encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")

# The .encode() method converts a text string into a list of token integers.
encoding.encode("tiktoken is great!")
encoding.encode(prompt_input)

def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

#now let's test
print(num_tokens_from_string(prompt_input,"cl100k_base"))

#.decode() converts a list of token integers to a string.
x = encoding.decode([83, 1609, 5963, 374, 2294, 0]) 
#print(x) #  >>>  tiktoken is great!

