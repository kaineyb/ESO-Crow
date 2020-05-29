import string
import networkx as nx
import eso_routes


# DONE Make Locations automatic
# DONE and also feed typeahead.

# TODO See TODO on eso_routes.py


G = nx.DiGraph()


def sort_dict(my_dict):
    new_dict = dict(
        [v for v in sorted(my_dict.items(), key=lambda kv: (kv[1], kv[0]))])
    return new_dict


def get_node_routes(node):
    try:
        node = string.capwords(is_stros_mkai(node))
        all_edges = dict(nx.all_pairs_dijkstra_path_length(G))
        data = sort_dict(all_edges[node])
        # Deletes the node requested as it will return 0
        del data[node]
        return data

    except KeyError:
        # Doesn't actually get shown anywhere, but needs to *not* be a dict.
        error_message = "Sorry that location wasn't found :("
        return error_message


def how_to_get_to(node):
    try:
        node = string.capwords(is_stros_mkai(node))
        data = dict(nx.single_target_shortest_path_length(G, node))
        data = sort_dict(data)
        del data[node]
        return data

    except KeyError:
        # Doesn't actually get shown anywhere, but needs to *not* be a dict.
        error_message = "Sorry that location wasn't found :("
        return error_message

    except nx.NodeNotFound:
        error_message = "Node Not Found!"
        return error_message


def add_set_to_graph(setname, labelname):
    for tuples in setname:
        label_name = labelname
        # Unpack Set
        (source, target, npc_name) = tuples
        # Add each line of Set to Graph
        G.add_edge(source, target, npc=npc_name, label=label_name)


def is_stros_mkai(source_or_destination):

    stros_mkai = "Stros M'Kai"
    if source_or_destination.lower() == stros_mkai.lower():
        source_or_destination = ("Stros M'Kai")

    return source_or_destination


def dijkstra(source, target, test=False):
    try:
        source = string.capwords(source)
        target = string.capwords(target)

        source = is_stros_mkai(source)
        target = is_stros_mkai(target)

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
                    [start, finish, att_label[pairs], att_npc[pairs]])

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


# Add Data to Graphs
# AddSetToGraph(siltstriders, 'Siltstrider')
add_set_to_graph(eso_routes.siltstriders, 'Silt Strider')
add_set_to_graph(eso_routes.faction_boatswain, 'Boatswains')
add_set_to_graph(eso_routes.boats, 'Boats')
add_set_to_graph(eso_routes.navigator, 'Navigators')
add_set_to_graph(eso_routes.carts, 'Carts')


# Attribues - NEED TO BE AFTER add_set_to_graph()
att_npc = nx.get_edge_attributes(G, 'npc')
att_label = nx.get_edge_attributes(G, 'label')

S = "daggerfall"
T = "stros m'kai"

# dijkstra(S, T, test=True)

# print("Where you can go from: ", get_node_routes('Daggerfall'))
# print('-'*20)
# how_to_get_to('Lilmoth')


# Feeds /locations
locations = G.nodes
locations = sorted(locations)
