import pyray as pr
from Presets.make_planet import make_planet
from vector.vector import *


class preset_3_1():

    def __init__(self): ## triangle 3 body problem chat gpt verison

        self.planets = [

    #              radius Mm   position Mm              yaw  pitch  density g/cm3   speed km/s   colour      id

    make_planet(   20,         Vector3(-100, 0, 0),     -90, 0,     1.0,             3.59,       pr.RED,     "planet1"),

    make_planet(   20,         Vector3(50, 86.60, 0),   150, 0,     1.0,             3.59,       pr.BLUE,    "planet2"),

    make_planet(   20,         Vector3(50, -86.60, 0),  30, 0,     1.0,             3.59,       pr.GREEN,   "planet3"),

]