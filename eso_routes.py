siltstriders = [
    ("Balmora", "Gnisis", "Nevos Sareloth"),
    ("Balmora", "Vivec", "Nevos Sareloth"),

    ("Gnisis", "Balmora", "Amili Yahaz"),
    ("Gnisis", "Vivec", "Amili Yahaz"),

    ("Molag Mar", "Suran", "Narisa Androm"),
    ("Molag Mar", "Tel Mora", "Narisa Androm"),

    ("Seyda Neen", "Gnisis", "Medyn Hleran"),
    ("Seyda Neen", "Suran", "Medyn Hleran"),

    ("Suran", "Molag Mar", "Faven Thendas"),
    ("Suran", "Seyda Neen", "Faven Thendas"),
    ("Suran", "Vivec", "Faven Thendas"),

    ("Tel Mora", "Molag Mar", "Adosi Delvi"),
    ("Tel Mora", "Vivec", "Adosi Delvi"),

    ("Vivec", "Balmora", "Helseth Sadalvel"),
    ("Vivec", "Gnisis", "Helseth Sadalvel"),
    ("Vivec", "Suran", "Helseth Sadalvel"),
    ("Vivec", "Tel Mora", "Helseth Sadalvel"),

    ("Brentwood", "Shenfield", "Brentwood Station")
]

faction_boatswain = [
    # From Data on https://en.uesp.net/wiki/Online:Boatswains

    # Aldmeri Dominion
    # Sugar-Claws will take you both ways
    ("Vulkhel Guard", "Khenarthi's Roost", "Sugar-Claws"),
    ("Khenarthi's Roost", "Khenarthi's Roost", "Sugar-Claws"),

    # Scout Linimondil will take you both ways
    ("Skywatch", "Haven", "Scout Linimondil"),
    ("Haven", "Skywatch", "Scout Linimondil"),

    # Daggerfall Covenant
    # Gilzir will take you three ways
    ("Daggerfall", "Stros M'Kai", "Gilzir"),
    ("Daggerfall", "Betnikh", "Gilzir"),

    ("Stros M'Kai", "Daggerfall", "Gilzir"),
    ("Stros M'Kai", "Betnikh", "Gilzir"),

    ("Betnikh", "Daggerfall", "Gilzir"),
    ("Betnikh", "Stros M'Kai", "Gilzir"),

    ("Wayrest", "Sentinel", "Zihlijdel"),
    ("Sentinel", "Wayrest", "Captain Carlier"),

    # Ebonheart Pact
    # TODO The Boatmaster is quest NPC that requires an invite?
    # ("Mournhold ", "Shad Astula", "The Boatmaster"),

    # TODO Need to check that Dasta can take you both ways or not.
    # TODO Also not on ESO Transport map?
    ("Bleakrock Isle", "Seyda Neen", "Dastas Arenim"),

    ("Bleakrock Isle", "Davon's Watch", "Liezl"),
    ("Bleakrock Isle", "Dhalmora", "Liezl"),

    ("Davon's Watch", "Bleakrock Isle", "Liezl"),
    ("Davon's Watch", "Dhalmora", "Liezl"),

    ("Dhalmora", "Bleakrock Isle", "Liezl"),
    ("Dhalmora", "Davon's Watch", "Liezl"),


    ("Alten Corimont", "Windhelm", "Muz-Muz"),
    ("Windhelm", "Alten Corimont", "Muz-Muz"),
]

# TODO Found more Boatswains like Taros in Seyda Need. Few missing?


boats = [
    ("Abah's Landing", "Vivec", "Unnamed Sailboat"),  # One way
    ("Abah's Landing", "Windhelm", "Harbor Skiff"),
    ("Abah's Landing", "Woodhearth", "Harbor Skiff"),
    ("Abah's Landing", "Wayrest", "Harbor Skiff"),

    # Anvil
    ("Anvil", "Vivec", "The Razorbill"),  # One way
    ("Anvil", "Vulkhel Guard", "The Egret"),
    ("Anvil", "Davon's Watch", "The Osprey"),
    ("Anvil", "Daggerfall", "The Heron"),
    ("Anvil", "Shimmerene", "The Golden Gryphon"),

    # Daggerfall
    ("Daggerfall", "Anvil", "Harbor Skiff"),
    ("Daggerfall", "Davon's Watch", "The Hotspur"),
    ("Daggerfall", "Vulkhel Guard", "The Lydia"),

    #  Murkmire Boat
    ("Daggerfall", "Lilmoth", "Southern Dock - Murkmire Boat"),

    # Davon's Watch
    ("Davon's Watch", "Anvil", "Harbor Skiff"),
    ("Davon's Watch", "Vulkhel Guard", "The Rusty Argonian Blade"),
    ("Davon's Watch", "Daggerfall", "Summerwind"),

    #  Mournhold
    ("Mournhold", "Vivec", "Unnamed Sailboat"),

    # Vivec
    ("Vivec", "Mournhold", "Coastal Skiff"),

    # Vulkhel Guard
    ("Vulkhel Guard", "Anvil", "Harbor Skiff"),
    ("Vulkhel Guard", "Davon's Watch", "Harbor Skiff"),
    ("Vulkhel Guard", "Daggerfall", "The Interim Suitor"),
    ("Vulkhel Guard", "Lilmoth", "Murkmire Boat"),

    # Wayrest
    ("Wayrest", "Vivec", "Unnamed Sailboat"),  # One way
    ("Wayrest", "Abah's Landing", "Harbor Skiff"),

    # Windhelm
    ("Windhelm", "Abah's Landing", "Longboat"),

    # Woodhearth
    ("Woodhearth", "Vivec", "Unnamed Sailboat"),  # One way
    ("Woodhearth", "Abah's Landing", "Harbor Skiff"),
]

navigator = [
    # Alliance Navigators

    # AD - Selandilwen
    ("Vulkhel Guard", "Elden Root", "Selandilwen"),
    ("Vulkhel Guard", "Rawl'kha", "Selandilwen"),
    ("Vulkhel Guard", "Daggerfall", "Selandilwen"),
    ("Vulkhel Guard", "Davon's Watch", "Selandilwen"),

    ("Elden Root", "Woodhearth", "Selandilwen"),
    ("Elden Root", "Vulkhel Guard", "Selandilwen"),
    ("Elden Root", "Wayrest", "Selandilwen"),
    ("Elden Root", "Mournhold", "Selandilwen"),

    ("Woodhearth", "Vulkwasten", "Selandilwen"),
    ("Woodhearth", "Elden Root", "Selandilwen"),
    ("Woodhearth", "Shornhelm", "Selandilwen"),
    ("Woodhearth", "Stormhold", "Selandilwen"),

    ("Vulkwasten", "Rawl'kha", "Selandilwen"),
    ("Vulkwasten", "Woodhearth", "Selandilwen"),
    ("Vulkwasten", "Sentinel", "Selandilwen"),
    ("Vulkwasten", "Windhelm", "Selandilwen"),

    ("Rawl'kha", "Vulkhel Guard", "Selandilwen"),
    ("Rawl'kha", "Vulkwasten", "Selandilwen"),
    ("Rawl'kha", "Evermore", "Selandilwen"),
    ("Rawl'kha", "Riften", "Selandilwen"),

    # EP - Falvis Raram

    ("Davon's Watch", "Mournhold", "Falvis Raram"),
    ("Davon's Watch", "Riften", "Falvis Raram"),
    ("Davon's Watch", "Vulkhel Guard", "Falvis Raram"),
    ("Davon's Watch", "Daggerfall", "Falvis Raram"),

    ("Mournhold", "Stormhold", "Falvis Raram"),
    ("Mournhold", "Davon's Watch", "Falvis Raram"),
    ("Mournhold", "Elden Root", "Falvis Raram"),
    ("Mournhold", "Wayrest", "Falvis Raram"),

    ("Stormhold", "Windhelm", "Falvis Raram"),
    ("Stormhold", "Mournhold", "Falvis Raram"),
    ("Stormhold", "Woodhearth", "Falvis Raram"),
    ("Stormhold", "Shornhelm", "Falvis Raram"),

    ("Windhelm", "Riften", "Falvis Raram"),
    ("Windhelm", "Stormhold", "Falvis Raram"),
    ("Windhelm", "Vulkwasten", "Falvis Raram"),
    ("Windhelm", "Sentinel", "Falvis Raram"),

    ("Riften", "Davon's Watch", "Falvis Raram"),
    ("Riften", "Windhelm", "Falvis Raram"),
    ("Riften", "Rawl'kha", "Falvis Raram"),
    ("Riften", "Evermore", "Falvis Raram"),


    # DC - Azoufah

    ("Daggerfall", "Wayrest", "Azoufah"),
    ("Daggerfall", "Evermore", "Azoufah"),
    ("Daggerfall", "Vulkhel Guard", "Azoufah"),
    ("Daggerfall", "Davon's Watch", "Azoufah"),

    ("Wayrest", "Shornhelm", "Azoufah"),
    ("Wayrest", "Daggerfall", "Azoufah"),
    ("Wayrest", "Elden Root", "Azoufah"),
    ("Wayrest", "Mournhold", "Azoufah"),

    ("Shornhelm", "Sentinel", "Azoufah"),
    ("Shornhelm", "Wayrest", "Azoufah"),
    ("Shornhelm", "Woodhearth", "Azoufah"),
    ("Shornhelm", "Stormhold", "Azoufah"),

    ("Sentinel", "Evermore", "Azoufah"),
    ("Sentinel", "Shornhelm", "Azoufah"),
    ("Sentinel", "Vulkwasten", "Azoufah"),
    ("Sentinel", "Windhelm", "Azoufah"),

    ("Evermore", "Daggerfall", "Azoufah"),
    ("Evermore", "Sentinel", "Azoufah"),
    ("Evermore", "Rawl'kha", "Azoufah"),
    ("Evermore", "Riften", "Azoufah"),

    # TODO Morrowind - Check Morrowind
    # Captain Jenassa
    ("Elden Root", "Seyda Neen", "Captain Jenassa"),
    ("Elden Root", "Vivec", "Captain Jenassa"),

    ("Daggerfall", "Seyda Neen", "Captain Jenassa"),
    ("Daggerfall", "Vivec", "Captain Jenassa"),

    ("Davon's Watch", "Seyda Neen", "Captain Jenassa"),
    ("Davon's Watch", "Vivec", "Captain Jenassa"),

    ("Stormhold", "Seyda Neen", "Captain Jenassa"),
    ("Stormhold", "Vivec", "Captain Jenassa"),

    # Bolnora Romavel
    ("Tel Mora", "Sadrith Mora", "Bolnora Romavel"),

    # Ranor Sadralo
    ("Gnisis", "Sadrith Mora", "Bolnora Romavel"),

    # Rinori Mathendis
    ("Sadrith Mora", "Gnisis", "Rinori Mathendis"),
    ("Sadrith Mora", "Tel Mora", "Rinori Mathendis"),
    ("Sadrith Mora", "Vivec", "Rinori Mathendis"),

    # Synda Imyam
    ("Vivec", "Sadrith Mora", "Synda Imyam"),
    ("Vivec", "Elden Root", "Synda Imyam"),
    ("Vivec", "Mournhold", "Synda Imyam"),
    ("Vivec", "Wayrest", "Synda Imyam"),

    # TODO - CHECK Summerset - Ciryelda - also found in Stros M'Kai?
    ("Bleakrock Isle", "Alinor", "Ciryelda"),
    ("Davon's Watch", "Alinor", "Ciryelda"),

    ("Elden Root", "Alinor", "Ciryelda"),
    ("Mournhold", "Alinor", "Ciryelda"),
    ("Wayrest", "Alinor", "Ciryelda"),

    ("Alinor", "Elden Root", "Ciryelda"),
    ("Alinor", "Mournhold", "Ciryelda"),
    ("Alinor", "Wayrest", "Ciryelda")
]


carriages = []

# TODO Carts was rushed, needs checking

CART_LABEL = "Self-driven Cart"

carts = [
    # Wrothgar
    ("Orsinium", "Vulkhel Guard", CART_LABEL),
    ("Orsinium", "Daggerfall", CART_LABEL),
    ("Orsinium", "Davon's Watch", CART_LABEL),

    ("Vulkhel Guard", "Orsinium", CART_LABEL),
    ("Wayrest", "Orsinium", CART_LABEL),
    ("Daggerfall", "Orsinium", CART_LABEL),

    # Craglorn

    ("Belkarth", "Mournhold", CART_LABEL),
    ("Belkarth", "Wayrest", CART_LABEL),
    ("Belkarth", "Elden Root", CART_LABEL),

    ("Mournhold", "Belkarth", CART_LABEL),
    ("Wayrest", "Belkarth", CART_LABEL),
    ("Elden Root", "Belkarth", CART_LABEL),
]

# TODO ZTP was rushed, needs checking

ZTP_LABEL = "Zone Transition Point"

zone_transition_points = [

    # DC
    ("Glenumbra", "Stormhaven", ZTP_LABEL),
    ("Stormhaven", "Glenumbra", ZTP_LABEL),

    ("Rivenspire", "Stormhaven", ZTP_LABEL),
    ("Stormhaven", "Rivenspire", ZTP_LABEL),

    ("Stormhaven", "Wrothgar", ZTP_LABEL),
    ("Wrothgar", "Stormhaven", ZTP_LABEL),

    ("Stormhaven", "Bangkorai", ZTP_LABEL),
    ("Bangkorai", "Stormhaven", ZTP_LABEL),

    ("Bangkorai", "Wrothgar", ZTP_LABEL),
    ("Wrothgar", "Bangkorai", ZTP_LABEL),

    ("Craglorn", "Bangkorai", ZTP_LABEL),
    ("Bangkorai", "Craglorn", ZTP_LABEL),

    # AD

    ("Grahtwood", "Reaper's March", ZTP_LABEL),
    ("Reaper's March", "Grahtwood", ZTP_LABEL),

    ("Malabal Tor", "Reaper's March", ZTP_LABEL),
    ("Reaper's March", "Malabal Tor", ZTP_LABEL),

    ("Malabal Tor", "Grahtwood", ZTP_LABEL),
    ("Grahtwood", "Malabal Tor", ZTP_LABEL),

    ("Malabal Tor", "Greenshade", ZTP_LABEL),
    ("Greenshade", "Malabal Tor", ZTP_LABEL),

    ("Greenshade", "Grahtwood", ZTP_LABEL),
    ("Grahtwood", "Greenshade", ZTP_LABEL),

    # EP

    ("East March", "The Rift", ZTP_LABEL),
    ("The Rift", "East March", ZTP_LABEL),

    ("The Rift", "Stonefalls", ZTP_LABEL),
    ("Stonefalls", "The Rift", ZTP_LABEL),

    ("Stonefalls", "Bal Foyen", ZTP_LABEL),
    ("Bal Foyen", "Stonefalls", ZTP_LABEL),

    ("Stonefalls", "Deshaan", ZTP_LABEL),
    ("Deshaan", "Stonefalls", ZTP_LABEL),

    ("Deshaan", "Shadowfen", ZTP_LABEL),
    ("Shadowfen", "Deshaan", ZTP_LABEL)
]

mage_guild_portals = []
