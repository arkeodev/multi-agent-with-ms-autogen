import logging
from typing import Any, Dict

from autogen import GroupChat, GroupChatManager


def rag_chat(agents: Dict[str, Any]):
    logging.info("Starting RAG chat.")
    groupchat = GroupChat(
        agents=list(agents.values()),
        messages=[],
        max_round=12,
        speaker_selection_method="auto",
    )
    manager = GroupChatManager(
        groupchat=groupchat, llm_config=agents["boss"].llm_config
    )
    agents["boss_aid"].initiate_chat(
        manager,
        message=agents["boss_aid"].message_generator,
        problem="Your problem statement here",
        n_results=3,
    )
    logging.info("RAG chat initiated.")


def norag_chat(agents: Dict[str, Any]):
    logging.info("Starting non-RAG chat.")
    groupchat = GroupChat(
        agents=list(agents.values()),
        messages=[],
        max_round=12,
        speaker_selection_method="auto",
        allow_repeat_speaker=False,
    )
    manager = GroupChatManager(
        groupchat=groupchat, llm_config=agents["boss"].llm_config
    )
    agents["boss"].initiate_chat(
        manager,
        message="Your problem statement here",
    )
    logging.info("Non-RAG chat initiated.")


def call_rag_chat(agents: Dict[str, Any]):
    logging.info("Starting call RAG chat.")
    groupchat = GroupChat(
        agents=list(agents.values()),
        messages=[],
        max_round=12,
        speaker_selection_method="auto",
    )
    manager = GroupChatManager(
        groupchat=groupchat, llm_config=agents["boss"].llm_config
    )
    agents["boss"].initiate_chat(
        manager,
        message="Your problem statement here",
    )
    logging.info("Call RAG chat initiated.")
