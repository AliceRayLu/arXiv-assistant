# arXiv-assistant
use LangChain to build LLM-based arXiv, easier search, easier use
> repository location: https://github.com/AliceRayLu/arXiv-assistant

## How to Use
Run the following command:
`npm run serve`
to start the project webpage locally


Run the following command in the *interfaces* directory: 
`uvicorn main:app --reload`
to start backend service
> Attention: This project is based on arXiv database distributed
> on NJU campus network. You also need to fill in the openAI api key 
> to use LLM service.

## Project Info
This project uses Vue+Typescript to build frontend, uses fastAPI+langchain to build backend.

To run this project locally, you must install node.js and python interpreter.

The virtual environment in *interfaces* requires fastapi, uvicorn, openai, langchain. 
See *requirement.txt* for detail.
