from entities.Planet import *
from .preset_1 import preset_1
from .preset_2 import preset_2

class Preset():
    presets = {
        "preset_1": preset_1,
        "preset_2": preset_2,
        "preset_3": None
    }

    

    def load(self, name):
        return self.presets[name]()
    

  


