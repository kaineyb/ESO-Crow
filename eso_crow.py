import string
import networkx as nx
from collections import OrderedDict
import eso_routes
import eso_zones

import pprint


G = nx.DiGraph()


def sort_dict(my_dict):
    # Sorts Dict by Value, then by Key
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


def find_for_city(city, zone_type=False):
    if zone_type:
        try:
            result = eso_zones.find_zone_info(eso_zones.map_ctz[city])
        except KeyError:
            result = "Zone not found"

    else:
        try:
            result = eso_zones.map_ctz[city]
        except KeyError:
            result = "Zone not found"
    return result


# print(find_for_city("Eagle's Strand", zone_type=True))

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
                    [start, finish, att_label[pairs], att_npc[pairs], find_for_city(finish), find_for_city(finish, zone_type=True)])

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
    # Create a dictionary of all Locations, adds Zone and Zone Type to each Location.
    new_dict = {}
    for location in locations:
        new_dict[location] = {
            'Zone': find_for_city(location),
            'Zone Type': find_for_city(location, zone_type=True)}
    return new_dict


city_info_dict = city_info_dict()

# Returns Murkmire
# print(city_info_dict['Lilmoth']['Zone Type'])


def list_cities_in_zone(zone):
    # Creates a List of Cities that are in the 'Cities' key within a dict
    city_list = []
    for city, dict2 in city_info_dict.items():
        zone_name = dict2['Zone']
        if zone == zone_name:
            city_list.append(city)
    return city_list


# print(list_cities_in_zone('Vvardenfell'))


def list_zones_in_type(expansion):
    # Creates a List of Zones that are in the 'Type' key within a dict
    zone_list = []
    for city, dict2 in city_info_dict.items():
        zone_type = dict2['Zone Type']
        zone_name = dict2['Zone']
        if expansion == zone_type:
            zone_list.append(zone_name)
    return zone_list


# print(list_zones_in_type('Daggerfall Covenant'))


def zonal_info_dict():
    # Starts with:
    # City { Zone  Type }

    # Ends with:
    # Zone { Type  [List of Cities]}
    # new_dict = { "ZoneName": {"Cities": ["City1" , "City2"], "Type": "DLC" }}

    new_dict = {}
    for city, zone_dict in city_info_dict.items():
        zone = zone_dict['Zone']
        zone_type = zone_dict['Zone Type']

        new_dict[zone] = {
            'Type': zone_type,
            'Cities': list_cities_in_zone(zone)}  # TODO Need to get a list of cities!
    return new_dict


zonal_info_dict = zonal_info_dict()


# new_dict = OrderedDict(zonal_info_dict.items())

# pprint.pprint(zonal_info_dict)


def sort_zonal_dict(my_dict):
    new_dict = {}
    # Sorts Dict by Value, then by Key
    new_dict = dict(
        [v for v in sorted(my_dict.items(), key=lambda kv: (kv[1], kv[0]))])
    return new_dict


# pprint.pprint(sort_zonal_dict(zonal_info_dict))

# TODO Maybe coming soon? If Needed?
# Type > List of Zones > List of Cities
# new_type_dict = {"TypeName": {"Zone":"ZoneName", "Cities": ["City1" , "City2"]}}

# Python3 code to demonstrate
# Sort nested dictionary by key
# using sorted()

# initializing dictionary
test_dict = {
    'A': {'City': 'A', 'Type': 'DC'},
    'B': {'City': 'B', 'Type': 'EP'},
    'C': {'City': 'C', 'Type': 'AD'},
    'D': {'City': 'C', 'Type': 'DLC'},
    'E': {'City': 'C', 'Type': 'DLC'},
    'F': {'City': 'C', 'Type': 'DLC'},
    'G': {'City': 'C', 'Type': 'Expansion'},
    'H': {'City': 'C', 'Type': 'Expansion'},
    'I': {'City': 'C', 'Type': 'Expansion'},
}

# printing original dict
# pprint.pprint(test_dict)
# print('-' * 20)

# using sorted()
# Sort nested dictionary by key
# res = OrderedDict(sorted(test_dict.items(), key=lambda x: x[1]['Type']))

# print result
# pprint.pprint(res)

# print(test_dict.get('City', {}).get('Type'))


sort_key_list = sorted(zonal_info_dict, key=lambda x: (
    zonal_info_dict[x]['Type'], zonal_info_dict[x]['Cities']))

for item in sort_key_list:
    print(item, zonal_info_dict[item])

# pprint.pprint(sort_key_list)

# Create the order of the dictionary using a list

# iterate of this list using each entry as a key to print out the remainder?
