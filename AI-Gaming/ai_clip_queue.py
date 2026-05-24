import os
import shutil
import time

SOURCE = "spectator-logs"
QUEUE = "highlight-queue"

os.makedirs(QUEUE, exist_ok=True)

keywords = [
    "enemy",
    "kill",
    "combat",
    "explosion",
    "battle",
    "victory",
    "weapon",
    "firefight"
]

seen = set()

print("BBB AI Clip Queue Started")

while True:
    files = os.listdir(SOURCE)

    for file in files:
        if file.endswith(".txt") and file not in seen:
            seen.add(file)

            txt_path = os.path.join(SOURCE, file)

            with open(txt_path, "r") as f:
                text = f.read().lower()

            if any(word in text for word in keywords):
                base = file.replace(".txt", "")

                jpg = f"{base}.jpg"

                jpg_src = os.path.join(SOURCE, jpg)
                jpg_dst = os.path.join(QUEUE, jpg)

                txt_dst = os.path.join(QUEUE, file)

                if os.path.exists(jpg_src):
                    shutil.copy2(jpg_src, jpg_dst)

                shutil.copy2(txt_path, txt_dst)

                print("")
                print("=== CLIP CANDIDATE ===")
                print(file)
                print(text)
                print("")

    time.sleep(5)
