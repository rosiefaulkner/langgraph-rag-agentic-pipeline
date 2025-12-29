from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel


class StructuredOutputSchema(BaseModel):
    x: str


def test_structured_output() -> None:
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
    print(f"Has with_structured_output: {hasattr(llm, 'with_structured_output')}")

    if hasattr(llm, "with_structured_output"):
        try:
            structured_llm = llm.with_structured_output(StructuredOutputSchema)
            print("✓ with_structured_output works!")
        except Exception as e:
            print(f"✗ Error: {e}")
    else:
        print("✗ Method not available")
