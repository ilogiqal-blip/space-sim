import pyray as pr

class Sim_settings():
    def __init__(self):
        self.time_scale = 1.0 # we want it to apply the gravity 20 times so the "frame time "
        self.substeps = 20  # is now divided by 20 as its 20 times per frame
        self.display_scale = 1.0
        self.target_frames = 60
        self.simulation_start = False
        self.initial_total_system_energy = 0

        self.mode_value = 0
        self.mode = [
            "time_scale",
            "substeps",
            "display_scale",
            "target_frames",
            "integrator",
            "sim start"
        ]

        self.integrator_value = 0
        self.integrator = [
            "eular",
            "RK4",
            "velocity verlet"
        ]
        
    def get_mode(self):
        return self.mode[self.mode_value]
    
    def Get_colour(self,other):
        if self.get_mode() == other:
            return pr.GREEN
        else:
            return pr.WHITE
        
    def get_integrator(self):
        return self.integrator[self.integrator_value]

