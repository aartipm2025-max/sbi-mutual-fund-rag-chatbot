
import sys, os
from pathlib import Path

# Setup paths
ROOT = Path(r"c:\IND MONEY-RAG CHATBOT-M1\mf_rag_chatbot")
sys.path.insert(0, str(ROOT))

from phase4_rag_pipeline.retriever import get_retriever

def verify_elss():
    question = "SBI ELSS Tax Saver Fund"
    retriever = get_retriever()
    chunks = retriever.retrieve(question, top_k=3)
    print(f"\nVerifying ELSS URL retrieval:")
    for i, c in enumerate(chunks):
        print(f"Chunk {i+1}: Source={c['source']}, URL={c['url']}")

if __name__ == "__main__":
    verify_elss()
