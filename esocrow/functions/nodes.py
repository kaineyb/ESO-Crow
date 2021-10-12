# Built-ins
from typing import Union

# Networkx
from networkx import DiGraph
import networkx as nx

# EsoCrow
from esocrow.functions.misc import sort_dict


def travel_from(G: DiGraph, node: str) -> Union[dict, str]:
    """ 
    Used on the Solo Node Pages.
    Returns a dictionary of all the places that can take you to node
    """

    """ Takes a node, checks a digraph and returns a dictionary or a str (error message) """
    try:
        all_edges: dict = dict(nx.all_pairs_dijkstra_path_length(G))
        data: dict = sort_dict(all_edges[node])
        # Deletes the node requested as it will return 0
        del data[node]
        return data

    except KeyError:
        # Doesn't actually get shown anywhere, but needs to *not* be a dict.
        error_message = "Sorry that location wasn't found :("
        return error_message


def travel_to(G: DiGraph, node: str) -> Union[dict, str]:
    """
    Used on the Solo Node Pages.
    Returns a dictionary of all the places that can take you to node
    """
    try:
        data = dict(nx.single_target_shortest_path_length(G, node))
        data = sort_dict(data)
        del data[node]  # delete itself from the dictionery
        return data

    except KeyError:
        # Doesn't actually get shown anywhere, but needs to *not* be a dict.
        error_message = "Sorry that location wasn't found :("
        return error_message

    except nx.NodeNotFound:
        error_message = "Node Not Found!"
        return error_message
