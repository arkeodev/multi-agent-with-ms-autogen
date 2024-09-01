import os
import logging
from dotenv import load_dotenv
import chromadb

def set_api_keys(env_file_path=".env"):
    """Loads and sets necessary API keys for OpenAI and LangFuse."""
    logging.info("Attempting to load API keys from specified .env file.")
    load_dotenv(env_file_path)

    openai_key = os.getenv("OPENAI_API_KEY")
    if openai_key:
        logging.info("OpenAI API key loaded successfully.")
    else:
        logging.error("OpenAI API key not found in .env file.")

def setup_logging():
    """Sets up logging configuration."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[logging.StreamHandler()],
    )

def create_rag_collection(document_content):
    logging.info("Creating RAG collection.")
    chroma_db = chromadb.ChromaDB()
    collection_name = "groupchat"
    chroma_db.create_collection(collection_name)
    chroma_db.add_documents(collection_name, [document_content])
    logging.info("RAG collection created successfully.")

def termination_msg(x):
    return isinstance(x, dict) and "TERMINATE" == str(x.get("content", ""))[-9:].upper()
