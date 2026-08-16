import pyray as pr
from physics.total_energy import *


def calc_percentage_loss(objects,sim_settings):
                        percentage_loss = 0
                        difference = 0
                        dt = pr.get_frame_time() 
                        sim_settings.elapsed_time += dt 
    
                        sim_settings.current_total_system_energy = calc_total_energy(objects)
    
                        difference = sim_settings.current_total_system_energy - sim_settings.initial_total_system_energy
                        
    
                        if sim_settings.initial_total_system_energy == 0:
                            percentage_loss = 0
                        else:
                            percentage_loss = (difference/sim_settings.initial_total_system_energy) * 100
    
                        #print(f"difference = {difference}")
                        #print(f"elapsed time = {sim_settings.elapsed_time}")
                        #print(f"% loss = {percentage_loss}")

                        return percentage_loss 