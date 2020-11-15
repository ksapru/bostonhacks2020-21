import os
from app import app
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

from config import Constants
from app.ImageHandling import ImageHandle
from app.dbManager import DbManager


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/picture')
def upload_form():
    return render_template('upload.html')


@app.route('/picture', methods=['POST'])
def upload_image():
    if request.method == "POST" and request.files:
        image = request.files["image"]
        ImageHandle.save_img(image)
        return redirect(request.url)

    return render_template("upload.html")


@app.route('/display/<filename>')
def display_image(filename):
    # print('display_image filename: ' + filename)
    dbconnect = DbManager()
    table = "Research"
    col = ["ResearchTitle","Category"]
    result =dbconnect.select(table,col)
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


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    # if request.method == 'POST':
    #     if request.form['username'] != 'admin' or request.form['password'] != 'admin':
    #         error = 'Invalid credentials. Please try again'
    #     else:
    #         session['logged_in'] = True
    #         return redirect(url_for('home'))
    return render_template(('login.html'))


@app.route('/welcome')
def welcome():
    return render_template('login.html')
