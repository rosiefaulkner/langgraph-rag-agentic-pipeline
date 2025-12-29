import os
from dotenv import load_dotenv
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain_community.document_loaders import WebBaseLoader

os.environ["USER_AGENT"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"

load_dotenv()

urls = [
    "https://lilianweng.github.io/posts/2023-06-23-agent/",
    "https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/",
    "https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/",
]

# Setup Embeddings
embeddings = GoogleGenerativeAIEmbeddings(
    model="text-embedding-004",
    google_api_key=os.getenv("GEMINI_API_KEY")
)

persist_dir = "./.chroma"

# Check if vectorstore already exists and has documents
vectorstore_exists = os.path.exists(persist_dir)
needs_reindex = False

if vectorstore_exists:
    # Try to load existing vectorstore and check if it has documents
    try:
        test_vectorstore = Chroma(
            collection_name="rag-chroma",
            embedding_function=embeddings,
            persist_directory=persist_dir,
        )
        # Check collection count to see if vectorstore has documents
        collection = test_vectorstore._collection
        doc_count = collection.count()
        if doc_count == 0:
            # Vectorstore exists but is empty
            needs_reindex = True
            print("Vectorstore exists but is empty. Re-indexing...")
        else:
            # Test retrieval to ensure embeddings are compatible
            test_retriever = test_vectorstore.as_retriever()
            test_results = test_retriever.invoke("agent")
            if len(test_results) == 0:
                # Embedding mismatch - vectorstore was created with different model
                needs_reindex = True
                print("Vectorstore has embedding mismatch. Re-indexing...")
            else:
                vectorstore = test_vectorstore
                print(f"Loaded existing vectorstore with {doc_count} documents")
    except Exception as e:
        # If loading fails, we need to re-index
        needs_reindex = True
        print(f"Error loading vectorstore: {e}. Re-indexing...")

if not vectorstore_exists or needs_reindex:
    # Create or recreate vectorstore
    if needs_reindex:
        # Remove old vectorstore if the embeddings use different model
        import shutil
        if os.path.exists(persist_dir):
            shutil.rmtree(persist_dir)
            print("Removed old vectorstore directory")
    
    loader = WebBaseLoader(urls)
    docs_list = loader.load()
    
    text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=250, chunk_overlap=0
    )
    doc_splits = text_splitter.split_documents(docs_list)
    
    vectorstore = Chroma.from_documents(
        documents=doc_splits,
        collection_name="rag-chroma",
        embedding=embeddings,
        persist_directory=persist_dir,
    )

# Create Retriever
retriever = vectorstore.as_retriever()