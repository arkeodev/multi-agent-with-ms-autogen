import os

import openai
from dotenv import load_dotenv

from agents import (
    APIReaderAgent,
    CodeWriterAgent,
    DocumentWriterAgent,
    PDFAnalyzerAgent,
    PDFReaderAgent,
    PlanningManagerAgent,
    PostgresAgent,
    WebBrowserAgent,
    WebSearcherAgent,
    WikipediaAgent,
)

# Load environment variables from .env file
load_dotenv()


def test_web_searcher_agent():
    agent = WebSearcherAgent(name="Web Searcher")
    query = "OpenAI GPT-4"
    openai.api_key = os.getenv("OPENAI_API_KEY")
    llm = openai.Completion.create
    results = agent.perform_task(query, llm)
    for result in results:
        print(result)


def test_web_browser_agent():
    agent = WebBrowserAgent(name="Web Browser")
    url = "https://www.example.com"
    openai.api_key = os.getenv("OPENAI_API_KEY")
    llm = openai.Completion.create
    content = agent.perform_task(url, llm)
    print(content)


def test_pdf_reader_agent():
    agent = PDFReaderAgent(name="PDF Reader")
    file_path = "sample.pdf"  # Replace with the path to your PDF file
    openai.api_key = os.getenv("OPENAI_API_KEY")
    llm = openai.Completion.create
    content = agent.perform_task(file_path, llm)
    print(content)


def test_wikipedia_agent():
    agent = WikipediaAgent(name="Wikipedia Researcher")
    topic = "OpenAI"
    openai.api_key = os.getenv("OPENAI_API_KEY")
    llm = openai.Completion.create
    content = agent.perform_task(topic, llm)
    print(content)


def test_planning_manager_agent():
    web_searcher = WebSearcherAgent(name="Web Searcher")
    wikipedia_researcher = WikipediaAgent(name="Wikipedia Researcher")

    agents = {
        "Web Searcher": web_searcher,
        "Wikipedia Researcher": wikipedia_researcher,
    }

    planning_manager = PlanningManagerAgent(name="Planning Manager", agents=agents)
    task_list = [("Web Searcher", "OpenAI GPT-4"), ("Wikipedia Researcher", "OpenAI")]
    openai.api_key = os.getenv("OPENAI_API_KEY")
    llm = openai.Completion.create

    results = planning_manager.perform_task(task_list, llm)
    for agent_name, result in results.items():
        print(f"{agent_name}: {result}")


def test_document_writer_agent():
    agent = DocumentWriterAgent(name="Document Writer")
    content = "This is a sample content for the generated report."
    openai.api_key = os.getenv("OPENAI_API_KEY")
    llm = openai.Completion.create
    result = agent.perform_task(content, llm)
    print(result)


def test_code_writer_agent():
    agent = CodeWriterAgent(name="Code Writer")
    requirements = "sorts a list of integers in ascending order"
    openai.api_key = os.getenv("OPENAI_API_KEY")
    llm = openai.Completion.create
    result = agent.perform_task(requirements, llm)
    print(result)


def test_pdf_analyzer_agent():
    agent = PDFAnalyzerAgent(name="PDF Analyzer")
    file_path = "sample.pdf"  # Replace with the path to your PDF file
    openai.api_key = os.getenv("OPENAI_API_KEY")
    llm = openai.Completion.create
    result = agent.perform_task(file_path, llm)
    print(result)


def test_postgres_agent():
    db_config = {
        "dbname": "your_db_name",
        "user": "your_db_user",
        "password": "your_db_password",
        "host": "your_db_host",
        "port": "your_db_port",
    }
    agent = PostgresAgent(name="Postgres Agent", db_config=db_config)
    query = "list all users with their email addresses"
    openai.api_key = os.getenv("OPENAI_API_KEY")
    llm = openai.Completion.create
    result = agent.perform_task(query, llm)
    print(result)


def test_api_reader_agent():
    agent = APIReaderAgent(name="API Reader")
    api_url = "https://api.example.com/data"  # Replace with your API URL
    api_key = "your_api_key"  # Replace with your API key
    openai.api_key = os.getenv("OPENAI_API_KEY")
    llm = openai.Completion.create
    result = agent.perform_task(api_url, api_key, llm)
    print(result)


if __name__ == "__main__":
    test_web_searcher_agent()
    test_web_browser_agent()
    test_pdf_reader_agent()
    test_wikipedia_agent()
    test_planning_manager_agent()
    test_document_writer_agent()
    test_code_writer_agent()
    test_pdf_analyzer_agent()
    test_postgres_agent()
    test_api_reader_agent()
