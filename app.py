from flask import Flask, request, redirect, url_for
from flask import render_template
from markupsafe import escape
from flask_bootstrap import Bootstrap

import hello
import eso_crow


app = Flask(__name__)

bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/tip')
def tip():
    return render_template('tip.html')


@app.route('/bootstrap')
def bootstrap():
    return render_template('bootstrap.html')


@app.route('/<source>/<target>')
def dijkstra(source, target):
    result = eso_crow.dijkstra(source, target)

    if type(result) == list:
        return render_template('dijkstra.html', pairs_list=result)

    else:
        return render_template('dijkstra.html', error_message=result)


@app.route('/handle_data', methods=['POST'])
def handle_data():
    source = request.form['source']
    target = request.form['destination']
    return redirect('/' + source + '/' + target)
