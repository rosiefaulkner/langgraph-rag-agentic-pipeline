import os

from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field

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


class GradeAnswer(BaseModel):
    """
    Binary score for hallucination present in generated answer.
    """

    binary_score: bool = Field(
        description="Answer addresses the question, 'yes' or 'no'"
    )
    reasoning: str = Field(description="Brief explanation of why the score was given.")


structured_llm_grader = llm.with_structured_output(GradeAnswer)

system = """You are a grader assessing whether an answer addresses / resolves a question \n 
     Give a binary score 'yes' or 'no'. Yes' means that the answer resolves the question."""

answer_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("human", "User question: \n\n {question} \n\n LLM generation: {generation}"),
    ]
)

answer_grader: RunnableSequence = answer_prompt | structured_llm_grader
