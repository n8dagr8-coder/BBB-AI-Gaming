from mss import mss
from PIL import Image
import requests
import time
import base64
import io
import os
from datetime import datetime

OLLAMA_URL = "http://192.168.0.101:11434/api/generate"
MODEL = "llava"
LOG_DIR = "spectator-logs"

os.makedirs(LOG_DIR, exist_ok=True)

PROMPT = """
You are a premium AI gaming spectator.
Describe what is visible on screen in one short useful sentence.
If it is a game, mention gameplay-relevant details.
If it is not a game, mention the visible app or desktop.
Keep it under 20 words.
"""

def speak(text):
    safe = text.replace('"', '').replace("'", "")
    os.system(f'espeak "{safe}"')

with mss() as sct:
    print("BBB AI Spectator Logger Started")
    print("Press CTRL+C to stop.")

    while True:
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

            monitor = sct.monitors[1]
            screenshot = sct.grab(monitor)

            img = Image.frombytes("RGB", screenshot.size, screenshot.rgb)
            img_path = f"{LOG_DIR}/{timestamp}.jpg"
            txt_path = f"{LOG_DIR}/{timestamp}.txt"

            img.save(img_path)

            buffer = io.BytesIO()
            img.save(buffer, format="JPEG", quality=75)
            img_b64 = base64.b64encode(buffer.getvalue()).decode("utf-8")

            response = requests.post(
                OLLAMA_URL,
                json={
                    "model": MODEL,
                    "prompt": PROMPT,
                    "images": [img_b64],
                    "stream": False
                },
                timeout=120
            )

            text = response.json().get("response", "").strip()

            with open(txt_path, "w") as f:
                f.write(text)

            print(f"\n[{timestamp}] AI: {text}")

            if text:
                speak(text)

        except Exception as e:
            print("ERROR:", e)

        time.sleep(20)
