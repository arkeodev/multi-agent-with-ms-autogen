import logging
from typing import Dict, Any
from autogen import GroupChat, GroupChatManager

def custom_speaker_selection_func(last_speaker: str, groupchat: GroupChat) -> str:
    if last_speaker == "Boss":
        return "Planner"
    elif last_speaker == "Planner":
        return "Critic"
    elif last_speaker == "Critic":
        return "Admin"
    elif last_speaker == "Admin":
        if "proceed" in groupchat.messages[-1].content.lower():
            return "Engineer"
        else:
            return "Planner"
    elif last_speaker == "Engineer":
        return "Scientist"
    elif last_speaker == "Scientist":
        return "Boss"
    else:
        return "Boss"

def rag_chat(agents: Dict[str, Any]):
    logging.info("Starting RAG chat.")
    groupchat = GroupChat(
        agents=list(agents.values()),
        messages=[],
        max_round=12,
        speaker_selection_method=custom_speaker_selection_func
    )
    manager = GroupChatManager(groupchat=groupchat, llm_config=agents['boss'].llm_config)
    agents['boss_aid'].initiate_chat(
        manager,
        message=agents['boss_aid'].message_generator,
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
        speaker_selection_method=custom_speaker_selection_func,
        allow_repeat_speaker=False,
    )
    manager = GroupChatManager(groupchat=groupchat, llm_config=agents['boss'].llm_config)
    agents['boss'].initiate_chat(
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
        speaker_selection_method=custom_speaker_selection_func
    )
    manager = GroupChatManager(groupchat=groupchat, llm_config=agents['boss'].llm_config)
    agents['boss'].initiate_chat(
        manager,
        message="Your problem statement here",
    )
    logging.info("Call RAG chat initiated.")
