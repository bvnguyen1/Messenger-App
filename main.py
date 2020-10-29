from threading import Thread
import json
from flask_socketio import SocketIO, send, emit, namespace
from flask import Flask, render_template, request, session, flash, redirect, url_for, Blueprint, jsonify

app = Flask(__name__, instance_relative_config=False)
app.secret_key = "thisismysecretkey"
socketio = SocketIO(app)

NAME_KEY = 'name'


client_list = []


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        name = request.form["clientName"]
        if len(name) > 1:   # add name to session
            session[NAME_KEY] = request.form["clientName"]
            return redirect(url_for("home"))
    return render_template("register.html")


@app.route("/logout")
def logout():
    # Pop NAME_KEY out of seesion after log out
    session.pop(NAME_KEY, None)
    flash("0You were logged out.")
    return redirect(url_for("logout.html"))


@app.route("/")
@app.route("/home", methods=["POST", "GET"])
def home():
    if NAME_KEY not in session:
        return redirect(url_for("register"))
    return render_template("index.html")


# This function will return the name in Session as json
@app.route("/get_name")
def get_name():
    if NAME_KEY in session:
        clientName = {"name": session[NAME_KEY]}
        return jsonify(clientName)
    return "none"


@socketio.on('my event')
def handle_messages(data):
    print(data)
    emit('message_response', data, broadcast=True)


if __name__ == '__main__':
    socketio.run(app, host='192.168.0.109', port=5000, debug=True)
