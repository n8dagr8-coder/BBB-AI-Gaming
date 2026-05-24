import os
from datetime import datetime

QUEUE = "highlight-queue"
OUT = "highlight-report.md"

scores = {
    "enemy": 1,
    "combat": 2,
    "kill": 5,
    "victory": 8,
    "explosion": 3,
    "battle": 2,
    "weapon": 1,
    "fire": 1
}

results = []

for file in os.listdir(QUEUE):
    if file.endswith(".txt"):
        path = os.path.join(QUEUE, file)

        with open(path, "r") as f:
            text = f.read().strip()

        score = 0
        lower = text.lower()

        for word, value in scores.items():
            if word in lower:
                score += value

        results.append((score, file, text))

results.sort(reverse=True)

with open(OUT, "w") as out:
    out.write("# BBB AI Highlight Report\n\n")
    out.write(f"Generated: {datetime.now()}\n\n")

    for score, file, text in results:
        out.write(f"## HYPE {score} — {file}\n\n")
        out.write(text + "\n\n")

print(f"Created {OUT}")
