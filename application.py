import os
import requests
from flask import Flask, session,render_template, redirect, url_for, request

# Configure app
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/councils")
def councils():
    return render_template('councils.html')

@app.route("/timeline")
def timeline():
    return render_template('timeline.html')

@app.route("/resources")
def resources():
    return render_template('resources.html')

@app.route("/secretariat")
def secretariat():
    return render_template('secretariat.html')

@app.route("/faq")
def faq():
    return render_template('faq.html')


if __name__ == '__main__':
    app.run(debug=True)
