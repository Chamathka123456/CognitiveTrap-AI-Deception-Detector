
from fastapi import FastAPI
from analyzer import analyze_text

app = FastAPI(title="CognitiveTrap - AI Deception Detector")

@app.post("/analyze")
def analyze(payload: dict):
    text = payload.get("text", "")
    return analyze_text(text)
