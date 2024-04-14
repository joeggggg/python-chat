import tiktoken
#import openai

#reference
#  https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb


# Load an encoding
encoding = tiktoken.get_encoding("cl100k_base")
encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")

# The .encode() method converts a text string into a list of token integers.
encoding.encode("tiktoken is great!")

def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

#now let's test
print(num_tokens_from_string("Xin chào, mình là Bé Lợi! Các bạn cùng mình khám phá ẩm thực Quận 5 nhé!","cl100k_base"))
print(num_tokens_from_string("Hello, I'm Beloi! Let's explore District 5 street food with me.","cl100k_base"))

#.decode() converts a list of token integers to a string.
x = encoding.decode([83, 1609, 5963, 374, 2294, 0]) 
#print(x) #  >>>  tiktoken is great!

#Counting tokens for chat completions API calls
# def num_tokens_from_messages(messages, model="gpt-3.5-turbo-0613"):
#     """Return the number of tokens used by a list of messages."""
#     try:
#         encoding = tiktoken.encoding_for_model(model)
#     except KeyError:
#         print("Warning: model not found. Using cl100k_base encoding.")
#         encoding = tiktoken.get_encoding("cl100k_base")
#     if model in {
#         "gpt-3.5-turbo-0613",
#         "gpt-3.5-turbo-16k-0613",
#         "gpt-4-0314",
#         "gpt-4-32k-0314",
#         "gpt-4-0613",
#         "gpt-4-32k-0613",
#         }:
#         tokens_per_message = 3
#         tokens_per_name = 1
#     elif model == "gpt-3.5-turbo-0301":
#         tokens_per_message = 4  # every message follows <|start|>{role/name}\n{content}<|end|>\n
#         tokens_per_name = -1  # if there's a name, the role is omitted
#     elif "gpt-3.5-turbo" in model:
#         print("Warning: gpt-3.5-turbo may update over time. Returning num tokens assuming gpt-3.5-turbo-0613.")
#         return num_tokens_from_messages(messages, model="gpt-3.5-turbo-0613")
#     elif "gpt-4" in model:
#         print("Warning: gpt-4 may update over time. Returning num tokens assuming gpt-4-0613.")
#         return num_tokens_from_messages(messages, model="gpt-4-0613")
#     else:
#         raise NotImplementedError(
#             f"""num_tokens_from_messages() is not implemented for model {model}. See https://github.com/openai/openai-python/blob/main/chatml.md for information on how messages are converted to tokens."""
#         )
#     num_tokens = 0
#     for message in messages:
#         num_tokens += tokens_per_message
#         for key, value in message.items():
#             num_tokens += len(encoding.encode(value))
#             if key == "name":
#                 num_tokens += tokens_per_name
#     num_tokens += 3  # every reply is primed with <|start|>assistant<|message|>
#     return num_tokens



# example_messages = [
#     {
#         "role": "system",
#         "content": "You are a helpful, pattern-following assistant that translates corporate jargon into plain English.",
#     },
#     {
#         "role": "system",
#         "name": "example_user",
#         "content": "New synergies will help drive top-line growth.",
#     },
#     {
#         "role": "system",
#         "name": "example_assistant",
#         "content": "Things working well together will increase revenue.",
#     },
#     {
#         "role": "system",
#         "name": "example_user",
#         "content": "Let's circle back when we have more bandwidth to touch base on opportunities for increased leverage.",
#     },
#     {
#         "role": "system",
#         "name": "example_assistant",
#         "content": "Let's talk later when we're less busy about how to do better.",
#     },
#     {
#         "role": "user",
#         "content": "This late pivot means we don't have time to boil the ocean for the client deliverable.",
#     },
# ]

# for model in [
#     "gpt-3.5-turbo-0301",
#     "gpt-3.5-turbo-0613",
#     "gpt-3.5-turbo",
#     "gpt-4-0314",
#     "gpt-4-0613",
#     "gpt-4",
#     ]:
#     print(model)
#     # example token count from the function defined above
#     print(f"{num_tokens_from_messages(example_messages, model)} prompt tokens counted by num_tokens_from_messages().")
#     # example token count from the OpenAI API
#     response = openai.ChatCompletion.create(
#         model=model,
#         messages=example_messages,
#         temperature=0,
#         max_tokens=1,  # we're only counting input tokens here, so let's not waste tokens on the output
#     )
#     print(f'{response["usage"]["prompt_tokens"]} prompt tokens counted by the OpenAI API.')
#     print()