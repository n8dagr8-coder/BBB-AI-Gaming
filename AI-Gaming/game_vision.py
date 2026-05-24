from mss import mss
from PIL import Image
import requests
import time
import base64
import io

OLLAMA_URL = "http://192.168.0.101:11434/api/generate"
MODEL = "llava"

PROMPT = """
You are an AI gaming spectator.
Describe what is visible on screen.
If it looks like a desktop or terminal, say that.
If it looks like a game, describe gameplay-relevant details.
Keep the answer short.
"""

with mss() as sct:
    print("BBB AI Gaming Vision started.")
    print("Capturing screen every 10 seconds.")
    print("Press CTRL+C to stop.")

    while True:
        try:
            monitor = sct.monitors[1]
            screenshot = sct.grab(monitor)

            img = Image.frombytes("RGB", screenshot.size, screenshot.rgb)

            buffer = io.BytesIO()
            img.save(buffer, format="JPEG", quality=80)
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

            print("\n=== AI RESPONSE ===")

            if response.status_code != 200:
                print("HTTP ERROR:", response.status_code)
                print(response.text[:1000])
            else:
                data = response.json()
                print(data.get("response", "No response field returned."))

        except Exception as e:
            print("\n=== ERROR ===")
            print(e)

        time.sleep(10)
