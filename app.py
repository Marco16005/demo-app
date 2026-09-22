import os
from flask import Flask, jsonify

app = Flask(__name__)
VERSION = os.getenv("APP_VERSION", "local")

@app.get("/")
def home():
    return jsonify(message="Hola desde Harness", version=VERSION)

@app.get("/health")
def health():
    return jsonify(status="ok")