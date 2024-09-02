import logging
from typing import Dict

from openai import OpenAI

from chatbot import ChatBot
from utils import create_rag_collection


class Application:
    def __init__(self, llm_config: Dict, llm: OpenAI, model: str, temperature: float):
        self.llm_config = llm_config
        self.llm = llm
        self.model = model
        self.temperature = temperature
        # Initialize ChatBot with the llm_config
        self.chatbot = ChatBot(self.llm_config)

    def process_user_input(self, user_input):
        self.user_input = user_input
        # Define the problem through conversation
        self.define_problem_conversation()
        # Refine the problem definition
        self.refine_problem_definition()
        # Delegate tasks
        self.delegate_tasks()
        # Execute tasks
        self.execute_tasks()
        # Get final response
        return self.get_model_response()

    def define_problem_conversation(self) -> str:
        logging.info("Defining problem through conversation.")
        prompt = f"User input: {self.user_input}\nDefine the problem or task based on this input:"
        response = self.llm.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=self.temperature,
        )
        self.problem_definition = response.choices[0].message.content
        logging.info("Problem defined.")

    def refine_problem_definition(self) -> str:
        logging.info("Refining problem definition.")
        prompt = f"Refine the problem definition: {self.problem_definition}"
        response = self.llm.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=self.temperature,
        )
        self.refined_problem_definition = response.choices[0].message.content
        logging.info("Problem definition refined.")

    def delegate_tasks(self):
        logging.info("Delegating tasks based on problem definition.")
        prompt = f"Based on the problem definition: {self.refined_problem_definition}, list the tasks and the agents required to solve the problem."
        response = self.llm.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=self.temperature,
        )
        self.tasks_and_agents = response.choices[0].message.content
        logging.info("Tasks and agents listed.")

    def execute_tasks(self):
        logging.info("Executing tasks.")
        prompt = f"Execute the following tasks: {self.tasks_and_agents}"
        response = self.llm.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=self.temperature,
        )
        self.execution_result = response.choices[0].message.content
        logging.info("Tasks executed.")

    def get_model_response(self):
        logging.info("Getting model response for user input.")
        prompt = f"Get the final response for the user input: {self.execution_result}"
        response = self.llm.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=self.temperature,
        )
        result = response.choices[0].message.content
        logging.info("Model response received.")
        return result

    def create_rag_collection(self, document_content):
        self.rag_collection = create_rag_collection(document_content)
        logging.info("RAG collection created and set in ChatBot.")
