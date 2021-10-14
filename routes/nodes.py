from app import app
from esocrow.main import G

# Built-ins
import string
from random import choice

# Flask
from flask import request, redirect, render_template
from flask.wrappers import Response


# 3rd Party:


# My stuff:

from esocrow.functions.misc import convert_spaces
from esocrow.functions.nodes import travel_from, travel_to
from esocrow.functions.routing import dijkstra

from esocrow.main import locations
from esocrow.main import att_label, att_npc


@ app.route('/handle_data', methods=['POST'])
def handle_data() -> Response:
    """ 
    Checks if Source and Target have BOTH been used or just one.
    Returns the correct redirect
    """

    source = request.form['source']
    target = request.form['destination']

    if len(source) > 0 and len(target) == 0:
        url = redirect('/' + source)

    elif len(source) > 0 and len(target) > 0:
        url = redirect('/' + source + '/' + target)

    else:
        url = redirect('/')
    return url


@ app.route('/<node>')
def node_page(node):
    node = convert_spaces(node)

    travel_from_dict = travel_from(G, node)

    travel_to_dict = travel_to(G, node)

    node = string.capwords(node)

    if isinstance(travel_from_dict, dict):
        return render_template('routing/node.html', node=node, travel_from=travel_from_dict, travel_to=travel_to_dict)

    else:
        return render_template('errors/page_not_found.html'), 404


@ app.route('/<source>/<target>')
def source_target(source, target):
    source = convert_spaces(source)
    target = convert_spaces(target)

    result = dijkstra(G, source, target, att_label, att_npc)

    if isinstance(result, list):
        return render_template('routing/dijkstra.html', pairs_list=result, source=source, target=target)

    else:
        return render_template('routing/dijkstra.html', error_message=result)


@ app.route('/random_route')
def random_route():

    nodes = locations

    url1 = choice(nodes)
    url2 = choice(nodes)

    while url1 == url2:
        url2 = choice(nodes)

    return redirect(f'/{url1}/{url2}')
