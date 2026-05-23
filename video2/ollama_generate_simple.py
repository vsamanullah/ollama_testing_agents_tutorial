import requests

# Using /api/generate - single prompt, single response (no message history)
url = "http://localhost:11434/api/generate"

payload = {
    "model": "llama3.2",
    "prompt": "Why is the sky blue?",
    "stream": False,
}

response = requests.post(url, json=payload)
print(response.json()["response"])
