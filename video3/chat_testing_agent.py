import streamlit as st
from langchain_ollama import ChatOllama

# ============================================================
#   STEP 1: Initialize the AI Model
# ============================================================

# ChatOllama is the conversational version of OllamaLLM
# It understands message history (human/assistant/system)
llm = ChatOllama(model="llama3.2", temperature=0.7)

# ============================================================
#   STEP 2: Define the System Prompt
# ============================================================

# This invisible instruction shapes how the AI behaves
# throughout the entire conversation
SYSTEM_PROMPT = """You are an expert QA engineer and testing specialist with 10+ years of experience.

Your job is to help the user with all things related to software testing:
- Generate test cases (functional, negative, edge case, security, performance)
- Create test data
- Write bug reports
- Design test plans
- Suggest testing strategies

When generating test cases, always use this format:
- Test Case ID (e.g. TC001)
- Title
- Preconditions
- Test Steps (numbered)
- Expected Result
- Priority (High / Medium / Low)

Be specific, professional, and practical. Ask clarifying questions when needed."""

# ============================================================
#   STEP 3: Initialize Chat History in Session State
# ============================================================

# st.session_state keeps data alive between Streamlit reruns
# We only create the messages list once (on first run)
if "messages" not in st.session_state:
    st.session_state.messages = []

# ============================================================
#   STEP 4: Page Layout
# ============================================================

st.title("AI Testing Agent")
st.caption("Your conversational QA assistant — powered by LLaMA running locally")

# Sidebar with quick prompts to help users get started
with st.sidebar:
    st.header("Quick Prompts")
    st.markdown("""
    Try asking:
    - *Generate 3 test cases for user login*
    - *Add edge cases for email validation*
    - *Create a bug report for a broken button*
    - *What is the difference between smoke and regression testing?*
    - *Generate test data for a registration form*
    """)

    # Clear chat button
    if st.button("Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# ============================================================
#   STEP 5: Display Existing Chat History
# ============================================================

# Loop through saved messages and display each one
# This runs every time the script reruns (on every user action)
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ============================================================
#   STEP 6: Handle New User Input
# ============================================================

# st.chat_input shows the input bar at the bottom of the screen
# It returns the text when user presses Enter, otherwise None
user_input = st.chat_input("Ask your testing question...")

if user_input:

    # --- 6a: Save and display the user's message ---
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    # --- 6b: Build the full message list to send to the AI ---
    # We always start with the system prompt (invisible to user)
    # Then we add the entire conversation history
    # This is how the AI "remembers" — it reads the whole thread
    full_message_history = [("system", SYSTEM_PROMPT)]

    for msg in st.session_state.messages:
        full_message_history.append((msg["role"], msg["content"]))

    # --- 6c: Get AI response ---
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = llm.invoke(full_message_history)
            ai_reply = response.content

        st.markdown(ai_reply)

    # --- 6d: Save AI response to history ---
    st.session_state.messages.append({
        "role": "assistant",
        "content": ai_reply
    })


