import os
import streamlit as st
from langchain_groq import ChatGroq
from dotenv import load_dotenv

#load env file -api key
load_dotenv()

st.set_page_config(
    page_title ="chatBot",
    page_icon="",
    layout="centered"
)
st.title("AI ChatBot")


if "chat_history" not in st.session_state:
    st.session_state.chat_history=[]

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature = 1.0
)

user_prompt=st.chat_input("Ask!")

if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role":"user", "content":user_prompt})

    response = llm.invoke([{"role":"system", "content":"You are chat assistant, be consice when reply!"}, *st.session_state.chat_history])

    st.chat_message("ai").markdown(response.content)
    st.session_state.chat_history.append({"role":"ai", "content":response.content})

