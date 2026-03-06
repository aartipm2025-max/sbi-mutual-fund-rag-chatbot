"""
Phase 5 — Streamlit Chat Frontend
===================================
INDMoney Mutual Fund FAQ Chatbot
Powered by: SBI AMC · SEBI · AMFI official data

Run with:
    streamlit run phase5_frontend/app.py
"""

import os
import sys
import logging
import re
import streamlit as st
from pathlib import Path

# ── Path Setup ────────────────────────────────────────────────────────────────
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from phase4_rag_pipeline.prompt_builder import check_guardrails, build_prompt, INSUFFICIENT_INFO, OPINION_REFUSAL
from phase4_rag_pipeline.retriever import get_retriever

# ── LLM Client ────────────────────────────────────────────────────────────────
try:
    from groq import Groq
    _LLM = "groq"
except ImportError:
    import openai
    _LLM = "openai"

logger = logging.getLogger(__name__)

# ── Page Config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="INDMoney MF Facts Assistant",
    page_icon="🏦",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ── Premium Dark Theme CSS ────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

/* ── Global Reset ── */
*, *::before, *::after { box-sizing: border-box; }

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif !important;
    -webkit-font-smoothing: antialiased;
}

/* ── Deep Navy Background ── */
.stApp {
    background: linear-gradient(145deg, #0B1120 0%, #0F1723 50%, #111827 100%);
    background-attachment: fixed;
    color: #E8EDF5;
}

/* ── Hide Streamlit chrome ── */
#MainMenu, footer, header { visibility: hidden; }
.stDeployButton { display: none; }

/* ── Center container, max 720px ── */
.main .block-container {
    max-width: 720px !important;
    margin: 0 auto;
    padding: 2rem 1.5rem 6rem 1.5rem;
}

/* ── Header Section ── */
.mf-header-wrapper {
    text-align: center;
    padding: 2.5rem 1rem 1.5rem;
    margin-bottom: 0.5rem;
}
.mf-header-icon {
    font-size: 2.6rem;
    margin-bottom: 0.6rem;
    display: block;
}
.mf-header-title {
    font-size: 1.75rem;
    font-weight: 700;
    color: #FFFFFF;
    letter-spacing: -0.3px;
    margin: 0 0 0.5rem 0;
}
.mf-header-subtitle {
    font-size: 0.9rem;
    color: #7A8BA8;
    font-weight: 400;
    margin: 0;
}
.mf-teal-bar {
    width: 48px;
    height: 3px;
    background: linear-gradient(90deg, #00C9A7, #00E5C1);
    border-radius: 2px;
    margin: 0.9rem auto 0;
}

/* ── Suggestion Chips Container ── */
.chips-wrapper {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    justify-content: center;
    margin: 1.5rem 0;
    padding: 0 0.5rem;
}
.chip {
    display: inline-flex;
    align-items: center;
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(0,201,167,0.3);
    border-radius: 100px;
    padding: 0.4rem 1rem;
    font-size: 0.8rem;
    color: #A8C0D6;
    cursor: pointer;
    transition: all 0.2s ease;
    white-space: nowrap;
    backdrop-filter: blur(8px);
}
.chip:hover {
    background: rgba(0,201,167,0.12);
    border-color: rgba(0,201,167,0.7);
    color: #00E5C1;
    transform: translateY(-1px);
    box-shadow: 0 4px 16px rgba(0,201,167,0.15);
}
.chip-icon {
    margin-right: 0.35rem;
    font-size: 0.75rem;
    opacity: 0.7;
}

/* ── Divider ── */
.mf-divider {
    border: none;
    border-top: 1px solid rgba(255,255,255,0.06);
    margin: 0.5rem 0 1.5rem;
}

/* ── Chat Messages ── */
[data-testid="stChatMessage"] {
    border-radius: 14px !important;
    padding: 0.25rem !important;
    margin-bottom: 0.75rem !important;
    border: none !important;
    background: transparent !important;
}

/* User bubble — right-side dark slate */
[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]),
[data-testid="stChatMessage"][data-role="user"] {
    background: rgba(30, 45, 69, 0.75) !important;
    border: 1px solid rgba(255,255,255,0.07) !important;
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
}

/* Assistant bubble — glassmorphism with teal left accent */
[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarAssistant"]),
[data-testid="stChatMessage"][data-role="assistant"] {
    background: rgba(17, 24, 39, 0.85) !important;
    border: 1px solid rgba(0,201,167,0.2) !important;
    border-left: 3px solid #00C9A7 !important;
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    box-shadow: 0 4px 24px rgba(0,0,0,0.35), 0 0 0 1px rgba(0,201,167,0.05);
}

/* Text inside chat */
[data-testid="stChatMessage"] p,
[data-testid="stChatMessage"] li,
[data-testid="stChatMessage"] span {
    color: #D8E4F0 !important;
    line-height: 1.65;
}

/* ── Chat Input Bar ── */
[data-testid="stChatInput"] {
    border-radius: 50px !important;
    border: 1px solid rgba(0,201,167,0.25) !important;
    background: rgba(15, 23, 42, 0.9) !important;
    backdrop-filter: blur(20px);
    box-shadow: 0 0 0 1px rgba(0,201,167,0.08), 0 8px 32px rgba(0,0,0,0.4) !important;
}
[data-testid="stChatInput"] textarea {
    color: #E8EDF5 !important;
    background: transparent !important;
}
[data-testid="stChatInput"] textarea::placeholder {
    color: #4A607A !important;
}
[data-testid="stChatInput"] button {
    background: linear-gradient(135deg, #00C9A7, #00B894) !important;
    border-radius: 50px !important;
    color: #0B1120 !important;
    font-weight: 600 !important;
}
[data-testid="stChatInput"] button:hover {
    background: linear-gradient(135deg, #00E5C1, #00C9A7) !important;
    box-shadow: 0 0 16px rgba(0,201,167,0.4) !important;
}

/* ── Source Citation ── */
.mf-source {
    margin-top: 0.6rem;
    padding-top: 0.5rem;
    border-top: 1px solid rgba(255,255,255,0.07);
    font-size: 0.78rem;
    color: #4A607A;
    display: flex;
    align-items: center;
    gap: 0.3rem;
}
.mf-source a {
    color: #00C9A7 !important;
    text-decoration: none !important;
    font-weight: 500;
    transition: color 0.2s;
}
.mf-source a:hover {
    color: #00E5C1 !important;
    text-decoration: underline !important;
}

/* ── Disclaimer Footer ── */
.mf-disclaimer {
    text-align: center;
    font-size: 0.72rem;
    color: #3A4F66;
    margin-top: 1.5rem;
    padding: 0.5rem 1rem;
    letter-spacing: 0.3px;
}

/* ── Spinner text ── */
[data-testid="stSpinner"] { color: #00C9A7 !important; }

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: rgba(0,201,167,0.2); border-radius: 10px; }
::-webkit-scrollbar-thumb:hover { background: rgba(0,201,167,0.4); }

/* ── Seed question buttons ── */
.stButton > button {
    background: rgba(255,255,255,0.03) !important;
    border: 1px solid rgba(0,201,167,0.25) !important;
    color: #A8C0D6 !important;
    border-radius: 100px !important;
    font-size: 0.8rem !important;
    padding: 0.35rem 0.9rem !important;
    transition: all 0.2s ease !important;
    font-family: 'Inter', sans-serif !important;
    backdrop-filter: blur(8px);
}
.stButton > button:hover {
    background: rgba(0,201,167,0.1) !important;
    border-color: rgba(0,201,167,0.6) !important;
    color: #00E5C1 !important;
    transform: translateY(-1px);
    box-shadow: 0 4px 16px rgba(0,201,167,0.15) !important;
}
</style>
""", unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="mf-header-wrapper">
    <span class="mf-header-icon">🏦</span>
    <h1 class="mf-header-title">INDMoney SBI Mutual Fund Facts Assistant</h1>
    <p class="mf-header-subtitle">Facts-only information sourced from AMC, SEBI, and AMFI.</p>
    <div style="font-size: 0.75rem; color: #00C9A7; margin-top: 0.8rem; opacity: 0.9;">
        Currently trained on 5 major SBI Funds
    </div>
    <div class="mf-teal-bar"></div>
</div>
""", unsafe_allow_html=True)

# ── Sidebar Training Info ─────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 📊 Knowledge Base")
    st.markdown("""
    This assistant is specifically trained on the following **SBI Mutual Fund** schemes:
    
    *   **SBI Small Cap Fund**
    *   **SBI Large & Midcap Fund**
    *   **SBI ELSS Tax Saver Fund**
    *   **SBI Nifty Next 50 Index Fund**
    *   **SBI Infrastructure Fund**
    
    ---
    **Data Sources:**
    *   Official SBI AMC Factsheets
    *   SEBI Regulatory Circulars
    *   AMFI Knowledge Portal
    """)
    st.info("Ask about NAV, Expense Ratio, Exit Load, or Fund Managers for these schemes.")

# ── Suggestion Chips Display ──────────────────────────────────────────────────
SUGGESTIONS = [
    ("📊", "Expense ratio of SBI Small Cap Fund"),
    ("🔍", "Fund manager of SBI Infrastructure Fund"),
    ("🔒", "Lock-in period for SBI ELSS Tax Saver"),
    ("📈", "NAV of SBI Nifty Next 50 Index Fund"),
]

# ── Session State Init ────────────────────────────────────────────────────────
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "pending_chip" not in st.session_state:
    st.session_state.pending_chip = None
if "retriever" not in st.session_state:
    with st.spinner("Loading knowledge base …"):
        try:
            st.session_state.retriever = get_retriever()
        except FileNotFoundError as e:
            st.error(
                f"⚠️ Vector store not found. Please run `phase3_embeddings/embedder.py` first.\n\n`{e}`"
            )
            st.stop()

# ── LLM Wrapper ───────────────────────────────────────────────────────────────

def call_llm(prompt: str) -> str:
    """Send the assembled prompt to Groq or OpenAI and return the text."""
    try:
        if _LLM == "groq":
            client = Groq(api_key=os.environ.get("GROQ_API_KEY") or st.secrets.get("GROQ_API_KEY", ""))
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=220,
                temperature=0.1,
            )
            return response.choices[0].message.content.strip()
        else:
            import openai
            openai.api_key = os.environ.get("OPENAI_API_KEY") or st.secrets.get("OPENAI_API_KEY", "")
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=220,
                temperature=0.1,
            )
            return response.choices[0].message.content.strip()
    except Exception as e:
        logger.error(f"LLM call failed: {e}")
        return "⚠️ I encountered an error reaching the language model. Please try again."

# ── Core Answer Function ──────────────────────────────────────────────────────

def answer_question(question: str) -> str:
    """Full RAG pipeline: guardrail → retrieve → prompt → LLM → answer."""
    # 1. Guardrail check
    allowed, refusal = check_guardrails(question)
    if not allowed:
        return refusal

    # 2. Retrieve relevant chunks
    retriever = st.session_state.retriever
    chunks    = retriever.retrieve(question)

    # 3. Build prompt
    prompt = build_prompt(question, chunks)

    # 4. LLM inference
    answer = call_llm(prompt)
    return answer

# ── Output Formatting ─────────────────────────────────────────────────────────

def format_answer(text: str) -> str:
    """Extract markdown links from LLM answer and render teal source citation."""
    # Pass through guardrail refusals as-is
    if text.strip() in (OPINION_REFUSAL.strip(), INSUFFICIENT_INFO.strip()):
        return text

    matches = list(re.finditer(r'\[([^\]]+)\]\((https?://[^\)]+)\)', text))
    if matches:
        url = matches[-1].group(2)
        # Strip all markdown links from the visible answer text
        clean_text = text
        for match in reversed(matches):
            link_text = match.group(1)
            clean_text = clean_text[:match.start()] + link_text + clean_text[match.end():]

        source_html = (
            f'<div class="mf-source">'
            f'<span>🔗</span>'
            f'<span>Source: <a href="{url}" target="_blank">{url}</a></span>'
            f'</div>'
        )
        return clean_text + "\n" + source_html

    return text

# ── Process Suggestion Chip (if selected) ────────────────────────────────────
chip_query = None
if st.session_state.pending_chip:
    chip_query = st.session_state.pending_chip
    st.session_state.pending_chip = None

# ── Chat History Render ───────────────────────────────────────────────────────
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        if msg["role"] == "assistant":
            st.markdown(format_answer(msg["content"]), unsafe_allow_html=True)
        else:
            st.markdown(msg["content"])

# ── Handle Chip-Triggered Question ───────────────────────────────────────────
if chip_query:
    st.session_state.chat_history.append({"role": "user", "content": chip_query})
    with st.chat_message("user"):
        st.markdown(chip_query)
    with st.chat_message("assistant"):
        with st.spinner("Searching official sources …"):
            raw_reply = answer_question(chip_query)
        formatted_reply = format_answer(raw_reply)
        st.markdown(formatted_reply, unsafe_allow_html=True)
    st.session_state.chat_history.append({"role": "assistant", "content": raw_reply})

# ── Suggestion Chips (shown when chat is empty) ───────────────────────────────
if not st.session_state.chat_history:
    st.markdown('<div class="chips-wrapper">', unsafe_allow_html=True)
    chip_cols = st.columns(len(SUGGESTIONS))
    for i, (icon, label) in enumerate(SUGGESTIONS):
        with chip_cols[i]:
            if st.button(f"{icon} {label}", key=f"chip_{i}"):
                st.session_state.pending_chip = label
                st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<hr class="mf-divider">', unsafe_allow_html=True)

# ── Chat Input ────────────────────────────────────────────────────────────────
if prompt := st.chat_input("Ask a factual question about mutual funds..."):
    # 1. Append user question
    st.session_state.chat_history.append({"role": "user", "content": prompt})

    # 2. Render user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # 3. Generate and render assistant answer
    with st.chat_message("assistant"):
        with st.spinner("Searching official sources …"):
            raw_reply = answer_question(prompt)
        formatted_reply = format_answer(raw_reply)
        st.markdown(formatted_reply, unsafe_allow_html=True)

    # 4. Append assistant response
    st.session_state.chat_history.append({"role": "assistant", "content": raw_reply})

# ── Footer Disclaimer ─────────────────────────────────────────────────────────
st.markdown(
    '<div class="mf-disclaimer">🔒 Facts-only assistant. No investment advice.</div>',
    unsafe_allow_html=True
)
