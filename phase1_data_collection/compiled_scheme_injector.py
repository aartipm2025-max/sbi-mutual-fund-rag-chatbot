"""
Phase 1 — Compiled Scheme Knowledge Injector
============================================
Processes the curated, structured factsheets provided by the user (March 2026).
These are treated as "Master Factual Data" for the RAG system.
"""

import json
from datetime import datetime
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).resolve().parents[1]
OUTPUT_DIR = BASE_DIR / "data" / "raw_documents"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

CURATED_SCHEMES = [
    {
        "doc_id": "curated_sbi_small_cap",
        "source": "Master Scheme Dataset",
        "url": "https://www.sbimf.com/en-us/equity-funds/sbi-small-cap-fund",
        "text": """DOCUMENT TYPE: MUTUAL FUND SCHEME FACTSHEET
SCHEME NAME: SBI Small Cap Fund
SCHEME TYPE: Open-ended equity scheme investing predominantly in small-cap stocks
CATEGORY: Equity
STRUCTURE: Open Ended
RISK LEVEL: Very High Risk
INVESTMENT OBJECTIVE: Provide long-term capital appreciation by investing in a diversified basket of small-cap companies.
INVESTMENT STRATEGY: Blend of growth and value investing using bottom-up stock selection.
ASSET ALLOCATION: Minimum 65% small-cap equities; Up to 35% other equities, debt, and money market instruments.
BENCHMARK: Primary: BSE 250 SmallCap Index TRI; Additional: BSE Sensex TRI
FUND MANAGER: R Srinivasan (since November 2013)
DATE OF ALLOTMENT: 09 September 2009
AUM: ₹34,449.23 Crore (31 Jan 2026)
RETURNS SINCE INCEPTION: Regular Growth: 18.39%; Direct Growth: 22.5%
NAV: ₹154.7423 (04 Mar 2026)
MINIMUM SIP: ₹500"""
    },
    {
        "doc_id": "curated_sbi_large_midcap",
        "source": "Master Scheme Dataset",
        "url": "https://www.sbimf.com/en-us/equity-funds/sbi-large-midcap-fund",
        "text": """DOCUMENT TYPE: MUTUAL FUND SCHEME FACTSHEET
SCHEME NAME: SBI Large & Midcap Fund
SCHEME TYPE: Open-ended equity scheme investing in large-cap and mid-cap stocks
CATEGORY: Equity
STRUCTURE: Open Ended
RISK LEVEL: Very High Risk
INVESTMENT OBJECTIVE: Provide long-term capital appreciation through a diversified portfolio of large-cap and mid-cap companies.
INVESTMENT STRATEGY: Blend of growth and value investing with top-down and bottom-up stock selection.
ASSET ALLOCATION: Minimum 35% large-cap equities; Minimum 35% mid-cap equities; Up to 30% other equity or debt instruments.
BENCHMARK: Primary: Nifty LargeMidcap 250 TRI; Additional: BSE Sensex TRI
FUND MANAGER: Saurabh Pant (since September 2016)
DATE OF ALLOTMENT: 28 February 1993
AUM: ₹37,496.73 Crore (31 Jan 2026)
RETURNS SINCE INCEPTION: Regular Growth: 14.86%; Direct Growth: 17.11%
NAV: ₹632.554 (04 Mar 2026)
MINIMUM SIP: ₹500"""
    },
    {
        "doc_id": "curated_sbi_elss_taxsaver",
        "source": "Master Scheme Dataset",
        "url": "https://www.sbimf.com/en-us/equity-funds/sbi-long-term-equity-fund",
        "text": """DOCUMENT TYPE: MUTUAL FUND SCHEME FACTSHEET
SCHEME NAME: SBI ELSS Tax Saver Fund
SCHEME TYPE: Open-ended Equity Linked Saving Scheme (ELSS)
CATEGORY: Equity
STRUCTURE: Open Ended
RISK LEVEL: Very High Risk
INVESTMENT OBJECTIVE: Provide long-term capital appreciation while offering tax benefits under Section 80C.
LOCK-IN PERIOD: 3 Years
ASSET ALLOCATION: Minimum 80% equity and equity-related instruments; Up to 20% money market instruments.
BENCHMARK: Primary: BSE 500 TRI; Additional: BSE Sensex TRI
FUND MANAGER: Dinesh Balachandran (since September 2016)
DATE OF ALLOTMENT: 31 March 1993
AUM: ₹31,861.52 Crore (31 Jan 2026)
RETURNS SINCE INCEPTION: Regular Growth: 16.16%; Direct Growth: 16.14%
NAV: ₹429.3901 (04 Mar 2026)
MINIMUM SIP: ₹500"""
    },
    {
        "doc_id": "curated_sbi_nifty_next50",
        "source": "Master Scheme Dataset",
        "url": "https://www.sbimf.com/en-us/index-funds/sbi-nifty-next-50-index-fund",
        "text": """DOCUMENT TYPE: MUTUAL FUND SCHEME FACTSHEET
SCHEME NAME: SBI Nifty Next 50 Index Fund
SCHEME TYPE: Open-ended index fund tracking Nifty Next 50 Index
CATEGORY: Passive Solutions
STRUCTURE: Open Ended
RISK LEVEL: Very High Risk
INVESTMENT OBJECTIVE: Provide returns that correspond to the performance of the Nifty Next 50 Total Returns Index.
INVESTMENT STRATEGY: Passive index replication strategy tracking the Nifty Next 50 TRI.
BENCHMARK: Primary: Nifty Next 50 TRI; Additional: BSE Sensex TRI
FUND MANAGER: Raviprakash Sharma (since March 2015)
DATE OF ALLOTMENT: 19 May 2021
AUM: ₹1,814.36 Crore (31 Jan 2026)
RETURNS SINCE INCEPTION: Regular Growth: 13.74%; Direct Growth: 14.27%
NAV: ₹18.0534 (04 Mar 2026)
MINIMUM SIP: ₹500"""
    },
    {
        "doc_id": "curated_sbi_infrastructure",
        "source": "Master Scheme Dataset",
        "url": "https://www.sbimf.com/en-us/equity-funds/sbi-infrastructure-fund",
        "text": """DOCUMENT TYPE: MUTUAL FUND SCHEME FACTSHEET
SCHEME NAME: SBI Infrastructure Fund
SCHEME TYPE: Open-ended equity scheme investing in infrastructure and allied sectors
CATEGORY: Equity
STRUCTURE: Open Ended
RISK LEVEL: Very High Risk
INVESTMENT OBJECTIVE: Provide long-term capital appreciation by investing in companies involved in infrastructure growth.
ASSET ALLOCATION: Minimum 80% infrastructure-related equities; Up to 20% other equities, debt, and money market instruments.
BENCHMARK: Primary: Nifty Infrastructure TRI; Additional: BSE Sensex TRI
FUND MANAGER: Bhavin Vithlani (since January 2022)
DATE OF ALLOTMENT: 06 July 2007
AUM: ₹4,545.62 Crore (31 Jan 2026)
RETURNS SINCE INCEPTION: Regular Growth: 8.77%; Direct Growth: 14.66%
NAV: ₹46.9983 (04 Mar 2026)
MINIMUM SIP: ₹500"""
    }
]

def save_docs():
    print(f"Injecting {len(CURATED_SCHEMES)} Master Scheme Factsheets …\n")
    for doc in CURATED_SCHEMES:
        doc["fetched_at"] = datetime.now().isoformat()
        
        out_path = OUTPUT_DIR / f"{doc['doc_id']}.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(doc, f, indent=2, ensure_ascii=False)
        print(f"✓ Master Data Saved → {out_path.name}")
    
    # Save Unified JSON as well
    unified_doc = {
        "doc_id": "unified_scheme_dataset",
        "source": "Master Scheme Dataset",
        "url": "https://www.sbimf.com",
        "fetched_at": datetime.now().isoformat(),
        "text": "Unified Dataset Summary: Includes Small Cap, Large & Midcap, ELSS Tax Saver, Nifty Next 50, and Infrastructure funds AUM, NAV, and Managers as of March 2026."
    }
    with open(OUTPUT_DIR / "unified_scheme_dataset.json", "w", encoding="utf-8") as f:
        json.dump(unified_doc, f, indent=2)
    
    print(f"\n✅ All Master Factsheets injected successfully.")

if __name__ == "__main__":
    save_docs()
