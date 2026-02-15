from flask import Flask, request, jsonify
import os

app = Flask(__name__)

SECRET = os.environ.get("TV_SECRET")

@app.route("/")
def home():
    return "TV Webhook Bridge running"

@app.route("/tv", methods=["POST"])
def webhook():
    data = request.json
    
    if not data:
        return jsonify({"error": "No JSON"}), 400
    
    if data.get("secret") != SECRET:
        return jsonify({"error": "Unauthorized"}), 403
    
    print("Signal received:", data)
    
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
