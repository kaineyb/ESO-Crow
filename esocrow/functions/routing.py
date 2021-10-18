# Built-ins
import string
from typing import Union, Any

# Networkx
from networkx import DiGraph
import networkx as nx

# EsoCrow
from esocrow.functions.misc import city_zone, city_zone_type


def dijkstra(G: DiGraph, source: str, destination: str, attribute_label: "dict[Any | tuple, Any]",
             attribute_npc: "dict[Any | tuple, Any]") -> Union[str, list]:
    """
    Source and Destination are nodes names, these will be locations within ESO.

    attribute_label and attribute_npc are names for 
    nx.get_edge_attributes(G, 'X') where 'X' is npc or label

    """
    try:
        # Coverts to Capwords, only for better presentation in the f-strings/output.
        source = string.capwords(source)
        destination = string.capwords(destination)

        if not G.has_node(source) and not G.has_node(destination):
            return f"Both Source: {source} and Destination: {destination} not found"

        elif not G.has_node(source):
            return f"Source: {source} not found"

        elif not G.has_node(destination):
            return f"Destination: {destination} not found"

        else:
            route = nx.dijkstra_path(G, source, destination)

            route_pairs = [(route[i], route[i+1])
                           for i, _ in enumerate(route[:-1])]

            pairs_list = []

            for pairs in route_pairs:

                start, finish = pairs

                pairs_list.append(
                    [start, finish,
                     attribute_label[pairs], attribute_npc[pairs],
                     city_zone(finish), city_zone_type(finish)])

            if len(pairs_list) > 0:
                return pairs_list

            else:
                return "Source and Destination are the same!"

    except nx.exception.NetworkXNoPath:
        return f"Cannot find a route between {source} and {destination}. Route not possible."
