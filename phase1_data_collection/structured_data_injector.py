"""
Phase 1 — Structured Data Injector
==================================
Injects the master structured JSON data (schemes.json, statements.json) 
into the raw documents folder so they can be processed and indexed.
"""

import json
from pathlib import Path
from datetime import datetime

# Paths
BASE_DIR = Path(__file__).resolve().parents[1]
RAW_DIR = BASE_DIR / "data" / "raw_documents"
STRUCTURED_SRC_DIR = Path("c:/IND MONEY-RAG CHATBOT-M1/data/structured")

RAW_DIR.mkdir(parents=True, exist_ok=True)

def inject_structured_data():
    files_to_inject = [
        STRUCTURED_SRC_DIR / "schemes.json",
        STRUCTURED_SRC_DIR / "data" / "structured" / "statements.json"
    ]
    
    for src_path in files_to_inject:
        if not src_path.exists():
            print(f"⚠️ Source not found: {src_path}")
            continue
            
        print(f"Injecting {src_path.name} …")
        with open(src_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            
        # If it's a list (like schemes.json), we'll create a single doc for the retriever
        # or multiple docs. Let's create one doc per file for simplicity if they are small.
        
        doc_id = f"master_{src_path.stem}"
        doc_text = ""
        
        if isinstance(data, list):
            # Convert list of dicts to a legible text format for RAG
            for item in data:
                doc_text += f"\n---\n"
                for k, v in item.items():
                    doc_text += f"{k.replace('_', ' ').upper()}: {v}\n"
        else:
            doc_text = json.dumps(data, indent=2)
            
        doc_obj = {
            "doc_id": doc_id,
            "source": "Master Official Data",
            "url": "https://www.sbimf.com", # Default to SBI for master data
            "text": doc_text.strip(),
            "fetched_at": datetime.now().isoformat()
        }
        
        out_path = RAW_DIR / f"{doc_id}.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(doc_obj, f, indent=2, ensure_ascii=False)
        print(f"✓ Injected → {out_path.name}")

if __name__ == "__main__":
    inject_structured_data()
    print("\n✅ Structured data injection complete.")
