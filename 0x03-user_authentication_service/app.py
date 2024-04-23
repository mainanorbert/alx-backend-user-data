#!/usr/bin/env python3
"""flask app"""

from flask import Flask, jsonify, request, redirect, abort
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


@app.route('/sessions', methods=['POST'])
def login():
    """login route"""
    email: str = request.form.get('email')
    password: str = request.form.get('password')
    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        res = jsonify({"email": f"{email}", "message": "logged in"})
        res.set_cookie("session_id", session_id)
        return res, 200
    else:
        abort(401)


@app.route('/sessions', methods=['DELETE'])
def logging_out() -> str:
    """deleting user"""
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user is None:
        abort(403)
    AUTH.destroy_session(user.id)
    return redirect('/')


@app.route('/profile', methods=['GET'])
def profile():
    """user profile"""
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        return jsonify({"email": user.email}), 200
    abort(403)


@app.route('/reset_password', methods=['POST'])
def get_reset_password_token():
    """Get reset password token"""
    email = request.form.get('email')
    try:
        user = AUTH.find_user_by(email=email)
        return jsonify({"email": user.email,
                       "reset_token": AUTH.get_reset_password_token})
    except ResultNotFound:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
