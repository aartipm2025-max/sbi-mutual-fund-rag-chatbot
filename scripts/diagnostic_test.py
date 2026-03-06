"""
Diagnostic Test: Verifying Official Source Prioritization
=========================================================
This script tests if the chatbot correctly pulls the exit load 
for the SBI Flexicap Fund from the Master Official Data.
"""
import sys, os
from pathlib import Path

# Setup paths
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from phase4_rag_pipeline.retriever import get_retriever
from phase4_rag_pipeline.prompt_builder import build_prompt
from groq import Groq
import tomllib

# Load key from secrets
secrets_path = ROOT / ".streamlit" / "secrets.toml"
if secrets_path.exists():
    with open(secrets_path, "rb") as f:
        secrets = tomllib.load(f)
    os.environ["GROQ_API_KEY"] = secrets.get("GROQ_API_KEY", "")

client = Groq()

def test_flexicap_exit_load():
    question = "If I withdraw from the SBI Flexicap Fund within one year, what will be the exit load?"
    print(f"\n❓ TESTING QUESTION: {question}")
    
    retriever = get_retriever()
    chunks = retriever.retrieve(question)
    
    print(f"\n🔍 [Step 1] Retrieved {len(chunks)} chunks.")
    for i, c in enumerate(chunks):
        print(f"   - Context {i+1}: Source='{c['source']}' | URL='{c['url'][:50]}...'")
    
    prompt = build_prompt(question, chunks)
    
    print(f"\n🚀 [Step 2] Querying LLM (llama-3.1-8b-instant)...")
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=250,
        temperature=0.1,
    )
    
    answer = response.choices[0].message.content.strip()
    print(f"\n🤖 LLM ANSWER:\n{answer}")
    
    if "1%" in answer and "sbimf.com" in answer.lower():
        print("\n✅ TEST PASSED: Official data identified and prioritized.")
    else:
        print("\n❌ TEST FAILED: Check if master_schemes_clean.json was properly indexed.")

if __name__ == "__main__":
    try:
        test_flexicap_exit_load()
    except Exception as e:
        print(f"\n❌ ERROR DURING TEST: {e}")
