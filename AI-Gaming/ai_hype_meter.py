import os
import time

WATCH = "highlight-queue"

scores = {
    "enemy": 1,
    "combat": 2,
    "kill": 4,
    "victory": 6,
    "explosion": 3,
    "weapon": 1,
    "battle": 2,
    "fire": 1
}

seen = set()

print("BBB AI Hype Meter Started")

while True:
    total_score = 0

    files = os.listdir(WATCH)

    for file in files:
        if file.endswith(".txt") and file not in seen:
            seen.add(file)

            with open(os.path.join(WATCH, file), "r") as f:
                text = f.read().lower()

            score = 0

            for word, value in scores.items():
                if word in text:
                    score += value

            print("")
            print("==== HYPE EVENT ====")
            print(file)
            print("Score:", score)
            print(text)

            total_score += score

    if total_score > 0:
        print("")
        print("CURRENT SESSION HYPE:", total_score)
        print("")

    time.sleep(5)
