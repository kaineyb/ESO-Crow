import networkx as nx
import string
import eso_routes

G = nx.DiGraph()


def add_set_to_graph(setname, labelname):
    for tuples in setname:
        label_name = labelname
        # Unpack Set
        (source, target, npc_name) = tuples
        # Add each line of Set to Graph
        G.add_edge(source, target, npc=npc_name, label=label_name)


def dijkstra(source, target, test=False):

    source = string.capwords(source)
    target = string.capwords(target)

    try:
        route = nx.dijkstra_path(G, source, target)
        route_pairs = [(route[i], route[i+1])
                       for i, _ in enumerate(route[:-1])]

        pairs_list = []
        for pairs in route_pairs:
            (start, finish) = pairs
            pairs_list.append(
                [start, finish, att_label[pairs], att_npc[pairs]])
        if test:
            print(pairs_list)
        return pairs_list

    except nx.NodeNotFound:
        error_message = "Source: {} not found" .format(source)
        if test:
            print(error_message)
        return error_message

    except nx.exception.NetworkXNoPath:
        error_message = "Cannot find a route between source and destination. Route may not be possible or {} doesn't exist" .format(
            target)
        if test:
            print(error_message)
        return error_message

    except:
        error_message = "Something doesn't seem right there"
        if test:
            print(error_message)
        return error_message


# Add Data to Graphs
# AddSetToGraph(siltstriders, 'Siltstrider')
add_set_to_graph(eso_routes.siltstriders, 'Siltstrider')
add_set_to_graph(eso_routes.faction_boatswain, 'Boatswain')
add_set_to_graph(eso_routes.boats, 'Boats')
add_set_to_graph(eso_routes.navigator, 'Navigators')
add_set_to_graph(eso_routes.carts, 'Carts')


# Attribues - NEED TO BE AFTER add_set_to_graph()
att_npc = nx.get_edge_attributes(G, 'npc')
att_label = nx.get_edge_attributes(G, 'label')

s = r"daggerfall"
t = "Tilbury"

#dijkstra(s, t, test=True)
