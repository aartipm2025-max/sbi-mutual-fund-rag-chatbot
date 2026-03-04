# Phase 6 — Deployment Notes

## Streamlit Cloud Deployment

### Steps
1. Push the `mf_rag_chatbot/` folder to a GitHub repository.
2. Go to [share.streamlit.io](https://share.streamlit.io) and click **"New app"**.
3. Connect your GitHub account and select the repository.
4. Set **Main file path** to: `phase5_frontend/app.py`
5. Under **Advanced settings → Secrets**, add:
   ```toml
   GROQ_API_KEY = "gsk_your_key_here"
   ```
6. Click **Deploy** — your app will be live at:
   `https://<your-app-name>.streamlit.app`

### Important Notes
- The `vector_store/faiss_index.bin` and `vector_store/chunks_metadata.pkl` 
  files MUST be committed to the repo (they are built offline and loaded at startup).
- Do NOT commit `.env` or `secrets.toml` to Git.
- Add the following to `.gitignore`:
  ```
  .env
  .streamlit/secrets.toml
  __pycache__/
  *.pyc
  data/raw_documents/
  ```
- LLM | `groq` (llama-3.1-8b-instant) / `openai` (gpt-3.5-turbo)

## Streamlit Config

Create `.streamlit/config.toml` in the project root:
```toml
[theme]
primaryColor = "#1B4FD8"
backgroundColor = "#0F172A"
secondaryBackgroundColor = "#1E293B"
textColor = "#F8FAFC"
font = "sans serif"
```

## Environment Variables (Streamlit Secrets Format)

```toml
# .streamlit/secrets.toml (local only)
GROQ_API_KEY = "your_key"
OPENAI_API_KEY = "your_key"
```
