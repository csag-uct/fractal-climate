from flask import Flask
from flask import render_template



app = Flask(__name__)



@app.route('/static/<path>')
def serve_static(path):
	return open('static/{}'.format(path)).read()


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/map/<shortname>')
def map(shortname):
	