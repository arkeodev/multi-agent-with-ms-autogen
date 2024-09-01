import streamlit as st
from agents import ChatBot
from chatbot import (
    get_model_response,
    define_problem_conversation,
    refine_problem_definition,
    delegate_tasks,
    execute_tasks
)
from utils import set_api_keys
import openai

class Application:
    def __init__(self, llm_config, llm):
        self.llm_config = llm_config
        self.llm = llm
        # Initialize ChatBot with the llm_config
        self.chatbot = ChatBot(self.llm_config)

    def process_user_input(self, user_input):
        # Define the problem through conversation
        problem_definition = define_problem_conversation(user_input, self.llm)
        
        # Refine the problem definition
        refined_problem = refine_problem_definition(problem_definition, self.llm)
        
        # Delegate tasks
        tasks_and_agents = delegate_tasks(refined_problem, self.llm)
        
        # Execute tasks
        execution_result = execute_tasks(tasks_and_agents, self.llm)
        
        # Get final response
        final_response = get_model_response(execution_result, self.llm)
        
        return final_response

    def generate_report(self):
        # Implement report generation logic
        return "Generated report content"

    def create_rag_collection(self, document_content):
        # Implement RAG collection creation logic
        pass

def streamlit_ui():
    st.set_page_config(layout="wide")
    left_column, middle_column, right_column = st.columns([1, 2, 2])

    # Left column: Model selection, temperature adjustment, API URL, and API key
    with left_column:
        st.expander("Settings", expanded=True)
        model = st.selectbox("Select Model", ["gpt-4o-mini", "gpt-4o"])
        temperature = st.slider("Temperature", 0.0, 1.0, 0.2)
        
    llm_config = {"config_list": [{"model": model, "api_type": "openai", "tags": [model]}]}
    llm = openai.chat.completions.create(model=model, temperature=temperature)

    # Initialize Application
    app = Application(llm_config, llm)

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
        report_content = app.generate_report()
        st.write(report_content)

    # File input for RAG collection
    uploaded_file = st.file_uploader("Upload a document for RAG collection")
    if uploaded_file:
        document_content = uploaded_file.read().decode("utf-8")
        app.create_rag_collection(document_content)
        st.success("RAG collection created successfully.")

    return app

# Load environment variables and set API keys
set_api_keys()

# Main execution
if __name__ == "__main__":
    app = streamlit_ui()