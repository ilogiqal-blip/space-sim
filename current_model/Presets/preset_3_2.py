import pyray as pr
from Presets.make_planet import make_planet
from vector.vector import *


class preset_3_2():

    def __init__(self): ## triangle 3 body problem chat gpt verison FIXED

        self.planets = [

    #              radius Mm   position Mm               yaw    pitch  density g/cm3   speed km/s   colour      id

    make_planet(   20,         Vector3(-100, 0, 0),        0.0,   0,     1.0,           3.5934,    pr.RED,     "planet1"),

    make_planet(   20,         Vector3(50, 0, 86.60),    240.0,   0,     1.0,           3.5934,    pr.BLUE,    "planet2"),

    make_planet(   20,         Vector3(50, 0, -86.60),   120.0,   0,     1.0,           3.5934,    pr.GREEN,   "planet3"),

]