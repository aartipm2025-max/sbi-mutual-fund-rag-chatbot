"""
Phase 1 (Top-up) — Fetch the 5 remaining AMFI pages via
mutualfundssahihai.com (AMFI's official investor education portal).
All URLs verified accessible with requests (no JS required).
Saves to the same /data/raw_documents/ directory.
"""

import json, time, logging, requests
from bs4 import BeautifulSoup
from datetime import datetime
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

BASE_DIR   = Path(__file__).resolve().parents[1]
OUTPUT_DIR = BASE_DIR / "data" / "raw_documents"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/122.0.0.0 Safari/537.36"
    )
}

# ── 5 replacement AMFI pages via MF Sahi Hai (AMFI's investor education site) ─
TOPUP_URLS = [
    {"id": "amfi_what_is_mf",
     "source": "AMFI",
     "url": "https://www.mutualfundssahihai.com/en/what-are-mutual-funds"},
    {"id": "amfi_types_of_mf",
     "source": "AMFI",
     "url": "https://www.mutualfundssahihai.com/en/types-of-mutual-funds"},
    {"id": "amfi_benefits_of_mf",
     "source": "AMFI",
     "url": "https://www.mutualfundssahihai.com/en/advantages-of-mutual-funds"},
    {"id": "amfi_how_to_invest",
     "source": "AMFI",
     "url": "https://www.mutualfundssahihai.com/en/how-to-invest"},
    {"id": "amfi_sip_guide",
     "source": "AMFI",
     "url": "https://www.mutualfundssahihai.com/en/what-is-systematic-investment-plan-sip"},
]


def fetch_page(url, retries=3, delay=2.0):
    for attempt in range(1, retries + 1):
        try:
            r = requests.get(url, headers=HEADERS, timeout=15)
            r.raise_for_status()
            logger.info(f"  ✓ [{r.status_code}] {url}")
            return r.text
        except requests.RequestException as e:
            logger.warning(f"  ✗ Attempt {attempt}/{retries}: {e}")
            if attempt < retries:
                time.sleep(delay * attempt)
    return None


def extract_text(html):
    soup = BeautifulSoup(html, "lxml")
    for tag in soup(["script", "style", "nav", "footer",
                     "header", "aside", "form", "iframe", "noscript"]):
        tag.decompose()
    main = soup.find("main") or soup.find("article") or soup.body
    return main.get_text(separator="\n", strip=True) if main else ""


if __name__ == "__main__":
    logger.info(f"Top-up scrape: {len(TOPUP_URLS)} AMFI pages\n")
    for entry in TOPUP_URLS:
        logger.info(f"[{entry['source']}] {entry['id']}")
        html = fetch_page(entry["url"])
        if html:
            text = extract_text(html)
            doc  = {
                "doc_id":     entry["id"],
                "source":     entry["source"],
                "url":        entry["url"],
                "fetched_at": datetime.now().isoformat(),
                "word_count": len(text.split()),
                "text":       text,
            }
            out = OUTPUT_DIR / f"{entry['id']}.json"
            with open(out, "w", encoding="utf-8") as f:
                json.dump(doc, f, indent=2, ensure_ascii=False)
            logger.info(f"  💾 Saved → {out.name}  ({doc['word_count']} words)")
        else:
            logger.error(f"  ✗ Failed: {entry['url']}")
        time.sleep(1.5)
    logger.info("\n✅ Top-up done.")
