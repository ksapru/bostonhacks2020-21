from flask import Flask
from config import Constants


app = Flask(__name__)

app.secret_key = "secret key"

app.config['MAX_CONTENT_LENGTH'] = 2160 * 2160 * 2
