import streamlit as st
from groq_api import call_groq_chat, SYSTEM_PROMPT

st.set_page_config(page_title=" Healthcare Chatbot", layout="wide")
st.markdown(
    "<h1 style='display: inline; font-size: 3em;'>Sanobot</h1>"
    "<span style='font-size: 1.5em; font-weight: normal;'>Your AI-powered medical assistant</span>",
    unsafe_allow_html=True
)

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [SYSTEM_PROMPT]
user_input = st.text_input(" Describe your symptoms or ask a health question:")

if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    with st.spinner(" Thinking..."):
        reply = call_groq_chat(st.session_state.chat_history)
    st.session_state.chat_history.append({"role": "assistant", "content": reply})

# Display messages
for msg in st.session_state.chat_history[1:]:  # Skip system message
    speaker = " Assistant" if msg["role"] == "assistant" else " You"
    st.markdown(f"{speaker}: {msg['content']}")
