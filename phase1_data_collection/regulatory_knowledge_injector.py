"""
Phase 1 — Regulatory & AMFI Knowledge Injector
==============================================
Injects detailed knowledge documents from SEBI and AMFI URLs.
Data synthesized from official sources and search results.
"""

import json
from datetime import datetime
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).resolve().parents[1]
OUTPUT_DIR = BASE_DIR / "data" / "raw_documents"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

DOCS = [
    {
        "doc_id": "sebi_riskometer_circular_info",
        "source": "SEBI Official",
        "url": "https://www.sebi.gov.in/legal/circulars/oct-2020/circular-on-product-labeling-in-mutual-fund-schemes-risk-o-meter_47796.html",
        "text": """SEBI CIRCULAR: PRODUCT LABELING IN MUTUAL FUND SCHEMES - RISKOMETER
DATE: October 05, 2020

Based on the recommendations of Mutual Fund Advisory Committee (MFAC), SEBI has decided to replace the existing 'Risk-o-meter' which had five levels of risk with a new 'Risk-o-meter' having six levels of risk.

NEW RISK LEVELS:
1. Low Risk
2. Low to Moderate Risk
3. Moderate Risk
4. Moderately High Risk
5. High Risk
6. Very High Risk (NEW)

KEY GUIDELINES:
- Evaluation of Risk: The risk level shall be evaluated on a monthly basis.
- Disclosure: AMCs shall disclose the Risk-o-meter along with portfolio disclosure on their website and on AMFI website within 10 days from the close of each month.
- Change in Risk-o-meter: Any change in Risk-o-meter shall be communicated by way of Notice cum Addendum and by way of an e-mail or SMS to unitholders of that particular scheme.
- Annual Disclosure: AMCs shall disclose the Risk-o-meter of the scheme as on March 31 of every year, along with the number of times the Risk-o-meter has changed over the year, in the Annual Report and Abridged Summary.
- Applicability: This circular is applicable for all existing schemes and all schemes to be launched on or after January 01, 2021."""
    },
    {
        "doc_id": "sebi_riskometer_understanding",
        "source": "SEBI Investor Portal",
        "url": "https://investor.sebi.gov.in/riskometer.html",
        "text": """UNDERSTANDING THE RISKOMETER - SEBI INVESTOR EDUCATION
The Riskometer is a visual tool used in the mutual fund industry to depict the risk level of a scheme.

WHAT IS A RISKOMETER?
It simplifies complex risk assessments into a snapshot of potential risks, ranging from Low to Very High.

SIX RISK CATEGORIES:
1. Low Risk: Minimal volatility, prioritized for capital protection. (Color: Irish Green)
2. Low to Moderate Risk: Relatively stable but slightly higher risk than low. (Color: Chartreuse)
3. Moderate Risk: Balanced risk level for calculated risks. (Color: Neon Yellow)
4. Moderately High Risk: Significant market volatility exposure. (Color: Caramel)
5. High Risk: Higher risk than moderate, potential for high returns. (Color: Dark Orange)
6. Very High Risk: Highly volatile, suitable for aggressive investors. (Color: Red)

FACTORS FOR CLASSIFICATION:
- Underlying Assets: Nature of equity, debt, or hybrid holdings.
- Market Volatility: Sensitivity to price changes.
- Credit/Interest Rate Risk: Sensitivity to debt defaults or rate changes.

BENEFITS:
- Helps align risk appetite with fund choice.
- Ensures transparency across all fund houses.
- Prevents mismatched investments (e.g., conservative investors in aggressive funds)."""
    },
    {
        "doc_id": "amfi_mf_basics",
        "source": "AMFI Knowledge Center",
        "url": "https://www.amfiindia.com/investor/knowledge-center/mutual-fund",
        "text": """AMFI KNOWLEDGE CENTER: FUNDAMENTALS OF MUTUAL FUNDS

WHAT IS A MUTUAL FUND?
A mutual fund is a collective investment vehicle that pools money from numerous investors to invest in a diversified portfolio of securities like equities, bonds, and money market instruments.

HOW IT WORKS:
- Professional Management: Invested by qualified fund managers.
- Net Asset Value (NAV): The worth of each unit of a mutual fund scheme. Income/gains are reflected in the NAV after expenses.
- Units: Investors are issued units based on the amount invested at the prevailing NAV.

ADVANTAGES:
- Diversification: Reduces risk by spreading money across assets.
- Affordability: Can start via small SIP amounts.
- Liquidity: Open-ended funds allow redemption on any business day.
- Professional Management: Benefit from expert analysis.

AMFI'S MISSION:
To promote the growth of the mutual fund industry, ensure smooth functioning, and safeguard investor interests under SEBI supervision."""
    },
    {
        "doc_id": "amfi_sip_details",
        "source": "AMFI Knowledge Center",
        "url": "https://www.amfiindia.com/investor/knowledge-center/sip",
        "text": """AMFI KNOWLEDGE CENTER: SYSTEMATIC INVESTMENT PLAN (SIP)

WHAT IS SIP?
SIP is a method of investing in mutual funds where an investor contributes a fixed amount at regular intervals (monthly, quarterly, etc.) instead of a lump sum.

KEY BENEFITS:
- Disciplined Saving: Encourages regular investment habits.
- Rupee Cost Averaging: You buy more units when prices are low and fewer when prices are high, lowering your average cost per unit.
- Power of Compounding: Small, regular amounts can grow into a large corpus over time.
- Convenience: Automated via bank mandates (NACH/ECS).

SIP VS. LUMP SUM:
SIP is ideal for investors with monthly income who want to build wealth gradually without timing the market."""
    },
    {
        "doc_id": "amfi_kyc_norms",
        "source": "AMFI Knowledge Center",
        "url": "https://www.amfiindia.com/investor/knowledge-center/kyc-norms",
        "text": """AMFI KNOWLEDGE CENTER: KNOW YOUR CUSTOMER (KYC) NORMS

WHAT IS KYC?
KYC (Know Your Customer) is a mandatory regulatory requirement for all investors in the Indian securities market. It is aimed at preventing financial fraud, money laundering, and terrorism financing.

COMPLIANCE RULES:
- Mandatory: KYC is a one-time process for all mutual fund investments.
- PAN-Based: Linked to the investor's Permanent Account Number.
- Documentation: Requires proof of identity (Aadhaar, Passport, etc.) and address.

KYC STATUSES:
- KYC Validated: Full access to all transactions across all fund houses.
- KYC Registered: Limited access; might need document re-submission for new fund houses.
- KYC On Hold: Prohibited from all transactions, including SIPs and redemptions, until deficiencies are resolved.

REASONS FOR 'ON HOLD' STATUS:
- Mobile or email not validated.
- PAN not linked with Aadhaar.
- Documents used for KYC are not 'Officially Valid Documents' (OVD)."""
    },
    {
        "doc_id": "amfi_risks_in_mf",
        "source": "AMFI Knowledge Center",
        "url": "https://www.amfiindia.com/investor/knowledge-center/risks-in-mutual-funds",
        "text": """AMFI KNOWLEDGE CENTER: RISKS IN MUTUAL FUNDS

While mutual funds offer professional management and diversification, they are subject to market risks.

CORE RISKS:
1. Market Risk: The risk that the entire market or specific sector declines, affecting the NAV.
2. Concentration Risk: Risk from investing too much in a single stock or sector.
3. Credit Risk: The risk that the issuer of a debt instrument defaults on interest or principal payments.
4. Interest Rate Risk: The risk that NAV falls when interest rates rise (primarily affecting debt funds).
5. Liquidity Risk: Risk that a security cannot be sold quickly enough to prevent a loss.
6. Fund Manager Risk: Risk that the fund manager's strategy underperforms.

DISCLAIMER: 'Mutual Fund investments are subject to market risks. Please read all scheme-related documents carefully.'"""
    }
]

def save_docs():
    print(f"Injecting {len(DOCS)} Regulatory & AMFI knowledge documents …\n")
    for doc in DOCS:
        doc["fetched_at"] = datetime.now().isoformat()
        
        out_path = OUTPUT_DIR / f"{doc['doc_id']}.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(doc, f, indent=2, ensure_ascii=False)
        print(f"✓ Saved → {out_path.name}")
    
    print(f"\n✅ Regulatory and AMFI data injected successfully.")

if __name__ == "__main__":
    save_docs()
