import requests
from dotenv import load_dotenv
import os
# reads variables from a .env file and sets them in os.enviro
load_dotenv()

base_url = os.getenv("OLLAMA_BASE_URL")
llm_model = os.getenv("OLLAMA_MODEL")

print(base_url)
print(llm_model)


url = f"{base_url}/api/chat"

payload = {
  "model": llm_model,
  "messages": [
    {
      "role": "user",
      "content": "why is the sky blue?"
    }
  ],
    "stream" : False,
}

response_val = requests.post(url,json=payload)
response_body = response_val.json()['message']['content']
print(response_body)