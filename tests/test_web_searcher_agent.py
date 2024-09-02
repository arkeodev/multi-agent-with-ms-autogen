import openai

from agents import WebSearcherAgent


def test_web_searcher_agent():
    agent = WebSearcherAgent(name="Web Searcher")
    query = "OpenAI GPT-4"
    openai.api_key = "your_openai_api_key"  # Replace with your actual API key
    llm = openai.Completion.create
    results = agent.perform_task(query, llm)
    for result in results:
        print(result)


if __name__ == "__main__":
    test_web_searcher_agent()
