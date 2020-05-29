import string

from flask import Flask, request, redirect
from flask import render_template
from flask_bootstrap import Bootstrap


# My stuff:
import eso_crow
import locations


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


@app.route('/<node>')
def node_page(node):
    result = eso_crow.get_node_routes(node)

    node = string.capwords(node)

    node = eso_crow.is_stros_mkai(node)

    if isinstance(result, dict):
        return render_template('node.html', node=node, edges=result)

    else:
        return render_template('node.html', node=node, error_message=result)


@app.route('/locations')
def get_locations():
    return render_template('locations.html', locations=locations.locations)


@app.route('/handle_data', methods=['POST'])
def handle_data():
    source = request.form['source']
    target = request.form['destination']

    if len(source) > 0 and len(target) == 0:
        url = redirect('/' + source)

    elif len(source) > 0 and len(target) > 0:
        url = redirect('/' + source + '/' + target)

    else:
        url = redirect('/')
    return url
