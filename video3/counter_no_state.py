import streamlit as st

st.title("Counter WITHOUT Session State")

# Normal variable - DIES on every rerun
counter = 0  # always resets to 0

if st.button("Click me"):
    counter += 1  # this increment is lost immediately after the rerun

st.write(f"Button clicked {counter} times")
st.warning("Notice: the counter NEVER goes above 1 — it resets every click!")
