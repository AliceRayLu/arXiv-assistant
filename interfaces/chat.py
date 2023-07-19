from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os
os.environ["OPENAI_API_KEY"] = ""
llm = OpenAI(temperature=0.9)

# prompt = PromptTemplate.from_template("What is a good name for a company that makes {product}?")
# prompt.format(product="colorful socks")

def summarize(query:str,abstract:list):
    prompt = PromptTemplate(
        input_variables=["query","abstract"],
        template="Answer the question {query} according to the text given below: {abstract}"
    )
    chain = LLMChain(llm=llm,prompt=prompt)
    allAbs = " ".join(abstract)
    return chain.run({
        'query': query,
        'abstract':allAbs
    })
