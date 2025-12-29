from typing import Any, Dict, List

from graph.state import GraphState
from ingestion import retriever

def retrieve(state: GraphState) -> Dict[str, Any]:
    """
    Retrieve documents from the vector database.
    Performs vector search semantically and returns
    relevant documents.
    
    Args:
        state: GraphState
    
    Returns:
        Dict[str, Any]: Dictionary containing the retrieved documents
    """
    print("---RETRIEVE---")
    question = state["question"]
    documents = retriever.invoke(question)
    print(f"Retrieved {len(documents)} documents")
    return {"documents": documents, "question": question}