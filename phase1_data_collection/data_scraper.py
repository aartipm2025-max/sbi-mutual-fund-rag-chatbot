"""
Phase 1 — Data Collection
=========================
Scrapes official pages from:
  - SBI Mutual Fund  (sbimf.com)
  - SEBI             (sebi.gov.in)
  - AMFI             (amfiindia.com)

Each page is saved as a JSON file in /data/raw_documents/.

URLs verified as of March 2026.
"""

import os
import json
import time
import logging
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from pathlib import Path

# ── Logging ──────────────────────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)

# ── Paths ─────────────────────────────────────────────────────────────────────
BASE_DIR   = Path(__file__).resolve().parents[1]
OUTPUT_DIR = BASE_DIR / "data" / "raw_documents"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# ── Target URLs (verified live — March 2026) ──────────────────────────────────
TARGET_URLS = [
    # ── SBI Mutual Fund (sbimf.com) ──────────────────────────────────────────
    {"id": "sbimf_home",
     "source": "SBI AMC",
     "url": "https://www.sbimf.com/"},
    {"id": "sbimf_equity_funds",
     "source": "SBI AMC",
     "url": "https://www.sbimf.com/mutual-fund/equity-mutual-funds"},
    {"id": "sbimf_debt_funds",
     "source": "SBI AMC",
     "url": "https://www.sbimf.com/mutual-fund/debt-mutual-funds"},
    {"id": "sbimf_hybrid_funds",
     "source": "SBI AMC",
     "url": "https://www.sbimf.com/mutual-fund/hybrid-mutual-funds"},
    {"id": "sbimf_solution_schemes",
     "source": "SBI AMC",
     "url": "https://www.sbimf.com/mutual-fund/solution-oriented-schemes"},
    {"id": "sbimf_passive",
     "source": "SBI AMC",
     "url": "https://www.sbimf.com/mutual-fund/passive-solutions"},
    {"id": "sbimf_all_schemes",
     "source": "SBI AMC",
     "url": "https://www.sbimf.com/mutual-fund"},
    {"id": "sbimf_sip",
     "source": "SBI AMC",
     "url": "https://www.sbimf.com/sip"},
    {"id": "sbimf_nav",
     "source": "SBI AMC",
     "url": "https://www.sbimf.com/mutual-fund-nav"},
    {"id": "sbimf_learn",
     "source": "SBI AMC",
     "url": "https://www.sbimf.com/learn-about-mutual-funds"},
    # ── SEBI (sebi.gov.in) ───────────────────────────────────────────────────
    {"id": "sebi_home",
     "source": "SEBI",
     "url": "https://www.sebi.gov.in"},
    {"id": "sebi_investor_faq",
     "source": "SEBI",
     "url": "https://www.sebi.gov.in/sebiweb/other/OtherAction.do?doRecognisedFpi=yes&intmId=13"},
    {"id": "sebi_investor_charter",
     "source": "SEBI",
     "url": "https://www.sebi.gov.in/sebiweb/other/OtherAction.do?doInvestorEducation=yes"},
    {"id": "sebi_investor_awareness",
     "source": "SEBI",
     "url": "https://www.sebi.gov.in/sebiweb/other/OtherAction.do?doRecognisedFpi=yes&intmId=3"},
    {"id": "sebi_mutual_fund_info",
     "source": "SEBI",
     "url": "https://www.sebi.gov.in/sebiweb/other/OtherAction.do?doRecognisedFpi=yes&intmId=12"},
    {"id": "sebi_about",
     "source": "SEBI",
     "url": "https://www.sebi.gov.in/about-sebi.html"},
    # ── AMFI (amfiindia.com) ─────────────────────────────────────────────────
    {"id": "amfi_home",
     "source": "AMFI",
     "url": "https://www.amfiindia.com/"},
    {"id": "amfi_about",
     "source": "AMFI",
     "url": "https://www.amfiindia.com/about-amfi"},
    {"id": "amfi_investor_corner",
     "source": "AMFI",
     "url": "https://www.amfiindia.com/investor-corner"},
    {"id": "amfi_mf_sahi_hai",
     "source": "AMFI",
     "url": "https://www.amfiindia.com/investor-corner/knowledge-center"},
    {"id": "amfi_nav_all",
     "source": "AMFI",
     "url": "https://www.amfiindia.com/net-asset-value"},
    {"id": "amfi_industry_data",
     "source": "AMFI",
     "url": "https://www.amfiindia.com/research-information/nfo-information"},
    {"id": "amfi_distributor",
     "source": "AMFI",
     "url": "https://www.amfiindia.com/distributor-corner"},
    {"id": "amfi_regulatory",
     "source": "AMFI",
     "url": "https://www.amfiindia.com/industry-information"},
    {"id": "amfi_terms_of_use",
     "source": "AMFI",
     "url": "https://www.amfiindia.com/terms-of-use"},
]

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/122.0.0.0 Safari/537.36"
    )
}


# ── Core Functions ────────────────────────────────────────────────────────────

def fetch_page(url: str, retries: int = 3, delay: float = 2.0) -> str | None:
    """Fetch raw HTML from a URL with retry logic."""
    for attempt in range(1, retries + 1):
        try:
            response = requests.get(url, headers=HEADERS, timeout=15)
            response.raise_for_status()
            logger.info(f"  ✓ Fetched [{response.status_code}]: {url}")
            return response.text
        except requests.RequestException as e:
            logger.warning(f"  ✗ Attempt {attempt}/{retries} failed for {url}: {e}")
            if attempt < retries:
                time.sleep(delay * attempt)
    return None


def extract_text(html: str) -> str:
    """Extract visible body text from raw HTML."""
    soup = BeautifulSoup(html, "lxml")
    # Remove noise tags
    for tag in soup(["script", "style", "nav", "footer",
                     "header", "aside", "form", "iframe", "noscript"]):
        tag.decompose()
    main = soup.find("main") or soup.find("article") or soup.body
    if not main:
        return ""
    return main.get_text(separator="\n", strip=True)


def save_document(doc: dict) -> None:
    """Save a scraped document as JSON."""
    filepath = OUTPUT_DIR / f"{doc['doc_id']}.json"
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(doc, f, indent=2, ensure_ascii=False)
    logger.info(f"  💾 Saved → {filepath.name}")


def scrape_all() -> None:
    """Main entry point: scrape all target URLs."""
    logger.info(f"Starting scrape of {len(TARGET_URLS)} URLs …\n")
    success, failed = 0, 0

    for entry in TARGET_URLS:
        logger.info(f"[{entry['source']}] {entry['id']}")
        html = fetch_page(entry["url"])

        if html:
            text = extract_text(html)
            doc = {
                "doc_id":     entry["id"],
                "source":     entry["source"],
                "url":        entry["url"],
                "fetched_at": datetime.now().isoformat(),
                "word_count": len(text.split()),
                "text":       text,
            }
            save_document(doc)
            success += 1
        else:
            logger.error(f"  ✗ Failed to fetch: {entry['url']}")
            failed += 1

        time.sleep(1.5)  # Polite crawl delay

    logger.info(f"\n✅ Done — {success} succeeded, {failed} failed.")


# ── Entry Point ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    scrape_all()
