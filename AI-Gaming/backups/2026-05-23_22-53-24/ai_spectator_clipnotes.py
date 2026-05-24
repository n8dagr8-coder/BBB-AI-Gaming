import os
from datetime import datetime

LOG_DIR = "spectator-logs"
OUT = "highlight-notes.md"

files = sorted([f for f in os.listdir(LOG_DIR) if f.endswith(".txt")])

with open(OUT, "w") as out:
    out.write("# BBB AI Gaming Highlight Notes\n\n")

    for file in files[-50:]:
        path = os.path.join(LOG_DIR, file)
        with open(path, "r") as f:
            text = f.read().strip()

        if text:
            out.write(f"## {file}\n")
            out.write(text + "\n\n")

print(f"Created {OUT}")
