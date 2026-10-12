from flask import Flask, render_template, jsonify
from monitor import get_stats

app = Flask(__name__)

import socket
import os

@app.route("/")
def home():
    return render_template("index.html",
        user=os.getenv("USER", "user"),
        host=socket.gethostname(),
    )

@app.route("/api/stats")
def stats():
    return jsonify(get_stats())

if __name__ == "__main__":
    app.run(debug=os.getenv("FLASK_DEBUG") == "1", port=8000)