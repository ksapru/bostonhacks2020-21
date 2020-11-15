import os
from flask import render_template
from app import app
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

from config import Constants
from app.ImageHandling import ImageHandle


@app.route("/")
def hello():
    return "Hello, World!"


@app.route('/picture')
def upload_form():
    return render_template('upload.html')


@app.route('/picture', methods=['POST'])
def upload_image():
    if request.method == "POST":

        if request.files:

            image = request.files["image"]

            if image.filename == "":
                print("No filename")
                return redirect(request.url)

            if ImageHandle.allowed_image(image.filename):
                filename = secure_filename(image.filename)

                os.chdir(Constants.UPLOAD_FOLDER)
                image.save(os.path.join(Constants.UPLOAD_FOLDER, filename))
                os.chdir(Constants.BASEDIR)

                print("Image saved")

                return redirect(request.url)

            else:
                print("That file extension is not allowed")
                return redirect(request.url)

    return render_template("upload.html")


@app.route('/display/<filename>')
def display_image(filename):
    # print('display_image filename: ' + filename)
    return redirect(url_for('static', filename='uploads/' + filename), code=301)

def login_required(f):
    pass
    # @wraps(f)
    # def wrap(*args, **kwargs):
    #     if 'logged_in' in session:
    #         return f(*args,**kwargs)
    #     else:
    #         flash('You need to login first')
    #         return redirect(url_for('login'))
    #     return wrap

@app.route('/')
@login_required

def home():

    return render_template('index.html')

@app.route('/welcome')
def welcome():
    return render_template('login.html')


@app.route('/login', methods = ['GET','POST'])
def login():
    error = None
    # if request.method == 'POST':
    #     if request.form['username'] != 'admin' or request.form['password'] != 'admin':
    #         error = 'Invalid credentials. Please try again'
    #     else:
    #         session['logged_in'] = True
    #         return redirect(url_for('home'))
    return render_template(('login.html'))


