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

SOURCES
source_id,source_name,url,category,scrape_priority
indmoney_sbi_small_cap,INDmoney,https://www.indmoney.com/mutual-funds/sbi-small-cap-fund,Scheme Page,2
indmoney_sbi_large_midcap,INDmoney,https://www.indmoney.com/mutual-funds/sbi-large-midcap-fund,Scheme Page,2
indmoney_sbi_elss,INDmoney,https://www.indmoney.com/mutual-funds/sbi-elss-tax-saver-fund,Scheme Page,2
indmoney_sbi_nifty_next50,INDmoney,https://www.indmoney.com/mutual-funds/sbi-nifty-next-50-index-fund,Scheme Page,2
indmoney_sbi_infra,INDmoney,https://www.indmoney.com/mutual-funds/sbi-infrastructure-fund,Scheme Page,2
sbi_small_cap_official,SBI AMC,https://www.sbimf.com/sbimf-scheme-details/sbi-small-cap-fund-329,Official Factsheet,1
sbi_large_midcap_official,SBI AMC,https://www.sbimf.com/sbimf-scheme-details/sbi-large--midcap-fund-2,Official Factsheet,1
sbi_elss_official,SBI AMC,https://www.sbimf.com/sbimf-scheme-details/sbi-elss-tax-saver-fund-(formerly-known-as-sbi-long-term-equity-fund)-3,Official Factsheet,1
sbi_nifty_next50_official,SBI AMC,https://www.sbimf.com/sbimf-scheme-details/sbi-nifty-next-50-index-fund-587,Official Factsheet,1
sbi_infra_official,SBI AMC,https://www.sbimf.com/sbimf-scheme-details/sbi-infrastructure-fund-85,Official Factsheet,1
sebi_riskometer_circular,SEBI,https://www.sebi.gov.in/legal/circulars/oct-2020/circular-on-product-labeling-in-mutual-fund-schemes-risk-o-meter_47796.html,Regulatory,1
sebi_riskometer_info,SEBI,https://investor.sebi.gov.in/riskometer.html,Knowledge,1
sebi_circulars_list,SEBI,https://www.sebi.gov.in/sebiweb/home/HomeAction.do?doListing=yes&sid=1&ssid=7&smid=0,Regulatory,2
amfi_knowledge_info,AMFI,https://www.amfiindia.com/investor/knowledge-center-info,Knowledge,1
amfi_mf_knowledge,AMFI,https://www.amfiindia.com/investor/knowledge-center/mutual-fund,Knowledge,1
amfi_sip_knowledge,AMFI,https://www.amfiindia.com/investor/knowledge-center/sip,Knowledge,1
amfi_kyc_knowledge,AMFI,https://www.amfiindia.com/investor/knowledge-center/kyc-norms,Knowledge,1
amfi_risks_knowledge,AMFI,https://www.amfiindia.com/investor/knowledge-center/risks-in-mutual-funds,Knowledge,1
cams_statements,CAMS,https://www.camsonline.com/Investors/Statements,Services,3


