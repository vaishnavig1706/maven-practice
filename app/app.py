from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Azure AKS!"

@app.route("/health")
def health():
    return "OK"

@app.route("/secret")
def secret():
    return os.getenv("APP_SECRET", "Secret not configured")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
