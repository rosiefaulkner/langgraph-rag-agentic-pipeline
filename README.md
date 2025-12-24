# Agentic RAG with LangGraph 🦜🔍

Implementation of Reflective RAG, Self-RAG & Adaptive RAG tailored for production-oriented applications that need to make intelligent decisions about retrieving information, grade document relevance and detect hallucinations and can switch between local knowledge and web search.

This repository contains a refactored version of the original [LangChain's Cookbook](https://github.com/mistralai/cookbook/tree/main/third_party/langchain),

Mistral YouTube video:[Advance RAG control flow with Mistral and LangChain](https://www.youtube.com/watch?v=sgnrL7yo1TE)

of [Sophia Young](https://x.com/sophiamyang) from Mistral & [Lance Martin](https://x.com/RLanceMartin) from LangChain

![Logo](https://github.com/emarco177/langgraph-course/blob/project/agentic-rag/static/Langgraph%20Adaptive%20Rag.png)



## What This Repo Achieves

- **Agentic RAG Implementation**: Builds a system that can make intelligent decisions about retrieving information
- **Graph-Based Control Flow**: Uses LangGraph to create sophisticated control flows for RAG pipelines
- **Document Relevance Evaluation**: Implements logic to grade document relevance and detect hallucinations
- **Adaptive Information Retrieval**: Creates a system that can switch between local knowledge and web search
- **State Management**: Implements proper state handling for complex information flows

## Core elements of this Agentic RAG system:

| # | Commit | Description | Key Components |
|----------|--------|-------------|----------------|
| 1 | **Ingestion** | Vector database | Creates ingestion pipeline; Implements vector store with Chroma and OpenAI embeddings |
| 2 | **State** | Defines the state management | Creates GraphState class; Sets up typed dictionaries for state tracking |
| 3 | **Retrieve Node** | Implements the document retrieval | Builds retrieve node; Connects retrieval to vector database |
| 4 | **Grade Documents Node** | Evaluats document relevance | Creates document grading functionality; Implements decision logic for document relevance |
| 5 | **Web Search with Tavily** | Adds external search capability | Integrates Tavily search API; Implements fallback for insufficient local knowledge |
| 6 | **Generation Node** | Creats the answer generation component | Builds generate node; Implements context-aware response generation |
| 7 | **Graph** | Constructs the complete LangGraph workflow | Connects all nodes into workflow; Implements conditional edges for adaptive behavior |
| 8 | **Self-RAG** | Adds self-evaluation capabilities | Implements hallucination detection; Creates feedback loops for answer improvement |
| 9 | **Router** | Smart query routing | Creates intelligent routing between retrieval and web search; Optimizes entry point for different query types |

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file:

```bash
OPENAI_API_KEY=your_openai_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here  # For web search capabilities
LANGCHAIN_API_KEY=your_langchain_api_key_here  # Optional, for tracing - Langsmith
LANGCHAIN_TRACING_V2=true                      # Optional
LANGCHAIN_PROJECT=your_project_name_here       # Optional
```

> **Important Note**: If you enable tracing by setting `LANGCHAIN_TRACING_V2=true`, you must have a valid LangSmith API key set in `LANGCHAIN_API_KEY`. Without a valid API key, the application will throw an error.

## Getting Started


Install dependencies:

```bash
# using Poetry:
poetry install
```

## Run Locally

1. Clone the project & start environment

2. Start the Agentic Rag flow

```bash
  poetry run main.py
```

## Running Tests

To run tests, run the following command

```bash
  poetry run pytest . -s -v
```
## Acknowledgements

Original LangChain repository: [LangChain Cookbook](https://github.com/mistralai/cookbook/tree/main/third_party/langchain)
By [Sophia Young](https://x.com/sophiamyang) from Mistral & [Lance Martin](https://x.com/RLanceMartin) from LangChain
![Logo](https://github.com/emarco177/langgraph-course/blob/project/agentic-rag/static/LangChain-logo.png)



## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://github.com/rosiefaulkner)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/rosiefaulkner/)
[![Medium Follow](https://seekvectorlogo.com/wp-content/uploads/2021/12/medium-vector-logo-small-2021.png)](https://medium.com/@faulknerproject) 