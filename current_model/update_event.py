import pyray as pr

def update_event_menu(ui):

    if pr.is_key_pressed(pr.KEY_O):
                ui.main_menu.state.toggle_menu()

                if ui.main_menu.state.menu_open:
                    pr.enable_cursor()
                else:
                    pr.disable_cursor()

    if not ui.main_menu.state.menu_open:
        ui.config_menu.state.menu_open = False
          



    