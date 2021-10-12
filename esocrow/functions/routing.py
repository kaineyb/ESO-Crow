#########################
# Below enables Sentinel, when run directly.
#########################

if __package__ is None:
    import sys
    from pathlib import Path
    DIR = Path(__file__).resolve().parent
    sys.path.insert(0, str(DIR.parent))
    __package__ = DIR.name
    print(__package__)


#########################

# Built-ins
import string
from typing import Union

# Networkx
from networkx import DiGraph
import networkx as nx

# EsoCrow
from esocrow.functions.misc import find_for_city


def dijkstra(G: DiGraph, source, target, attribute_label, attribute_npc, test=False):
    try:
        source = string.capwords(source)
        target = string.capwords(target)

        if not G.has_node(source) and not G.has_node(target):
            error_message = "Both Source: {} and Destination: {} not found" .format(
                source, target)
            if test:
                print(error_message)
            return error_message

        elif not G.has_node(source):
            error_message = "Source: {} not found" .format(source)
            if test:
                print(error_message)
            return error_message

        elif not G.has_node(target):
            error_message = "Destination: {} not found" .format(target)
            if test:
                print(error_message)
            return error_message

        else:
            route = nx.dijkstra_path(G, source, target)
            route_pairs = [(route[i], route[i+1])
                           for i, _ in enumerate(route[:-1])]

            pairs_list = []

            for pairs in route_pairs:
                (start, finish) = pairs
                pairs_list.append(
                    [start, finish, attribute_label[pairs], attribute_npc[pairs], find_for_city(finish), find_for_city(finish, zone_type=True)])

            if len(pairs_list) > 0:
                if test:
                    print("We're good")
                    print(pairs_list)
                return pairs_list

            else:
                error_message = "Source and Destination are the same!"
                if test:
                    print("We're not good")
                    print(error_message)
                return error_message

    except nx.exception.NetworkXNoPath:
        error_message = "Cannot find a route between {} and {}. Route not possible." .format(
            source, target)
        if test:
            print(error_message)
        return error_message


if __name__ == '__main__':
    """ """

    from main import G, att_label, att_npc

    source = "Riften"
    target = "Mournhold"

    attribute_label = att_label
    attribute_npc = att_npc

    result = dijkstra(G, source, target, attribute_label, attribute_npc)

    print(result)
