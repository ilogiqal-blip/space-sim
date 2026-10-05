import pyray as pr
from data.gathered_data import *

class Sim_settings():
    def __init__(self):
        self.time_scale = 1.0 # we want it to apply the gravity 20 times so the "frame time "
        self.substeps = 20  # is now divided by 20 as its 20 times per frame
        self.display_scale = 1.0
        self.target_frames = 60
        self.start = False
        self.test_start = False

        self.show_group_0 = True
        self.show_group_1 = True

        self.group_0_initial_total_system_energy = 0
        self.group_0_current_total_system_energy = 0

        self.group_1_initial_total_system_energy = 0
        self.group_1_current_total_system_energy = 0
        
        self.elapsed_time = 0
        self.group_0_gathered_data = gathered_data()
        self.group_1_gathered_data = gathered_data()
        self.simulation_duration = 1800
        self.unit_y_division = 1
        

        self.mode_value = 0
        self.mode = [
            "time_scale",
            "substeps",
            "display_scale",
            "target_frames",
            "group 0 integrator",
            "group 1 integrator",
            "start",
            "test start"
        ]

        self.group_0_integrator_value = 0
        self.group_1_integrator_value = 0

        self.integrator = [
            "euler",
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
        
    def get_integrator(self,group):
        if group == "0":
            return self.integrator[self.group_0_integrator_value]
        elif group == "1":
            return self.integrator[self.group_1_integrator_value]

