#app.py
from langchain_core.utils import raise_for_status_with_text
import streamlit as st
import requests

st.set_page_config(page_title="Enterprise AI Assistant", page_icon="🤖")

st.title("Enterprise Knowledge Assistant")
st.caption("Chat with your documents using your preferred AI model.")

#----------------------------------------------------------------------------------
with st.sidebar:
  st.header("⚙️ Settings")
  provider = st.selectbox("Select AI Provider", ["google", "openai", "anthropic"])

  if provider == "google":
    model_name = st.selectbox("Model", ["gemini-2.5-flash", "gemini-2.5-pro"])
  elif provider == "openai":
    model_name = st.selectbox("Model", ["gpt-4o", "gpt-4o-mini"])
  elif provider == "anthropic":
    model_name = st.selectbox("Model", ["haiku-4.5", "claude-3.5-sonnet"])

  api_key = st.text_input("Enter your API key", type="password")
  st.info("Your API key is only used for this session and is never stored")
#----------------------------------------------------------------------------------

if "messages" not in st.session_state:
  st.session_state.messages = []

for msg in st.session_state.messages:
  with st.chat_message(msg["role"]):
    st.markdown(msg["content"])

if prompt := st.chat_input("Ask a question about your documents..."):
  if not api_key:
    st.warning("Please enter your API key in the sidebar to continue.")
    st.stop()

  st.session_state.messages.append({"role": "user", "content": prompt})
  with st.chat_message("user"):
    st.markdown(prompt)

  with st.chat_message("assistant"):
    with st.spinner("Searching documents and generating answer..."):
      try:
        response = requests.post(
            "http://localhost:8000/ask",
            json={
                "question": prompt,
                "provider": provider,
                "model_name": model_name,
            },
            headers={"x-api-key": api_key}
        )
        response.raise_for_status()
        answer = response.json()["answer"]
        st.markdown(answer)
        st.session_state.messages.append({"role": "assistant", "content": answer})
        
      except Exception as e:
        st.error(f"Error communicating with the AI provider: {e}")