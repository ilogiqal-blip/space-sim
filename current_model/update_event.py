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
    
        


    