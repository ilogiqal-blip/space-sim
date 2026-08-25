import pyray as pr
from Presets.make_planet import make_planet


class preset_2():

    def __init__(self):

        self.planets = [

            make_planet(696,pr.Vector3(0, 0, 0),0, 0,1.408,0,pr.YELLOW,"sun"),
            make_planet(6.371,pr.Vector3(149600, 0, 0),0, 0,5.514,29.78,pr.BLUE,"earth"),
        ]

