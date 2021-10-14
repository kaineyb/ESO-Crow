from esocrow.main import G, att_label, att_npc
from esocrow.functions.routing import dijkstra


def test_output():
    source = "Riften"
    destination = "Mournhold"

    result = dijkstra(G, source, destination, att_label, att_npc)

    criteria = [['Riften', "Davon's Watch", 'Navigators', 'Falvis Raram', 'Stonefalls', 'EP'],
                ["Davon's Watch", 'Mournhold', 'Navigators', 'Falvis Raram', 'Deshaan', 'EP']]

    assert result == criteria
    assert isinstance(result, list)


def test_no_route():
    """ """
    source = "Woodhearth"
    destination = "Skywatch"

    result = dijkstra(G, source, destination, att_label, att_npc)

    criteria = "Cannot find a route between Woodhearth and Skywatch. Route not possible."

    assert result == criteria
    assert isinstance(result, str)


def test_both_not_found():
    """ """
    source = "Silver"
    destination = "Gold"

    result = dijkstra(G, source, destination, att_label, att_npc)

    criteria = f"Both Source: {source} and Destination: {destination} not found"

    assert result == criteria
    assert isinstance(result, str)


def test_destination_not_found():
    """ """
    source = "Wayrest"
    destination = "Gold"

    result = dijkstra(G, source, destination, att_label, att_npc)

    criteria = f"Destination: {destination} not found"

    assert result == criteria


def test_source_not_found():
    """ """
    source = "Gold"
    destination = "Wayrest"

    result = dijkstra(G, source, destination, att_label, att_npc)

    criteria = f"Source: {source} not found"

    assert result == criteria
    assert isinstance(result, str)


def test_same_source_and_destination():
    """ """
    source = "Wayrest"
    destination = "Wayrest"

    result = dijkstra(G, source, destination, att_label, att_npc)

    criteria = f"Source and Destination are the same!"

    assert result == criteria
    assert isinstance(result, str)
