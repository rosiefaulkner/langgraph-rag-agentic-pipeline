from langchain_classic import hub
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key and ensure it's set
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY environment variable is not set. Please set it in your .env file.")

# Allow model to be configured via environment variable, with fallback options
# Options: gemini-2.5-flash (20 req/day free), gemini-2.5-flash-lite (1000 req/day free), gemini-1.5-flash
model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash-lite")  # Default to lite for higher quota

llm = ChatGoogleGenerativeAI(
    model=model,
    temperature=0,
    google_api_key=api_key
)

prompt = hub.pull("rlm/rag-prompt")

generation_chain = prompt | llm | StrOutputParser()