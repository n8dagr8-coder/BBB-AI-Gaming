from flask import Flask
import os

app = Flask(__name__)

LOG_DIR = "spectator-logs"

@app.route("/")
def home():
    files = sorted(os.listdir(LOG_DIR), reverse=True)[:20]

    html = """
    <html>
    <head>
        <title>BBB AI Spectator</title>
        <style>
            body {
                background:#111;
                color:#eee;
                font-family:Arial;
                padding:20px;
            }
            .entry {
                border:1px solid #333;
                margin-bottom:20px;
                padding:15px;
                background:#1b1b1b;
            }
            img {
                width:500px;
                border-radius:10px;
            }
            pre {
                white-space:pre-wrap;
                color:#7df9ff;
            }
        </style>
    </head>
    <body>
        <h1>BBB AI Spectator Dashboard</h1>
    """

    for file in files:
        if file.endswith(".txt"):
            txt_path = os.path.join(LOG_DIR, file)
            img_path = file.replace(".txt", ".jpg")

            with open(txt_path, "r") as f:
                text = f.read()

            html += f"""
            <div class='entry'>
                <h3>{file}</h3>
                <img src='/logs/{img_path}'><br><br>
                <pre>{text}</pre>
            </div>
            """

    html += "</body></html>"

    return html

@app.route("/logs/<path:filename>")
def logs(filename):
    from flask import send_from_directory
    return send_from_directory(LOG_DIR, filename)

app.run(host="0.0.0.0", port=5090)
