from flask import Flask, request, redirect
from flask import render_template
from flask_bootstrap import Bootstrap

import eso_crow


app = Flask(__name__)

bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/updates')
def updates():
    return render_template('updates.html')


@app.route('/tip')
def tip():
    return render_template('tip.html')


@app.route('/faq')
def faq():
    return render_template('faq.html')


@app.route('/<source>/<target>')
def dijkstra(source, target):
    result = eso_crow.dijkstra(source, target)

    if isinstance(result, list):
        return render_template('dijkstra.html', pairs_list=result)

    else:
        return render_template('dijkstra.html', error_message=result)


@app.route('/handle_data', methods=['POST'])
def handle_data():
    source = request.form['source']
    target = request.form['destination']
    print(source)
    print(target)

    if len(source) > 0 and len(target) > 0:
        url = redirect('/' + source + '/' + target)
    else:
        url = redirect('/')
    return url
