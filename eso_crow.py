import networkx as nx

import eso_routes

G = nx.DiGraph()


def add_set_to_graph(setname, labelname):
    for tuples in setname:
        label_name = labelname
        # Unpack Set
        (source, target, npc_name) = tuples
        # Add each line of Set to Graph
        G.add_edge(source, target, npc=npc_name, label=label_name)


def dijkstra(source, target):

    source = str.title(source)
    target = str.title(target)

    route = nx.dijkstra_path(G, source, target)
    route_pairs = [(route[i], route[i+1]) for i, _ in enumerate(route[:-1])]

    pairs_list = []
    for pairs in route_pairs:
        (start, finish) = pairs
        pairs_list.append([start, finish, att_label[pairs], att_npc[pairs]])

    return pairs_list

# def show_todo():
# my_list = []
# for key, value in cal.items():
#     my_list.append([value[0], key])
# return my_list


# Add Data to Graphs
# AddSetToGraph(siltstriders, 'Siltstrider')
add_set_to_graph(eso_routes.siltstriders, 'Siltstrider')
add_set_to_graph(eso_routes.faction_boatswain, 'Boatswain')
add_set_to_graph(eso_routes.boats, 'Boats')
add_set_to_graph(eso_routes.navigator, 'Navigator')
add_set_to_graph(eso_routes.carts, 'Carts')


# Attribues - NEED TO BE AFTER add_set_to_graph()
att_npc = nx.get_edge_attributes(G, 'npc')
att_label = nx.get_edge_attributes(G, 'label')

dijkstra("Mournhold", "Alinor")
