from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route("/")
def home():
    return send_from_directory("web", "index.html")

@app.route("/summary")
def summary():
    if os.path.exists("session-summary.md"):
        with open("session-summary.md", "r") as f:
            return f.read()
    return "No session summary yet."

app.run(host="0.0.0.0", port=5091)
