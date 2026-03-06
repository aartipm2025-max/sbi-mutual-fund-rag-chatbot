
import sys, os
from pathlib import Path

# Setup paths
ROOT = Path(r"c:\IND MONEY-RAG CHATBOT-M1\mf_rag_chatbot")
sys.path.insert(0, str(ROOT))

from phase4_rag_pipeline.retriever import get_retriever

def verify_all_urls():
    funds = [
        {"name": "SBI Small Cap Fund", "url": "https://www.sbimf.com/sbimf-scheme-details/sbi-small-cap-fund-329"},
        {"name": "SBI Large & Midcap Fund", "url": "https://www.sbimf.com/sbimf-scheme-details/sbi-large--midcap-fund-2"},
        {"name": "SBI ELSS Tax Saver Fund", "url": "https://www.sbimf.com/sbimf-scheme-details/sbi-elss-tax-saver-fund-(formerly-known-as-sbi-long-term-equity-fund)-3"},
        {"name": "SBI Nifty Next 50 Index Fund", "url": "https://www.sbimf.com/sbimf-scheme-details/sbi-nifty-next-50-index-fund-587"},
        {"name": "SBI Infrastructure Fund", "url": "https://www.sbimf.com/sbimf-scheme-details/sbi-infrastructure-fund-85"}
    ]
    
    retriever = get_retriever()
    print("\n" + "="*50)
    print("VERIFYING OFFICIAL SBI URL RETRIEVAL")
    print("="*50)
    
    for fund in funds:
        print(f"\n🔍 Testing: {fund['name']}")
        chunks = retriever.retrieve(fund['name'], top_k=5)
        found = False
        for c in chunks:
            if fund['url'] == c.get('url'):
                found = True
                print(f"✅ Found: {c['url']} (Source: {c['source']})")
                break
        if not found:
            print(f"❌ NOT FOUND: {fund['url']}")
            for i, c in enumerate(chunks):
                print(f"   Ref {i+1}: {c.get('url')} ({c.get('source')})")

if __name__ == "__main__":
    verify_all_urls()
