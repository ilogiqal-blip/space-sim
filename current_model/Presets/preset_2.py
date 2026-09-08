import pyray as pr
from Presets.make_planet import make_planet
from vector.vector import *


class preset_2():

    def __init__(self):

        self.planets = [

    #              radius Mm   position Mm             yaw  pitch  density g/cm3   speed km/s   colour      id

    make_planet(   20,         Vector3(-100,0,0),   0,  0,     1.0,             2,      pr.RED,     "planet1"),

    make_planet(   20,         Vector3(100,0,0),    -180, 0,     1.0,             2,      pr.BLUE,    "planet2"),

]

