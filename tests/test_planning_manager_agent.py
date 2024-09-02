import openai

from agents import PlanningManagerAgent, WebSearcherAgent, WikipediaAgent


def test_planning_manager_agent():
    web_searcher = WebSearcherAgent(name="Web Searcher")
    wikipedia_researcher = WikipediaAgent(name="Wikipedia Researcher")

    agents = {
        "Web Searcher": web_searcher,
        "Wikipedia Researcher": wikipedia_researcher,
    }

    planning_manager = PlanningManagerAgent(name="Planning Manager", agents=agents)
    task_list = [("Web Searcher", "OpenAI GPT-4"), ("Wikipedia Researcher", "OpenAI")]
    openai.api_key = "your_openai_api_key"  # Replace with your actual API key
    llm = openai.Completion.create

    results = planning_manager.perform_task(task_list, llm)
    for agent_name, result in results.items():
        print(f"{agent_name}: {result}")


if __name__ == "__main__":
    test_planning_manager_agent()
