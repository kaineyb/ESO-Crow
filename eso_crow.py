import string
import networkx as nx
import eso_routes
import eso_zones

import pprint


G = nx.DiGraph()


def sort_dict(my_dict):
    new_dict = dict(
        [v for v in sorted(my_dict.items(), key=lambda kv: (kv[1], kv[0]))])
    return new_dict


def get_node_routes(node):
    try:
        node = is_stros_mkai(string.capwords(node))
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
        node = is_stros_mkai(string.capwords(node))
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
                    [start, finish, att_label[pairs], att_npc[pairs], eso_zones.map_ctz[finish], eso_zones.find_zone_info(eso_zones.map_ctz[finish])])

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
add_set_to_graph(eso_routes.baandari_caravan_stop, 'Baandari Caravan Stop')


# Attribues - NEED TO BE AFTER add_set_to_graph()
att_npc = nx.get_edge_attributes(G, 'npc')
att_label = nx.get_edge_attributes(G, 'label')

S = "daggerfall"
T = "Bleakrock isle"

# dijkstra(S, T, test=True)

# print("Where you can go from: ", get_node_routes('Daggerfall'))
# print('-'*20)

# print(how_to_get_to("stros m'kai"))

# print(is_stros_mkai("stros m'kai"))


# Feeds /locations
locations = G.nodes
locations = sorted(locations)


# nested_dict = { 'Abah's Landing': {'Hew's Bane': 'DLC'},

# Dict = { }
# print("Initial nested dictionary:-")
# print(Dict)

# Dict['Dict1'] = {}

# # Adding elements one at a time
# Dict['Dict1']['name'] = 'Bob'
# Dict['Dict1']['age'] = 21
# print("\nAfter adding dictionary Dict1")
# print(Dict)

# # Adding whole dictionary
# Dict['Dict2'] = {'name': 'Cara', 'age': 25}
# print("\nAfter adding dictionary Dict1")
# print(Dict)

def city_info_dict():
    new_dict = {}
    for location in locations:
        new_dict[location] = {
            'Zone': eso_zones.map_ctz[location],
            'Zone Type': eso_zones.find_zone_info(eso_zones.map_ctz[location])}
    return new_dict


city_info_dict = city_info_dict()

# Returns Murkmire
# pprint.pprint(city_info_dict)


def list_cities_in_zone(zone):
    city_list = []
    for city, dict2 in city_info_dict.items():
        zone_name = dict2['Zone']
        if zone == zone_name:
            city_list.append(city)
    return city_list


# print(list_cities_in_zone('Vvardenfell'))


def list_zones_in_expansion(expansion):
    zone_list = []
    for city, dict2 in city_info_dict.items():
        zone_type = dict2['Zone Type']
        zone_name = dict2['Zone']
        if expansion == zone_type:
            zone_list.append(zone_name)
    return zone_list

# print(list_zones_in_expansion('DLC'))


def zonal_info_dict():

    new_dict = {}
    # Start with:
    # City { Zone  Type }

    # Zone { Type  [List of Cities]}
    # new_zonal_dict = { "ZoneName": {"Type": "DLC", "Cities": ["City1" , "City2"] }}

    for city, zone_dict in city_info_dict.items():
        zone = zone_dict['Zone']
        zone_type = zone_dict['Zone Type']

        new_dict[zone] = {
            'Type': zone_type,
            'Cities': list_cities_in_zone(zone)}  # TODO Need to get a list of cities!

    return new_dict


zonal_info_dict = zonal_info_dict()

# pprint.pprint(zonal_info_dict['Vvardenfell'])

# Type > List of Zones > List of Cities
# new_type_dict = {"TypeName": {"Zone":"ZoneName", "Cities": ["City1" , "City2"]}}
