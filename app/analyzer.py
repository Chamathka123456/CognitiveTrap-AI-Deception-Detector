from app.risk_engine import calculate_risk
def analyze_text(text: str) -> dict:
    risk = calculate_risk(text)

    return {
        "input": text,
        "risk_score": risk,
        "verdict": "High Risk" if risk >= 60 else "Low Risk"
    }
