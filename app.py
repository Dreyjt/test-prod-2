from flask import Flask, jsonify
from database import get_users
import os


app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "live Website on blue green deployment",
        "environment": os.getenv("ENVIRONMENT", "production")
    })


@app.route("/users")
def users():
    return jsonify(get_users())


@app.route("/health")
def health():
    return jsonify({"status": "OK"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
