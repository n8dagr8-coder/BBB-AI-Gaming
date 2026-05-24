import requests

OLLAMA_URL = "http://192.168.0.101:11434/api/generate"

with open("highlight-report.md", "r") as f:
    report = f.read()

prompt = f"""
Based on this gaming highlight report:

{report}

Generate:
1. 5 YouTube titles
2. 5 Twitch stream titles
3. 5 TikTok clip titles

Make them exciting but not cringe.
"""

response = requests.post(
    OLLAMA_URL,
    json={
        "model": "qwen2.5-coder:7b",
        "prompt": prompt,
        "stream": False
    },
    timeout=180
)

print(response.json()["response"])
