"""
Phase 1 — INDmoney SBI Mutual Fund Knowledge Injector
=====================================================
Processes detailed real-time fund data (NAV, Holdings, Performance, Ranking) 
provided from the INDmoney platform (as of March 2026).
Supports multiple schemes.
"""

import json
from datetime import datetime
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).resolve().parents[1]
OUTPUT_DIR = BASE_DIR / "data" / "raw_documents"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

INDMONEY_SCHEMES = [
    {
        "doc_id": "indmoney_sbi_smallcap_detailed",
        "source": "INDmoney Portal",
        "url": "https://www.indmoney.com/mutual-funds/sbi-small-cap-fund",
        "text": """SBI Small Cap Fund — Real-time Detailed Analysis (as of March 2026)

Basic Info:
- NAV: ₹178.00 (as of 04 Mar 2026)
- 1-Day Change: ▼-1.9%
- Inception Return: 22.32% per year
- Category: Equity (Small-Cap)
- Fund House: SBI Mutual Fund
- Fund Manager: R. Srinivasan (since Nov 2013)

Performance vs. Benchmark & Peers (as on 04-Mar-26):
- 1-Year Return: 8.39% (Fund) vs 15.45% (Nifty Smallcap 250) vs 14.32% (Category Avg)
- 3-Year Return: 13.69% (Fund) vs 20.44% (Nifty Smallcap 250) vs 18.71% (Category Avg)
- 5-Year Return: 15.62% (Fund) vs 17.24% (Nifty Smallcap 250) vs 18.96% (Category Avg)
- Analysis: The fund has underperformed the benchmark and category average over 1Y, 3Y, and 5Y periods.

INDmoney Ranking:
- Rank: 16/18 in Small-Cap category.
- Performance Score: 23%
- Risk Management Score: 50%
- Cost Efficiency Score: 44%
- Peer Comparison: Bandhan Small Cap (Rank 1), Invesco India Smallcap (Rank 2), Edelweiss Small Cap (Rank 3).
- 3-Year Metrics: Alpha (-2.74), Beta (0.71), Sharpe Ratio (0.57), Sortino Ratio (0.86), Info Ratio (-1.09).

Asset Allocation (as on 14-Feb-26):
- Equity: 94.1%
- Debt & Cash: 5.9%
- Market Cap Breakup: Small Cap (84.6%), Mid Cap (5.6%).
- Allocation Changes: Small Cap allocation increased from 83.8% to 84.6% between Nov'25 and Feb'26.

Sector Allocation (as on 14-Feb-26):
- Industrial: 31.2% (Top sector)
- Consumer Cyclical: 22.9%
- Basic Materials: 16.5%
- Financial Services: 16.2%
- Others: Consumer Defensive (5.1%), Health (3.1%), Communication (1.7%), Real Estate (1.5%), Tech (1.4%).

Top Stock Holdings (as on 28-Feb-26):
1. City Union Bank Ltd: 3.63%
2. Ather Energy Ltd: 3.62%
3. ZF Commercial Vehicle Control Systems India Ltd: 3.05%
4. Navin Fluorine International Ltd: 2.66%
5. Kalpataru Projects International Ltd: 2.62%
6. Honeywell Automation India Ltd: 2.23%
7. EID Parry India Ltd: 2.5%
8. DOMS Industries Ltd: 2.28%

Fund Statistics:
- AUM: ₹34,449 Crore (Jan 26)
- Expense Ratio: 0.76%
- Exit Load: 1.0% if redeemed within 1 year.
- Risk Profile: Very High Risk.
- Turnover Ratio: 23.58%

Pros: Lower volatility within category, large AUM size, beats FD returns.
Cons: Not generated consistent returns, does not beat the benchmark consistently, underperforms during bull runs.

Source: INDmoney | Updated: March 2026"""
    },
    {
        "doc_id": "indmoney_sbi_largemidcap_detailed",
        "source": "INDmoney Portal",
        "url": "https://www.indmoney.com/mutual-funds/sbi-large-midcap-fund",
        "text": """SBI Large & Midcap Fund — Real-time Detailed Analysis (as of March 2026)

Basic Info:
- NAV: ₹703.33 (as of 02 Mar 2026)
- 1-Day Change: ▼-1.3%
- Inception Return: 17.04% per year
- Category: Large & Mid-Cap
- Fund House: SBI Mutual Fund
- Fund Manager: Saurabh Pant (since 10 September 2016)

Performance vs. Benchmark (Nifty 500) (as on 02-Mar-26):
- 1-Month Return: 1.21% (Fund) vs -1.19% (Nifty 500)
- 1-Year Return: 20.62% (Fund) vs 16.43% (Nifty 500) vs 16.47% (Category Avg)
- 3-Year Return: 19.82% (Fund) vs 16.18% (Nifty 500) vs 18.81% (Category Avg)
- 5-Year Return: 18.08% (Fund) vs 12.66% (Nifty 500) vs 15.69% (Category Avg)
- Analysis: The fund has consistently outperformed the benchmark (NIFTY 500) over 1Y, 3Y, and 5Y time periods.

INDmoney Ranking:
- Rank: 4/21 in Large & Mid-Cap category.
- Performance Score: 53%
- Risk Management Score: 95%
- Cost Efficiency Score: 59%
- Peer Comparison: Bandhan Large & Mid Cap (Rank 1), ICICI Prudential (Rank 2), UTI Large & Mid Cap (Rank 3).
- 3-Year Metrics: Alpha (2.34), Beta (0.80), Sharpe Ratio (1.19), Sortino Ratio (2.19), Info Ratio (-0.03).

Asset Allocation (as on 14-Feb-26):
- Equity: 94.8%
- Debt & Cash: 5.2%
- Market Cap Breakup: Large cap (41.2%), Mid cap (38.7%), Small cap (14.4%).
- Allocation Changes: Mid Cap and Large Cap allocation increased significantly between Nov'25 and Feb'26.

Sector Allocation (as on 14-Feb-26):
- Financial Services: 28.8%
- Basic Materials: 17.8%
- Consumer Cyclical: 14.3%
- Health: 12.4%
- Industrial: 9.8%

Top Stock Holdings (as on 28-Feb-26):
1. HDFC Bank Ltd: 5.45%
2. Axis Bank Ltd: 3.36%
3. State Bank of India: 3.3%
4. ICICI Bank Ltd: 3%
5. Ashok Leyland Ltd: 2.83%

Fund Statistics:
- AUM: ₹37,497 Crore (Jan 26)
- Expense Ratio: 0.73%
- Exit Load: 0.1% if redeemed within 30 days.
- Risk Profile: Very High Risk.
- Turnover Ratio: 21.26%

Pros: Lower volatility within category, lower probability of downside risk, protects capital during bear phase.
Cons: Underperforms benchmarks during bull run.

Source: INDmoney | Updated: March 2026"""
    },
    {
        "doc_id": "indmoney_sbi_elss_taxsaver_detailed",
        "source": "INDmoney Portal",
        "url": "https://www.indmoney.com/mutual-funds/sbi-elss-tax-saver-fund",
        "text": """SBI ELSS Tax Saver Fund — Real-time Detailed Analysis (as of March 2026)

Basic Info:
- NAV: ₹465.89 (as of 04 Mar 2026)
- 1-Day Change: ▼-1.3%
- Inception Return: 15.99% per year
- Category: ELSS (Tax Savings)
- Fund House: SBI Mutual Fund
- Fund Manager: Milind Agrawal (since 1 January 2026)

Performance vs. Benchmark (Nifty 500) (as on 04-Mar-26):
- 1-Year Return: 14.67% (Fund) vs 16.43% (Nifty 500) vs 13.55% (Category Avg)
- 3-Year Return: 24.38% (Fund) vs 16.18% (Nifty 500) vs 16.61% (Category Avg)
- 5-Year Return: 19.58% (Fund) vs 12.66% (Nifty 500) vs 13.86% (Category Avg)
- Analysis: Underperformed benchmark over 1Y but strongly outperformed over 3Y and 5Y.

INDmoney Ranking:
- Rank: 2/23 in ELSS category.
- Performance Score: 78%
- Risk Management Score: 67%
- Cost Efficiency Score: 47%
- Peer Comparison: HDFC ELSS (Rank 1), DSP ELSS (Rank 3), Mirae Asset ELSS (Rank 4).
- 3-Year Metrics: Alpha (6.51), Beta (0.97), Sharpe Ratio (1.32), Sortino Ratio (2.48), Info Ratio (1.96).

Asset Allocation (as on 14-Feb-26):
- Equity: 96.2%
- Debt & Cash: 3.8%
- Market Cap Breakup: Large cap (62.8%), Mid cap (18.7%), Small cap (14.7%).
- Allocation Changes: Large Cap exposure increased from 58.4% to 62.8% recently to provide stability.

Sector Allocation (as on 14-Feb-26):
- Financial Services: 31.4%
- Basic Materials: 10.7%
- Consumer Cyclical: 9.9%
- Energy: 9.6%
- Industrial: 9%

Top Stock Holdings (as on 28-Feb-26):
1. HDFC Bank Ltd: 8.34%
2. Reliance Industries Ltd: 4.94%
3. Axis Bank Ltd: 4.29%
4. Kotak Mahindra Bank Ltd: 4.19%
5. State Bank of India: 4.17%

Fund Statistics:
- AUM: ₹31,862 Crore (Jan 26)
- Expense Ratio: 0.89%
- Exit Load: 0%
- Lock-in: 3 Years (Mandatory for ELSS)
- Turnover Ratio: 19.46%

Pros: Generated consistent returns, consistently beats benchmark, lower probability of downside risk.
Cons: No major negative points found.

Source: INDmoney | Updated: March 2026"""
    },
    {
        "doc_id": "indmoney_sbi_nifty_next50_detailed",
        "source": "INDmoney Portal",
        "url": "https://www.indmoney.com/mutual-funds/sbi-nifty-next-50-index-fund",
        "text": """SBI Nifty Next 50 Index Fund — Real-time Detailed Analysis (as of March 2026)

Basic Info:
- NAV: ₹18.46 (as of 04 Mar 2026)
- 1-Day Change: ▼-1.5%
- Inception Return: 14.32% per year
- Category: Index Fund (Tracks Nifty Next 50)
- Fund House: SBI Mutual Fund
- Fund Manager: Raviprakash Sharma (since inception May 2021)

Performance (as on 04-Mar-26):
- 1-Year Return: 20.88% (CAGR)
- 3-Year Return: 22.61% (CAGR)
- Passively managed fund; returns mirror Nifty Next 50 TRI minus tracking error and expense ratio.

INDmoney Ranking:
- Rank: 1/12 in Nifty Next 50 Index Funds category.
- Expense Ratio: 0.31% (Relatively low for an index fund).
- 3-Year Metrics: Info Ratio (-7.51), Sharpe (0.99), Beta (1.00).

Asset Allocation (as on 14-Feb-26):
- Equity: 100%
- Large cap (84.8%), Mid cap (15.2%).
- Market cap mirrors the Nifty Next 50 Index.

Sector Allocation (as on 14-Feb-26):
- Financial Services: 20.3%
- Industrial: 14.6%
- Consumer Defensive: 13.9%
- Consumer Cyclical: 11%
- Utilities: 10.7%

Top Stock Holdings (as on 28-Feb-26):
1. Vedanta Ltd: 5.1%
2. Hindustan Aeronautics Ltd: 3.87%
3. TVS Motor Co Ltd: 3.81%
4. Divi's Laboratories Ltd: 3.39%
5. Bharat Petroleum Corp Ltd: 3.12%

Fund Statistics:
- AUM: ₹1,814 Crore (Jan 26)
- Exit Load: 0.2% if redeemed within 30 days.
- Turnover Ratio: 70.44%
- Tracking Error: AMC monitors closely to minimize deviation from index.

Who Should Invest:
- Investors seeking market returns with lower costs.
- Long-term investors (5-7+ years) who want exposure beyond Nifty 50.

Source: INDmoney | Updated: March 2026"""
    },
    {
        "doc_id": "indmoney_sbi_infrastructure_detailed",
        "source": "INDmoney Portal",
        "url": "https://www.indmoney.com/mutual-funds/sbi-infrastructure-fund",
        "text": """SBI Infrastructure Fund — Real-time Detailed Analysis (as of March 2026)

Basic Info:
- NAV: ₹51.03 (as of 04 Mar 2026)
- 1-Day Change: ▼-1.8%
- Inception Return: 14.76% per year
- Category: Equity (Thematic - Infrastructure)
- Fund House: SBI Mutual Fund
- Fund Manager: Bhavin Vithlani (since 1 January 2022)

Performance vs. Benchmark (Nifty Infrastructure) (as on 04-Mar-26):
- 1-Year Return: 14.28% (Fund) vs 16.43% (Nifty 500) vs 19.27% (Category Avg)
- 3-Year Return: 21.63% (Fund) vs 16.18% (Nifty 500) vs 23.28% (Category Avg)
- 5-Year Return: 20.34% (Fund) vs 12.66% (Nifty 500) vs 20.84% (Category Avg)
- Analysis: Outperformed broad benchmark (Nifty 500) over 3Y/5Y, but slightly lagging behind category average.

INDmoney Ranking:
- Rank: 8/14 in Infrastructure category.
- Performance Score: 26%
- Risk Management Score: 66%
- Cost Efficiency Score: 72%
- Peer Comparison: ICICI Prudential Infra (Rank 1), HDFC Infra (Rank 2), Canara Robeco Infra (Rank 3).
- 3-Year Metrics: Alpha (0.22), Beta (0.88), Sharpe Ratio (1.01), Sortino Ratio (1.65).

Asset Allocation (as on 14-Feb-26):
- Equity: 95.1%
- Debt & Cash: 4.9%
- Market Cap Breakup: Large cap (53.6%), Small cap (26.4%), Mid cap (15.1%).
- Major change: Small cap allocation reduced from 29.5% to 26.4% recently.

Sector Allocation (as on 14-Feb-26):
- Industrial: 34.9%
- Financial Services: 17.9%
- Energy: 13%
- Basic Materials: 12.8%
- Communication: 8.6%

Top Stock Holdings (as on 28-Feb-26):
1. Larsen & Toubro Ltd (L&T): 9.52%
2. Reliance Industries Ltd: 9.21%
3. Shree Cement Ltd: 5.94%
4. Bharti Airtel Ltd: 5.85%
5. Adani Energy Solutions Ltd: 4.13%

Fund Statistics:
- AUM: ₹4,546 Crore (Jan 26)
- Expense Ratio: 1.04%
- Exit Load: 0.5% if redeemed within 30 days.
- Risk Profile: Very High Risk (Thematic concentration).
- Turnover Ratio: 24.56%

Pros: Lower volatility within category, larger AUM size, beats FD returns for both 3Y & 5Y.
Cons: Underperforms benchmarks during bull run.

Source: INDmoney | Updated: March 2026"""
    }
]

def save_docs() -> None:
    print(f"Processing {len(INDMONEY_SCHEMES)} INDmoney knowledge documents …\n")
    for doc in INDMONEY_SCHEMES:
        doc["fetched_at"] = datetime.now().isoformat()
        doc["word_count"] = len(doc["text"].split())
        
        out_path = OUTPUT_DIR / f"{doc['doc_id']}.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(doc, f, indent=2, ensure_ascii=False)
        
        print(f"✓ Saved → {out_path.name}  ({doc['word_count']} words)")
    
    print(f"\n✅ Done — {len(INDMONEY_SCHEMES)} documents written to {OUTPUT_DIR}")

if __name__ == "__main__":
    save_docs()
