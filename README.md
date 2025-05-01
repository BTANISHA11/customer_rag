# Alltius.ai RAG Chatbot

A Retrieval-Augmented Generation (RAG) chatbot using AngelOne support documentation and insurance PDFs.

## 🧠 Features

- Answers questions only from provided sources
- Web scraping + PDF ingestion
- Uses FAISS for retrieval and HuggingFace BART for generation
- Streamlit UI

## 🚀 Setup

```bash
git clone <this-repo>
cd rag_chatbot

# 1. Install dependencies
pip install -r requirements.txt

# 2. Place insurance PDFs in docs/insurance/
# 3. Run ingestion to build index
python ingest.py

# 4. Launch the chatbot
streamlit run app.py
