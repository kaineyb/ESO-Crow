# Built-ins
from typing import Union

# Networkx
from networkx import DiGraph
import networkx as nx

# EsoCrow
from esocrow.functions.misc import sort_dict


def travel_from(G: DiGraph, node: str) -> Union[dict, None]:
    """ 
    Used on the Solo Node Pages.
    Returns a dictionary of all the places that can take you to node
    """

    """ Takes a node, checks a digraph and returns a dictionary or None """
    try:
        all_edges: dict = dict(nx.all_pairs_dijkstra_path_length(G))
        data: dict = sort_dict(all_edges[node])
        # data = all_edges[node]
        # Deletes the node requested as it will return 0
        del data[node]
        return data

    except KeyError:
        return None


def travel_to(G: DiGraph, node: str) -> Union[dict, None]:
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
        return None

    except nx.NodeNotFound:
        return None
