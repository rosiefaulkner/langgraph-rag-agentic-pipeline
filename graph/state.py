from typing import TypedDict, Literal, List

class GraphState(TypedDict):
    """
    State for the graph

    Args:
        question: question
        generation: generation by LLM
        web_search: whether to add search
        documents: documents retrieved from the vector database
    """
    question: str
    generation: str
    web_search: bool
    documents: List[str]
    
    