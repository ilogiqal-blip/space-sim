import pyray as pr

class Sim_settings():
    def __init__(self):
        self.time_scale = 10000 # we want it to apply the gravity 20 times so the "frame time "
        self.substeps = 20  # is now divided by 20 as its 20 times per frame
        self.display_scale = 1

        self.mode_value = 0
        self.mode = [
            "time_scale",
            "substeps",
            "display_scale"
        ]
        
    def get_mode(self):
        return self.mode[self.mode_value]
    
    def Get_colour(self,other):
        if self.get_mode() == other:
            return pr.GREEN
        else:
            return pr.WHITE