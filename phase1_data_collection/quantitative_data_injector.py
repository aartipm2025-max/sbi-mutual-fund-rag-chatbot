"""
Phase 1 — Quantitative Data Knowledge Injector
==============================================
Processes structured quantitative metrics and IDCW history for SBI funds (March 2026).
"""

import json
from datetime import datetime
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).resolve().parents[1]
OUTPUT_DIR = BASE_DIR / "data" / "raw_documents"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

QUANT_DATA = [
    {
        "doc_id": "quant_sbi_infra",
        "source": "Official Quantitative Dataset",
        "url": "https://www.sbimf.com/sbimf-scheme-details/sbi-infrastructure-fund-85",
        "text": """SCHEME NAME: SBI Infrastructure Fund
QUANTITATIVE METRICS (as on Feb/Mar 2026):
- Expense Ratio (Regular Plan): 1.93% (28 Feb 2026)
- Expense Ratio (Direct Plan): 1.04% (28 Feb 2026)
- Tracking Error (Regular Plan): 5.7594% (02 Mar 2026)
- Sharpe Ratio: 1.04
- Standard Deviation: 15.19%
- Beta: 0.88
- Tracking Error Calculation: 1-year period ending 02 Mar 2026 based on day-end NAV (Total Returns Index).
- Expense Ratio Note: Inclusive of GST on management fees.

IDCW HISTORY:
- Plan: SBI Infrastructure Fund – Regular Plan – IDCW
- 16 Mar 2018: IDCW ₹1.7 (NAV ₹13.6863)
- Face Value: ₹10"""
    },
    {
        "doc_id": "quant_sbi_large_midcap",
        "source": "Official Quantitative Dataset",
        "url": "https://www.sbimf.com/sbimf-scheme-details/sbi-large--midcap-fund-2",
        "text": """SCHEME NAME: SBI Large & Midcap Fund
QUANTITATIVE METRICS (as on Feb/Mar 2026):
- Expense Ratio (Regular Plan): 1.55% (28 Feb 2026)
- Expense Ratio (Direct Plan): 0.72% (28 Feb 2026)
- Sharpe Ratio: 1.23
- Standard Deviation: 10.84%
- Beta: 0.79
- Source: CRISIL Fund Analyser
- Risk-Free Rate Used: FBIL Overnight MIBOR 9.39% (30 Sep 2024)
- Calculation Basis: 3 Years Monthly Data Points

IDCW HISTORY:
- Plan: SBI Large & Midcap Fund – Regular Plan – IDCW
- 09 Mar 2018: IDCW ₹11 (NAV ₹94.1106)
- 27 Feb 2017: IDCW ₹7.8 (NAV ₹89.6546)
- 12 Sep 2014: IDCW ₹11.5 (NAV ₹74.96410)
- Face Value: ₹10"""
    },
    {
        "doc_id": "quant_sbi_elss",
        "source": "Official Quantitative Dataset",
        "url": "https://www.sbimf.com/sbimf-scheme-details/sbi-elss-tax-saver-fund-(formerly-known-as-sbi-long-term-equity-fund)-3",
        "text": """SCHEME NAME: SBI ELSS Tax Saver Fund
QUANTITATIVE METRICS (as on Feb/Mar 2026):
- Expense Ratio (Regular Plan): 1.57% (28 Feb 2026)
- Expense Ratio (Direct Plan): 0.92% (28 Feb 2026)
- Sharpe Ratio: 1.36
- Standard Deviation: 12.81%
- Beta: 0.97
- Source: CRISIL Fund Analyser
- Risk-Free Rate Used: FBIL Overnight MIBOR 9.39% (30 Sep 2024)
- Calculation Basis: 3 Years Monthly Data Points

IDCW HISTORY:
- Plan: SBI ELSS Tax Saver Fund – Direct Plan – IDCW
- 24 Mar 2023: IDCW ₹6.8 (NAV ₹60.5306)
- 17 Mar 2022: IDCW ₹6.5 (NAV ₹62.9052)
- 06 Mar 2020: IDCW ₹3.8072572 (NAV ₹42.3469)
- 08 Mar 2019: IDCW ₹3.8072572 (NAV ₹48.1586)
- Face Value: ₹10"""
    },
    {
        "doc_id": "quant_sbi_next50",
        "source": "Official Quantitative Dataset",
        "url": "https://www.sbimf.com/sbimf-scheme-details/sbi-nifty-next-50-index-fund-587",
        "text": """SCHEME NAME: SBI Nifty Next 50 Index Fund
QUANTITATIVE METRICS (as on Feb/Mar 2026):
- Expense Ratio (Regular Plan): 0.70% (28 Feb 2026)
- Expense Ratio (Direct Plan): 0.31% (28 Feb 2026)
- Tracking Error (Direct Plan): 0.0436% (02 Mar 2026)
- Tracking Error (Regular Plan): 0.0495% (02 Mar 2026)
- Sharpe Ratio: 1.03
- Standard Deviation: 16.58%
- Beta: 1

TRACKING DIFFERENCE (as on 31 Jan 2026):
Direct Plan 1Y: -0.377, 3Y: -0.4307, SI: -0.4322
Regular Plan 1Y: -0.8097, 3Y: -0.9757, SI: -0.9688
Tracking difference is computed based on annualised returns of dividend-adjusted NAVs."""
    }
]

def save_docs():
    print(f"Injecting {len(QUANT_DATA)} Quantitative Data Documents …\n")
    for doc in QUANT_DATA:
        doc["fetched_at"] = datetime.now().isoformat()
        
        out_path = OUTPUT_DIR / f"{doc['doc_id']}.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(doc, f, indent=2, ensure_ascii=False)
        print(f"✓ Quant Data Saved → {out_path.name}")
    
    print(f"\n✅ All Quantitative Data injected successfully.")

if __name__ == "__main__":
    save_docs()
