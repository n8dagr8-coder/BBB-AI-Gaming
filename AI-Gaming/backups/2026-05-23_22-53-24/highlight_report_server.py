from flask import Flask
import os

app = Flask(__name__)

REPORT = "highlight-report.md"

@app.route("/")
def home():
    if not os.path.exists(REPORT):
        content = "No highlight report yet."
    else:
        with open(REPORT, "r") as f:
            content = f.read()

    html = f"""
    <html>
    <head>
      <title>BBB Highlight Report</title>
      <style>
        body {{ background:#101010; color:#eee; font-family:Arial; padding:30px; }}
        h1 {{ color:#7df9ff; }}
        pre {{ white-space:pre-wrap; background:#1b1b1b; padding:20px; border-radius:12px; border:1px solid #333; }}
      </style>
    </head>
    <body>
      <h1>BBB AI Highlight Report</h1>
      <pre>{content}</pre>
    </body>
    </html>
    """
    return html

app.run(host="0.0.0.0", port=5093)
