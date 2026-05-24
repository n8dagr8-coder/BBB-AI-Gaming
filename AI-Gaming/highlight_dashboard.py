from flask import Flask, send_from_directory
import os

app = Flask(__name__)

QUEUE = "highlight-queue"

@app.route("/")
def home():
    os.makedirs(QUEUE, exist_ok=True)

    files = sorted(os.listdir(QUEUE), reverse=True)

    html = """
    <html>
    <head>
      <title>BBB Highlight Queue</title>
      <style>
        body { background:#101010; color:#eee; font-family:Arial; padding:30px; }
        h1 { color:#7df9ff; }
        .card { background:#1b1b1b; border:1px solid #333; border-radius:12px; padding:20px; margin:20px 0; }
        img { width:520px; border-radius:10px; border:1px solid #444; }
        pre { white-space:pre-wrap; color:#9ee7ff; font-size:16px; }
      </style>
    </head>
    <body>
    <h1>BBB AI Highlight Queue</h1>
    """

    for file in files:
        if file.endswith(".txt"):
            txt_path = os.path.join(QUEUE, file)
            img_file = file.replace(".txt", ".jpg")

            with open(txt_path, "r") as f:
                text = f.read()

            html += f"""
            <div class="card">
              <h2>{file}</h2>
              <img src="/queue/{img_file}">
              <pre>{text}</pre>
            </div>
            """

    html += "</body></html>"
    return html

@app.route("/queue/<path:filename>")
def queue_file(filename):
    return send_from_directory(QUEUE, filename)

app.run(host="0.0.0.0", port=5092)
