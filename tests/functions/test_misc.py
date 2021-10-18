from esocrow.functions.misc import sort_dict, city_zone, city_zone_type


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
