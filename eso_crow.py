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

# Feeds /locations
locations = G.nodes
locations = sorted(locations)


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


# Used in Zonal_info_dict
def list_cities_in_zone(zone):
    # Creates a List of Cities that are in the 'Cities' key within a dict
    city_list = []
    for city, dict2 in city_info_dict.items():
        zone_name = dict2['Zone']
        if zone == zone_name:
            city_list.append(city)
    return city_list


# print(list_cities_in_zone('Vvardenfell'))


# TODO Not used anywhere?
def list_zones_in_type(expansion):
    # Creates a List of Zones that are in the 'Type' key within a dict
    zone_list = []
    for city, dict2 in city_info_dict.items():
        zone_type = dict2['Zone Type']
        zone_name = dict2['Zone']
        if expansion == zone_type:
            zone_list.append(zone_name)
    return zone_list


# print(list_zones_in_type('EP'))


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


def get_locations_via_expansion(expansion):

    new_list = []

    for location in zonal_info_dict:
        if zonal_info_dict[location]['Type'] == expansion:
            new_list.append([zonal_info_dict[location]['Type'], location, zonal_info_dict[location]['Cities']
                             ])

    new_list.sort(key=lambda x: x[1])

    return new_list


# print(zonal_info_dict["Hew's Bane"]['Type'])

ad_zonal = get_locations_via_expansion("AD")
dc_zonal = get_locations_via_expansion("DC")
ep_zonal = get_locations_via_expansion("EP")
neutral_zonal = get_locations_via_expansion("Neutral")
expansion_zonal = get_locations_via_expansion("Expansion")
dlc_zonal = get_locations_via_expansion("DLC")

list_for_zones = ad_zonal + dc_zonal + ep_zonal + \
    neutral_zonal + expansion_zonal + dlc_zonal

# pprint.pprint(list_for_zones)

# key=lambda kv: (kv[1], kv[0]))]
