import esocrow.data.zones as zones


def sort_dict(my_dict: dict) -> dict:
    """ Sorts Dict by Value, then by Key """
    new_dict = dict(
        [v for v in sorted(my_dict.items(), key=lambda kv: (kv[1], kv[0]))])
    return new_dict


def city_zone(city) -> str:
    """ Returns the Zone that a City is in """

    try:
        result = zones.city_to_zone[city]
    except KeyError:
        result = "Zone not found"
    return result


def city_zone_type(city) -> str:
    """ Returns the type of Zone that a City is in """

    try:
        result = find_zone_info(zones.city_to_zone[city])
    except KeyError:
        result = "Zone not found"
    return result


def find_zone_info(zone: str):

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
