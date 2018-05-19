from flask import Flask, render_template, flash, redirect, url_for
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


@app.route("/article")
def article():
    return render_template('article.html')


#This method displays the 16px x 16px icon in the browser tab
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


#Runs the server
#Remove debug=True when deploying to gcloud
app.run(host='0.0.0.0', port=8080, debug=True)
