# AutoGen using OAI to process the logs from a recursive AI art project and produce a markdown file

import os, autogen

log_path = "log_wavy.csv"
image_path = "images/2023-10-27"

openai_api_key = os.environ.get("OPENAI_API_KEY")

config_list = [
    {
        "api_type": "open_ai",
        "api_key": openai_api_key,
    }
]

llm_config = {
    "request_timeout": 600,
    # "seed": 42,
    "config_list": config_list,
    "temperature": 0,
}

assistant = autogen.AssistantAgent(
    name="Coder",
    llm_config=llm_config,
    system_message="You are a coder specializing in Python. Your job is to write the code to solve problems assigned to you.",
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
Write Python code to load the local `log_wavy.csv` file and then print out the `prompt` and `filename` columns for each record. When you have working code, save the code to 
a file called `print_that_shit.py` and terminate the task.
"""

user_proxy.initiate_chat(assistant, message=task)
