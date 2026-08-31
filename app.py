import os
from flask import Flask, jsonify, render_template, request

from jarvis_core import JarvisCore

app = Flask(__name__)
jarvis = JarvisCore()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/status")
def status():
    return jsonify(jarvis.get_status_summary())


@app.route("/api/command", methods=["POST"])
def command():
    payload = request.get_json(silent=True) or {}
    text = payload.get("command") or payload.get("text") or ""
    response = jarvis.handle_command(text)
    return jsonify(response)


@app.route("/api/voice", methods=["POST"])
def voice():
    payload = request.get_json(silent=True) or {}
    text = payload.get("text") or ""
    return jsonify(jarvis.speak(text))


@app.route("/api/health")
def health():
    return jsonify({"status": "ok", "name": jarvis.name})


if __name__ == "__main__":
    host = os.environ.get("HOST", "0.0.0.0")
    port = int(os.environ.get("PORT", "5000"))
    app.run(host=host, port=port, debug=True)
