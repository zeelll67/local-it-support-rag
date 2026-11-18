# 🔒 Local Privacy-First IT Support RAG Assistant

A 100% offline, privacy-first Retrieval-Augmented Generation (RAG) web application built in Python. Designed for complete data sovereignty, this tool enables IT teams and business stakeholders to query, search, and summarize 500+ IT support ticket logs using natural language—with zero external cloud APIs or third-party SaaS dependencies.

---

## 🏗️ Technical Architecture & Stack
* **Language:** Python 3.12
* **Vector Database:** ChromaDB (persistent local storage mode)
* **Local LLM Engine:** Ollama running `llama3.2:3b` offline
* **Frontend UI:** Streamlit (`http://localhost:8501`)
* **Dataset:** Synthetic IT Support Tickets (`synthetic_it_support_tickets.csv`)

---

## ⚙️ How It Works
1. **Dynamic Ingestion (`ingest.py`):** Parses structured CSV support ticket records (`ticket_id`, `issue_type`, `priority`, `status`, `initial_message`, `resolution_summary`, etc.), formats each row into a semantic text document, generates unique primary keys, and stores vector embeddings locally in **ChromaDB** (`./my_chroma_db`).
2. **Semantic Vector Retrieval (`app.py` / `query.py`):** Converts user questions into query vectors and performs cosine similarity search across the vector store to retrieve the top 10 most relevant support tickets.
3. **Offline LLM Synthesis (`app.py`):** Injects the retrieved ticket context into a grounded prompt sent to the local **Ollama (`llama3.2:3b`)** instance, returning structured business summaries alongside an expandable view of the raw source tickets for full transparency.

---

## 🚀 How to Run Locally

1. **Clone the repository and create a virtual environment:**
   ```bash
   git clone [https://github.com/zeelll67/local-it-support-rag.git](https://github.com/zeelll67/local-it-support-rag.git)
   cd local-it-support-rag
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
