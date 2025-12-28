import streamlit as st


def init_state():
    if "messages" not in st.session_state:
        st.session_state.messages = []


def add(role, content):
    st.session_state.messages.append({"role": role, "content": content})


def show_chat():
    for m in st.session_state.messages:
        with st.chat_message(m["role"]):
            st.markdown(m["content"])
