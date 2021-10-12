
faction_names = [
    "Aldmeri Dominion",
    "Ebonheart Pact",
    "Daggerfall Covenant"
]

ad = [
    "Auridon",
    "Grahtwood",
    "Greenshade",
    "Khenarthi's Roost",
    "Malabal Tor",
    "Reaper's March"

]

ep = [
    "Bal Foyen",
    "Bleakrock Isle",
    "Deshaan",
    "Eastmarch",
    "The Rift",
    "Shadowfen",
    "Stonefalls"
]


dc = [
    "Alik'r Desert",
    "Bangkorai",
    "Betnikh",
    "Glenumbra",
    "Rivenspire",
    "Stormhaven",
    "Stros M'Kai"
]

neutral = [
    "Coldharbour",
    "Craglorn",
    "Cyrodiil"
]

chapter = [
    "Artaeum",
    "Northern Elsweyr",
    "Summerset",
    "Vvardenfell",
    "Western Skyrim",
]

dlc = [
    "Clockwork City",
    "Gold Coast",
    "Hew's Bane",
    "Murkmire",
    "Southern Elsweyr",
    "Wrothgar",
]

faction_zones = ad + dc + ep

all = faction_zones + neutral + chapter + dlc

# List is alphabetical based on print out for G.nodes() - Zones added manually.

city_to_zone = {
    "Abah's Landing": "Hew's Bane",
    "Alinor": "Summerset",
    "Alten Corimont": "Shadowfen",
    "Anvil": "Gold Coast",
    "Balmora": "Vvardenfell",
    "Belkarth": "Craglorn",
    "Stonetooth Fortress": "Betnikh",
    "Bleakrock Village": "Bleakrock Isle",
    "Daggerfall": "Glenumbra",
    "Davon's Watch": "Stonefalls",
    "Dhalmora": "Bal Foyen",
    "Elden Root": "Grahtwood",
    "Evermore": "Bangkorai",
    "Gnisis": "Vvardenfell",
    "Haven": "Grahtwood",
    "Eagle's Strand": "Khenarthi's Roost",
    "Lilmoth": "Murkmire",
    "Molag Mar": "Vvardenfell",
    "Mournhold": "Deshaan",
    "Orsinium": "Wrothgar",
    "Rawl'kha": "Reaper's March",
    "Riften": "The Rift",
    "Rimmen": "Northern Elsweyr",
    "Sadrith Mora": "Vvardenfell",
    "Sentinel": "Alik'r Desert",
    "Seyda Neen": "Vvardenfell",
    "Shimmerene": "Summerset",
    "Shornhelm": "Rivenspire",
    "Skywatch": "Auridon",
    "Stormhold": "Shadowfen",
    "Port Hunding": "Stros M'Kai",
    "Suran": "Vvardenfell",
    "Tel Mora": "Vvardenfell",
    "Vivec": "Vvardenfell",
    "Vulkhel Guard": "Auridon",
    "Vulkwasten": "Malabal Tor",
    "Wayrest": "Stormhaven",
    "Windhelm": "Eastmarch",
    "Woodhearth": "Greenshade",
}

