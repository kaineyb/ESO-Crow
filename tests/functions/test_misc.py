from esocrow.functions.misc import sort_dict, city_zone, city_zone_type, find_zone_info, convert_spaces
import esocrow.data.zones as zones


def test_sort_dict():

    dict_in = {
        "Test 3.0": 3, "Test 3.1": 3, "Test 2.1": 2, "Test 2.0": 2,
        "Test 1.1": 1, "Test 1.0": 1, "Test 0.1": 0, "Test 0.0": 0,
    }

    result = sort_dict(dict_in)

    expected = {'Test 0.0': 0, 'Test 0.1': 0, 'Test 1.0': 1, 'Test 1.1': 1,
                'Test 2.0': 2, 'Test 2.1': 2, 'Test 3.0': 3, 'Test 3.1': 3}

    assert isinstance(result, dict)

    expected = list(expected.items())
    result = list(result.items())

    assert result == expected


def test_city_zone():

    result = city_zone("Elden Root")
    assert result == "Grahtwood"

    result = city_zone("Gold")
    assert result == "Zone not found"


def test_city_zone_type():

    result = city_zone_type("Elden Root")
    assert result == "AD"

    result = city_zone_type("Daggerfall")
    assert result == "DC"

    result = city_zone_type("Mournhold")
    assert result == "EP"

    result = city_zone_type("Gold")
    assert result == "Zone not found"


def test_find_zone_info():

    result = find_zone_info("Grahtwood")
    assert result == "AD"

    result = find_zone_info("Deshaan")
    assert result == "EP"

    result = find_zone_info("Glenumbra")
    assert result == "DC"

    result = find_zone_info("Coldharbour")
    assert result == "Neutral"

    result = find_zone_info("Summerset")
    assert result == "Expansion"

    result = find_zone_info("Clockwork City")
    assert result == "DLC"

    result = find_zone_info("Gold")
    assert result == "Not Found"


def test_convert_spaces():

    input = "Bleakrock%20Village"

    result = convert_spaces(input)
    criteria = "Bleakrock Village"

    assert result == criteria
