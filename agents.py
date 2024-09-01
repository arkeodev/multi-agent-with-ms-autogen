import logging
from typing import Dict, Any
import json
from autogen import AssistantAgent, UserProxyAgent, config_list_from_json
from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent
from custom_agents import CustomAssistantAgent, CustomUserProxyAgent
from utils import create_rag_collection, termination_msg
from chat_functions import rag_chat, norag_chat, call_rag_chat

logging.basicConfig(level=logging.INFO)

class AgentFactory:
    @staticmethod
    def create_agent(agent_type: str, **kwargs) -> Any:
        agent_classes = {
            "AssistantAgent": AssistantAgent,
            "UserProxyAgent": UserProxyAgent,
            "RetrieveUserProxyAgent": RetrieveUserProxyAgent,
            "CustomAssistantAgent": CustomAssistantAgent,
            "CustomUserProxyAgent": CustomUserProxyAgent
        }
        
        if agent_type not in agent_classes:
            raise ValueError(f"Unknown agent type: {agent_type}")
        
        return agent_classes[agent_type](**kwargs)

def load_agent_configs() -> Dict[str, Any]:
    with open('agent_config.json', 'r') as f:
        return json.load(f)

def create_agents(llm_config: Dict[str, Any]) -> Dict[str, Any]:
    agent_configs = load_agent_configs()
    agents = {}
    for agent_name, agent_config in agent_configs.items():
        agent_config['llm_config'] = llm_config
        agent_config['is_termination_msg'] = termination_msg
        agents[agent_name] = AgentFactory.create_agent(**agent_config)
    return agents

def reset_agents(agents: Dict[str, Any]) -> None:
    for agent in agents.values():
        agent.reset()
    logging.info("All agents reset.")

class ChatBot:
    def __init__(self, llm_config: Dict[str, Any]):
        self.agents = create_agents(llm_config)
        self.rag_collection = create_rag_collection()  # Assuming this function exists in utils.py

    def rag_chat(self):
        rag_chat(self.agents)

    def norag_chat(self):
        norag_chat(self.agents)

    def call_rag_chat(self):
        call_rag_chat(self.agents)

    def reset(self):
        reset_agents(self.agents)

class Application:
    def __init__(self, config_path: str):
        llm_config = config_list_from_json(config_path)
        self.chatbot = ChatBot(llm_config)

    def run(self):
        # Example usage
        self.chatbot.rag_chat()
        self.chatbot.reset()
        self.chatbot.norag_chat()
        self.chatbot.reset()
        self.chatbot.call_rag_chat()

# Main execution
if __name__ == "__main__":
    app = Application("path/to/your/config.json")
    app.run()