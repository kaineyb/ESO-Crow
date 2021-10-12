#########################
# Below enables Sentinel, when run directly.
#########################

if __package__ is None:
    import sys
    from pathlib import Path
    DIR = Path(__file__).resolve().parent
    sys.path.insert(0, str(DIR.parent))
    __package__ = DIR.name

#########################

# Networkx
import networkx as nx

# EsoCrow
from esocrow.functions.graph import add_routes_to_graph
from esocrow.functions.misc import city_info, zonal_info, get_locations_via_expansion
import esocrow.nodes.all as nodes

import pprint as pp

G = nx.DiGraph()


# Add Data to Graphs
# AddSetToGraph(siltstriders, 'Siltstrider')
add_routes_to_graph(G, nodes.siltstriders, 'Silt Strider')
add_routes_to_graph(G, nodes.faction_boatswain, 'Boatswains')
add_routes_to_graph(G, nodes.boats, 'Boats')
add_routes_to_graph(G, nodes.navigator, 'Navigators')
add_routes_to_graph(G, nodes.carts, 'Carts')
add_routes_to_graph(G, nodes.baandari_caravan_stop, 'Baandari Caravan Stop')


# Attributes - NEED TO BE AFTER add_set_to_graph()
att_npc = nx.get_edge_attributes(G, 'npc')
att_label = nx.get_edge_attributes(G, 'label')


# Feeds /locations
locations = G.nodes
locations = sorted(locations)

city_info_dict = city_info(locations)
zonal_info_dict = zonal_info(city_info_dict)

ad_zonal = get_locations_via_expansion("AD", zonal_info_dict)
dc_zonal = get_locations_via_expansion("DC", zonal_info_dict)
ep_zonal = get_locations_via_expansion("EP", zonal_info_dict)
neutral_zonal = get_locations_via_expansion("Neutral", zonal_info_dict)
expansion_zonal = get_locations_via_expansion("Expansion", zonal_info_dict)
dlc_zonal = get_locations_via_expansion("DLC", zonal_info_dict)

list_for_zones = ad_zonal + dc_zonal + ep_zonal + \
    neutral_zonal + expansion_zonal + dlc_zonal

if __name__ == '__main__':

    """ Sentinel """

    print("*"*20)
    print("att_npc")
    print("*"*20)
    pp.pprint(att_npc)

    print("*"*20)
    print("att_label")
    print("*"*20)
    pp.pprint(att_label)
