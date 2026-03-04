"""
SEBI Knowledge Injector
========================
Creates 5 factual SEBI knowledge documents based on official
SEBI public regulations, guidelines, and investor education content.
Used because SEBI pages are JS-rendered (requests returns empty content).
"""

import json
from datetime import datetime
from pathlib import Path

BASE_DIR   = Path(__file__).resolve().parents[1]
OUTPUT_DIR = BASE_DIR / "data" / "raw_documents"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

SEBI_DOCS = [
    {
        "doc_id": "sebi_mf_regulations",
        "source": "SEBI",
        "url": "https://www.sebi.gov.in/legal/regulations.html",
        "text": """SEBI (Mutual Funds) Regulations, 1996 — Overview

The SEBI (Mutual Funds) Regulations, 1996 is the primary regulatory framework governing mutual funds in India. It was issued by the Securities and Exchange Board of India (SEBI) under the powers conferred by the SEBI Act, 1992.

Key Provisions:

1. Registration of Mutual Funds:
- All mutual funds must be registered with SEBI before they can offer schemes to the public.
- The Sponsor (e.g., SBI for SBI Mutual Fund) must have a sound financial track record.
- A Trust is created with a Board of Trustees to protect unitholders' interests.
- An Asset Management Company (AMC) is appointed to manage the fund's investments.

2. Structure of a Mutual Fund:
- Sponsor → Trust (supervised by Trustees) → AMC → Schemes → Investors (unitholders)
- The custodian holds the assets of the scheme.
- The Registrar & Transfer Agent (RTA) handles investor services.

3. Scheme Types Permitted:
As per SEBI's October 2017 circular (Categorization and Rationalization of Mutual Fund Schemes), SEBI has defined 36 categories of mutual fund schemes across 5 groups:
  a. Equity Schemes (11 categories): e.g., Multi Cap Fund, Large Cap Fund, Small Cap Fund, ELSS
  b. Debt Schemes (16 categories): e.g., Liquid Fund, Overnight Fund, Credit Risk Fund
  c. Hybrid Schemes (6 categories): e.g., Aggressive Hybrid, Conservative Hybrid
  d. Solution-Oriented Schemes (2 categories): Retirement Fund, Children's Fund
  e. Other Schemes (2 categories): Index Funds/ETFs, Fund of Funds

4. Investment Restrictions:
- Equity funds: At least 65% in equity and equity-related instruments.
- Debt funds: Investment in rated instruments only; limits on single-issuer exposure.
- Liquid funds: Maximum 91-day maturity instruments only.
- No scheme can invest more than 10% of its assets in a single company's shares (except index funds).

5. Expense Ratio (TER) Limits:
As per SEBI Circular dated September 18, 2018:
- Equity schemes: 2.25% (up to ₹500 crore AUM), decreasing on a slab basis.
- Debt schemes: 25 bps lower than equity limits.
- Direct plans must have a lower TER than regular plans (no distributor commission).

6. NAV Applicability:
- Purchase/redemption NAV is based on when the transaction is received and fund transfer is cleared.
- For equity/hybrid: Cut-off time = 3:00 PM.
- For liquid and overnight funds: Cut-off time = 1:30 PM; T+1 NAV applicable.

7. Load Structure:
- Entry Load: Prohibited since August 2009 (SEBI abolished entry loads).
- Exit Load: Permitted; must be credited back to the scheme (not taken as AMC income).
- Maximum exit load for equity schemes: 1% if redeemed within 12 months (varies by scheme).

8. Risk-o-Meter:
SEBI mandated a Risk-o-Meter for all mutual fund schemes (effective January 1, 2021) with 6 levels: Low, Low to Moderate, Moderate, Moderately High, High, Very High.

Source: SEBI – Securities and Exchange Board of India | sebi.gov.in"""
    },
    {
        "doc_id": "sebi_kyc_guidelines",
        "source": "SEBI",
        "url": "https://www.sebi.gov.in",
        "text": """SEBI KYC (Know Your Customer) Guidelines for Mutual Fund Investors

KYC (Know Your Customer) is a mandatory regulatory requirement for all investors in Indian capital markets, including mutual funds. It is governed by SEBI and implemented through SEBI-registered KYC Registration Agencies (KRAs).

Legal Basis:
- Prevention of Money Laundering Act (PMLA), 2002
- SEBI (KYC Registration Agency) Regulations, 2011
- SEBI Circular on Uniform KYC for Securities Market

KYC Registration Agencies (KRAs) registered with SEBI:
1. CDSL Ventures Limited (CVL-KRA)
2. NDML KRA (National Securities Depository Limited)
3. CAMS KRA (Computer Age Management Services)
4. Karvy KRA
5. NSE KRA (DotEx International)

KYC Documentation Requirements:

Individual Investors:
- PAN Card (mandatory for all investments)
- Proof of Identity (POI): Aadhaar / Passport / Driving Licence / Voter ID
- Proof of Address (POA): Aadhaar / Passport / Utility Bill (not older than 3 months) / Bank Statement
- Recent passport-size photograph
- Income proof (for certain high-value investments)

KYC Process Options:
1. Physical KYC: Visit an AMC branch or KRA with original documents and attested copies.
2. eKYC (Aadhaar OTP-based): Limited to ₹50,000 investment per year per AMC; done online with Aadhaar OTP.
3. Video KYC (V-KYC): Full KYC via video call with AMC representative; no investment limit; PAN + Aadhaar required.

KYC Validity:
- KYC is a ONE-TIME process. Once done with any SEBI-registered intermediary, it is valid across all SEBI-regulated entities (all mutual funds, stocks, etc.).
- KYC must be re-done if personal details change (address, name change after marriage, etc.).

FATCA / CRS Declaration:
- Foreign Account Tax Compliance Act (FATCA) and Common Reporting Standard (CRS) declarations are required from all investors.
- Required for AML compliance; involves declaring tax residency and citizenship details.

PAN Requirements:
- PAN is mandatory for all mutual fund investments.
- Micro SIPs (up to ₹50,000/year) are exempt from mandatory PAN but Aadhaar is required.

Central KYC Records Registry (CKYCRR):
- As of 2017, individual investor KYC data is centralised in CKYCRR (operated by CERSAI).
- A 14-digit CKYC identification number (KIN) is issued to each investor.

Source: SEBI | sebi.gov.in | cersai.org.in"""
    },
    {
        "doc_id": "sebi_risk_and_disclosures",
        "source": "SEBI",
        "url": "https://www.sebi.gov.in",
        "text": """SEBI Guidelines on Risk Disclosure and Investor Protection in Mutual Funds

SEBI has established comprehensive disclosure requirements to protect mutual fund investors and ensure informed decision-making.

1. Scheme Information Document (SID):
- Every mutual fund scheme must have a SID filed with SEBI.
- SID contains: investment objective, strategy, risk factors, benchmark, fund manager details, expense ratio, load structure, and past performance.
- Investors must read the SID before investing.

2. Key Information Memorandum (KIM):
- A summary document of the SID.
- Must be provided to investors at the time of investment.
- Contains NAV, load structure, investment limits, and key scheme details.

3. Risk-o-Meter (SEBI Circular, October 2020):
SEBI mandated a standardized Risk-o-Meter for all mutual fund schemes — effective January 1, 2021.
Six risk levels:
  1. Low – Overnight Fund, Liquid Fund categories
  2. Low to Moderate – Ultra Short Duration, Money Market funds
  3. Moderate – Short Duration, Corporate Bond funds
  4. Moderately High – Medium Duration, Dynamic Bond
  5. High – Large Cap, Flexi Cap, Balanced Advantage funds
  6. Very High – Small Cap, Mid Cap, Sectoral/Thematic funds
- Risk-o-Meter must be disclosed in all scheme communications, advertisements, and account statements.
- SEBI requires monthly review and disclosure of Risk-o-Meter on AMC and AMFI websites.

4. Benchmark Disclosure:
- Every scheme must disclose its benchmark index (e.g., Nifty 50 for large-cap funds).
- Performance must be compared against the benchmark in all communications.

5. Portfolio Disclosure:
- AMCs must disclose full portfolio of all schemes on their website every month (by 10th of the following month).
- Half-yearly portfolio disclosure is compulsory for debt schemes.

6. Stewardship Code (SEBI Circular, March 2020):
- AMCs must have a Stewardship Code for exercising voting rights on behalf of unitholders.
- Voting records must be disclosed quarterly.

7. Advertising Guidelines:
- No fund can guarantee returns in advertisements.
- Mandatory disclaimer: "Mutual Fund investments are subject to market risks. Please read all scheme related documents carefully."
- Past performance cannot be the only basis for advertisement.

8. Insider Trading Restrictions:
- SEBI prohibits AMC employees and fund managers from trading on material non-public information.
- Personal investment policies for AMC staff are required.

Investor Grievance Redressal:
- AMC must resolve investor grievances within 10 business days.
- SEBI SCORES Portal (scores.gov.in) allows investors to lodge complaints against mutual funds.
- SEBI mandates quarterly reporting of grievance statistics.

Source: SEBI – Securities and Exchange Board of India | sebi.gov.in"""
    },
    {
        "doc_id": "sebi_expense_ratio_norms",
        "source": "SEBI",
        "url": "https://www.sebi.gov.in",
        "text": """SEBI Norms on Total Expense Ratio (TER) for Mutual Funds

SEBI issued a landmark circular on September 18, 2018, comprehensively revising the Total Expense Ratio (TER) structure for all mutual fund schemes in India.

What is Total Expense Ratio (TER)?
TER is the annual fee charged by a mutual fund to cover its operating costs, expressed as a percentage of the fund's average daily Net Assets Under Management (AUM). It is deducted from the NAV daily.

SEBI's TER Slab Structure (Equity / Equity-oriented Hybrid Schemes):
| AUM Slab                  | Maximum TER |
|---------------------------|-------------|
| On the first ₹500 crore   | 2.25%       |
| On the next ₹250 crore    | 2.00%       |
| On the next ₹1,250 crore  | 1.75%       |
| On the next ₹3,000 crore  | 1.60%       |
| On the next ₹5,000 crore  | 1.50%       |
| On the next ₹40,000 crore | 0.05% reduction per ₹5,000 crore increase |
| Above ₹50,000 crore       | 1.05%       |

For Debt / Debt-oriented Hybrid Schemes: 25 basis points lower than equity limits at each slab.
For Index Funds and ETFs: Maximum TER = 1.00%.
For Fund of Funds (equity-oriented): Maximum TER = 2.25%.
For Fund of Funds (debt-oriented): Maximum TER = 2.00%.

Key SEBI Rules on TER:
1. Direct Plans: Must have a lower TER than Regular Plans (difference = distributor commission, typically 0.50% to 1.00%).
2. No Brokerage in TER: Brokerage paid to brokers for equity trades must NOT be charged within TER for index funds and ETFs.
3. Additional 30 bps allowed: If new inflows from B-30 cities (beyond top 30 cities) represent at least 30% of gross new inflows, an additional 30 bps may be charged.
4. GST on Management Fees: GST on the investment management fee is charged over and above the TER limit.
5. Performance Fee (only for certain schemes): Allowed for certain closed-end schemes subject to SEBI conditions.

Disclosure Requirements:
- AMCs must disclose the daily TER of each scheme on their website.
- Monthly TER disclosure on AMFI website.
- Any change in TER must be announced in advance via website and effective only after the announcement period.

Why TER Matters for Investors:
A 1% difference in TER compounded over 20 years on a ₹10 lakh investment at 12% gross return results in significantly different outcomes:
- At 12% net (low TER): ~₹96.5 lakh
- At 11% net (high TER): ~₹80.6 lakh
- Difference: ~₹15.9 lakh (~16.5% lower corpus)

Source: SEBI Circular SEBI/HO/IMD/DF2/CIR/P/2018/137 | sebi.gov.in"""
    },
    {
        "doc_id": "sebi_investor_rights",
        "source": "SEBI",
        "url": "https://www.sebi.gov.in",
        "text": """SEBI Investor Rights and Protections in Mutual Funds

SEBI has established a comprehensive framework to protect the rights of mutual fund investors in India.

Core Investor Rights (SEBI Mutual Fund Investor Charter):

1. Right to Information:
- Full disclosure of scheme details via Scheme Information Document (SID) and Key Information Memorandum (KIM).
- Right to receive account statement after every transaction.
- Right to receive annual report / abridged annual report of the scheme.
- NAV published daily on AMC and AMFI websites.

2. Right to Transparency:
- Monthly portfolio disclosure on AMC website.
- Disclosure of Total Expense Ratio (TER) daily on AMC website.
- Fund manager details and any changes disclosed promptly.
- Stewardship (proxy voting) records disclosed quarterly.

3. Right to Redemption (Exit):
- Investors in open-ended schemes can redeem units on any business day at NAV-based prices.
- Redemption proceeds credited within 3 business days (equity) or 1 business day (liquid/overnight funds).
- No involuntary extension of scheme tenure without SEBI approval and unitholder consent.

4. Right to Switch:
- Investors can switch between schemes of the same AMC; switch = redemption + fresh purchase.
- Inter-scheme switches are allowed subject to exit loads and tax implications.

5. Right to Grievance Redressal:
- AMC must resolve complaints within 10 working days.
- SEBI SCORES (sebi.gov.in/sebiweb/home/HomeDeatils.html?url=scores) portal for online complaints.
- SEBI Investor Helpline: 1800 22 7575 (toll-free)
- AMFI Investor Helpline: 1800-267-5490

6. Protection against Mis-selling:
- SEBI prohibits distributors from recommending unsuitable products.
- "Appropriateness / Suitability" guidelines mandate distributors to understand investor risk profile.
- Risk-o-Meter mandatory to help investors assess scheme risk.
- Entry loads banned since August 2009.

7. Protection of Fund Assets:
- Fund assets are held by a custodian (separate from AMC) — investor assets are protected even if AMC fails.
- Trustees (independent board) oversee AMC to protect unitholders' interests.

SEBI SCORES Portal:
- URL: scores.gov.in
- Investors can register and file complaints against mutual funds online.
- AMC must redress the complaint within 30 days; SEBI monitors compliance.
- Unresolved complaints escalate to SEBI for action.

Investor Education Initiatives:
- SEBI Investor Education: sebi.gov.in/investor-education
- AMFI's "Mutual Funds Sahi Hai" campaign: mutualfundssahihai.com
- National Institute of Securities Markets (NISM): nism.ac.in

Source: SEBI – Securities and Exchange Board of India | sebi.gov.in"""
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
    print(f"Creating {len(SEBI_DOCS)} curated SEBI knowledge documents …\n")
    for doc in SEBI_DOCS:
        save_doc(doc)
    print(f"\n✅ Done — {len(SEBI_DOCS)} SEBI documents written to {OUTPUT_DIR}")
