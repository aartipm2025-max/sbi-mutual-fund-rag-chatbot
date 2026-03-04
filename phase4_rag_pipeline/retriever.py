"""
Phase 4 — RAG Retrieval
========================
Loads the FAISS index and chunk metadata, embeds a user query,
and retrieves the top-K most relevant chunks with source URLs.
"""

import pickle
import logging
import numpy as np
from pathlib import Path

from sentence_transformers import SentenceTransformer
import faiss

# ── Logging ──────────────────────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)

# ── Paths ─────────────────────────────────────────────────────────────────────
BASE_DIR      = Path(__file__).resolve().parents[1]
FAISS_INDEX   = BASE_DIR / "vector_store" / "faiss_index.bin"
METADATA_FILE = BASE_DIR / "vector_store" / "chunks_metadata.pkl"

# ── Config ────────────────────────────────────────────────────────────────────
EMBEDDING_MODEL    = "sentence-transformers/all-MiniLM-L6-v2"
TOP_K              = 5      # Number of chunks to retrieve
DISTANCE_THRESHOLD = 1.2    # Only return genuinely relevant chunks


class Retriever:
    """
    Loads the FAISS index and chunk metadata once, then
    serves similarity-search requests for incoming queries.
    """

    def __init__(self) -> None:
        self._load_model()
        self._load_index()

    def _load_model(self) -> None:
        logger.info(f"Loading embedding model: {EMBEDDING_MODEL}")
        self.model = SentenceTransformer(EMBEDDING_MODEL)

    def _load_index(self) -> None:
        if not FAISS_INDEX.exists():
            raise FileNotFoundError(
                f"FAISS index not found at {FAISS_INDEX}. "
                "Run phase3_embeddings/embedder.py first."
            )
        if not METADATA_FILE.exists():
            raise FileNotFoundError(
                f"Chunk metadata not found at {METADATA_FILE}. "
                "Run phase3_embeddings/embedder.py first."
            )

        logger.info("Loading FAISS index …")
        self.index = faiss.read_index(str(FAISS_INDEX))

        with open(METADATA_FILE, "rb") as f:
            self.chunks_metadata: list[dict] = pickle.load(f)

        logger.info(
            f"Index loaded — {self.index.ntotal} vectors, "
            f"{len(self.chunks_metadata)} chunks."
        )

    def retrieve(self, query: str, top_k: int = TOP_K) -> list[dict]:
        """
        Embed the query and return the top-K most relevant chunks.

        Args:
            query:  User's question string.
            top_k:  Maximum number of chunks to return.

        Returns:
            List of chunk dicts, each containing:
                chunk_id, text, source, url, distance
        """
        query_embedding = self.model.encode([query], show_progress_bar=False).astype("float32")
        distances, indices = self.index.search(query_embedding, top_k)

        results = []
        for dist, idx in zip(distances[0], indices[0]):
            if idx == -1:
                continue
            if dist > DISTANCE_THRESHOLD:
                logger.debug(f"  Skipping chunk idx={idx} — distance {dist:.3f} > {DISTANCE_THRESHOLD}")
                continue
            chunk = self.chunks_metadata[idx].copy()
            chunk["distance"] = float(dist)
            results.append(chunk)

        logger.info(f"Retrieved {len(results)} relevant chunks for query.")
        return results


# ── Singleton helper ──────────────────────────────────────────────────────────

_retriever_instance: Retriever | None = None


def get_retriever() -> Retriever:
    """Return a cached singleton Retriever (loaded once per process)."""
    global _retriever_instance
    if _retriever_instance is None:
        _retriever_instance = Retriever()
    return _retriever_instance


# ── Entry Point (smoke test) ──────────────────────────────────────────────────
if __name__ == "__main__":
    test_query = "What is the expense ratio of SBI Blue Chip Fund?"
    retriever  = get_retriever()
    chunks     = retriever.retrieve(test_query)

    print(f"\nQuery: {test_query}\n{'─'*60}")
    for i, chunk in enumerate(chunks, 1):
        print(f"\n[Chunk {i}] Source: {chunk['source']} | Distance: {chunk['distance']:.4f}")
        print(f"URL: {chunk['url']}")
        print(f"Text: {chunk['text'][:300]} …")
