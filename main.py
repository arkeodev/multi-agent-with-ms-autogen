import os

import streamlit as st
from openai import OpenAI

from app import Application
from utils import set_api_keys


def streamlit_ui():
    st.set_page_config(layout="wide")
    set_api_keys()
    api_key = os.environ.get("OPENAI_API_KEY")
    left_column, middle_column, right_column = st.columns([1, 2, 2])

    # Left column: Model selection, temperature adjustment, API URL, and API key
    with left_column:
        st.expander("Settings", expanded=True)
        model = st.selectbox("Select Model", ["gpt-4o-mini", "gpt-4o"])
        temperature = st.slider("Temperature", 0.0, 1.0, 0.2)
        # Initialize the LLM configuration
        llm_config = {
            "config_list": [{"model": model, "api_type": "openai", "tags": [model]}]
        }
        # Create the LLM instance using the new API
        llm = OpenAI(api_key=api_key)
        # Initialize Application
        app = Application(llm_config, llm, model, temperature)
        # File input for RAG collection
        uploaded_file = st.file_uploader("Upload a document for RAG collection")
        if uploaded_file:
            document_content = uploaded_file.read().decode("utf-8")
            app.create_rag_collection(document_content)
            st.success("RAG collection created successfully.")

    # Middle column: Chatbot interaction space
    with middle_column:
        st.header("Chatbot Interaction")
        user_input = st.chat_input("Enter your query: ")
        if user_input:
            response = app.process_user_input(user_input)
            st.write(f"Bot: {response}")

    # Right column: Generated report and visual content
    with right_column:
        st.header("Generated Report")


# Main execution
if __name__ == "__main__":
    streamlit_ui()
