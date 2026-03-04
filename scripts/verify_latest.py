"""
Quick Test: Verifying March 2026 Live Data
==========================================
Checks the RAG pipeline for the most recently added INDmoney facts.
"""
import sys, os
from pathlib import Path

# Setup paths
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from phase4_rag_pipeline.retriever import get_retriever
from phase4_rag_pipeline.prompt_builder import build_prompt
from groq import Groq
import streamlit as st

# Load key from secrets
import tomllib
secrets_path = ROOT / ".streamlit" / "secrets.toml"
with open(secrets_path, "rb") as f:
    secrets = tomllib.load(f)
os.environ["GROQ_API_KEY"] = secrets["GROQ_API_KEY"]

client = Groq()

def ask(question):
    print(f"\n❓ QUERY: {question}")
    retriever = get_retriever()
    chunks = retriever.retrieve(question)
    prompt = build_prompt(question, chunks)
    print(f"DEBUG PROMPT:\n{prompt}\n{'='*50}")
    
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=250,
        temperature=0.1,
    )
    print(f"🤖 ANSWER:\n{response.choices[0].message.content.strip()}")
    print("-" * 50)

if __name__ == "__main__":
    print("🚀 RUNNING LATEST DATA VERIFICATION...")
    
    # 1. Test Small Cap NAV
    ask("What is the latest NAV of SBI Small Cap Fund as of March 2026?")
    
    # 2. Test Large & Midcap Rank
    ask("What is the INDmoney rank and performance of SBI Large & Midcap Fund?")
    
    # 3. Test Infra Portfolio Changes
    ask("Which top stocks were sold in the SBI Infrastructure Fund recently?")
    
    print("\n✅ Verification Complete.")
