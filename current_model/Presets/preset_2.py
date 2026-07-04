import pyray as pr
from Presets.make_planet import make_planet


class preset_2():

    def __init__(self):

        self.planets = [
            #                radius Mm   position Mm                  yaw  pitch  density g/cm3  speed km/s   colour            id
            make_planet(     696,        pr.Vector3(0,0,0),            0,   0,     1.408,          0,          pr.YELLOW,        "sun"),
            make_planet(     2.4397,     pr.Vector3(57900,0,0),        0,   0,     5.427,          47.36,      pr.GRAY,          "mercury"),
            make_planet(     6.0518,     pr.Vector3(108200,0,0),       0,   0,     5.243,          35.02,      pr.ORANGE,        "venus"),
            make_planet(     6.371,      pr.Vector3(149600,0,0),       0,   0,     5.514,          29.78,      pr.BLUE,          "earth"),
            make_planet(     3.3895,     pr.Vector3(227900,0,0),       0,   0,     3.9335,         24.07,      pr.RED,           "mars"),
            make_planet(     69.911,     pr.Vector3(778500,0,0),       0,   0,     1.326,          13.07,      pr.BEIGE,         "jupiter"),
            make_planet(     58.232,     pr.Vector3(1433500,0,0),      0,   0,     0.687,          9.68,       pr.GOLD,          "saturn"),
            make_planet(     25.362,     pr.Vector3(2872500,0,0),      0,   0,     1.271,          6.80,       pr.SKYBLUE,       "uranus"),
            make_planet(     24.622,     pr.Vector3(4495100,0,0),      0,   0,     1.638,          5.43,       pr.DARKBLUE,      "neptune"),
        ]

