import pyray as pr
from Presets.make_planet import make_planet


class preset_1():

    def __init__(self):

        self.planets = [
            #radius Mm, position Mm, yaw_deg, pitch_deg, density g/cm3, speed km/s, colour, planet_id
            make_planet(6.371, pr.Vector3(0,0,0), 0, 0, 5.51, 0, pr.BLUE, "Earth"),
            make_planet(1.737, pr.Vector3(384.4,0,0), 0, 0, 3.344, 1.022, pr.GRAY, "Moon"),
        ]

