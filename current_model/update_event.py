import pyray as pr
from physics.collisions import *
from physics.total_energy import *
from data.matplot_graphs import *



def update_event_menu(ui):

    if pr.is_key_pressed(pr.KEY_O):
                ui.main_menu.state.toggle_state()

                if ui.main_menu.state.menu_open:
                    pr.enable_cursor()
                else:
                    pr.disable_cursor()

    if not ui.main_menu.state.menu_open:
        ui.config_menu.state.menu_open = False
          

def update_event_sim_settings(sim_settings,group_0_objects,group_1_objects):
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

     if mode == "group 0 integrator" and not sim_settings.test_start:
          if change == "increase" and sim_settings.group_0_integrator_value < 2:
               sim_settings.group_0_integrator_value += 1
          elif change == "decrease" and sim_settings.group_0_integrator_value > 0:
               sim_settings.group_0_integrator_value -= 1

     if mode == "group 1 integrator" and not sim_settings.test_start:
               if change == "increase" and sim_settings.group_1_integrator_value < 2:
                    sim_settings.group_1_integrator_value += 1
               elif change == "decrease" and sim_settings.group_1_integrator_value > 0:
                    sim_settings.group_1_integrator_value -= 1

     if mode == "start":
          if change == "increase":
               sim_settings.start = True
          if change == "decrease" and not sim_settings.test_start:
               sim_settings.start = False

     if mode == "test start":
          if change == "increase":
               sim_settings.test_start = True
               sim_settings.start = True     

          if not sim_settings.test_start and pr.is_key_pressed(pr.KEY_BACKSPACE):

               sim_settings.test_start = False
               sim_settings.start = False
               sim_settings.elapsed_time = 0

               sim_settings.group_0_initial_total_system_energy = 0
               sim_settings.group_0_current_total_system_energy = 0

               sim_settings.group_1_initial_total_system_energy = 0
               sim_settings.group_1_current_total_system_energy = 0

               sim_settings.group_0_gathered_data.clear_data()
               sim_settings.group_1_gathered_data.clear_data()
     

          elif change == "decrease":
               sim_settings.test_start = False
               sim_settings.start = False


     if sim_settings.test_start:
          group_0_energy = calc_total_energy(group_0_objects)
          group_1_energy = calc_total_energy(group_1_objects)
          
          if sim_settings.elapsed_time == 0:
               sim_settings.group_0_initial_total_system_energy = group_0_energy
               sim_settings.group_1_initial_total_system_energy = group_1_energy

               

          
     if pr.is_key_pressed(pr.KEY_I):

          plot_graph(
               sim_settings.group_0_gathered_data,
               sim_settings.group_1_gathered_data,
               sim_settings.get_integrator("0"),
               sim_settings.get_integrator("1"),
          )

          sim_settings.test_start = False
          sim_settings.start = False


     

     if sim_settings.elapsed_time > sim_settings.simulation_duration and sim_settings.test_start:
          

          sim_settings.start = False

          sim_settings.elapsed_time = 0

          sim_settings.test_start = False

          sim_settings.gathered_data.clear_data()


     
          


    