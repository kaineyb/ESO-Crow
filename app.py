from flask import Flask
from flask import render_template
from markupsafe import escape

import hello
import eso_crow

app = Flask(__name__)


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/')
def index():
    return 'Index'


@ app.route('/crow/<source>/<target>')
def dijkstra(source, target):
    result = eso_crow.dijkstra(source, target)

    if type(result) == list:
        return render_template('dijkstra.html', pairs_list=result)

    else:
        return render_template('dijkstra.html', error_message=result)
