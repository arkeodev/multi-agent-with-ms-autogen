from agents import PostgresAgent
import openai

def test_postgres_agent():
    db_config = {
        'dbname': 'your_db_name',
        'user': 'your_db_user',
        'password': 'your_db_password',
        'host': 'your_db_host',
        'port': 'your_db_port'
    }
    agent = PostgresAgent(name="Postgres Agent", db_config=db_config)
    query = "list all users with their email addresses"
    openai.api_key = "your_openai_api_key"  # Replace with your actual API key
    llm = openai.Completion.create
    result = agent.perform_task(query, llm)
    print(result)

if __name__ == "__main__":
    test_postgres_agent()