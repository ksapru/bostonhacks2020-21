import users as users

from dbconnect import session


def user(username, password):
    pass


users.append(user(username ='Anthony', password ='password'))
users.append(user(username ='bob', password ='password'))
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


@app.route('/login', methods = ['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid credentials. Please try again'
        else:
            session['logged_in'] = True
            return redirect(url_for('home'))
    return render_template(('login.html', None)


@app.route('/logout()')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('welcome.'))
