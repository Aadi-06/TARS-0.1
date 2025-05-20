import streamlit as st
from ollama_client import query_ollama
from utils import build_prompt_from_history
from agents import run_tool, detect_tool_call

st.set_page_config(page_title = "TARS", layout = "wide")
st.title("🤖 TARS - Chatbot")
st.sidebar.title("⚙️ Settings")

model = st.sidebar.selectbox(
    "Choose base model: ",
    options = ['gemma3:1b'],
    index = 0
)

st.session_state['model'] = model

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt:= st.chat_input("Say something..."):
    st.session_state.messages.append({"role" : "user", "content" : prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    full_prompt = build_prompt_from_history(st.session_state.messages[:-1], prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = query_ollama(full_prompt, st.session_state["model"])

            tool_name, tool_input = detect_tool_call(response)

            if tool_name:
                with st.spinner(f"🔍 Using tool `{tool_name}`..."):
                    tool_result = run_tool(tool_name, tool_input)
                with st.expander(f"🧠 TARS Thinking via `{tool_name}`"):
                    st.markdown(tool_result)
                response = response.strip() + "\n\n" + tool_result.strip()
        st.markdown(response)
    st.session_state.messages.append({"role" : "assisntat", "content" : response})