#!/usr/bin/env python3
# The FLASK_APP environment variable is used to specify how to load the application.
# flask is aware of static and templates folder

from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
import configparser
import sqlite3
import requests

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

@app.route('/weather.html')
def weather():
    return render_template('weather.html')

@app.route('/post.html',methods=['POST'])
def post():
    city = request.form['city']
    API_KEY = 'ce619ba6ee4b5979b052381875ebe756'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={API_KEY}'
    response = requests.get(url).json()
    current_temperature = response.get('main', {}).get('temp')
    if current_temperature:
        current_temperature_celsius = round(current_temperature - 273.15, 2)
        return render_template('post.html',city=city.title(),temperature=current_temperature_celsius)
        
    else:
        return render_template('post.html',mess="Something is wrong")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    # app.run(host,port,debug,options)

