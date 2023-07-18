from langchain.llms import OpenAI, OpenAIChat
import os
os.environ["OPENAI_API_KEY"] = "None"
os.environ["OPENAI_API_BASE"] = "http://172.29.7.155:8000/v1"
llm_completion = OpenAI(model_name="vicuna-13b")
llm_chat = OpenAIChat(model_name="vicuna-13b")

res = llm_completion.predict("hello, tell me about you.")
print(res)