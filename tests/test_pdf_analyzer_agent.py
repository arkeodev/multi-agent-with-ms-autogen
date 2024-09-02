import openai

from agents import PDFAnalyzerAgent


def test_pdf_analyzer_agent():
    agent = PDFAnalyzerAgent(name="PDF Analyzer")
    file_path = "sample.pdf"  # Replace with the path to your PDF file
    openai.api_key = "your_openai_api_key"  # Replace with your actual API key
    llm = openai.Completion.create
    result = agent.perform_task(file_path, llm)
    print(result)


if __name__ == "__main__":
    test_pdf_analyzer_agent()
