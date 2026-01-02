import streamlit as st
from ui.chat_interface import ChatInterface
from ui.components import render_response

st.set_page_config("GA02 Hybrid RAG", layout="wide")

chat = ChatInterface()

st.sidebar.title("📂 Document Manager")
files = st.sidebar.file_uploader(
    "Upload PDFs or TXT",
    type=["pdf", "txt"],
    accept_multiple_files=True
)

if st.sidebar.button("Index Documents") and files:
    paths = []
    for f in files:
        path = f"data/documents/{f.name}"
        with open(path, "wb") as out:
            out.write(f.read())
        paths.append(path)
    chat.ingest(paths)
    st.sidebar.success("Documents indexed")

st.title("🤖 GA02: Hybrid Multi-Document RAG Search Engine")

query = st.chat_input("Ask a question")
if query:
    result = chat.ask(query)
    render_response(result)
