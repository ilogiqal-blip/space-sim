import pyray as pr
from Presets.make_planet import make_planet
from vector.vector import *

class preset_5():

    def __init__(self): # intermediate-mass black hole (1000 solar masses) and earth

        self.planets = [
            #radius Mm, position Mm, yaw_deg, pitch_deg, density g/cm3, speed km/s, colour, planet_id
            make_planet(2.95, Vector3(0,0,0), 0, 0, 1.85e10, 0, pr.BLACK, "black_hole"),
            make_planet(6.371, Vector3(20000,0,0), 0, 0, 5.51, 1288, pr.BLUE, "earth"),
            make_planet(69.911, Vector3(40000,0,0), 0, 0, 1.326, 911, pr.ORANGE, "jupiter"),
        ]