"""
Phase 2 — Document Processing
==============================
Reads raw JSON files from /data/raw_documents/,
cleans and normalizes them, and saves clean JSON
files to /data/processed_documents/.
"""

import os
import re
import json
import logging
from pathlib import Path
from datetime import datetime

# ── Logging ──────────────────────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)

# ── Paths ─────────────────────────────────────────────────────────────────────
BASE_DIR    = Path(__file__).resolve().parents[1]
INPUT_DIR   = BASE_DIR / "data" / "raw_documents"
OUTPUT_DIR  = BASE_DIR / "data" / "processed_documents"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# ── Config ────────────────────────────────────────────────────────────────────
MIN_LINE_LENGTH = 5    # Preserves short factual lines (e.g., AUM, NAV, etc.)
MIN_DOC_WORDS   = 40    # Reduced slightly for short but dense technical notes


# ── Cleaning Functions ────────────────────────────────────────────────────────

def remove_extra_whitespace(text: str) -> str:
    """Collapse multiple blank lines and strip trailing spaces."""
    text = re.sub(r"\n{3,}", "\n\n", text)   # Max 2 consecutive newlines
    text = re.sub(r"[ \t]+", " ", text)       # Collapse inline whitespace
    return text.strip()


def filter_short_lines(text: str, min_len: int = MIN_LINE_LENGTH) -> str:
    """Remove lines that are too short to be meaningful content."""
    lines = text.splitlines()
    filtered = [line for line in lines if len(line.strip()) >= min_len]
    return "\n".join(filtered)


def remove_boilerplate(text: str) -> str:
    """Remove common web boilerplate phrases."""
    boilerplate_patterns = [
        r"cookie[s]?\s+policy",
        r"accept\s+all\s+cookies",
        r"privacy\s+policy",
        r"terms\s+(of\s+)?(use|service)",
        r"all\s+rights\s+reserved",
        r"©\s*\d{4}",
        r"follow\s+us\s+on",
        r"subscribe\s+to\s+(our\s+)?newsletter",
    ]
    combined = re.compile("|".join(boilerplate_patterns), re.IGNORECASE)
    lines = text.splitlines()
    cleaned = [line for line in lines if not combined.search(line)]
    return "\n".join(cleaned)


def normalize_unicode(text: str) -> str:
    """Replace common unicode artifacts with ASCII equivalents."""
    replacements = {
        "\u2019": "'", "\u2018": "'",
        "\u201c": '"', "\u201d": '"',
        "\u2013": "-", "\u2014": "-",
        "\u00a0": " ",
        "\u2022": "-",
    }
    for char, replacement in replacements.items():
        text = text.replace(char, replacement)
    return text


def clean_document(raw_text: str) -> str:
    """Run all cleaning steps on raw extracted text."""
    text = normalize_unicode(raw_text)
    text = remove_boilerplate(text)
    text = filter_short_lines(text)
    text = remove_extra_whitespace(text)
    return text


# ── Main Pipeline ─────────────────────────────────────────────────────────────

def process_document(raw_doc: dict) -> dict | None:
    """Clean a single raw document and return a processed document dict."""
    doc_id = raw_doc.get("doc_id", "unknown")
    raw_text = raw_doc.get("text", "")

    if not raw_text:
        logger.warning(f"  ⚠ Skipping '{doc_id}' — empty text.")
        return None

    clean_text = clean_document(raw_text)
    word_count = len(clean_text.split())

    if word_count < MIN_DOC_WORDS:
        logger.warning(f"  ⚠ Skipping '{doc_id}' — only {word_count} words after cleaning.")
        return None

    return {
        "doc_id":       doc_id,
        "source":       raw_doc.get("source", "Unknown"),
        "url":          raw_doc.get("url", ""),
        "fetched_at":   raw_doc.get("fetched_at", ""),
        "processed_at": datetime.now().isoformat(),
        "word_count":   word_count,
        "text":         clean_text,
    }


def process_all() -> None:
    """Process all raw documents in the input directory."""
    raw_files = list(INPUT_DIR.glob("*.json"))
    if not raw_files:
        logger.warning(f"No raw documents found in {INPUT_DIR}")
        return

    logger.info(f"Processing {len(raw_files)} raw documents …\n")
    success, skipped = 0, 0

    for filepath in raw_files:
        logger.info(f"→ {filepath.name}")
        with open(filepath, "r", encoding="utf-8") as f:
            raw_doc = json.load(f)

        processed = process_document(raw_doc)

        if processed:
            out_path = OUTPUT_DIR / f"{processed['doc_id']}_clean.json"
            with open(out_path, "w", encoding="utf-8") as f:
                json.dump(processed, f, indent=2, ensure_ascii=False)
            logger.info(f"  ✓ Saved → {out_path.name}  ({processed['word_count']} words)")
            success += 1
        else:
            skipped += 1

    logger.info(f"\n✅ Done — {success} processed, {skipped} skipped.")


# ── Entry Point ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    process_all()
