from langchain_ollama import OllamaLLM
 model = OllamaLLM(
     model="llama3.2",
     temperature=0.7,
     num_predict=256,
     # base_url="http://localhost:11434",
     # other params...
 )

 input_text = "The meaning of life is "
 response = model.invoke(input_text)
 print(response)

from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.2",
    temperature=0,
    # other params...
)

messages = [
    (
        "system",
        "You are a helpful assistant that translates English to French. Translate the user sentence.",
    ),
    ("human", "I love programming."),
]
ai_msg = llm.invoke(messages)
print(ai_msg.content)