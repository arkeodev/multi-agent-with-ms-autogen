import openai

from agents import CodeWriterAgent


def test_code_writer_agent():
    agent = CodeWriterAgent(name="Code Writer")
    requirements = "sorts a list of integers in ascending order"
    openai.api_key = "your_openai_api_key"  # Replace with your actual API key
    llm = openai.Completion.create
    result = agent.perform_task(requirements, llm)
    print(result)


if __name__ == "__main__":
    test_code_writer_agent()
