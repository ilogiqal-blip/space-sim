import pyray as pr
from physics.collisions import *
from physics.total_energy import *
from data.data_display import *



def update_event_menu(ui):

    if pr.is_key_pressed(pr.KEY_O):
                ui.main_menu.state.toggle_state()

                if ui.main_menu.state.menu_open:
                    pr.enable_cursor()
                else:
                    pr.disable_cursor()

    if not ui.main_menu.state.menu_open:
        ui.config_menu.state.menu_open = False
          
def update_event_collision(ui,objects):
    
    if check_collision(objects):
        if not ui.collision_menu.state.menu_open:
            ui.collision_menu.state.toggle_state()

def update_event_sim_settings(sim_settings,objects,graph_texture):
     change = None
     mode = sim_settings.get_mode()

     if pr.is_key_pressed(pr.KEY_DOWN) and (sim_settings.mode_value < len(sim_settings.mode) - 1):
          sim_settings.mode_value += 1
     elif pr.is_key_pressed(pr.KEY_UP) and (sim_settings.mode_value > 0):
          sim_settings.mode_value -= 1


     if pr.is_key_pressed(pr.KEY_RIGHT):
          change = "increase"
     elif pr.is_key_pressed(pr.KEY_LEFT):
          change = "decrease"
     else:
         change = None

     if mode == "time_scale" and not sim_settings.test_start:
          if change == "increase":
               sim_settings.time_scale *= 10
          elif change == "decrease":
               sim_settings.time_scale /= 10 

     elif mode == "substeps" and not sim_settings.test_start:
          if change == "increase":
               sim_settings.substeps += 10
          elif change == "decrease" and sim_settings.substeps > 10:
               sim_settings.substeps -= 10

     elif mode == "display_scale":
          if change == "increase":
               sim_settings.display_scale *= 2
          elif change == "decrease":
               sim_settings.display_scale /= 2  

     if mode ==  "target_frames" and not sim_settings.test_start:
          if change == "increase":
               sim_settings.target_frames += 10
          elif change == "decrease":
               sim_settings.target_frames -= 10

     if mode == "integrator" and not sim_settings.test_start:
          if change == "increase" and sim_settings.integrator_value < 2:
               sim_settings.integrator_value += 1
          elif change == "decrease" and sim_settings.integrator_value > 0:
               sim_settings.integrator_value -= 1

     if mode == "start":
          if change == "increase":
               sim_settings.start = True
          if change == "decrease" and not sim_settings.test_start:
               sim_settings.start = False

     if mode == "test start":
          if change == "increase":
               sim_settings.test_start = True
               sim_settings.start = True
               sim_settings.show_data = False
               sim_settings.gathered_data.data = []

               energy = calc_total_energy(objects)
               sim_settings.initial_total_system_energy = energy
               sim_settings.current_total_system_energy = energy
               
               print(sim_settings.initial_total_system_energy,sim_settings.current_total_system_energy)
          
     if pr.is_key_pressed(pr.KEY_I):
          
          if sim_settings.show_data:
               sim_settings.show_data = False
          else:
               sim_settings.show_data = True 

     

     if sim_settings.elapsed_time > sim_settings.simulation_duration and sim_settings.test_start:
          sim_settings.show_data = True

          sim_settings.start = False

          sim_settings.elapsed_time = 0

          sim_settings.test_start = False

          sim_settings.initial_total_system_energy = 0
          sim_settings.current_total_system_energy = 0


          draw_graph(f"elapsed time",f"energy loss",sim_settings.gathered_data,graph_texture)
          #for i in range(len(sim_settings.gathered_data.data)):
          #        print(sim_settings.gathered_data.data[i])

     
          


    