# arXiv-assistant
use LangChain to build LLM-based arXiv, easier search, easier use
> repository location: https://github.com/AliceRayLu/arXiv-assistant

## Project Info
This project uses Vue+Typescript to build frontend, uses fastAPI+langchain to build backend.
This project doesn't use arXiv official api. This project uses Milvus database distributed 
on NJU campus network.

## How to Use
### Prerequisite
- Access to the NJU campus network
- Access to the openAI (openAI API key)
- Local environment setup
### How to Set Up Local Environment
To run this project locally, you must install node.js and python interpreter.
- node version >= 18.x
- python version >= 3.9.x


The virtual environment in *interfaces* requires fastapi, uvicorn, pymilvus, openai, langchain.
See *requirement.txt* for detail.


To start the project, run the following command:


Run `npm run serve` to start the project webpage locally. 
(Run `npm install` first to install all the dependencies.)


Run the following command in the *interfaces* directory: 
`uvicorn main:app --reload`
to start backend service
(Don't forget to activate the virtual python environment first)
> Attention: You must fill in the openAI api key in chat.py
> to use LLM service.

## Examples
### Example1
![example1](https://github.com/AliceRayLu/arXiv-assistant/blob/main/src/assets/example2.png?raw=true)
### Example2
![example2](https://github.com/AliceRayLu/arXiv-assistant/blob/main/src/assets/example1.png?raw=true)

## LLM Usage
1. ask LLM to reorganize user input
2. extract key words and discipline of the polished sentence
3. search the database through Milvus
4. iteration trial: calculate the similarity between key words and papers' abstract sentence, 
choose the largest paper's title to search similar papaer
> iteration trial costs too much time, so give up iteration in the final edition
5. ask LLM to summarize the abstracts
6. return the result
