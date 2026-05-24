import requests
from datetime import datetime

OLLAMA_URL = "http://192.168.0.101:11434/api/generate"

with open("highlight-report.md", "r") as f:
    report = f.read()

prompt = f"""
Create a full content pack from this gaming highlight report:

{report}

Output:
1. Best YouTube title
2. YouTube description
3. 10 hashtags
4. TikTok caption
5. Twitch stream recap
6. Thumbnail text ideas
7. 3 short promo blurbs
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

content = response.json()["response"]

filename = f"content-pack-{datetime.now().strftime('%Y-%m-%d_%H-%M')}.md"

with open(filename, "w") as f:
    f.write(content)

print(content)
print(f"\nSaved to {filename}")
