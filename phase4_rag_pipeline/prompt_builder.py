"""
Phase 4 — Prompt Builder
=========================
Assembles the final prompt sent to the LLM by combining:
  - A strict system instruction
  - Retrieved context chunks with source URLs
  - The user's question

Also includes guardrails to block investment-advice queries.
"""

import re
import logging

logger = logging.getLogger(__name__)

# ── Guardrail Patterns ────────────────────────────────────────────────────────

BLOCKED_PATTERNS: list[str] = [
    r"should i invest",
    r"is it good to (buy|invest)",
    r"will (it|the fund|nav) (go up|rise|fall|drop)",
    r"recommend(ation)? (me|for me)",
    r"best fund for me",
    r"should i (sell|switch|redeem)",
    r"which is better",
    r"predict",
    r"give me (your )?opinion",
    r"what do you think",
    r"suggest (me )?a? ?(fund|scheme)",
    r"can i make money",
    r"will i (get|earn|lose)",
]

OPINION_REFUSAL = (
    "I'm designed to answer **factual questions** about SBI Mutual Fund schemes "
    "using only official public information from SBI AMC, SEBI, and AMFI.\n\n"
    "I'm **unable to provide investment advice or personal recommendations**. "
    "For personalised guidance, please consult a SEBI-registered financial advisor or "
    "visit [SEBI Investor Education](https://www.sebi.gov.in)."
)

INSUFFICIENT_INFO = (
    "I don't have enough information from official sources (SBI AMC, SEBI, AMFI) "
    "to answer this question accurately. Please check "
    "[sbimf.com](https://www.sbimf.com), "
    "[sebi.gov.in](https://www.sebi.gov.in), or "
    "[amfiindia.com](https://www.amfiindia.com) directly."
)

# ── System Prompt ─────────────────────────────────────────────────────────────

SYSTEM_PROMPT = """You are a knowledgeable and helpful assistant for the INDMoney platform, specialising in SBI Mutual Fund information for Indian retail investors.

STRICT RULES — follow every rule without exception:
1. Answer ONLY using the information in the CONTEXT below. Do NOT use any outside knowledge.
2. Keep your answer to a MAXIMUM of 3 clear, concise sentences.
3. You MUST include exactly one citation link from the CONTEXT sources in your answer.
   Format: [Source Name](URL)  e.g. [INDmoney Portal](https://www.indmoney.com/mutual-funds/sbi-small-cap-fund)
4. Do NOT give investment advice, personal recommendations, or return predictions.
5. Do NOT express opinions or say things like "I recommend" or "you should".
6. If the provided context contains PARTIAL information, use what is available to give the best factual answer.
7. Treat all information in the CONTEXT (from SBI AMC, AMFI, SEBI, and INDmoney) as the single source of truth.
8. Only say "I don't have enough information from official sources to answer this accurately" if the context has ZERO relevant information about the question.
9. Be specific and direct — investors want clear, factual answers."""


# ── Public API ────────────────────────────────────────────────────────────────

def check_guardrails(question: str) -> tuple[bool, str]:
    """
    Check whether the question violates guardrails.

    Returns:
        (is_allowed: bool, refusal_message: str)
        If is_allowed is True, refusal_message is empty.
    """
    q_lower = question.lower().strip()
    for pattern in BLOCKED_PATTERNS:
        if re.search(pattern, q_lower):
            logger.info(f"Guardrail triggered for pattern: '{pattern}'")
            return False, OPINION_REFUSAL
    return True, ""


def build_prompt(question: str, chunks: list[dict]) -> str:
    """
    Assemble the full LLM prompt from retrieved chunks and the user question.

    Args:
        question: The user's factual question.
        chunks:   List of retrieved chunk dicts (from retriever.py).

    Returns:
        A fully-formed prompt string ready to send to the LLM.
    """
    if not chunks:
        logger.warning("No chunks provided — using insufficient-info fallback.")
        return _fallback_prompt(question)

    context_blocks = []
    for i, chunk in enumerate(chunks, 1):
        block = (
            f"[Context {i}]\n"
            f"Source: {chunk['source']}\n"
            f"URL: {chunk['url']}\n"
            f"Text: {chunk['text']}"
        )
        context_blocks.append(block)

    context_section = "\n\n".join(context_blocks)

    prompt = (
        f"{SYSTEM_PROMPT}\n\n"
        f"{'='*60}\n"
        f"CONTEXT:\n\n{context_section}\n\n"
        f"{'='*60}\n"
        f"USER QUESTION: {question}\n\n"
        f"ANSWER (max 3 sentences, include one citation link):"
    )
    return prompt


def _fallback_prompt(question: str) -> str:
    """Return a prompt that will produce the insufficient-info message."""
    return (
        f"{SYSTEM_PROMPT}\n\n"
        f"CONTEXT:\n(No relevant official information was found)\n\n"
        f"USER QUESTION: {question}\n\n"
        f"ANSWER:"
    )


# ── Entry Point (smoke test) ──────────────────────────────────────────────────
if __name__ == "__main__":
    sample_chunks = [
        {
            "source": "SBI AMC",
            "url":    "https://www.sbimf.com/en-us/sbi-bluechip-fund",
            "text":   "SBI Blue Chip Fund is an open-ended equity scheme predominantly "
                      "investing in large-cap stocks. The expense ratio (Regular Plan) "
                      "is 1.73% per annum as of the latest factsheet.",
        }
    ]

    # Test allowed question
    q = "What is the expense ratio of SBI Blue Chip Fund?"
    allowed, refusal = check_guardrails(q)
    if allowed:
        prompt = build_prompt(q, sample_chunks)
        print("=== ALLOWED QUESTION — PROMPT ===")
        print(prompt)
    else:
        print("=== BLOCKED ===")
        print(refusal)

    # Test blocked question
    q2 = "Should I invest in SBI Blue Chip Fund now?"
    allowed2, refusal2 = check_guardrails(q2)
    print("\n=== BLOCKED QUESTION — REFUSAL ===")
    print(refusal2 if not allowed2 else "Allowed (unexpected)")
