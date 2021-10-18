from networkx.classes.reportviews import NodeView
import networkx as nx

from esocrow.functions.graph import add_routes_to_graph


def test_add_routes_to_graph():

    test_graph1 = nx.DiGraph()

    test_set = [
        ("Location 1", "Location 2", "NPC"),
        ("Location 2", "Location 1", "NPC"),

        ("Location 1", "Location 3", "NPC"),
        ("Location 3", "Location 1", "NPC"),

        ("Location 1", "Location 4", "NPC"),
        ("Location 4", "Location 1", "NPC")
    ]

    add_routes_to_graph(test_graph1, test_set,
                        'label')

    result = test_graph1.nodes

    criteria = ['Location 1', 'Location 2', 'Location 3', 'Location 4']

    assert isinstance(result, NodeView)
    assert list(result) == criteria


def test_add_routes_to_graph_attributes():
    """ """

    test_graph2 = nx.DiGraph()

    test_set = [("Source", "Destination", "NPC")]

    add_routes_to_graph(test_graph2, test_set,
                        'Label')

    att_npc = nx.get_edge_attributes(test_graph2, 'npc')
    att_label = nx.get_edge_attributes(test_graph2, 'label')

    assert isinstance(att_npc, dict)
    assert isinstance(att_label, dict)

    assert att_npc[('Source', 'Destination')] == 'NPC'
    assert att_label[('Source', 'Destination')] == 'Label'
