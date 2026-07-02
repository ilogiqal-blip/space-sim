import pyray as pr
from physics.collisions import *


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

def update_event_sim_settings(sim_settings):
    change = None
    mode = sim_settings.get_mode()

    if pr.is_key_pressed(pr.KEY_DOWN) and (sim_settings.mode_value < len(sim_settings.mode)):
         sim_settings.mode_value += 1
    elif pr.is_key_pressed(pr.KEY_UP) and (sim_settings.mode_value > 0):
         sim_settings.mode_value -= 1


    if pr.is_key_pressed(pr.KEY_RIGHT):
         change = "increase"
    elif pr.is_key_pressed(pr.KEY_LEFT):
         change = "decrease"
    else:
         change = None

    if mode == "time_scale":
         if change == "increase":
              sim_settings.time_scale *= 10
         elif change == "decrease":
              sim_settings.time_scale /= 10 

    elif mode == "substeps":
         if change == "increase":
              sim_settings.substeps += 10
         elif change == "decrease" and sim_settings.substeps > 10:
              sim_settings.substeps -= 10

    elif mode == "display_scale":
         if change == "increase":
              sim_settings.display_scale *= 2
         elif change == "decrease":
              sim_settings.display_scale /= 2   


    