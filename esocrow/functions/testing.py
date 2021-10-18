def list_zones_in_type(expansion, city_info_dict):
    # TODO Not used anywhere?
    # Creates a List of Zones that are in the 'Type' key within a dict
    zone_list = []
    for city, dict2 in city_info_dict.items():
        zone_type = dict2['Zone Type']
        zone_name = dict2['Zone']
        if expansion == zone_type:
            zone_list.append(zone_name)
    return None
    return zone_list
