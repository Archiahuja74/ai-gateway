import streamlit as st
import requests

st.title("AI Gateway")

prompt = st.text_input("Enter your question")

if st.button("Submit"):
    res = requests.post(
        "http://127.0.0.1:8000/chat",
        params={"prompt": prompt}
    )
    data = res.json()

    st.write("Response:", data["response"])
    st.write("Model used:", data.get("model"))
    st.write("Reason:", data.get("reason"))