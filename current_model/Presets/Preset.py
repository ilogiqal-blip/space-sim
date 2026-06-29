from entities.Planet import *
from .preset_1 import preset_1

class Preset():
    presets = {
        "preset_1": preset_1,
        "preset_2": None,
        "preset_3": None
    }

    

    def load(self, name):
        return self.presets[name]()
    

  


