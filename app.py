import os
import streamlit as st
from config.settings import settings
from ui.components import init_state, add, show_chat
from ui.chat_interface import ChatInterface

settings.validate()
st.set_page_config(page_title="GA02 Hybrid RAG", layout="wide")

os.makedirs("data/documents", exist_ok=True)
init_state()

chat = st.session_state.get("chat") or ChatInterface()
st.session_state.chat = chat

st.sidebar.header("Upload Documents")
files = st.sidebar.file_uploader("PDF / TXT", accept_multiple_files=True)

if st.sidebar.button("Index"):
    paths = []
    for f in files:
        path = f"data/documents/{f.name}"
        with open(path, "wb") as out:
            out.write(f.getbuffer())
        paths.append(path)
    chat.ingest(paths)

use_web = st.sidebar.toggle("Enable Web Search")

show_chat()

if q := st.chat_input("Ask a question"):
    add("user", q)
    ans = chat.ask(q, use_web)
    add("assistant", ans)
    show_chat()
