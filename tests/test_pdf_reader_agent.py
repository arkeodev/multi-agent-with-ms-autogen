import openai

from agents import PDFReaderAgent


def test_pdf_reader_agent():
    agent = PDFReaderAgent(name="PDF Reader")
    file_path = "sample.pdf"  # Replace with the path to your PDF file
    openai.api_key = "your_openai_api_key"  # Replace with your actual API key
    llm = openai.Completion.create
    content = agent.perform_task(file_path, llm)
    print(content)


if __name__ == "__main__":
    test_pdf_reader_agent()
