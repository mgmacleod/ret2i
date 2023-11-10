import json
import os
import random
from typing import Any, Callable, Dict, List, Optional, Tuple, Type, Union

import autogen
import requests
from autogen import Agent, AssistantAgent, ConversableAgent, UserProxyAgent
from termcolor import colored

from upstream.llava_agent import llava_call_binary

HOST_IP = "localhost"
LLAVA_PORT = "10000"
SDWUI_PORT = "8860"

llava_config_list = [
    {
        "model": "llava-v1.5-13b",
        "api_key": "None",
        "base_url": f"http://{HOST_IP}:{LLAVA_PORT}",
    }
]

# rst = llava_call(
#     "Describe this AutoGen framework <img https://raw.githubusercontent.com/microsoft/autogen/main/website/static/img/autogen_agentchat.png> with bullet points.",
#     llm_config={"config_list": llava_config_list, "temperature": 0},
# )


def call_stable_diffusion(prompt: str, steps: int = 5):
    payload = {"prompt": prompt, "steps": steps}

    response = requests.post(
        url=f"http://{HOST_IP}:{SDWUI_PORT}/sdapi/v1/txt2img", json=payload
    )

    r = response.json()
    img = r["images"][0]

    return img


def main():
    img = call_stable_diffusion("wavy lines")

    rst = llava_call_binary(
        prompt="what do you see here?",
        config_list=llava_config_list,
        images=[img],
    )
    print(rst)


if __name__ == "__main__":
    main()
