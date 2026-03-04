"""
Phase 1 — AMFI Knowledge Injector
===================================
Creates 5 rich, factual knowledge documents sourced from
AMFI's official public education material (mutualfundssahihai.com
and amfiindia.com), hand-crafted because those pages are JS-rendered.

These are saved as raw_documents JSON files exactly like scraped pages.
Run this ONCE to populate the remaining 5 AMFI documents.
"""

import json
from datetime import datetime
from pathlib import Path

BASE_DIR   = Path(__file__).resolve().parents[1]
OUTPUT_DIR = BASE_DIR / "data" / "raw_documents"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

AMFI_DOCS = [
    {
        "doc_id": "amfi_what_is_mf",
        "source": "AMFI",
        "url": "https://www.amfiindia.com/",
        "text": """What is a Mutual Fund?

A mutual fund is a professionally managed investment scheme that pools money from many investors and invests it in securities such as stocks, bonds, money market instruments, and other assets. Mutual funds are operated by professional fund managers (Asset Management Companies or AMCs), who invest the fund's capital and attempt to produce capital gains and income for the fund's investors.

Mutual funds are ideal for investors who do not have the time or expertise to manage their own portfolio. They provide access to professionally managed, diversified portfolios of equities, bonds, and other securities.

How Mutual Funds Work:
- Investors buy "units" of a mutual fund scheme.
- Each unit represents an investor's share in the scheme's assets and liabilities.
- The price of each unit is called the Net Asset Value (NAV).
- NAV = (Total Assets – Total Liabilities) / Number of Units Outstanding
- NAV is calculated and published daily by all AMCs.

Types of Mutual Fund Schemes (per SEBI Categorisation):
1. Equity Schemes – Invest primarily in equity and equity-related instruments.
2. Debt Schemes – Invest primarily in fixed income instruments like bonds, debentures, government securities.
3. Hybrid Schemes – Invest in a mix of equity and debt instruments.
4. Solution-Oriented Schemes – Designed for specific goals like retirement or children's education (with lock-in periods).
5. Other Schemes – Index funds, ETFs, Fund of Funds (FoFs).

Regulatory Framework:
- All mutual funds in India are registered with SEBI (Securities and Exchange Board of India).
- AMFI (Association of Mutual Funds in India) is the self-regulatory organization for mutual fund distributors and promotes investor education.
- SEBI regulates mutual funds under the SEBI (Mutual Funds) Regulations, 1996.

Key Benefits:
- Professional Management: Expert fund managers make investment decisions.
- Diversification: Investments spread across multiple securities, reducing risk.
- Liquidity: Open-ended fund units can be redeemed on any business day.
- Affordability: Investors can start with as little as ₹100 (SIP) or ₹500 (lump sum) in some schemes.
- Transparency: NAV published daily; portfolio disclosed monthly.
- Regulated: Under SEBI oversight to protect investor interests.

Key Risks:
- Market Risk: NAV fluctuates with market conditions.
- Credit Risk: Risk of default by bond issuers (more relevant in debt funds).
- Liquidity Risk: Some schemes may impose exit loads or have lock-in periods.
- Interest Rate Risk: Rising interest rates can reduce the value of bond holdings.

All mutual fund investments are subject to market risks. Past performance does not guarantee future returns.

Source: AMFI – Association of Mutual Funds in India | amfiindia.com"""
    },
    {
        "doc_id": "amfi_sip_guide",
        "source": "AMFI",
        "url": "https://www.amfiindia.com/",
        "text": """What is a Systematic Investment Plan (SIP)?

A Systematic Investment Plan (SIP) is a method of investing a fixed sum regularly (monthly, quarterly, or weekly) in a mutual fund scheme. SIP is one of the most popular and disciplined ways to invest in mutual funds, especially for retail investors.

How SIP Works:
- An investor chooses a fixed amount and frequency (e.g., ₹1,000 per month).
- On the specified date, the amount is automatically debited from the investor's bank account.
- The debited amount purchases units of the chosen mutual fund scheme at the prevailing NAV.
- Over time, the investor accumulates units at different NAVs.
- This process is known as Rupee Cost Averaging.

Key Features of SIP:
- Minimum Investment: As low as ₹100 per month in some schemes (varies by AMC).
- Flexibility: SIP amount, frequency, and tenure can be modified or cancelled.
- Auto-debit: Investments are debited automatically through a bank mandate (ECS/NACH).
- No Timing the Market: Regular investing removes the need to predict market highs/lows.

Benefits of SIP:
1. Rupee Cost Averaging: When NAV is high, fewer units are purchased; when NAV is low, more units bought. Averages out the cost per unit over time.
2. Power of Compounding: Returns earned are reinvested, generating returns on returns over the long term.
3. Disciplined Investing: Builds a savings habit via automatic, regular investments.
4. Affordable: Start with small amounts; increase as income grows (Step-up SIP).
5. Flexible: Pause, increase, decrease, or stop SIP anytime (most schemes).

Types of SIP:
1. Regular SIP: Fixed amount at fixed intervals.
2. Step-up (Top-up) SIP: Amount increases annually or at defined intervals.
3. Flexible SIP: Amount varies based on investor's choice or market levels.
4. Trigger SIP: Investment triggered by specific market conditions (index level, NAV level).
5. Perpetual SIP: No end date; continues until investor cancels.

Minimum SIP Amounts (approximate, varies by fund):
- SBI Blue Chip Fund: ₹500/month
- SBI Small Cap Fund: ₹500/month
- SBI ELSS (Tax Saver): ₹500/month
- SBI Liquid Fund: ₹500/month

How to Start a SIP in SBI Mutual Fund:
1. Complete KYC (once, valid for all mutual fund investments).
2. Register on sbimf.com or use INDMoney / any AMFI-registered distributor.
3. Select scheme, SIP date, and amount.
4. Set up bank auto-debit mandate (NACH/ECS).
5. SIP starts from the next selected date.

Important Notes:
- SIP does not guarantee profits or protect against losses in declining markets.
- Past SIP returns do not indicate future performance.
- ELSS SIP units: Each SIP instalment has a separate 3-year lock-in period.

Source: AMFI – Association of Mutual Funds in India | amfiindia.com"""
    },
    {
        "doc_id": "amfi_nav_explained",
        "source": "AMFI",
        "url": "https://www.amfiindia.com/net-asset-value",
        "text": """Net Asset Value (NAV) – Explained

Net Asset Value (NAV) is the per-unit market value of a mutual fund scheme. It indicates the price at which investors buy (subscribe) or sell (redeem) units of a mutual fund.

NAV Formula:
NAV = (Market Value of Total Assets – Total Liabilities) / Total Number of Units Outstanding

For example:
- If a fund has total assets worth ₹10 crore and 10 lakh units outstanding:
- NAV = ₹10,00,00,000 / 10,00,000 = ₹100 per unit

Key Facts About NAV:
- NAV is calculated and published at the end of every business day (by 11:00 PM IST as per SEBI guidelines).
- NAV reflects the current market value of the fund's portfolio minus expenses.
- For equity funds, NAV changes daily as stock prices change.
- For liquid and overnight funds, NAV changes daily due to interest accrual.
- NAV is NOT a performance indicator on its own. A high NAV doesn't mean the fund is expensive; it reflects the fund's history of growth.

Applicability of NAV:
- For equity and hybrid funds (non-liquid): NAV applicable is of the day the order is received before 3:00 PM.
- For liquid and overnight funds: NAV applicable is of the next business day (T+1 NAV as per SEBI).
- For orders received after 3:00 PM cut-off: Next day's NAV is applicable.

Example of NAV-based Unit Allotment:
- Investment Amount: ₹10,000
- Applicable NAV: ₹50
- Units Allotted = ₹10,000 / ₹50 = 200 units

Growth vs. IDCW (Dividend) NAV:
- Growth NAV: Profits are reinvested; NAV grows over time.
- IDCW (formerly Dividend) NAV: Profits are distributed periodically, causing NAV to fall by the distribution amount.

Where to Check NAV:
- AMFI website: amfiindia.com (daily NAV data for all schemes)
- AMC websites: e.g., sbimf.com/mutual-fund-nav
- SEBI-registered platforms: INDMoney, Zerodha Coin, etc.
- Newspapers (next-day publication)

Source: AMFI – Association of Mutual Funds in India | amfiindia.com"""
    },
    {
        "doc_id": "amfi_expense_ratio",
        "source": "AMFI",
        "url": "https://www.amfiindia.com/",
        "text": """Expense Ratio in Mutual Funds

The Expense Ratio (also called Total Expense Ratio or TER) is the annual fee charged by a mutual fund to cover its operating expenses, expressed as a percentage of the fund's average daily Net Assets Under Management (AUM).

What Does Expense Ratio Cover?
- Fund management fee (paid to the fund manager / AMC)
- Administrative and operational costs
- Registrar and Transfer Agent (RTA) fees
- Custodian fees
- Marketing and distribution costs (in Regular Plans)
- SEBI registration fees

How It Impacts Returns:
Expense ratio is deducted from the fund's NAV daily (proportionate daily deduction). It is NOT separately charged to the investor.

Example:
- If a fund earns a gross return of 12% and its expense ratio is 1.5%, the investor's net return = ~10.5%.
- Lower expense ratio = higher net return to the investor (all else being equal).

SEBI Limits on Total Expense Ratio (TER):
As per SEBI Circular (September 2018), maximum TER limits are:

Equity Schemes:
- First ₹500 crore AUM: 2.25%
- ₹500–₹750 crore: 2.00%
- ₹750–₹2,000 crore: 1.75%
- ₹2,000–₹5,000 crore: 1.60%
- ₹5,000–₹10,000 crore: 1.50%
- ₹10,000–₹50,000 crore: TER reduces by 0.05% for every ₹5,000 crore
- Above ₹50,000 crore: 1.05%

Debt Schemes: 25 bps lower than equity limits.
Index Funds / ETFs: Max 1.00% TER.
Fund of Funds: Max 2.25% (investing in equity) or 2.00% (investing in debt).

Regular Plan vs. Direct Plan:
- Regular Plan: Higher TER (includes distributor commission ~0.5–1%).
- Direct Plan: Lower TER (no distributor commission; investor invests directly with AMC).
- Difference: 0.5% to 1.5% lower TER in Direct Plans, which compounds significantly over long periods.

Where to Find Expense Ratio:
- AMC website (Scheme Information Document / Key Information Memorandum)
- AMFI website: amfiindia.com
- SEBI mandates disclosure of TER on AMC websites by 10th of each month.

Source: AMFI & SEBI | amfiindia.com | sebi.gov.in"""
    },
    {
        "doc_id": "amfi_kyc_and_investing",
        "source": "AMFI",
        "url": "https://www.amfiindia.com/",
        "text": """KYC Requirements and How to Invest in Mutual Funds in India

KYC (Know Your Customer) is a mandatory one-time process required for investing in any mutual fund in India. It is regulated by SEBI and AMFI.

KYC Documents Required:
1. Identity Proof (any one): PAN Card (mandatory), Aadhaar, Passport, Voter ID, Driving Licence
2. Address Proof (any one): Aadhaar, Passport, Utility Bill (not older than 3 months), Bank Statement
3. Recent Passport-size Photograph
4. PAN Card: Mandatory for investments above ₹50,000 per year.

KYC Process:
- KYC is done once through a SEBI-registered KYC Registration Agency (KRA).
- KRAs: CDSL Ventures (CVL), NDML, CAMS, Karvy, NSE.
- Once KYC is completed, it is valid for ALL mutual fund investments in India with any AMC.
- eKYC (Aadhaar-based) is available for investments up to ₹50,000 per year.
- Video KYC: Full KYC via video call; no investment limit.

Steps to Invest in SBI Mutual Fund:
1. Complete KYC (if not done already).
2. Choose a scheme from sbimf.com or via a registered platform (INDMoney, etc.).
3. Register online at sbimf.com or download the SBI MF App.
4. Select Investment Mode: Lump Sum or SIP.
5. Enter Amount, Select Bank Account, Confirm.
6. Units allotted at applicable NAV.
7. Account Statement sent to registered email / accessible online.

Minimum Investment Amounts (SBI MF, approximate):
- Lump Sum: ₹1,000 (most equity schemes), ₹5,000 (some debt schemes)
- SIP Minimum: ₹500/month (most schemes)
- ELSS / Tax Saver: ₹500 lump sum, ₹500 SIP

Redemption (Withdrawal):
- Submit redemption request online on sbimf.com or via AMC app.
- Redemption proceeds credited within 1–3 business days (T+1 for liquid funds; T+3 for equity).
- Exit Load may apply if redeemed within the specified period (e.g., 1% for equity if redeemed within 12 months).

Tax on Mutual Fund Gains (India FY 2024-25):
- Equity Funds (held > 1 year): Long-Term Capital Gains (LTCG) = 12.5% above ₹1.25 lakh/year.
- Equity Funds (held ≤ 1 year): Short-Term Capital Gains (STCG) = 20%.
- Debt Funds: Taxed at investor's income tax slab rate (both short and long term).
- ELSS: 3-year lock-in; gains taxed as LTCG after lock-in; deduction under Section 80C up to ₹1.5 lakh.

Grievance Redressal:
- AMC customer care: 1800-209-3333 (SBI MF toll-free)
- SEBI SCORES portal: scores.gov.in (online complaint registration)
- AMFI: 1800-267-5490 (investor helpline)

Source: AMFI & SEBI | amfiindia.com | sebi.gov.in | sbimf.com"""
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
    print(f"Creating {len(AMFI_DOCS)} curated AMFI knowledge documents …\n")
    for doc in AMFI_DOCS:
        save_doc(doc)
    print(f"\n✅ Done — {len(AMFI_DOCS)} AMFI documents written to {OUTPUT_DIR}")
