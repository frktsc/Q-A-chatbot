from dotenv import load_dotenv
load_dotenv()


import os
import streamlit as st
import google.generativeai as genai


genai.configure(api_key=os.getenv("GOOLE_API_KEY"))

model=genai.GenerativeModel("gemini-pro")
chat = model.start_chat()
def get_Response(question):
    response = chat.send_message(question)
    return response.text

st.set_page_config(page_title="Q-A CHATBOT")

st.header("Q-A CHATBOT")

input=st.text_input("Input: ",key="input")

submit=st.button("Submit")

if submit:
    response=get_Response(input)
    st.subheader("the response is")
    st.write(response)