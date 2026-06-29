import pyray as pr 
from ..config_menu.config_menu import * 
from ..state import *
from .input import *
from Presets.Preset import *



class menu():

    def __init__(self,objects):
        self.config_menu_state = menu_state()
        self.objects = objects
        self.start_x = 600 + 550
        self.start_y = 70
        self.input = get_main_menu_option()
        self.state = menu_state()
        self.preset = Preset()

    
     

    def draw_menu(self,config_menu):
    
        pr.draw_rectangle(50,50,460,700,pr.Color(50,50,50,125))
        pr.draw_rectangle_lines(50,50,460,700,pr.DARKGRAY)
 
        

        if self.input.get_option_hovered() == "create new planet":
            pr.draw_rectangle(70,70,420,150,pr.DARKGRAY)
            pr.draw_rectangle_lines(70,70,420,150,pr.GRAY)
            pr.draw_text("create new planet", 90, 100, 40, pr.WHITE)
        
            if pr.is_mouse_button_released(pr.MOUSE_BUTTON_LEFT):
                config_menu.state.toggle_state()
        else:
            pr.draw_rectangle(70,70,420,150,pr.GRAY)
            pr.draw_text("create new planet", 90, 100, 40, pr.WHITE)
           
    

########################################################################## reset button
        if self.input.get_option_hovered() == "reset":

            pr.draw_rectangle(70,250,420,150,pr.DARKGRAY)
            pr.draw_rectangle_lines(70,250,420,150,pr.GRAY)
            pr.draw_text("reset simulation", 90, 280, 40, pr.WHITE)
        

            if pr.is_mouse_button_released(pr.MOUSE_BUTTON_LEFT):

                self.objects.clear()
                config_menu.config_reset()

        else:
            pr.draw_rectangle(70,250,420,150,pr.GRAY)
            pr.draw_text("reset simulation", 90, 280, 40, pr.WHITE)

########################################################################## preset button
        if self.input.get_option_hovered() == "preset":

            pr.draw_rectangle(70,430,420,150,pr.DARKGRAY)
            pr.draw_rectangle_lines(70,430,420,150,pr.GRAY)
            pr.draw_text("preset 1", 90, 450, 40, pr.WHITE)
        

            if pr.is_mouse_button_released(pr.MOUSE_BUTTON_LEFT):

                preset = self.preset.load("preset_1")
                self.objects.extend(preset.planets)

        else:
            pr.draw_rectangle(70,430,420,150,pr.GRAY)
            pr.draw_text("preset 1", 90, 450, 40, pr.WHITE)




