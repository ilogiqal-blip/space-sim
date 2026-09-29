import pyray as pr
from Presets.make_planet import make_planet
from vector.vector import *


class preset_3():

    def __init__(self): ## triangle 3 body problem 

        self.planets = [

    #              radius Mm   position Mm                    yaw    pitch  density g/cm3   speed km/s   colour        id

    make_planet(   20,         Vector3(115.47, 0, 0),       90,    0,     1.0,             3.34,    pr.RED,      "planet1"),

    make_planet(   20,         Vector3(-57.74, 100, 0),      210,   0,     1.0,             3.34,    pr.GREEN,    "planet2"),

    make_planet(   20,         Vector3(-57.74, -100, 0),     330,   0,     1.0,             3.34,    pr.BLUE,     "planet3"),

]