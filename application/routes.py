from application.app import app
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from flask import flash

@app.route("/")
def homepage():
    return render_template("homepage.html")
