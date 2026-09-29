import pyray as pr
from Presets.make_planet import make_planet
from vector.vector import *


class preset_4(): ## figure 8

    def __init__(self):

        self.planets = [

    #              radius Mm   position Mm                      yaw      pitch  density g/cm3   speed km/s   colour        id

    make_planet(   20,         Vector3(210.740, 0, -52.810),  132.843,   0,     1.0,            2.0401,   pr.RED,      "planet1"),

    make_planet(   20,         Vector3(-210.740, 0, 52.810),  132.843,   0,     1.0,            2.0401,   pr.GREEN,    "planet2"),

    make_planet(   20,         Vector3(0, 0, 0),              312.843,   0,     1.0,            4.0802,   pr.BLUE,     "planet3"),

]