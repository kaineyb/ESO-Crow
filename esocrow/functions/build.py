from esocrow.functions.misc import city_zone_type, city_zone


def city_info(locations: list) -> dict:
    """ dict[Location, Zone, Zone Type] """
    # Create a dictionary of all Locations, adds Zone and Zone Type to each Location.
    new_dict = {}
    for location in locations:
        new_dict[location] = {
            'Zone': city_zone(location),
            'Zone Type': city_zone_type(location)}
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


def get_locations_via_expansion(expansion: str, zonal_info:dict):

    new_list = []

    for location in zonal_info:
        if zonal_info[location]['Type'] == expansion:
            new_list.append([zonal_info[location]['Type'], location, zonal_info[location]['Cities']
                             ])

    new_list.sort(key=lambda x: x[1])

    return new_list
