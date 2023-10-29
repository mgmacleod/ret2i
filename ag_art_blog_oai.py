# AutoGen using OAI to process the logs from a recursive AI art project and produce a markdown file

import os, autogen, argparse

log_path = "/home/mgm/development/code/ret2i/log_wavy.csv"
image_path = "/home/mgm/development/code/ret2i/images/2023-10-27"


def create_openai_config_list():
    openai_api_key = os.environ.get("OPENAI_API_KEY")
    config_list = [
        {"api_type": "open_ai", "api_key": openai_api_key, "model": "gpt-3.5-turbo-16k"}
    ]
    return config_list


def create_local_config_list(base_url):
    config_list = [
        {
            "api_type": "open_ai",
            "api_base": base_url,
            "api_key": "sk-111111111111111111111111111111",
        }
    ]

    return config_list


def main(config_list, task):
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
        is_termination_msg=lambda x: x.get("content", "")
        .rstrip()
        .endswith("TERMINATE"),
        code_execution_config={"work_dir": "out", "use_docker": False},
        llm_config=llm_config,
        system_message="""Reply TERMINATE if the task has been solved at full satisfaction.
    Otherwise, reply CONTINUE, or the reason why the task is not solved yet.""",
    )

    user_proxy.initiate_chat(assistant, message=task)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--provider", type=str, default="local")
    parser.add_argument("--model", type=str, default="gpt-3.5-turbo-16k")
    parser.add_argument("--api-url", type=str, default="http://localhost:5001/v1")
    parser.add_argument(
        "--task",
        type=str,
        default="Write python code to print the numbers 1 to 100 and then store the resulting code in a .py file.",
    )
    args = parser.parse_args()

    config_list = None

    if args.provider == "openai":
        config_list = create_openai_config_list()
    else:
        config_list = create_local_config_list(args.api_url)

    task_def = """
    Write Python code to load the local CSV file with absolute path `/home/mgm/development/code/ret2i/log_wavy.csv` file and then print out the `prompt` and `filename` columns for each record. When you have working code, save the code to
    a file called `print_prompt_and_image_pairs.py` and terminate the task.
    """
    main(config_list=config_list, task=task_def)
    # models = get_model_list()

    # demo = build_demo(args.embed)
