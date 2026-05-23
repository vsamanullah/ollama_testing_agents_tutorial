import requests

# Using /api/chat - uses messages list (supports conversation history)
url = "http://localhost:11434/api/chat"

payload = {
    "model": "llama3.2",
    "messages": [
        {
            "role": "user",
            "content": "Why is the sky blue?"
        }
    ],
    "stream": False,
}

response = requests.post(url, json=payload)
print(response.json()["message"]["content"])
