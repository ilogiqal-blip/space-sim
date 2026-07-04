import pyray as pr
from Presets.make_planet import make_planet


class preset_1():

    def __init__(self):

        self.planets = [
            #radius Mm, position Mm, yaw_deg, pitch_deg, density g/cm3, speed km/s, colour, planet_id
            make_planet(696, pr.Vector3(0,0,0), 0, 0, 1.408, 0, pr.YELLOW, "sun"),
            make_planet(6.371, pr.Vector3(149600,0,0), 0, 0, 5.51, 29.78, pr.BLUE, "earth"),
            make_planet(1.737, pr.Vector3(149984.4,0,0), 0, 0, 3.344, 30.802, pr.GRAY, "moon"),
        ]

