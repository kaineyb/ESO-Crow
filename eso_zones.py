from eso_cities_to_zones import map_ctz

factions = [
    "Aldmeri Dominion",
    "Ebonheart Pact",
    "Daggerfall Covenant"
]

ad_zones = [
    "Auridon",
    "Grahtwood",
    "Greenshade",
    "Khenarthi's Roost",
    "Malabal Tor",
    "Reaper's March"

]

ep_zones = [
    "Bal Foyen",
    "Bleakrock Isle",
    "Deshaan",
    "Eastmarch",
    "The Rift",
    "Shadowfen",
    "Stonefalls"
]


dc_zones = [
    "Alik'r Desert",
    "Bangkorai",
    "Betnikh",
    "Glenumbra",
    "Rivenspire",
    "Stormhaven",
    "Stros M'Kai"
]

neutral_zones = [
    "Coldharbour",
    "Craglorn",
    "Cyrodiil"
]

chapter_zones = [
    "Artaeum",
    "Northern Elsweyr",
    "Summerset",
    "Vvardenfell",
    "Western Skyrim",
]

dlc_zones = [
    "Clockwork City",
    "Gold Coast",
    "Hew's Bane",
    "Murkmire",
    "Southern Elsweyr",
    "Wrothgar",
]

faction_zones = ad_zones + dc_zones + ep_zones

zones = faction_zones + neutral_zones + chapter_zones + dlc_zones


def find_zone_info(zone):

    if zone in zones:
        if zone in dlc_zones:
            zone_info = "DLC"

        elif zone in chapter_zones:
            zone_info = "Expansion"

        elif zone in neutral_zones:
            zone_info = "Neutral"

        elif zone in dc_zones:
            zone_info = "DC"

        elif zone in ep_zones:
            zone_info = "EP"

        elif zone in ad_zones:
            zone_info = "AD"

    else:
        zone_info = "Not Found"

    return zone_info


# find_zone_info("Wrothgar")
