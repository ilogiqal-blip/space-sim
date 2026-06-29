import pyray as pr
from Presets.make_planet import make_planet


class preset_1():

    def __init__(self):

        self.planets = [
            #radius, position, yaw_deg, pitch_deg, density, speed, colour, planet_id
            make_planet(20, pr.Vector3(0,0,0), 0, 0, 5, 0, pr.YELLOW, "sun"),
            make_planet(5, pr.Vector3(200,0,0), 0, 0, 3, 30, pr.BLUE, "earth"),
        ]

