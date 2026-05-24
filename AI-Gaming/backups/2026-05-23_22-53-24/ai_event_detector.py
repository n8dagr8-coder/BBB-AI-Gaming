import os
import time

WATCH_DIR = "spectator-logs"

seen = set()

print("BBB AI Event Detector Started")

while True:
    files = sorted(os.listdir(WATCH_DIR))

    for file in files:
        if file.endswith(".txt") and file not in seen:
            seen.add(file)

            path = os.path.join(WATCH_DIR, file)

            with open(path, "r") as f:
                text = f.read().lower()

            triggers = [
                "enemy",
                "weapon",
                "kill",
                "victory",
                "battle",
                "combat",
                "gun",
                "explosion",
                "fire",
                "player"
            ]

            for trigger in triggers:
                if trigger in text:
                    print("")
                    print("=== POSSIBLE HIGHLIGHT DETECTED ===")
                    print(file)
                    print(text)
                    print("")
                    break

    time.sleep(5)
