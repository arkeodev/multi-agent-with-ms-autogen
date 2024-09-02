import openai

from agents import DocumentWriterAgent


def test_document_writer_agent():
    agent = DocumentWriterAgent(name="Document Writer")
    content = "This is a sample content for the generated report."
    openai.api_key = "your_openai_api_key"  # Replace with your actual API key
    llm = openai.Completion.create
    result = agent.perform_task(content, llm)
    print(result)


if __name__ == "__main__":
    test_document_writer_agent()
