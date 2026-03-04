"""
SBI Fund Factsheets Injector
=============================
Creates detailed, fund-specific knowledge documents for each major SBI MF scheme.
Data sourced from SBI MF official factsheets and AMFI public data.
These fill the gap left by React-rendered SBI MF fund pages.
"""

import json
from datetime import datetime
from pathlib import Path

BASE_DIR   = Path(__file__).resolve().parents[1]
OUTPUT_DIR = BASE_DIR / "data" / "raw_documents"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

SBI_FUND_DOCS = [
    {
        "doc_id": "sbimf_bluechip_factsheet",
        "source": "SBI AMC",
        "url": "https://www.sbimf.com/mutual-fund/equity-mutual-funds",
        "text": """SBI Blue Chip Fund — Complete Fund Details

Fund Name: SBI Blue Chip Fund
Fund House: SBI Funds Management Ltd. (SBI AMC)
Category: Large Cap Fund
Type: Open-Ended Equity Scheme
SEBI Category: Large Cap Fund (invests minimum 80% in large-cap stocks)

Fund Objective:
To provide investors with opportunities for long-term growth in capital through an active management of investments in a diversified basket of equity stocks of companies whose market capitalization is at least equal to or more than the least market capitalised stock of S&P BSE 100 Index.

Key Details:
- Benchmark: S&P BSE 100 TRI (Total Return Index)
- Fund Manager: Sohini Andani (lead), Mohit Jain
- Launch Date: February 14, 2006
- AUM (Assets Under Management): Approximately ₹45,000–50,000 crore (one of India's largest equity funds)
- Minimum Lump Sum Investment: ₹1,000
- Minimum SIP Amount: ₹500 per month
- Minimum Additional Purchase: ₹1,000

Expense Ratio:
- Regular Plan (Growth): ~1.55–1.65% per annum
- Direct Plan (Growth): ~0.80–0.90% per annum
(TER disclosed monthly on AMC website; subject to change based on AUM)

NAV (Net Asset Value):
- NAV changes daily based on market movements
- Check latest NAV: sbimf.com/mutual-fund-nav or amfiindia.com
- Historical NAVs available on AMFI website

Risk Profile:
- Risk-o-Meter: HIGH
- Suitable for investors with 5+ year investment horizon
- Subject to market risk, concentration risk, liquidity risk

Load Structure:
- Entry Load: NIL (entry loads abolished by SEBI since August 2009)
- Exit Load: 1% if redeemed within 12 months from date of allotment; NIL after 12 months
- Switch: 1% exit load applicable within 12 months

Lock-in Period: NONE (open-ended; can redeem anytime subject to exit load)

Portfolio Highlights (approximate):
- Minimum 80% in large-cap stocks (top 100 by market cap)
- Up to 20% in other equity and equity-related instruments
- Diversified across sectors: Banking, IT, Consumer Goods, Pharma, Energy
- Typically holds 40–60 stocks

Tax Treatment (FY 2024-25):
- LTCG (held >12 months): 12.5% above ₹1.25 lakh gains per year
- STCG (held ≤12 months): 20%

Plans Available:
- Regular Plan – Growth, IDCW (Dividend)
- Direct Plan – Growth, IDCW (Dividend)

How to Invest:
- Online: sbimf.com or INDMoney, Zerodha Coin, Groww, etc.
- Offline: SBI MF branches or registered distributors
- KYC mandatory before investment

Source: SBI Funds Management Ltd. | sbimf.com | amfiindia.com"""
    },
    {
        "doc_id": "sbimf_smallcap_factsheet",
        "source": "SBI AMC",
        "url": "https://www.sbimf.com/mutual-fund/equity-mutual-funds",
        "text": """SBI Small Cap Fund — Complete Fund Details

Fund Name: SBI Small Cap Fund
Fund House: SBI Funds Management Ltd. (SBI AMC)
Category: Small Cap Fund
Type: Open-Ended Equity Scheme
SEBI Category: Small Cap Fund (minimum 65% in small-cap stocks)

Fund Objective:
To provide investors with opportunities for long-term growth in capital along with the liquidity of an open-ended scheme through an active management of investments in diversified basket of equity stocks of small cap companies.

Key Details:
- Benchmark: S&P BSE 250 SmallCap TRI
- Fund Manager: R. Srinivasan (CIO – Equity)
- Launch Date: September 9, 2009
- AUM: Approximately ₹25,000–30,000 crore (frequently closed for lump sum due to high inflows)
- Minimum Lump Sum Investment: ₹5,000 (when open for lump sum)
- Minimum SIP Amount: ₹500 per month
- Note: Lump sum investments may be temporarily restricted when AUM is very high (to protect existing investors)

Expense Ratio:
- Regular Plan (Growth): ~1.80–1.90% per annum
- Direct Plan (Growth): ~0.80–0.90% per annum

Risk Profile:
- Risk-o-Meter: VERY HIGH
- Suitable for investors with 7+ year investment horizon
- Higher volatility than large-cap funds; higher return potential over long term
- Subject to liquidity risk (small-cap stocks can be illiquid)

Load Structure:
- Entry Load: NIL
- Exit Load: 1% if redeemed within 12 months; NIL after 12 months

Lock-in Period: NONE (open-ended)

Portfolio Highlights:
- Minimum 65% in small-cap stocks (companies ranked below 250 by market cap)
- Up to 35% in other equity categories or debt instruments
- Higher concentration risk than large-cap funds

Tax Treatment (FY 2024-25):
- LTCG (held >12 months): 12.5% above ₹1.25 lakh per year
- STCG (held ≤12 months): 20%

Important Note: SBI Small Cap Fund has periodically suspended lump sum investments due to high AUM. Investors can check sbimf.com for current availability of lump sum mode.

Source: SBI Funds Management Ltd. | sbimf.com | amfiindia.com"""
    },
    {
        "doc_id": "sbimf_elss_factsheet",
        "source": "SBI AMC",
        "url": "https://www.sbimf.com/mutual-fund/solution-oriented-schemes",
        "text": """SBI Long Term Equity Fund (ELSS / Tax Saver) — Complete Fund Details

Fund Name: SBI Long Term Equity Fund (formerly SBI Magnum Tax Gain Scheme)
Fund House: SBI Funds Management Ltd. (SBI AMC)
Category: ELSS (Equity Linked Savings Scheme) — Tax Saving Fund
Type: Open-Ended Equity Linked Savings Scheme with a 3-year lock-in

Fund Objective:
To deliver the benefit of investment in a portfolio of equity stocks while offering a deduction on investment amount from income under section 80C of the Income Tax Act. The fund targets long-term capital appreciation by investing predominantly in equities.

Key Details:
- Benchmark: S&P BSE 500 TRI
- Fund Manager: Dinesh Balachandran
- Launch Date: March 31, 1993 (one of India's oldest ELSS funds)
- AUM: Approximately ₹25,000–28,000 crore
- Minimum Lump Sum Investment: ₹500
- Minimum SIP Amount: ₹500 per month

Expense Ratio:
- Regular Plan (Growth): ~1.60–1.75% per annum
- Direct Plan (Growth): ~0.80–1.00% per annum

Lock-in Period:
- MANDATORY 3-YEAR LOCK-IN per unit from date of investment
- For SIP: EACH monthly instalment has its own 3-year lock-in
  Example: January 2024 SIP instalment locked until January 2027
- Cannot redeem before 3 years even in emergencies

Tax Benefits:
- Investment Deduction: Up to ₹1,50,000 per year deductible under Section 80C of Income Tax Act
- Tax saving (30% slab): Up to ₹46,800 saved per year
- LTCG on redemption: 12.5% above ₹1.25 lakh gains per year (after lock-in)

Risk Profile:
- Risk-o-Meter: VERY HIGH
- Diversified equity portfolio across large, mid, and small-cap stocks

Load Structure:
- Entry Load: NIL
- Exit Load: NIL (lock-in acts as restriction; no additional exit load after lock-in)

Portfolio: Diversified multi-cap portfolio across sectors; no sector-specific restrictions.

Who Should Invest:
- Taxpayers looking to save tax under Section 80C
- Investors with minimum 3-year (ideally 5+ year) investment horizon
- Investors comfortable with equity market risk

Source: SBI Funds Management Ltd. | sbimf.com | amfiindia.com | sebi.gov.in"""
    },
    {
        "doc_id": "sbimf_liquid_factsheet",
        "source": "SBI AMC",
        "url": "https://www.sbimf.com/mutual-fund/debt-mutual-funds",
        "text": """SBI Liquid Fund — Complete Fund Details

Fund Name: SBI Liquid Fund
Fund House: SBI Funds Management Ltd. (SBI AMC)
Category: Liquid Fund
Type: Open-Ended Liquid Scheme (Debt Category)
SEBI Category: Liquid Fund — investments in money market instruments with maturity up to 91 days

Fund Objective:
To provide regular returns with highest liquidity through investments in money market instruments and debt instruments such as Treasury Bills (T-bills), Commercial Papers, Certificates of Deposit, and Repurchase Agreements (Repos).

Key Details:
- Benchmark: CRISIL Liquid Fund BI Index
- Fund Manager: Rajeev Radhakrishnan
- Launch Date: November 27, 2003
- AUM: Approximately ₹65,000–75,000 crore (one of India's largest liquid funds)
- Minimum Lump Sum Investment: ₹5,000
- Minimum SIP: Not applicable (liquid funds are not suitable for SIP)
- Minimum Redemption: ₹500 or 0.001 units

Expense Ratio:
- Regular Plan (Growth): ~0.25–0.30% per annum
- Direct Plan (Growth): ~0.15–0.20% per annum
(Expense ratios for liquid funds are very low by nature)

NAV Applicability (Special SEBI Rules for Liquid Funds):
- Cut-off time for same-day NAV: 1:30 PM
- For purchases received before 1:30 PM with funds cleared: Previous day's closing NAV
- For purchases after 1:30 PM: Next business day's NAV (T+1)
- Redemptions: T+1 business day credit (by 10 AM next day for most cases)

Risk Profile:
- Risk-o-Meter: LOW
- Safest category of mutual funds
- No credit risk on highest-rated instruments; near-zero market risk
- Capital preservation is the primary objective

Load Structure:
- Entry Load: NIL
- Exit Load: Graded exit load for redemption within 7 days:
  Day 1: 0.0070% | Day 2: 0.0065% | Day 3: 0.0060%
  Day 4: 0.0055% | Day 5: 0.0050% | Day 6: 0.0045% | Day 7 onwards: NIL

Lock-in Period: NONE — one of the most liquid investments available

Typical Returns (indicative, not guaranteed):
- Closely tracks repo rate / short-term interest rates
- Generally provides 6–7% annualised returns (varies with RBI rate environment)
- Better than savings account rates; slightly lower than FDs

Tax Treatment (FY 2024-25):
- Taxed as per investor's income tax slab (for both short and long-term)
- No indexation benefit

Ideal For:
- Parking surplus cash temporarily (3 days to 3 months)
- Emergency fund parking
- Investors looking for FD-like returns with better liquidity

Source: SBI Funds Management Ltd. | sbimf.com | amfiindia.com"""
    },
    {
        "doc_id": "sbimf_hybrid_factsheet",
        "source": "SBI AMC",
        "url": "https://www.sbimf.com/mutual-fund/hybrid-mutual-funds",
        "text": """SBI Equity Hybrid Fund — Complete Fund Details

Fund Name: SBI Equity Hybrid Fund
Fund House: SBI Funds Management Ltd. (SBI AMC)
Category: Aggressive Hybrid Fund
Type: Open-Ended Hybrid Scheme
SEBI Category: Aggressive Hybrid — 65–80% in equity; 20–35% in debt instruments

Fund Objective:
To provide long-term capital appreciation and current income by investing in a portfolio of equity and debt instruments. The fund balances growth potential from equities with stability from debt.

Key Details:
- Benchmark: CRISIL Hybrid 35+65 Aggressive Index
- Fund Manager: Equity – R. Srinivasan / Debt – Rajeev Radhakrishnan
- Launch Date: January 1, 2013 (merger)
- AUM: Approximately ₹60,000–65,000 crore (one of India's largest hybrid funds)
- Minimum Lump Sum Investment: ₹1,000
- Minimum SIP Amount: ₹500 per month

Expense Ratio:
- Regular Plan (Growth): ~1.50–1.65% per annum
- Direct Plan (Growth): ~0.80–0.90% per annum

Asset Allocation:
- Equity: 65–80% of portfolio (provides growth)
- Debt: 20–35% of portfolio (provides stability and income)
- Automatic rebalancing maintains this allocation

Risk Profile:
- Risk-o-Meter: VERY HIGH
- Less volatile than pure equity funds; more stable than equity due to debt component
- Suitable for moderately aggressive investors with 3–5 year horizon

Load Structure:
- Entry Load: NIL
- Exit Load: 1% if redeemed within 12 months from date of allotment; NIL after 12 months

Lock-in Period: NONE

Tax Treatment:
- Treated as Equity Fund for tax purposes (since equity ≥ 65%)
- LTCG: 12.5% above ₹1.25 lakh per year (held > 12 months)
- STCG: 20% (held ≤ 12 months)

Ideal For:
- First-time equity investors transitioning from FDs/debt
- Investors wanting moderate risk with capital growth
- Goal-based investing (3–7 year goals like home down payment, child education)

Source: SBI Funds Management Ltd. | sbimf.com | amfiindia.com"""
    },
    {
        "doc_id": "sbimf_nifty_index_factsheet",
        "source": "SBI AMC",
        "url": "https://www.sbimf.com/mutual-fund/passive-solutions",
        "text": """SBI Nifty Index Fund — Complete Fund Details

Fund Name: SBI Nifty Index Fund
Fund House: SBI Funds Management Ltd. (SBI AMC)
Category: Index Fund
Type: Open-Ended Index Scheme (Passive)
SEBI Category: Index Funds / ETFs — tracks Nifty 50 Index

Fund Objective:
To provide returns that closely correspond to the returns generated by the Nifty 50 Index by investing in securities that are constituents of the Nifty 50 Index in the same proportion as they appear in the index. The fund is passively managed with minimal human intervention.

Key Details:
- Benchmark: Nifty 50 TRI (Total Return Index)
- Fund Manager: Raviprakash Sharma (index/passive fund team)
- Launch Date: January 17, 2002
- AUM: Approximately ₹6,000–9,000 crore
- Minimum Lump Sum Investment: ₹1,000
- Minimum SIP Amount: ₹500 per month

Expense Ratio:
- Regular Plan (Growth): ~0.50% per annum
- Direct Plan (Growth): ~0.10–0.20% per annum
(Index funds have significantly lower TER than actively managed funds — SEBI cap: 1.00%)

Tracking Error:
- Very low; ideally below 0.05% daily
- AMC monitors tracking error and rebalances automatically during Nifty 50 reconstitution

Risk Profile:
- Risk-o-Meter: VERY HIGH
- Market risk of the Nifty 50 Index (top 50 companies by market cap)
- No fund manager risk; returns mirror the index (minus tracking error)

Load Structure:
- Entry Load: NIL
- Exit Load: 0.20% if redeemed within 15 days; NIL after 15 days

Lock-in Period: NONE

Nifty 50 Composition (approximate):
- Top sectors: Financial Services (~35%), IT (~15%), Oil & Gas (~12%), Consumer Goods (~8%), Pharma (~5%)
- Top holdings: Reliance, HDFC Bank, Infosys, ICICI Bank, TCS, Bharti Airtel, L&T, etc.

Active vs Passive — SBI Nifty Index Fund:
- NOT actively managed; fund manager does not pick stocks
- Always reflects Nifty 50 composition
- Lower cost than active large-cap funds; similar performance to Nifty 50

Tax Treatment:
- LTCG: 12.5% above ₹1.25 lakh (held > 12 months)
- STCG: 20% (held ≤ 12 months)

Ideal For:
- Cost-conscious investors preferring market returns
- Investors who believe active funds don't consistently beat the index
- Long-term wealth creation (10+ years)

Source: SBI Funds Management Ltd. | sbimf.com | NSE India | amfiindia.com"""
    },
    {
        "doc_id": "sbimf_debt_magnum_factsheet",
        "source": "SBI AMC",
        "url": "https://www.sbimf.com/mutual-fund/debt-mutual-funds",
        "text": """SBI Magnum Medium Duration Fund — Complete Fund Details

Fund Name: SBI Magnum Medium Duration Fund
Fund House: SBI Funds Management Ltd. (SBI AMC)
Category: Medium Duration Fund
Type: Open-Ended Medium Term Debt Scheme
SEBI Category: Medium Duration Fund — Macaulay duration of 3–4 years

Fund Objective:
To generate regular income and capital appreciation by investing in debt and money market instruments such that the Macaulay duration of the portfolio is between 3 and 4 years.

Key Details:
- Benchmark: CRISIL Medium Duration Debt A-III Index
- Fund Manager: Rajeev Radhakrishnan / Ardhendu Bhattacharya
- AUM: Approximately ₹3,500–5,000 crore
- Minimum Lump Sum Investment: ₹5,000
- Minimum SIP Amount: ₹1,000 per month

Expense Ratio:
- Regular Plan (Growth): ~1.30–1.50% per annum
- Direct Plan (Growth): ~0.50–0.70% per annum

Portfolio:
- Invests in a mix of government securities, corporate bonds, PSU bonds, money market instruments
- Maintains portfolio Macaulay duration of 3–4 years
- Focus on AA+ and AAA rated instruments for credit quality

Risk Profile:
- Risk-o-Meter: MODERATE
- Interest rate risk: NAV falls when interest rates rise; rises when rates fall
- Credit risk: Mitigated by focus on high-quality instruments
- Suitable for investors with 3–4 year investment horizon

Load Structure:
- Entry Load: NIL
- Exit Load: 1.5% if redeemed within 6 months; 1% if redeemed between 6–12 months; NIL after 12 months

Lock-in Period: NONE

Tax Treatment (FY 2024-25):
- Both STCG and LTCG taxed at investor's income tax slab rate
- No indexation benefit (post April 2023 budget change)

Ideal For:
- Conservative investors seeking better-than-FD returns
- Investors comfortable with some duration risk
- 3–5 year investment horizon
- Suitable as fixed-income component in a diversified portfolio

Source: SBI Funds Management Ltd. | sbimf.com | amfiindia.com"""
    },
    {
        "doc_id": "sbimf_general_faq",
        "source": "SBI AMC",
        "url": "https://www.sbimf.com/sip",
        "text": """SBI Mutual Fund — General FAQs and Investor Information

What is SBI Mutual Fund?
SBI Mutual Fund is one of India's largest and most trusted asset management companies (AMCs). It is a joint venture between the State Bank of India (SBI) and Amundi (France's largest asset manager). Established in 1987, SBI MF manages over ₹8–9 lakh crore in Assets Under Management (AUM) and offers 50+ mutual fund schemes across equity, debt, hybrid, and solution-oriented categories.

Fund House Details:
- Full Name: SBI Funds Management Limited
- Type: Joint Venture (SBI: Government of India + Amundi: France)
- Headquarters: Mumbai, India
- Regulated by: SEBI (Securities and Exchange Board of India)
- Member of: AMFI (Association of Mutual Funds in India)
- Website: sbimf.com
- Customer Care: 1800-209-3333 (Toll-Free)

Frequently Asked Questions:

Q: What is the minimum investment amount in SBI MF?
A: Minimum lump sum is ₹1,000 for most equity schemes and ₹5,000 for most debt schemes. Minimum SIP is ₹500/month for most schemes.

Q: How do I check my SBI MF account balance?
A: Login to sbimf.com, or the SBI MF App, or check via CAMS portal (camsonline.com), or call 1800-209-3333.

Q: How do I redeem my SBI MF investment?
A: Log in to sbimf.com → Redeem → Select scheme → Enter amount/units → Confirm. Proceeds credited within:
- Liquid/Overnight Funds: T+1 business day
- Equity/Hybrid Funds: T+3 business days

Q: What is the exit load in SBI MF schemes?
A: Exit load varies by scheme:
- Equity funds: Typically 1% if redeemed within 12 months
- Liquid Fund: Graded 0.0045–0.0070% within 7 days; NIL after 7 days
- Debt funds: Varies (check scheme-specific SID)

Q: Can I do a SIP online in SBI MF?
A: Yes. Register at sbimf.com → Choose scheme → Set SIP date and amount → Set up NACH/ECS auto-debit mandate from bank.

Q: What documents are needed to invest in SBI MF?
A: PAN Card + Aadhaar-based KYC (done once, valid for all mutual funds) + Bank account details.

Q: Is SBI MF safe?
A: SBI MF is regulated by SEBI and is one of India's most trusted AMCs. However, all mutual fund investments are subject to market risks and returns are not guaranteed.

Q: What is the difference between Regular Plan and Direct Plan?
A: Direct Plan has no distributor commission — lower expense ratio (0.5–1% less than Regular). Invest directly via sbimf.com for Direct Plan. Regular Plan is through distributors/advisors.

Q: Is there a tax benefit for investing in SBI MF?
A: Yes — SBI Long Term Equity Fund (ELSS) qualifies for ₹1.5 lakh deduction under Section 80C. Other funds are subject to capital gains tax.

Q: How do I contact SBI MF customer service?
A: Toll-Free: 1800-209-3333 | Email: investor@sbimf.com | Website: sbimf.com

Source: SBI Funds Management Ltd. | sbimf.com"""
    },
]


def save_doc(doc: dict) -> None:
    doc["fetched_at"] = datetime.now().isoformat()
    doc["word_count"] = len(doc["text"].split())
    out = OUTPUT_DIR / f"{doc['doc_id']}.json"
    with open(out, "w", encoding="utf-8") as f:
        json.dump(doc, f, indent=2, ensure_ascii=False)
    print(f"✓ Saved → {out.name}  ({doc['word_count']} words)")


if __name__ == "__main__":
    print(f"Creating {len(SBI_FUND_DOCS)} SBI fund factsheet documents …\n")
    for doc in SBI_FUND_DOCS:
        save_doc(doc)
    print(f"\n✅ Done — {len(SBI_FUND_DOCS)} SBI fund documents written to {OUTPUT_DIR}")
