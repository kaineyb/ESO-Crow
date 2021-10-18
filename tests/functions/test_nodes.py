from esocrow.functions.nodes import travel_from, travel_to


from esocrow.main import G


def test_travel_to():
    """ """
    result = travel_to(G, "Wayrest")
    assert isinstance(result, dict)

    result = travel_to(G, "Gold")
    assert result == None


def test_travel_from():
    """ """
    result = travel_from(G, "Wayrest")
    assert isinstance(result, dict)

    result = travel_from(G, "Gold")
    assert result == None
