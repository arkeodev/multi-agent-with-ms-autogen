from agents import WikipediaAgent
import openai

def test_wikipedia_agent():
    agent = WikipediaAgent(name="Wikipedia Researcher")
    topic = "OpenAI"
    openai.api_key = "your_openai_api_key"  # Replace with your actual API key
    llm = openai.Completion.create
    content = agent.perform_task(topic, llm)
    print(content)

if __name__ == "__main__":
    test_wikipedia_agent()