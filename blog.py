from flask import Flask, render_template, flash, redirect, url_for, send_from_directory
from config import Config
import os

app = Flask(__name__)
app.config.from_object(Config)

#This method is called when a request is made to peterasmuth.com/
@app.route("/")
@app.route("/home")
def home():
    return render_template('front_page.html')


@app.route("/projects")
def projects():
    return render_template('front_page.html')


@app.route("/data_tree_one")
def data_tree_one():
    return render_template('data_tree_one.html')


@app.route("/data_tree_two")
def data_tree_two():
    return render_template('data_tree_two.html')


@app.route("/jsonsample")
def jsonsample():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'jsonsample.json')


@app.route("/geolookupsample")
def geolookupsample():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'geolookupsample.json')


#This method displays the 16px x 16px icon in the browser tab
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


#Runs the server
#Remove debug=True when deploying to gcloud
app.run(host='0.0.0.0', port=8080, debug=True)
