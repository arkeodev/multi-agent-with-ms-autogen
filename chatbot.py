import logging
from typing import Any, Callable, Dict

from agents import create_agents, reset_agents
from chat_functions import call_rag_chat, norag_chat, rag_chat


class ChatBot:
    def __init__(self, llm_config: Dict[str, Any]):
        self.agents = create_agents(llm_config)
        self.rag_collection = None
        self.reset()

    def rag_chat(self):
        rag_chat(self.agents, self.rag_collection)

    def norag_chat(self):
        norag_chat(self.agents)

    def call_rag_chat(self):
        call_rag_chat(self.agents, self.rag_collection)

    def reset(self):
        reset_agents(self.agents)
