# Networkx
from networkx import DiGraph


def add_routes_to_graph(G: DiGraph, routes: "list[tuple[str, str, str]]", labelname: str) -> None:
    """ Adds to main instance of DiGraph """
    for route in routes:

        # Unpack Set
        source, target, npc_name = route

        # Add each line of routes to Graph
        G.add_edge(source, target, npc=npc_name, label=labelname)
