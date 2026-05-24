from mss import mss
from PIL import Image
import requests
import time
import base64
import io
from datetime import datetime

OLLAMA_URL = "http://192.168.0.101:11434/api/generate"
MODEL = "llava"

PROMPT = """
You are an AI gaming spectator.
Describe what is visible on screen.
Keep the answer concise and gaming-focused.
"""

with mss() as sct:
    print("BBB AI Vision Logging Started")

    while True:
        try:
            monitor = sct.monitors[1]
            screenshot = sct.grab(monitor)

            img = Image.frombytes("RGB", screenshot.size, screenshot.rgb)

            timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
            img_path = f"captures/{timestamp}.jpg"
            txt_path = f"captures/{timestamp}.txt"

            img.save(img_path)

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

            text = response.json().get("response", "")

            with open(txt_path, "w") as f:
                f.write(text)

            print(f"\n[{timestamp}]")
            print(text)

        except Exception as e:
            print("ERROR:", e)

        time.sleep(15)
