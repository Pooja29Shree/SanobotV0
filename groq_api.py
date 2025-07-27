import streamlit as st
import os
import requests
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("❌ GROQ_API_KEY not found in st.secrets or environment variables.")

SYSTEM_PROMPT = {
    "role": "system",
    "content": "You are a helpful medical assistant. Never give diagnoses. Only provide general health information."
}

def call_groq_chat(messages, model="meta-llama/llama-4-scout-17b-16e-instruct"):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": model,
        "messages": messages,
        "temperature": 0.5
    }

    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]
