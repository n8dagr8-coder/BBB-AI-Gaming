import requests
import os

OLLAMA_URL = "http://192.168.0.101:11434/api/generate"
MODEL = "qwen2.5-coder:7b"

INPUT = "highlight-notes.md"
OUTPUT = "session-summary.md"

if not os.path.exists(INPUT):
    print("No highlight-notes.md found. Run ai_spectator_clipnotes.py first.")
    exit(1)

with open(INPUT, "r") as f:
    notes = f.read()

prompt = f"""
Summarize these AI gaming spectator notes into:
1. What happened
2. Interesting moments
3. Possible highlight clips
4. Suggested stream title
5. Suggested YouTube short title

Notes:
{notes}
"""

response = requests.post(
    OLLAMA_URL,
    json={
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    },
    timeout=180
)

summary = response.json().get("response", "")

with open(OUTPUT, "w") as f:
    f.write(summary)

print(summary)
print(f"\nSaved to {OUTPUT}")
