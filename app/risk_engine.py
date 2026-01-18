
import re

def score_risk(text: str):
    indicators = {
        "urgency": len(re.findall(r"(urgent|immediately|now)", text.lower())),
        "authority": bool(re.findall(r"(admin|security team|bank)", text.lower())),
        "fear": bool(re.findall(r"(suspend|breach|compromised)", text.lower())),
        "reward": bool(re.findall(r"(win|free|reward)", text.lower()))
    }

    risk_score = sum([v if isinstance(v, int) else int(v) for v in indicators.values()])

    return {
        "indicators": indicators,
        "risk_score": risk_score,
        "risk_level": "HIGH" if risk_score > 2 else "MEDIUM" if risk_score == 2 else "LOW"
    }
