from dotenv import load_dotenv

load_dotenv()

from graph.graph import app

if __name__ == "__main__":
    print("---HELLO ADVANCED RAG---")
    print(
        app.invoke(
            input={
                "question": "What is agent memory?"
            }
        )
    )
