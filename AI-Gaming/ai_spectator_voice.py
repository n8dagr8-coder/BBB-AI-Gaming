from mss import mss
from PIL import Image
import requests
import time
import base64
import io
import os

OLLAMA_URL = "http://192.168.0.101:11434/api/generate"
MODEL = "llava"

PROMPT = """
You are a premium AI gaming spectator.
Describe what is visible on screen in one short sentence.
If it is not a game, say what app or desktop is visible.
Keep it under 20 words.
"""

def speak(text):
    safe = text.replace('"', '').replace("'", "")
    os.system(f'espeak "{safe}"')

with mss() as sct:
    print("BBB AI Spectator Voice Started")
    print("Press CTRL+C to stop.")

    while True:
        try:
            monitor = sct.monitors[1]
            screenshot = sct.grab(monitor)

            img = Image.frombytes("RGB", screenshot.size, screenshot.rgb)

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
            print("\nAI:", text)

            if text:
                speak(text)

        except Exception as e:
            print("ERROR:", e)

        time.sleep(15)
