from flask import Flask, render_template, request, jsonify
import json, os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET")
ADMIN_TOKEN = os.getenv("ADMIN_TOKEN")

MESSAGES_FILE = 'messages.json'

def load_messages():
    if not os.path.exists(MESSAGES_FILE):
        with open(MESSAGES_FILE, 'w') as f:
            json.dump([], f)
    with open(MESSAGES_FILE, 'r') as f:
        return json.load(f)

def save_message(msg):
    messages = load_messages()
    messages.append(msg)
    with open(MESSAGES_FILE, 'w') as f:
        json.dump(messages, f, indent=2)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/contact", methods=["POST"])
def contact():
    data = request.get_json()
    required = ["name", "email", "subject", "message"]
    if not all(field in data and data[field] for field in required):
        return jsonify({"success": False, "error": "All fields are required."})
    save_message(data)
    return jsonify({"success": True, "message": "Message sent!"})

@app.route("/admin/messages")
def admin_messages():
    token = request.args.get("token", "")
    if token != ADMIN_TOKEN:
        return "Access denied", 403
    messages = load_messages()
    return render_template("admin_messages.html", messages=messages)

if __name__ == "__main__":
    app.run(debug=True)
