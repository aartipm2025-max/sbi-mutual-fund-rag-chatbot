# 🏦 INDMoney SBI Mutual Fund Facts Assistant

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-name.streamlit.app)

A **Retrieval-Augmented Generation (RAG)** chatbot that answers factual questions about **SBI Mutual Fund schemes** using only verified official sources from **SBI AMC, SEBI, and AMFI**.

> 🔒 Facts-only assistant. No investment advice.

---

## 🚀 Live Demo

👉 **[Launch the Chatbot](https://your-app-name.streamlit.app)**

---

## 📐 Architecture

```
Phase 1 → Data Collection     (scrape 25 official pages)
Phase 2 → Document Processing (clean + normalize HTML text)
Phase 3 → Chunking & Embeddings (FAISS vector store)
Phase 4 → RAG Pipeline        (retrieve + LLM + guardrails)
Phase 5 → Chat UI             (Streamlit dark-mode interface)
Phase 6 → Deployment          (Streamlit Cloud)
```

---

## 🎨 UI Features

- **Premium dark-mode UI** — deep navy + teal glassmorphism
- **ChatGPT-style chat layout** — chronological message history
- **Teal source citations** — clickable links under every answer
- **Suggestion chips** — quick-start factual questions
- **Guardrails** — opinion/advice questions politely refused

---

## 📁 Project Structure

```
mf_rag_chatbot/
├── phase1_data_collection/
│   └── data_scraper.py           # Scrape official pages
├── phase2_processing/
│   └── document_cleaner.py       # Clean + normalize raw docs
├── phase3_embeddings/
│   └── embedder.py               # Chunk docs & build FAISS index
├── phase4_rag_pipeline/
│   ├── retriever.py              # FAISS similarity search
│   └── prompt_builder.py         # Prompt assembly + guardrails
├── phase5_frontend/
│   └── app.py                    # Streamlit chat UI ← entrypoint
├── vector_store/
│   ├── faiss_index.bin           # FAISS vector index (pre-built)
│   └── chunks_metadata.pkl       # Chunk text + source metadata
├── .streamlit/
│   └── config.toml               # Dark theme + server config
├── packages.txt                  # System dependencies (Streamlit Cloud)
├── requirements.txt              # Python dependencies
└── README.md
```

---

## ⚡ Local Setup

### 1. Clone & Install
```bash
git clone https://github.com/YOUR_USERNAME/indmoney-mf-chatbot.git
cd indmoney-mf-chatbot
pip install -r requirements.txt
```

### 2. Add API Key
Create `.streamlit/secrets.toml`:
```toml
GROQ_API_KEY = "your_groq_api_key_here"
```
Get a free key at: https://console.groq.com

### 3. Run the App
```bash
streamlit run phase5_frontend/app.py
```

---

## ☁️ Streamlit Cloud Deployment

1. Push this repo to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Click **New app** → select this repo
4. Set **Main file path**: `phase5_frontend/app.py`
5. Go to **Advanced settings → Secrets** and add:
   ```toml
   GROQ_API_KEY = "your_groq_api_key_here"
   ```
6. Click **Deploy** 🚀

---

## 🛡️ Guardrails

| Rule | Enforcement |
|---|---|
| No investment advice | Regex blocklist on queries |
| Official sources only | SBI AMC · SEBI · AMFI only |
| Max 3 sentences | `max_tokens=220` + prompt constraint |
| Citation required | System prompt enforces one link |
| Opinion refusal | Polite message returned |

---

## 🔧 Tech Stack

| Layer | Technology |
|---|---|
| Embeddings | `sentence-transformers/all-MiniLM-L6-v2` |
| Vector Store | `faiss-cpu` |
| LLM | Groq (`llama-3.1-8b-instant`) |
| UI | `streamlit` |
| Deployment | Streamlit Cloud |

---

## ⚠️ Disclaimer

This chatbot provides **factual information only** from official public sources (SBI AMC, SEBI, AMFI).
It does **not** constitute investment advice. Always consult a SEBI-registered financial advisor before investing.
