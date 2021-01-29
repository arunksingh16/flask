#!/usr/bin/env python3
# The FLASK_APP environment variable is used to specify how to load the application.
# flask is aware of static and templates folder

from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
import sqlite3
# import logging

# Logging configuration
# logging.basicConfig(filename='demo.log', level=logging.DEBUG)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'


# flask creare URL map for this
@app.route('/')
def indexroot():
    return render_template('index.html',mess="Kubernetes")
    
@app.route('/index.html')
def index():
    return render_template('index.html',mess="Kubernetes")


@app.route('/about.html')
def aboutus():
    return render_template('about.html')

@app.route('/dblinks.html')
def dblinks():
    return render_template('dblinks.html')

@app.route('/monitor.html')
def monitor():
    return render_template('monitor.html')

@app.route('/work.html')
def work():
    return render_template('work.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
