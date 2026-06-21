import streamlit as st

st.title("Counter WITH Session State")

# Session state variable - SURVIVES reruns
if "counter" not in st.session_state:
    st.session_state.counter = 0  # only sets to 0 on FIRST run

if st.button("Click me"):
    st.session_state.counter += 1  # survives the rerun!

st.write(f"Button clicked {st.session_state.counter} times")
st.success("Notice: the counter correctly counts up on every click!")
