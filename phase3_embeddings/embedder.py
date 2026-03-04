"""
Phase 3 — Chunking & Embeddings
================================
Reads processed JSON documents from /data/processed_documents/,
splits them into chunks, generates vector embeddings using
SentenceTransformer, and saves a FAISS index to /vector_store/.

Chunk metadata is also saved as JSON in /data/chunks/.
"""

import os
import json
import logging
import pickle
import numpy as np
from pathlib import Path
from datetime import datetime

from langchain.text_splitter import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import faiss

# ── Logging ──────────────────────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)

# ── Paths ─────────────────────────────────────────────────────────────────────
BASE_DIR        = Path(__file__).resolve().parents[1]
INPUT_DIR       = BASE_DIR / "data" / "processed_documents"
CHUNKS_DIR      = BASE_DIR / "data" / "chunks"
VECTOR_DIR      = BASE_DIR / "vector_store"
FAISS_INDEX     = VECTOR_DIR / "faiss_index.bin"
METADATA_FILE   = VECTOR_DIR / "chunks_metadata.pkl"

CHUNKS_DIR.mkdir(parents=True, exist_ok=True)
VECTOR_DIR.mkdir(parents=True, exist_ok=True)

# ── Config ────────────────────────────────────────────────────────────────────
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
CHUNK_SIZE      = 500    # Characters per chunk
CHUNK_OVERLAP   = 50     # Overlap between adjacent chunks


# ── Step 1: Chunking ──────────────────────────────────────────────────────────

def load_processed_documents() -> list[dict]:
    """Load all cleaned documents from /data/processed_documents/."""
    docs = []
    for filepath in INPUT_DIR.glob("*.json"):
        with open(filepath, "r", encoding="utf-8") as f:
            docs.append(json.load(f))
    logger.info(f"Loaded {len(docs)} processed documents.")
    return docs


def chunk_documents(docs: list[dict]) -> list[dict]:
    """Split documents into overlapping text chunks."""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=["\n\n", "\n", ". ", " ", ""],
        length_function=len,
    )

    all_chunks = []
    for doc in docs:
        raw_chunks = splitter.split_text(doc["text"])
        for i, chunk_text in enumerate(raw_chunks):
            chunk = {
                "chunk_id":  f"{doc['doc_id']}_chunk_{i:03d}",
                "doc_id":    doc["doc_id"],
                "source":    doc["source"],
                "url":       doc["url"],
                "chunk_idx": i,
                "text":      chunk_text,
                "char_len":  len(chunk_text),
            }
            all_chunks.append(chunk)

    logger.info(f"Created {len(all_chunks)} chunks from {len(docs)} documents.")
    return all_chunks


def save_chunks(chunks: list[dict]) -> None:
    """Save all chunks as a single JSON file in /data/chunks/."""
    out_path = CHUNKS_DIR / "all_chunks.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(chunks, f, indent=2, ensure_ascii=False)
    logger.info(f"Chunks saved → {out_path}")


# ── Step 2: Embeddings ────────────────────────────────────────────────────────

def generate_embeddings(chunks: list[dict]) -> np.ndarray:
    """Generate sentence embeddings for all chunk texts."""
    logger.info(f"Loading embedding model: {EMBEDDING_MODEL} …")
    model = SentenceTransformer(EMBEDDING_MODEL)

    texts = [c["text"] for c in chunks]
    logger.info(f"Encoding {len(texts)} chunks …")
    embeddings = model.encode(texts, show_progress_bar=True, batch_size=32)

    return np.array(embeddings, dtype="float32")


# ── Step 3: FAISS Index ───────────────────────────────────────────────────────

def build_faiss_index(embeddings: np.ndarray) -> faiss.IndexFlatL2:
    """Build a FAISS flat L2 index from the embedding matrix."""
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    logger.info(f"FAISS index built — {index.ntotal} vectors ({dim}d).")
    return index


def save_index(index: faiss.IndexFlatL2, chunks: list[dict]) -> None:
    """Persist the FAISS index and chunk metadata to disk."""
    faiss.write_index(index, str(FAISS_INDEX))
    with open(METADATA_FILE, "wb") as f:
        pickle.dump(chunks, f)
    logger.info(f"FAISS index  → {FAISS_INDEX}")
    logger.info(f"Chunk metadata → {METADATA_FILE}")


# ── Main Pipeline ─────────────────────────────────────────────────────────────

def run_embedding_pipeline() -> None:
    """End-to-end: load → chunk → embed → index → save."""
    docs       = load_processed_documents()
    chunks     = chunk_documents(docs)
    save_chunks(chunks)
    embeddings = generate_embeddings(chunks)
    index      = build_faiss_index(embeddings)
    save_index(index, chunks)
    logger.info("\n✅ Embedding pipeline complete.")


# ── Entry Point ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    run_embedding_pipeline()
