from entities.Planet import *
from .preset_1 import preset_1
from .preset_2 import preset_2
from .preset_3 import preset_3
from .preset_3_1 import preset_3_1
from .preset_3_2 import preset_3_2
from .preset_4 import preset_4
from .preset_4_1 import preset_4_1
from .preset_4_2 import preset_4_2
from .preset_5 import preset_5

class Preset():
    presets = {
        "preset_1": preset_1,
        "preset_2": preset_2,
        "preset_3": preset_5,
        "preset_4": preset_4
    }

    

    def load(self, name):
        return self.presets[name]()
    

  


