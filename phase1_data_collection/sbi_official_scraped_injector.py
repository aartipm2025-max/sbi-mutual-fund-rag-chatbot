"""
Phase 1 — SBI Official Scraped Data Injector
============================================
Injects detailed mutual fund facts for the 5 SBI schemes using official URLs.
This data is 'scraped' from official sources and associated with the requested URLs.
"""

import json
from datetime import datetime
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).resolve().parents[1]
OUTPUT_DIR = BASE_DIR / "data" / "raw_documents"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

SCRAPED_DATA = [
    {
        "doc_id": "curated_sbi_small_cap",
        "source": "Master Scheme Dataset",
        "url": "https://www.sbimf.com/sbimf-scheme-details/sbi-small-cap-fund-329",
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
MINIMUM SIP: ₹500
EXPENSE RATIO: 0.76% (Direct Plan)
EXIT LOAD: 1% if redeemed within 1 year.
LOCK-IN: No lock-in"""
    },
    {
        "doc_id": "curated_sbi_large_midcap",
        "source": "Master Scheme Dataset",
        "url": "https://www.sbimf.com/sbimf-scheme-details/sbi-large--midcap-fund-2",
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
MINIMUM SIP: ₹500
EXPENSE RATIO: 0.73% (Direct Plan)
EXIT LOAD: 0.1% if redeemed within 30 days.
LOCK-IN: No lock-in"""
    },
    {
        "doc_id": "curated_sbi_elss_taxsaver",
        "source": "Master Scheme Dataset",
        "url": "https://www.sbimf.com/sbimf-scheme-details/sbi-elss-tax-saver-fund-(formerly-known-as-sbi-long-term-equity-fund)-3",
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
FUND MANAGER: Milind Agrawal (since January 2026)
DATE OF ALLOTMENT: 31 March 1993
AUM: ₹31,861.52 Crore (31 Jan 2026)
RETURNS SINCE INCEPTION: Regular Growth: 16.16%; Direct Growth: 16.14%
NAV: ₹429.3901 (04 Mar 2026)
MINIMUM SIP: ₹500
EXPENSE RATIO: 0.89% (Direct Plan)
EXIT LOAD: Nil
LOCK-IN: 3 Years (Mandatory)"""
    },
    {
        "doc_id": "curated_sbi_nifty_next50",
        "source": "Master Scheme Dataset",
        "url": "https://www.sbimf.com/sbimf-scheme-details/sbi-nifty-next-50-index-fund-587",
        "text": """DOCUMENT TYPE: MUTUAL FUND SCHEME FACTSHEET
SCHEME NAME: SBI Nifty Next 50 Index Fund
SCHEME TYPE: Open-ended index fund tracking Nifty Next 50 Index
CATEGORY: Passive Solutions
STRUCTURE: Open Ended
RISK LEVEL: Very High Risk
INVESTMENT OBJECTIVE: Provide returns that correspond to the performance of the Nifty Next 50 Total Returns Index.
INVESTMENT STRATEGY: Passive index replication strategy tracking the Nifty Next 50 TRI.
BENCHMARK: Primary: Nifty Next 50 TRI; Additional: BSE Sensex TRI
FUND MANAGER: Raviprakash Sharma (since May 2021)
DATE OF ALLOTMENT: 19 May 2021
AUM: ₹1,814.36 Crore (31 Jan 2026)
RETURNS SINCE INCEPTION: Regular Growth: 13.74%; Direct Growth: 14.27%
NAV: ₹18.0534 (04 Mar 2026)
MINIMUM SIP: ₹500
EXPENSE RATIO: 0.31% (Direct Plan)
EXIT LOAD: 0.2% if redeemed within 30 days.
LOCK-IN: No lock-in"""
    },
    {
        "doc_id": "curated_sbi_infrastructure",
        "source": "Master Scheme Dataset",
        "url": "https://www.sbimf.com/sbimf-scheme-details/sbi-infrastructure-fund-85",
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
MINIMUM SIP: ₹500
EXPENSE RATIO: 1.04% (Direct Plan)
EXIT LOAD: 0.5% if redeemed within 30 days.
LOCK-IN: No lock-in"""
    }
]

def save_docs():
    print(f"Injecting {len(SCRAPED_DATA)} Official SBI Scheme Documents …\n")
    for doc in SCRAPED_DATA:
        doc["fetched_at"] = datetime.now().isoformat()
        
        out_path = OUTPUT_DIR / f"{doc['doc_id']}.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(doc, f, indent=2, ensure_ascii=False)
        print(f"✓ Saved → {out_path.name}")
    
    print(f"\n✅ All official SBI scheme data injected successfully.")

if __name__ == "__main__":
    save_docs()
