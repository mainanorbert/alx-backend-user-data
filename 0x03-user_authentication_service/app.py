#!/usr/bin/env python3
"""flask app"""

from flask import Flask, jsonify, request
from auth import Auth

AUTH = Auth()

app = Flask(__name__)


@app.route('/')
def welcome():
    """returns json message"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users():
    """registering a user"""
    try:
        email = request.form.get('email')
        passwd = request.form.get('password')
        AUTH.register_user(email, passwd)
        return jsonify({"email": email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
