import pyray as pr
from physics.total_energy import *


def calc_percentage_loss(objects,sim_settings,group):
    
    difference = 0

    if group == "0":
        difference = sim_settings.group_0_current_total_system_energy - sim_settings.group_0_initial_total_system_energy

        if sim_settings.group_0_initial_total_system_energy == 0:
            percentage_difference = 0
        else:
            percentage_difference = (difference/sim_settings.group_0_initial_total_system_energy) * 100

    elif group == "1":
        difference = sim_settings.group_1_current_total_system_energy - sim_settings.group_1_initial_total_system_energy
        if sim_settings.group_1_initial_total_system_energy == 0:
            percentage_difference = 0
        else:
            percentage_difference = (difference/sim_settings.group_1_initial_total_system_energy) * 100                    
    


    return percentage_difference 