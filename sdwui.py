import base64
import io
import json

import requests
from PIL import Image

url = "http://localhost:8860"

payload = {"prompt": "puppy dog", "steps": 5}

response = requests.post(url=f"{url}/sdapi/v1/txt2img", json=payload)

r = response.json()

image = Image.open(io.BytesIO(base64.b64decode(r["images"][0])))
image.save("output.png")
