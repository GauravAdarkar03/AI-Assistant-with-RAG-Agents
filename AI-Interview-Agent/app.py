import requests
import streamlit as st

st.title("🤖 AI Interview Agent")

if st.button("Generate Interview Question"):

    response = requests.get("http://127.0.0.1:8000/question")

    st.write("Status Code:", response.status_code)

    st.json(response.json())