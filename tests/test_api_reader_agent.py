import openai

from agents import APIReaderAgent


def test_api_reader_agent():
    agent = APIReaderAgent(name="API Reader")
    api_url = "https://api.example.com/data"  # Replace with your API URL
    api_key = "your_api_key"  # Replace with your API key
    openai.api_key = "your_openai_api_key"  # Replace with your actual API key
    llm = openai.Completion.create
    result = agent.perform_task(api_url, api_key, llm)
    print(result)


if __name__ == "__main__":
    test_api_reader_agent()
