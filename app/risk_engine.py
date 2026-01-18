
import re
def calculate_risk(text: str) -> int:
    score = 0

    red_flags = [
        "urgent",
        "act now",
        "verify immediately",
        "account suspended",
        "click here"
    ]

    for flag in red_flags:
        if flag.lower() in text.lower():
            score += 20

    return min(score, 100)

