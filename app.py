from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/images")
def images():
    return render_template("images.html")