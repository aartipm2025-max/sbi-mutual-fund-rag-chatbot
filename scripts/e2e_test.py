"""
End-to-end RAG pipeline test.
Tests: retrieval → prompt build → Groq LLM → answer
Run from project root: python scripts/e2e_test.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Load .env if present
from dotenv import load_dotenv
load_dotenv()

# Also try reading from Streamlit secrets.toml directly
try:
    import tomllib
    secrets_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".streamlit", "secrets.toml")
    if os.path.exists(secrets_path):
        with open(secrets_path, "rb") as f:
            secrets = tomllib.load(f)
        if "GROQ_API_KEY" in secrets and secrets["GROQ_API_KEY"] != "paste_your_groq_key_here":
            os.environ["GROQ_API_KEY"] = secrets["GROQ_API_KEY"]
except Exception:
    pass

from phase4_rag_pipeline.retriever import get_retriever
from phase4_rag_pipeline.prompt_builder import check_guardrails, build_prompt

try:
    from groq import Groq
    client = Groq(api_key=os.environ.get("GROQ_API_KEY", ""))
    LLM = "groq"
except ImportError:
    LLM = None

DIVIDER = "─" * 60

def call_llm(prompt):
    if not LLM:
        return "⚠️ groq not installed."
    key = os.environ.get("GROQ_API_KEY", "")
    if not key or key == "paste_your_groq_key_here":
        return "⚠️ GROQ_API_KEY not set. Please add it to .streamlit/secrets.toml"
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=220,
        temperature=0.1,
    )
    return response.choices[0].message.content.strip()

def test_question(question, label=""):
    print(f"\n{'='*60}")
    print(f"🧪 TEST{' — ' + label if label else ''}")
    print(f"❓ Q: {question}")
    print(DIVIDER)

    # Guardrail check
    allowed, refusal = check_guardrails(question)
    if not allowed:
        print("🛡️  GUARDRAIL TRIGGERED")
        print(f"💬 Response:\n{refusal}")
        return

    # Retrieve
    retriever = get_retriever()
    chunks = retriever.retrieve(question)
    print(f"📦 Retrieved {len(chunks)} chunks:")
    for i, c in enumerate(chunks, 1):
        print(f"   [{i}] {c['source']} | dist={c['distance']:.4f} | {c['text'][:80]}…")

    # Build prompt & call LLM
    prompt = build_prompt(question, chunks)
    print(f"\n🤖 Calling Groq LLM…")
    answer = call_llm(prompt)
    print(f"\n💬 Answer:\n{answer}")


if __name__ == "__main__":
    print("\n🏦 INDMoney MF RAG Chatbot — End-to-End Test")
    print("=" * 60)

    # Test 1: Factual — should retrieve + answer
    test_question(
        "What is the expense ratio of SBI Blue Chip Fund?",
        label="FACTUAL QUESTION"
    )

    # Test 2: SIP question
    test_question(
        "How does a SIP work in SBI Mutual Fund?",
        label="SIP QUESTION"
    )

    # Test 3: Guardrail — should be blocked
    test_question(
        "Should I invest in SBI Blue Chip Fund right now?",
        label="GUARDRAIL TEST (should be blocked)"
    )

    print(f"\n{'='*60}")
    print("✅ E2E test complete.")
