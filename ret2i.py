import autogen

config_list = autogen.config_list_from_json(
    "OAI_CONFIG_LIST", filter_dict={"model": ["gpt-4"]}
)


# Create an assistant agent
assistant = autogen.AssistantAgent(
    name="assistant",
    llm_config={"seed": 42, "config_list": config_list, "temperature": 0},
)

# Create a UserProxyAgent
user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={"work_dir": "coding", "use_docker": False},
)
