# AI Personal Research Assistant

An AI-powered research assistant built with Python,
RAG, FastAPI, PostgreSQL, and LLMs.

## Features
- AI-powered research and question answering
- Retrieval-Augmented Generation (RAG)
- Research summaries and findings
- API integration
- Research output storage

## Tech Stack
- Python
- FastAPI
- PostgreSQL
- RAG
- Large Language Models (LLMs)


## Installation

Follow these steps to set up and run the AI Personal Research Assistant on your local machine.

### 1. Clone the Repository

Download the project from GitHub:

```bash
git clone ((https://github.com/RICK2601)/AI-Personal-Research-Assistant.git))
cd (C:\Users\ADMIN\PycharmProjects\Gr - 01)
```

Replace the placeholder URL and folder name with your actual repository details.

### 2. Install UV

This project uses UV for Python dependency and environment management. Install UV by following the official instructions at https://docs.astral.sh/uv/getting-started/installation/.

### 3. Create a Virtual Environment

Create an isolated Python environment:

```bash
uv venv
```

Activate it on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

If the project contains a `pyproject.toml` file with its dependencies configured, run:

```bash
uv sync
```

Otherwise, install the dependencies listed in your project's requirements file or configure them in `pyproject.toml` first.

### 5. Configure Environment Variables

Create a `.env` file in the project root and add the required configuration, such as your AI provider API key and PostgreSQL database connection string.

Use placeholder values in documentation and never publish real API keys or passwords.

### 6. Start the Application

Run the application's entry point using the command appropriate for your project. For a FastAPI application with an `app/main.py` entry point, this may be:

```bash
uv run uvicorn app.main:app --reload
```

## Environment Variables

The application uses environment variables to securely manage API keys, database credentials, and other configuration settings. These values are stored in a `.env` file in the project root directory.

### 1. Create a `.env` File

Create a new file named `.env` in the root directory of the project.

### 2. Configure the Environment Variables

Add the required configuration variables to the `.env` file. For example:

```env
GOOGLE_API_KEY=your_google_api_key_here
DATABASE_URL=postgresql://username:password@localhost:5432/research_db
```

- `GOOGLE_API_KEY`: Your API key for accessing the Google Gemini language model, if your application uses Gemini.
- `DATABASE_URL`: The PostgreSQL connection string used to connect the application to its database.

Replace the example values with your actual credentials and database configuration. Add other environment variables if required by your implementation.

### 3. Load Environment Variables

If the application uses `python-dotenv`, install it if necessary:

```bash
uv add python-dotenv
```

Load the variables in Python:

```python
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
database_url = os.getenv("DATABASE_URL")
```

### 4. Protect Your Credentials

Never upload your `.env` file or expose API keys, passwords, or other secrets in a public GitHub repository.

Add the following entry to your `.gitignore` file:

```gitignore
.env
```

If you need to share the required configuration with other developers, provide a `.env.example` file containing variable names and placeholder values, but no real credentials.

## Usage

Follow these steps to run the AI Personal Research Assistant locally and interact with its research capabilities.

### 1. Activate the Virtual Environment

On Windows PowerShell, run:

```powershell
.venv\Scripts\Activate.ps1
```

### 2. Configure the Environment

Ensure that your `.env` file contains the required API keys and database connection settings. Verify that PostgreSQL is running and the required database has been created if your application depends on it.

### 3. Start the Application

If your FastAPI application uses `app/main.py` as its entry point, start the development server with:

```bash
uv run uvicorn app.main:app --reload
```

Adjust the module path to match your actual project structure.

### 4. Access the API Documentation

Once the server starts successfully, open the following URL in your browser:

http://127.0.0.1:8000/docs

The interactive Swagger UI allows you to inspect available API endpoints, submit requests, and review responses.

### 5. Submit a Research Query

If the application provides a research endpoint, send a query through the interactive API documentation. For example, you might ask:

> Research the applications of artificial intelligence in agriculture and summarize the key findings.

The assistant should process the query using the research workflow configured in the application and return a response. Depending on the implementation, it may also retrieve relevant information, generate a summary, and save research findings.

### 6. Review Research Results

Check the API response and any output files generated by the application, such as `research_findings.md`, if your implementation supports saving findings.

### Troubleshooting

- **API key error:** Verify that your API key is valid and loaded from `.env`.
- **Database connection error:** Check PostgreSQL status and the connection string.
- **Module not found:** Confirm that dependencies are installed and the correct Python environment is active.
- **Endpoint not found:** Review the routes defined in your FastAPI application.

## Project Structure

The project is organized into separate modules to make the application easier to understand, maintain, test, and extend.

```text
AI-Personal-Research-Assistant/
│
├── app/
│   ├── main.py
│   ├── api/
│   ├── services/
│   ├── database/
│   └── models/
│
├── research_findings.md
├── tests/
├── .env
├── .env.example
├── .gitignore
├── pyproject.toml
├── uv.lock
└── README.md
```

### Directory and File Descriptions

- **`app/`** — Contains the main application code and its components.
- **`app/main.py`** — Defines the FastAPI application and initializes the API server.
- **`app/api/`** — Contains API routes and endpoints for handling incoming requests.
- **`app/services/`** — Implements research workflows, AI model integration, information retrieval, and response generation.
- **`app/database/`** — Manages database connections and database-related operations.
- **`app/models/`** — Defines data models and schemas used by the application.
- **`research_findings.md`** — Stores research findings and summaries generated by the assistant, if file-based output is implemented.
- **`tests/`** — Contains automated tests for application components.
- **`.env`** — Stores local environment variables and secret credentials. This file must not be committed to GitHub.
- **`.env.example`** — Provides a template showing the environment variables required to configure the application, without exposing real secrets.
- **`.gitignore`** — Specifies files and folders that Git should ignore.
- **`pyproject.toml`** — Defines project metadata, dependencies, and tool configuration for Python and UV.
- **`uv.lock`** — Records resolved dependency versions to support reproducible installations with UV.
- **`README.md`** — Documents the project's purpose, setup, features, and usage instructions.

### Architecture Overview

The application can follow a modular workflow:

1. The user submits a research query through an API endpoint.
2. The research service retrieves relevant information from configured data sources.
3. The RAG pipeline supplies relevant context to the language model.
4. PostgreSQL stores the appropriate application data.
5. The assistant returns a response and may save the findings to a Markdown file.

## Future Improvements

The AI Personal Research Assistant can be extended with additional features to improve research accuracy, automation, scalability, and usability.

- **Advanced RAG Pipeline:** Implement improved document chunking, embedding models, semantic search, and reranking to retrieve more relevant information.

- **Multiple Data Sources:** Integrate web search APIs, research papers, online documentation, and other trusted information sources to expand research capabilities.

- **Source Citations and References:** Provide source links and relevant document references alongside generated answers to improve transparency and enable fact-checking.

- **PDF and Document Processing:** Enable users to upload PDF, DOCX, and TXT files for document analysis, information extraction, and question answering.

- **Long-Term Research Memory:** Store previous research queries, findings, and relevant context in PostgreSQL to support follow-up questions and organized research sessions.

- **Automated Research Reports:** Generate structured research reports containing summaries, key findings, references, and conclusions, with options to export them into Markdown or PDF.

- **Vector Search Integration:** Explore PostgreSQL with the pgvector extension to store embeddings and perform similarity searches for retrieval-augmented generation.

- **Improved API Security:** Add authentication, authorization, request validation, rate limiting, and secure management of API credentials.

- **Testing and Evaluation:** Develop automated tests and evaluate retrieval relevance, factual accuracy, response quality, and API performance.

- **Deployment and Monitoring:** Deploy the application using Docker and a suitable cloud platform, with logging, error monitoring, and performance tracking.

- **User Interface:** Build a simple web interface where users can submit research questions, view results, and manage saved research projects.

### Long-Term Goal

The long-term goal is to develop a reliable, modular, and scalable AI research platform that combines information retrieval, language models, database management, and automated report generation into a unified workflow.

These improvements are planned development goals and may be implemented progressively as the project evolves.

LICENSE
This project is licensed under the MIT License. You are free to use, copy, modify, merge, publish, distribute, sublicense, and sell copies of the software, subject to the terms and conditions of the license.    
