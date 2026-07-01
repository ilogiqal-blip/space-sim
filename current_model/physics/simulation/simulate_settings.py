
class Sim_settings():
    def __init__(self):
        self.time_scale = 10000 # we want it to apply the gravity 20 times so the "frame time "
        self.substeps = 20  # is now divided by 20 as its 20 times per frame
        self.display_scale = 1