# python chat 
## Introduction

- Learn to interact with different llm models, such as OpenAI, Google Gemini, HuggingFace, VertexAI and etc., 
- And LLM with Langchain, VectorDB, ...

#### stacks

- Packages: litellm, langchain

## Get-started

### Python env setup

 - create the virtual environment, syntax: py -3 -m venv <virtual-environment-name>
```
py -3 -m venv venv
```
- select 'Python set Interpreter' 
- start the virtual env 
```
.\venv\Scripts\activate.bat
```
### common packages installation:
 ```
pip install -r requirements.txt
 ```
- openai 
```
pip install openai tiktoken
```
- google-generativeai
```
pip install -q -U google-generativeai Pillow
```
### environment variables
- To set the environment variable in the current session 
```
setx OPENAI_API_KEY "your-opepnai-api-key"

```

### resources
- [LiteLLM](https://github.com/BerriAI/litellm/)
