
import sys, os
from pathlib import Path

# Setup paths
ROOT = Path(r"c:\IND MONEY-RAG CHATBOT-M1\mf_rag_chatbot")
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

def test_smallcap_expense_ratio():
    question = "What is the expense ratio of SBI Small Cap Fund?"
    print(f"\n❓ TESTING QUESTION: {question}")
    
    retriever = get_retriever()
    chunks = retriever.retrieve(question)
    
    print(f"\n🔍 [Step 1] Retrieved {len(chunks)} chunks.")
    found_in_context = False
    for i, c in enumerate(chunks):
        print(f"   - Context {i+1}: Source='{c['source']}' | Text snippet='{c['text'][:100]}...'")
        if "0.76%" in c['text'] or "Expense Ratio: 0.76%" in c['text']:
            found_in_context = True
    
    if found_in_context:
        print("\n✅ INFO FOUND IN CONTEXT.")
    else:
        print("\n❌ INFO NOT FOUND IN CONTEXT.")
    
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
    
    if "0.76%" in answer:
        print("\n✅ TEST PASSED: Expense ratio found and reported.")
    else:
        print("\n❌ TEST FAILED: Expense ratio still missing from answer.")

if __name__ == "__main__":
    try:
        test_smallcap_expense_ratio()
    except Exception as e:
        print(f"\n❌ ERROR DURING TEST: {e}")
