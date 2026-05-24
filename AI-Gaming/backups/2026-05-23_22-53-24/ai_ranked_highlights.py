import os

QUEUE = "highlight-queue"

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
            text = f.read().lower()

        score = 0

        for word, value in scores.items():
            if word in text:
                score += value

        results.append((score, file, text))

results.sort(reverse=True)

print("")
print("===== BBB AI RANKED HIGHLIGHTS =====")
print("")

for score, file, text in results:
    print(f"[HYPE {score}] {file}")
    print(text)
    print("")
