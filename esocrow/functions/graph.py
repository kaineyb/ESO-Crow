# Networkx
from networkx import DiGraph


def add_routes_to_graph(G: DiGraph, routes: "list[tuple[str, str, str]]", labelname: str) -> None:
    """
    Adds to main instance of DiGraph

    routes to be a list of  ["source", "destination", "npc_name"]
    """

    for route in routes:

        # Unpack Set
        source, destination, npc_name = route

        # Add each line of routes to Graph
        G.add_edge(source, destination, npc=npc_name, label=labelname)
