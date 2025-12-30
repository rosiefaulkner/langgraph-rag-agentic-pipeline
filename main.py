from dotenv import load_dotenv

load_dotenv()

from graph.graph import app

if __name__ == "__main__":
    print("HELLO ADVANCED RAG")
    print(
        app.invoke(
            input={
                "question": "What is the most efficient way to identify the encoding by LLM dynamically. For example, is there a pypi library"
            }
        )
    )
