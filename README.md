# LLM Application with LCEL

## Project Overview
This project demonstrates a LangChain-based application that leverages a language model (LLM) for text translation. Using FastAPI, the application offers a server with an API endpoint, built using LangChain's Runnable interfaces for chaining prompts, models, and output parsers.

## Architecture
The architecture of this application includes:
1. **LangChain Components**: A series of connected LangChain components, including prompts, models, and output parsers.
2. **FastAPI Server**: A lightweight API server set up with FastAPI that provides an endpoint to process translations.
3. **Remote Model Execution**: The FastAPI server can execute model requests locally or remotely using LangServe.

### Components:
- **Prompt Templates**: Configured for specific translation tasks, enabling dynamic language specifications.
- **LLM Model**: Utilizes OpenAI's GPT-4 model for natural language processing.
- **Output Parsing**: Outputs are structured with LangChain parsers for straightforward API responses.
- **Remote Chain**: Allows the application to connect to a remote chain endpoint using LangServe.

## Technologies Used
- **Python**: Primary language for scripting and server setup.
- **LangChain**: Framework for developing LLM applications with flexible prompt, model, and output configuration.
- **FastAPI**: API server framework used to expose the translation chain as an endpoint.
- **LangServe**: Tool for deploying LangChain Runnable chains remotely.

## Setup Instructions
### Prerequisites
1. **Install Python packages**:
   ```bash
   pip install langchain langchain-openai fastapi uvicorn langserve
   ```

2. **API Key**: Set your OpenAI API Key as an environment variable:
   ```python
   import os
   os.environ["OPENAI_API_KEY"] = "your_openai_api_key_here"
   ```

### Running the Application
1. **Run Jupyter Notebook**:
   - Open a Jupyter Notebook and run the initial setup commands to verify your installation of LangChain.
   


2. **Using the Translation Chain**:
   - Send requests to `http://localhost:8000/chain/` with JSON input specifying the `language` and `text` to translate.
   - Example request body:
     ```json
     {
       "language": "japanese",
       "text": "Hello!"
     }
     ```
3. **Default client**:
    - By using a browser, navigate to http://localhost:8000/chain/playground/, and you can find a default client with an interface where you can put some text to test the translator
![image](https://github.com/user-attachments/assets/2610ea57-7d14-499e-9e93-fd1eb3317ff4)


## Author
**Juan Esteban Ortiz**
## Email
**juaneortiz1@gmail.com**
