from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os
os.environ["OPENAI_API_KEY"] = "..."
llm = OpenAI(temperature=0.9)

# prompt = PromptTemplate.from_template("What is a good name for a company that makes {product}?")
# prompt.format(product="colorful socks")

def summarize(query:str,abstract:list):
    prompt = PromptTemplate(
        input_variables=["query","abstract"],
        template="Answer the question {query} according to the text given below: {abstract}.\
            Give me the answer only."
    )
    chain = LLMChain(llm=llm,prompt=prompt)
    allAbs = " ".join(abstract)
    return chain.run({
        'query': query,
        'abstract':allAbs
    })

def polish(query: str):
    prompt = PromptTemplate(
        input_variables=["question"],
        template="i am currently trying to search papers in arXiv. \
        Give me one sentence which can search the correct answer for {question}.\
        Give me the sentence only."
    )
    chain = LLMChain(llm=llm,prompt=prompt)
    polished = chain.run({'question':query})
    key_prompt = PromptTemplate(
        input_variables=["sentence"],
        template = "Give me the key words of {sentence}. Give me the words only."
    )
    key_words = LLMChain(llm=llm,prompt = key_prompt).run({'sentence':polished})

    discipline_prompt = PromptTemplate(
        input_variables=["sentence"],
        template = "Give me the disciplines of the papers wanted by asking {sentence}.\
              Give me the names of disciplines only."
    )
    discipline = LLMChain(llm=llm,prompt = discipline_prompt).run({'sentence':polished})
    return key_words+discipline