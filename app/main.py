from fastapi import FastAPI
from app.analyzer import analyze_text
from app.models import TextInput

app = FastAPI(title="CognitiveTrap - AI Deception Detector")

@app.post("/analyze")
def analyze(input: TextInput):
    return analyze_text(input.text)
