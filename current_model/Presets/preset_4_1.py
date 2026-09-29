import pyray as pr
from Presets.make_planet import make_planet
from vector.vector import *


class preset_4_1(): ## figure 8, hinged 45 degrees at one end

    def __init__(self):

        self.planets = [

    #              radius Mm   position Mm                          yaw       pitch     density g/cm3   speed km/s   colour        id

    make_planet(   20,         Vector3(210.740, 0.000, -52.810),   123.256,   28.739,   1.0,            2.0401,   pr.RED,      "planet1"),

    make_planet(   20,         Vector3(-210.740, 74.685, 21.875),  123.256,   28.739,   1.0,            2.0401,   pr.GREEN,    "planet2"),

    make_planet(   20,         Vector3(0.000, 37.342, -15.468),    303.256,  -28.739,   1.0,            4.0802,   pr.BLUE,     "planet3"),

]
