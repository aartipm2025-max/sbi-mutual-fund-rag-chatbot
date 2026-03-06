
import sys
from pathlib import Path

# Setup paths
ROOT = Path(r"c:\IND MONEY-RAG CHATBOT-M1\mf_rag_chatbot")
sys.path.insert(0, str(ROOT))

from phase4_rag_pipeline.retriever import get_retriever

def test_retrieval():
    query = "expense ratio of SBI Small Cap Fund"
    print(f"\n❓ TESTING RETRIEVAL: {query}")
    
    retriever = get_retriever()
    chunks = retriever.retrieve(query, top_k=10)
    
    print(f"\n🔍 Retrieved {len(chunks)} chunks.")
    for i, c in enumerate(chunks):
        print(f"\n--- Chunk {i+1} ---")
        print(f"Source: {c['source']}")
        print(f"URL: {c['url']}")
        print(f"Distance: {c['distance']:.4f}")
        print(f"ID: {c['chunk_id']}")
        print(f"Text: {c['text'][:200]}...")

if __name__ == "__main__":
    test_retrieval()
