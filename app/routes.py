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


@app.route('/project')
def upload_form():
    relevantpics = ImageHandle.getPics()
    pics = [Constants.STATICDIR + x for x in relevantpics]
    print(pics)
    return render_template('project_page.html',pics = pics)


@app.route('/project', methods=['POST'])
def upload_image():
    if request.method == "POST" and request.files:
        image = request.files["image"]
        ImageHandle.save_img(image)
        return redirect(request.url)

    return render_template("project_page.html")


@app.route('/browse')
def view_projects():
    obj = DbManager()
    data = obj.select('Research', Constants.STATICDIR)
    print(data)
    return render_template('catalog.html', projects = data)


@app.route('/add')
def addition1():
    return render_template('add.html')


@app.route('/add', methods=['POST'])
def addition():
    if request.method == 'POST':
        result = request.form
    names = list(result.keys())
    values = list(result.values())

    obj = DbManager()
    table = "Research"
    cols = names
    vals = values
    vals[-1] = obj.last_entry(table, "ResearchID") + 1
    print(cols, vals)
    obj.insert(table, cols, vals)
    return redirect(request.url)


@app.route('/display/<filename>')
def display_image(filename):
    # print('display_image filename: ' + filename)
    # dbconnect = DbManager()
    # table = "Research"
    # col = ["ResearchTitle", "Category"]
    # result = dbconnect.select(table, col)
    fn = Constants.UPLOAD_FOLDER + filename
    print(fn)
    return redirect(url_for('static', filename=fn), code=301)


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
