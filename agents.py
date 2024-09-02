import json
import logging
from typing import Any, Dict

from autogen import AssistantAgent, UserProxyAgent
from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent

from chat_functions import call_rag_chat, norag_chat, rag_chat
from custom_agents import CustomAssistantAgent, CustomUserProxyAgent
from utils import create_rag_collection, termination_msg

logging.basicConfig(level=logging.INFO)


class AgentFactory:
    @staticmethod
    def create_agent(agent_type: str, **kwargs) -> Any:
        agent_classes = {
            "AssistantAgent": AssistantAgent,
            "UserProxyAgent": UserProxyAgent,
            "RetrieveUserProxyAgent": RetrieveUserProxyAgent,
            "CustomAssistantAgent": CustomAssistantAgent,
            "CustomUserProxyAgent": CustomUserProxyAgent,
        }

        if agent_type not in agent_classes:
            raise ValueError(f"Unknown agent type: {agent_type}")

        return agent_classes[agent_type](**kwargs)


def load_agent_configs() -> Dict[str, Any]:
    with open("agent_config.json", "r") as f:
        return json.load(f)


def create_agents(llm_config: Dict[str, Any]) -> Dict[str, Any]:
    agent_configs = load_agent_configs()
    agents = {}
    for agent_name, agent_config in agent_configs.items():
        agent_config["llm_config"] = llm_config
        agent_config["is_termination_msg"] = termination_msg
        agents[agent_name] = AgentFactory.create_agent(**agent_config)
    return agents


def reset_agents(agents: Dict[str, Any]) -> None:
    for agent in agents.values():
        agent.reset()
    logging.info("All agents reset.")
