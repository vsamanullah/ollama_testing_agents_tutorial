import streamlit as st
from langchain_ollama import ChatOllama
llm = ChatOllama(model="llama3.2", temperature=0)
st.title("Q&A with Ollama")
user_question = st.text_input("Ask me anything:")

if st.button("Get Answer") and user_question:
    messages = [
        ("system", "You are a helpful assistant that answers questions."),
        ("human", user_question),
    ]
    response = llm.invoke(messages)
    st.write("Response from Ollama is " ,response.content )

