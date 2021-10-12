import esocrow.data.zones as zones


def sort_dict(my_dict: dict) -> dict:
    """ Sorts Dict by Value, then by Key """
    new_dict = dict(
        [v for v in sorted(my_dict.items(), key=lambda kv: (kv[1], kv[0]))])
    return new_dict


def find_for_city(city, zone_type=False) -> str:
    if zone_type:
        try:
            result = find_zone_info(zones.city_to_zone[city])
        except KeyError:
            result = "Zone not found"

    else:
        try:
            result = zones.city_to_zone[city]
        except KeyError:
            result = "Zone not found"
    return result


def city_info(locations: list) -> dict:
    # Create a dictionary of all Locations, adds Zone and Zone Type to each Location.
    new_dict = {}
    for location in locations:
        new_dict[location] = {
            'Zone': find_for_city(location),
            'Zone Type': find_for_city(location, zone_type=True)}
    return new_dict


def list_cities_in_zone(zone: str, city_info: dict) -> list:
    # Used in Zonal_info_dict
    # Creates a List of Cities that are in the 'Cities' key within a dict
    city_list = []
    for city, dict2 in city_info.items():
        zone_name = dict2['Zone']
        if zone == zone_name:
            city_list.append(city)
    return city_list


def list_zones_in_type(expansion, city_info_dict):
    # TODO Not used anywhere?
    # Creates a List of Zones that are in the 'Type' key within a dict
    zone_list = []
    for city, dict2 in city_info_dict.items():
        zone_type = dict2['Zone Type']
        zone_name = dict2['Zone']
        if expansion == zone_type:
            zone_list.append(zone_name)
    return zone_list


def zonal_info(city_info: dict) -> dict:
    # Starts with:
    # City { Zone  Type }

    # Ends with:
    # Zone { Type  [List of Cities]}
    # new_dict = { "ZoneName": {"Cities": ["City1" , "City2"], "Type": "DLC" }}

    new_dict = {}
    for city, zone_dict in city_info.items():
        zone = zone_dict['Zone']
        zone_type = zone_dict['Zone Type']

        new_dict[zone] = {
            'Type': zone_type,
            'Cities': list_cities_in_zone(zone, city_info)}  # TODO Need to get a list of cities!
    return new_dict


def get_locations_via_expansion(expansion, zonal_info_dict):

    new_list = []

    for location in zonal_info_dict:
        if zonal_info_dict[location]['Type'] == expansion:
            new_list.append([zonal_info_dict[location]['Type'], location, zonal_info_dict[location]['Cities']
                             ])

    new_list.sort(key=lambda x: x[1])

    return new_list


def find_zone_info(zone):

    if zone in zones.all:
        if zone in zones.dlc:
            zone_info = "DLC"

        elif zone in zones.chapter:
            zone_info = "Expansion"

        elif zone in zones.neutral:
            zone_info = "Neutral"

        elif zone in zones.dc:
            zone_info = "DC"

        elif zone in zones.ep:
            zone_info = "EP"

        elif zone in zones.ad:
            zone_info = "AD"

    else:
        zone_info = "Not Found"

    return zone_info


def convert_spaces(request_name):
    """ Converts %20 into a space. """
    request_name = request_name.replace("%20", " ")
    return request_name
