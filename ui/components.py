import streamlit as st

def render_response(result):
    tabs = st.tabs(["Answer", "Document Evidence", "Web Evidence"])

    with tabs[0]:
        icon = {"doc":"📄", "web":"🌐", "hybrid":"🔀"}[result["mode"]]
        st.markdown(f"{icon} **Answer**")
        st.write(result["answer"])

    with tabs[1]:
        for s in result["doc_sources"]:
            st.write("📄", s)

    with tabs[2]:
        for s in result["web_sources"]:
            st.write("🌐", s)
