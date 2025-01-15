import streamlit as st
import os
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

# Constants
MODEL = "gpt-4o-mini"

# Button functionality
def generate_summary(email):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Generate a summary of this email:\n{email}"}
        ],
        temperature=0,
    )

    st.write(response.choices[0].message.content)

def generate_answer(email):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Generate an answer for this email:\n{email}"}
        ],
        temperature=0,
    )

    st.write(response.choices[0].message.content)


# OpenAI connection
client = AzureOpenAI(
  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
  api_key = os.getenv("AZURE_OPENAI_API_KEY"),  
  api_version = "2024-07-01-preview"
)


# Web UI
st.title("email_app")

txt = st.text_area("Email:")

left, right = st.columns(2)
if left.button("Generate Summary", use_container_width=True):
    generate_summary(txt)
if right.button("Generate answer", use_container_width=True):
    generate_answer(txt)

