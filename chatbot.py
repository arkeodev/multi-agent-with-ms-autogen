import logging

def get_model_response(user_input, llm):
    logging.info("Getting model response for user input.")
    response = llm(user_input)
    result = response.choices[0].text.strip()
    logging.info("Model response received.")
    return result

def define_problem_conversation(user_input, llm):
    logging.info("Defining problem through conversation.")
    prompt = f"Define the problem based on the following input: {user_input}"
    response = llm(prompt=prompt)
    problem_definition = response.choices[0].text.strip()
    logging.info("Problem defined.")
    return problem_definition

def refine_problem_definition(problem_definition, llm):
    logging.info("Refining problem definition.")
    prompt = f"Refine the problem definition: {problem_definition}"
    response = llm(prompt=prompt)
    refined_problem_definition = response.choices[0].text.strip()
    logging.info("Problem definition refined.")
    return refined_problem_definition

def delegate_tasks(problem_definition, llm):
    logging.info("Delegating tasks based on problem definition.")
    prompt = f"Based on the problem definition: {problem_definition}, list the tasks and the agents required to solve the problem."
    response = llm(prompt=prompt)
    tasks_and_agents = response.choices[0].text.strip()
    logging.info("Tasks and agents listed.")
    return tasks_and_agents

def execute_tasks(tasks_and_agents, llm):
    logging.info("Executing tasks.")
    prompt = f"Execute the following tasks: {tasks_and_agents}"
    response = llm(prompt=prompt)
    execution_result = response.choices[0].text.strip()
    logging.info("Tasks executed.")
    return execution_result
