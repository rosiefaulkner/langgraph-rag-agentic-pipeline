from typing import Any, Dict

from graph.chains.retrieval_grader import retrieval_grader
from graph.state import GraphState


def grade_documents(state: GraphState) -> Dict[str, Any]:
    """
    Determines whether the retrieved documents are relevant to the question.
    Only triggers web search if there are NO relevant documents or insufficient relevant documents.

    Args:
        state (GraphState): the current graph state

    Returns:
        Dict[str, Any]: Filtered out relevant documents and updated web_search state
    """
    print("---CHECK DOCUMENT RELEVANCE TO QUESTION---")
    question = state["question"]
    documents = state["documents"]
    
    filtered_docs = []
    web_search = False
    for d in documents:
        score = retrieval_grader.invoke(
            {"question": question, "document": d.page_content}
        )
        grade = score.binary_score
        if grade.lower() == "yes":
            print("---GRADE: DOCUMENT RELEVANT---")
            filtered_docs.append(d)
        else:
            print("---GRADE: DOCUMENT NOT RELEVANT---")
            web_search = True
            continue
    
    # Only trigger web search if we have NO relevant documents
    # This means we will return web-search results when the vector database doesn't have good information for this question
    # web_search = len(filtered_docs) == 0
    
    # if web_search:
    #     print(f"---NO RELEVANT DOCUMENTS FOUND ({len(documents)} retrieved, 0 relevant). TRIGGERING WEB SEARCH---")
    # else:
    #     print(f"---FOUND {len(filtered_docs)} RELEVANT DOCUMENT(S) OUT OF {len(documents)} RETRIEVED---")
    
    return {"documents": filtered_docs, "question": question, "web_search": web_search}