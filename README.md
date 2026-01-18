
# CognitiveTrap – AI Deception & Manipulation Detection Framework

CognitiveTrap detects psychological manipulation patterns used in phishing, scams, and AI-generated persuasion attacks.

## Features
- Detects urgency, authority, fear, and reward manipulation
- Risk scoring with explainable indicators
- Ethical, defensive cybersecurity project

## Run
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

POST to `/analyze` with JSON `{ "text": "your message" }`
