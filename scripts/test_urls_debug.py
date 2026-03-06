
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

def test_fund_retrieval(fund_name, expected_url_part):
    question = f"What are the details of {fund_name}?"
    print(f"\n❓ TESTING QUESTION: {question}")
    
    retriever = get_retriever()
    chunks = retriever.retrieve(question, top_k=5)
    
    print(f"\n🔍 Retrieved {len(chunks)} chunks.")
    found_official_source = False
    for i, c in enumerate(chunks):
        source_name = c.get('source', 'Unknown')
        url = c.get('url', 'No URL')
        print(f"   - Context {i+1}: Source='{source_name}' | URL='{url}'")
        if expected_url_part in url:
            found_official_source = True
            
    if found_official_source:
        print(f"✅ SUCCESS: Official {fund_name} URL found in retrieved chunks.")
    else:
        print(f"❌ FAILURE: Official {fund_name} URL NOT found in retrieved chunks.")

    # Get LLM Answer
    prompt = build_prompt(question, chunks)
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300,
        temperature=0.1,
    )
    answer = response.choices[0].message.content.strip()
    print(f"\n🤖 LLM ANSWER:\n{answer}")

if __name__ == "__main__":
    test_fund_retrieval("SBI Large & Midcap Fund", "sbi-large--midcap-fund-2")
    test_fund_retrieval("SBI Infrastructure Fund", "sbi-infrastructure-fund-85")
