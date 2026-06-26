from .menu.state import *
from .menu.main_menu.menu import *
from .menu.config_menu.config_menu import *
from .menu.collisions_menu.collision_menu import *


class UI():
    
    def __init__(self,camera,objects):
        
        self.main_menu = menu(objects)
        self.collision_menu = collision_menu()
        self.config_menu = config_menu(objects,self.collision_menu)
        self.camera = camera
        


    def draw_UI(self):


        if self.main_menu.state.menu_open:
            self.main_menu.draw_menu(self.config_menu)

        if self.config_menu.state.menu_open:
            pr.draw_rectangle(1160,70,420,600,pr.Color(50,50,50,200))    
            pr.draw_rectangle_lines(1160,70,420,600,pr.GRAY)
            pr.draw_text("Input Planet Parameters", 1160 + 10, 80, 20, pr.WHITE)

            self.config_menu.draw(self.camera)

            pr.draw_rectangle(70,70,420,150,pr.DARKGRAY)
            pr.draw_text("create new planet", 90, 100, 40, pr.WHITE)
        
        if self.collision_menu.state.menu_open:
            self.collision_menu.draw_menu()