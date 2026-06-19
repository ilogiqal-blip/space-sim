from .menu.state import *
from .menu.main_menu.menu import *
from .menu.config_menu.config_menu import *

class UI():
    
    def __init__(self,camera,objects):
        self.main_menu_state = menu_state()
        self.collision_menu_state = menu_state()
        self.main_menu = menu(camera,objects)


    def draw_UI(self):


        if self.main_menu_state.menu_open:
                self.main_menu.draw_menu()