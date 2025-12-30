import os
from typing import Literal

from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field


class RouteQuery(BaseModel):
    """Route a user query to the most relevant datasource."""

    datasource: Literal["vectorstore", "websearch"] = Field(
        ...,
        description="Given a user question choose to route it to web search or a vectorstore",
    )


# Load environment variables
load_dotenv()

# Get API key and ensure it's set
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError(
        "GEMINI_API_KEY environment variable is not set. Please set it in your .env file."
    )

# Allow model to be configured via environment variable, with fallback options
# Options: gemini-2.5-flash (20 req/day free), gemini-2.5-flash-lite (1000 req/day free), gemini-1.5-flash
model = os.getenv(
    "GEMINI_MODEL", "gemini-2.5-flash-lite"
)  # Default to lite for higher quota

llm = ChatGoogleGenerativeAI(model=model, temperature=0, google_api_key=api_key)
structured_llm_router = llm.with_structured_output(RouteQuery)

system = """You are an expert at routing a user question to a vectorstore or web search.
The vectorstore contains documents related to agents, prompt engineering, and adversarial attacks.
Use the vectorstore for questions on these topics. For all else, use web-search."""
route_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("human", "{question}"),
    ]
)

question_router = route_prompt | structured_llm_router
