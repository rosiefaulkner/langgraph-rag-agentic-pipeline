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

## Tutorial Structure

Core elements of this Agentic RAG system:

| # | Commit | Description | Key Components |
|----------|--------|-------------|----------------|
| 1 | **Start Here** | Introduction to the course and Agentic RAG concepts | Overview of the project; Introduction to LangGraph and Agentic RAG architecture |
| 2 | **Project Structure** | Setting up the project foundation | Initialize project structure; Configure Poetry for dependency management |
| 3 | **Ingestion** | Setting up the vector database | Create ingestion pipeline; Implement vector store with Chroma and OpenAI embeddings |
| 4 | **State** | Defining the state management | Create GraphState class; Set up typed dictionaries for state tracking |
| 5 | **Retrieve Node** | Implementing the document retrieval | Build retrieve node; Connect retrieval to vector database |
| 6 | **Grade Documents Node** | Evaluating document relevance | Create document grading functionality; Implement decision logic for document relevance |
| 7 | **Web Search with Tavily** | Adding external search capability | Integrate Tavily search API; Implement fallback for insufficient local knowledge |
| 8 | **Generation Node** | Creating the answer generation component | Build generate node; Implement context-aware response generation |
| 9 | **Graph** | Constructing the complete LangGraph workflow | Connect all nodes into workflow; Implement conditional edges for adaptive behavior |
| 10 | **Self-RAG** | Adding self-evaluation capabilities | Implement hallucination detection; Create feedback loops for answer improvement |
| 11 | **Router** | Smart query routing | Create intelligent routing between retrieval and web search; Optimize entry point for different query types |
| 12 | **Formatting** | Final code formatting and cleanup | Code optimization; Final documentation improvements |

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file:

```bash
OPENAI_API_KEY=your_openai_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here  # For web search capabilities
LANGCHAIN_API_KEY=your_langchain_api_key_here  # Optional, for tracing
LANGCHAIN_TRACING_V2=true                      # Optional
LANGCHAIN_PROJECT=agentic-rag                  # Optional
```

> **Important Note**: If you enable tracing by setting `LANGCHAIN_TRACING_V2=true`, you must have a valid LangSmith API key set in `LANGCHAIN_API_KEY`. Without a valid API key, the application will throw an error.

## Getting Started


Install dependencies:

```bash
# using Poetry:
poetry install
```

## Run Locally

1. Clone the project

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