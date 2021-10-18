from esocrow.functions.build import city_info, list_cities_in_zone, get_locations_via_expansion
from esocrow.main import locations, city_info_dict, zonal_info


def test_city_info():
    info = city_info(locations)
    assert isinstance(info, dict)

    city = "Abah's Landing"
    data = """{'Zone': "Hew's Bane", 'Zone Type': 'DLC'}"""

    result = str(info[city])
    assert result == data


def test_list_cities_in_zone():
    zone = "Auridon"
    results = list_cities_in_zone(zone, city_info_dict)

    criteria = ['Skywatch', 'Vulkhel Guard']

    assert isinstance(results, list)
    assert results == criteria


def test_zonal_info():
    results = zonal_info(city_info_dict)
    zone = "Alik'r Desert"
    criteria = {'Cities': ['Sentinel'], 'Type': 'DC'}

    assert results[zone] == criteria


def test_get_locations_via_expansion():

    zonal_info_dict = zonal_info(city_info_dict)

    types = ["AD", "DC", "EP", "Neutral", "Expansion", "DLC"]

    for type in types:
        result = get_locations_via_expansion(type, zonal_info_dict)
        assert isinstance(result, list)

    result = get_locations_via_expansion("AD", zonal_info_dict)
    assert result[0] == ['AD', 'Auridon', ['Skywatch', 'Vulkhel Guard']]
