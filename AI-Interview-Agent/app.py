import requests
import streamlit as st

st.title(" AI Interview Agent")

#User uploads Resume.

uploaded = st.file_uploader(
    "Upload Resume",
    type="pdf"
)

if uploaded:

    files = {

        "file":
        (
            uploaded.name,
            uploaded.getvalue(),
            "application/pdf"
        )
    }
#calls FastAPI
    response = requests.post(
        "http://127.0.0.1:8000/upload",
        files=files
    )

    st.write("Status Code:", response.status_code)
    st.write("Response Text:")
    st.code(response.text)


#app.py (Frontend)
#This is your Streamlit UI.
#The user only interacts with this file.

#User
#↓
#Browser
#↓
#Streamlit
#↓
#FastAPI