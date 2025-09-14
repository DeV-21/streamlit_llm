import os
from langchain_openai import ChatOpenAI
import streamlit as st

st.title("Ask Anything")

with st.sidebar:
    st.title("Provide your OpenAI API Key")
    OPENAI_API_KEY = st.text_input("OpenAI API Key", type="password")

if not OPENAI_API_KEY:
    st.info("Enter your OpenAI API Key to continue.")
    st.stop()

llm = ChatOpenAI(model="gpt-3.5-turbo", api_key=OPENAI_API_KEY)

question = st.text_input("Enter the question:")

if question:
    response = llm.invoke(question)

    st.write(response.content)
