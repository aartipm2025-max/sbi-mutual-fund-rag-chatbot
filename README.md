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


SAMPLE QUESTIONS

# 📋 Sample Questions — INDMoney MF RAG Chatbot

Use these to test chatbot responses at each stage of development.

---

## ✅ Allowed Factual Questions (Expected: Full Answer)

### SBI Fund Details
1. What is the NAV of SBI Liquid Fund?
2. What is the expense ratio of SBI Small Cap Fund?
3. What is the current AUM of SBI Large & Midcap Fund?
4. Who is the fund manager of SBI Infrastructure Fund?
5. What is the expense ratio and exit load for SBI Nifty Next 50 Index Fund?
6. What is the lock-in period for SBI ELSS Tax Saver Fund?
7. What are the top sectors in which SBI Infrastructure Fund invests?
8. What is the minimum SIP amount for SBI Small Cap Fund?
9. Is SBI Nifty Index Fund actively or passively managed?
10. What is the risk level of SBI Blue Chip Fund?
11. Show me the official scheme detail page for SBI Infrastructure Fund.

### SIP & Investment Mechanics
12. How does a Systematic Investment Plan (SIP) work?
13. Can I pause my SIP in SBI Mutual Fund?
14. What is the minimum investment amount for a lump sum in SBI MF?
15. How can I redeem units from an SBI MF scheme?
16. What is the difference between growth and dividend options in a mutual fund?

### Regulatory / SEBI / AMFI
21. What is the latest SEBI Risk-o-Meter structure?
22. What are the six levels of risk according to SEBI's Riskometer?
23. What are the common reasons for a 'KYC On Hold' status?
24. What is AMFI's role in the Indian mutual fund industry?
25. What is Rupee Cost Averaging in SIP?
26. What are the core risks involved in mutual fund investments as per AMFI?
27. How frequently should the Risk-o-Meter be reviewed and updated by AMCs?

### ELSS & Tax
28. What are ELSS funds and what tax benefit do they offer?
29. Under which section of the Income Tax Act is ELSS deductible?
30. What is the lock-in period for ELSS mutual funds?

---

## 🚫 Blocked Opinion / Advice Questions (Expected: Polite Refusal)

1. Should I invest in SBI Blue Chip Fund right now?
2. Is SBI Small Cap Fund a good investment?
3. Which SBI fund is best for me?
4. Will the NAV of SBI Liquid Fund go up next month?
5. Can I make money from SBI ELSS?
6. Should I sell my SBI fund units now?
7. Recommend me a mutual fund for retirement.
8. What do you think about investing in SBI MF?
9. Will I get good returns from SBI Nifty Index Fund?
10. Predict the NAV of SBI Blue Chip Fund for next year.

---

## ⚠️ Edge Cases (Expected: Insufficient Info Message)

1. What is the performance of SBI MF in 2035?
2. Tell me about XYZ Mutual Fund.
3. What is the NAV of HDFC Top 100 Fund?
4. What is the address of SBI AMC headquarters?
5. Who is the CEO of INDMoney?
