# 🤖 GA02: Hybrid Multi-Document RAG Search Engine  
**(Documents + Real-Time Web Search)**

A **Hybrid Retrieval-Augmented Generation (RAG) Search Engine** that allows users to ask questions over **multiple uploaded documents** and **live web data**, with **clear source attribution**.

This project is built as part of **GA02** to demonstrate real-world **enterprise-grade AI search systems**.

---

## 🌟 Key Features

✅ Multi-document semantic search (PDF / TXT)  
✅ FAISS-based vector indexing  
✅ Local HuggingFace embeddings (no API cost)  
✅ Real-time web search using **Tavily**  
✅ Automatic query routing (Doc / Web / Hybrid)  
✅ Citation-aware answers  
✅ Evidence-based Streamlit UI  
✅ Modular & scalable architecture  

---

## 🧠 What Problem Does This Solve?

Organizations store knowledge across:
- PDFs
- Reports
- Notes
- Research documents

However:
- Documents can be **outdated**
- Users often need **latest real-world information**

👉 This system **combines private documents + live web search** to provide **accurate, grounded answers**.

---

## 🏗️ System Architecture (High Level)

User Query
│
▼
Query Classifier
│
├── Document Search (FAISS)
├── Web Search (Tavily)
└── Hybrid (Both)
│
▼
Context Assembly + Source Tagging
│
▼
LLM (Groq via LangChain)
│
▼
Answer + Citations


---

## 🧰 Tech Stack

| Component | Technology |
|--------|-----------|
| Language | Python |
| LLM Orchestration | LangChain |
| LLM Provider | Groq |
| Embeddings | HuggingFace (Sentence-Transformers) |
| Vector DB | FAISS |
| Web Search | Tavily |
| UI | Streamlit |
| Environment | `uv` |

---

## 📂 Project Structure

rag-chatbot/
├── app.py # Streamlit app
├── requirements.txt
│
├── config/ # Config & environment
├── core/ # RAG core logic
│ ├── schemas.py
│ ├── text_cleaner.py
│ ├── document_processor.py
│ ├── embeddings.py
│ ├── vector_store.py
│ └── chain.py
│
├── tools/ # External tools
│ └── tavily_search.py
│
├── ui/ # Streamlit UI components
│ ├── chat_interface.py
│ └── components.py
│
├── data/ # Local data (ignored in git)
│ ├── documents/
│ └── faiss_index/



---

## 🚀 How to Run the Project (Using `uv`)

### 1️⃣ Create virtual environment
```bash
uv venv
```

### 2️⃣ Activate environment
```bash
Windows

.venv\Scripts\activate


macOS / Linux

source .venv/bin/activate
```

### 3️⃣ Install dependencies
```bash
uv pip install -r requirements.txt
```
### 4️⃣ Create .env file
```bash
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key


⚠️ Do NOT commit this file.
```
### 5️⃣ Run the app
```bash
streamlit run app.py

```
App opens at:

http://localhost:8501

### 🧪 Example Queries
## 📄 Document-based
Explain attention mechanism

### 🌐 Web-based
What are the latest developments in LLMs?

### 🔀 Hybrid
How does RAG compare with current LLM tools?

### 📊 UI Features

## 📄 Document Evidence Tab – Shows document chunks used

### 🌐 Web Evidence Tab – Shows URLs used

## 🔀 Hybrid Indicator – Shows retrieval mode

Transparent, explainable answers

### 🎓 Learning Outcomes

By completing this project, you demonstrate:

✅ Multi-document RAG system design
✅ Hybrid retrieval (vector + web)
✅ Real-time web integration
✅ Citation-aware answer generation
✅ Practical LangChain + Streamlit skills

## ⚠️ Limitations & Future Enhancements

Wikipedia loaders can be added easily

Automatic evaluation metrics (BLEU, ROUGE)

Multi-user authentication

Caching for large-scale deployments

## 🧾 License

This project is created for educational and academic purposes.

### 🙌 Author

Rishabh Jain
GA02 – Hybrid RAG Search Engine
