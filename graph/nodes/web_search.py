from typing import Any, Dict
import sys
from pathlib import Path

from langchain_core.documents import Document
from langchain_community.tools.tavily_search import TavilySearchResults
from dotenv import load_dotenv

# Handle imports for both module and direct execution
try:
    from graph.state import GraphState
except ImportError:
    # For testing, we will be running directly, so add project root to path
    project_root = Path(__file__).parent.parent.parent
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))
    from graph.state import GraphState

load_dotenv()
web_search_tool = TavilySearchResults(max_results=3)

def web_search(state: GraphState) -> Dict[str, Any]:
    print("---WEB SEARCH---")
    question = state["question"]
    documents = state["documents"]
    
    tavily_results = web_search_tool.invoke({"query": question})
    joined_tavily_result = "\n".join(
        [tavily_result["content"] for tavily_result in tavily_results]
    )
    web_results = Document(page_content=joined_tavily_result)
    if documents is not None:
        documents.append(web_results)
    else:
        documents = [web_results]
    return {"documents": documents, "question": question}

if __name__ == "__main__":
    web_search(state={"question": "agent memory", "documents": None})
