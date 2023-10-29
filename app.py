import autogen

config_list = [
    {
        "api_type": "open_ai",
        "api_base": "http://192.168.0.110:5001/v1",
        "api_key": "sk-111111111111111111111111111111",
    }
]

llm_config = {
    "request_timeout": 600,
    "seed": 42,
    "config_list": config_list,
    "temperature": 0,
}

assistant = autogen.AssistantAgent(
    name="Coder",
    llm_config=llm_config,
    system_message="You are a coder specializing in Python",
)

user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="TERMINATE",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={"work_dir": "out", "use_docker": False},
    llm_config=llm_config,
    system_message="""Reply TERMINATE if the task has been solved at full satisfaction.
Otherwise, reply CONTINUE, or the reason why the task is not solved yet.""",
)

task = """
Write python code to output numbers 1 to 100, confirm that the code works, and then store the code in a .py file.
"""

user_proxy.initiate_chat(assistant, message=task)

# task2 = """
# Change the code in the file you just created to instead output numbers 1 to 200
# """

# user_proxy.initiate_chat(assistant, message=task2)
