import pyray as pr 
from ..config_menu.config_menu import * 
from ..state import *
from .input import *
from Presets.Preset import *
from ..group_select.group_select import *


class menu():

    def __init__(self,group_0_objects,group_1_objects):
        self.config_menu_state = menu_state()
        self.group_0_objects = group_0_objects
        self.group_1_objects = group_1_objects
        self.start_x = 600 + 550
        self.start_y = 70
        self.input = get_main_menu_option()
        self.state = menu_state()
        self.preset = Preset()

    
     

    def draw_menu(self,config_menu,sim_settings):
    
        pr.draw_rectangle(50,50,460,800,pr.Color(50,50,50,125))
        pr.draw_rectangle_lines(50,50,460,800,pr.DARKGRAY)
 
        

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

                self.group_1_objects.clear()
                self.group_0_objects.clear()
                config_menu.config_reset(sim_settings)

        else:
            pr.draw_rectangle(70,250,420,150,pr.GRAY)
            pr.draw_text("reset simulation", 90, 280, 40, pr.WHITE)

########################################################################## preset button 1
        if self.input.get_option_hovered() == "preset_1":
            group = get_group(70,430)

            pr.draw_rectangle(70,430,420,75,pr.DARKGRAY)
            pr.draw_rectangle_lines(70,430,420,75,pr.GRAY)
            pr.draw_text("preset 1", 90, 450, 40, pr.WHITE)
        

            if group != -1:

                preset = self.preset.load("preset_1")
                if group == 0:
                    self.group_0_objects.extend(preset.planets)
                elif group == 1:
                    self.group_1_objects.extend(preset.planets)

        else:
            pr.draw_rectangle(70,430,420,75,pr.GRAY)
            pr.draw_text("preset 1", 90, 450, 40, pr.WHITE)

########################################################################## preset button 2
        if self.input.get_option_hovered() == "preset_2":

            group = get_group(70,535)

            pr.draw_rectangle(70,535,420,75,pr.DARKGRAY)
            pr.draw_rectangle_lines(70,535,420,75,pr.GRAY)
            pr.draw_text("preset 2", 90, 555, 40, pr.WHITE)
        

            if group != -1:

                preset = self.preset.load("preset_2")
                if group == 0:
                    self.group_0_objects.extend(preset.planets)
                elif group == 1:
                    self.group_1_objects.extend(preset.planets)

        else:
            pr.draw_rectangle(70,535,420,75,pr.GRAY)
            pr.draw_text("preset 2", 90, 555, 40, pr.WHITE)

########################################################################## preset button 3
        if self.input.get_option_hovered() == "preset_3":

            group = get_group(70,640)
        
            pr.draw_rectangle(70,640,420,75,pr.DARKGRAY)
            pr.draw_rectangle_lines(70,640,420,75,pr.GRAY)
            pr.draw_text("preset 3", 90, 660, 40, pr.WHITE)
                
        
            if group != -1:
        
                preset = self.preset.load("preset_3")
                if group == 0:
                    self.group_0_objects.extend(preset.planets)
                elif group == 1:
                    self.group_1_objects.extend(preset.planets)
        
        else:
            pr.draw_rectangle(70,640,420,75,pr.GRAY)
            pr.draw_text("preset 3", 90, 660, 40, pr.WHITE)

########################################################################## preset button 4
        if self.input.get_option_hovered() == "preset_4":

            group = get_group(70,745)
        
            pr.draw_rectangle(70,745,420,75,pr.DARKGRAY)
            pr.draw_rectangle_lines(70,745,420,75,pr.GRAY)
            pr.draw_text("preset 4", 90, 765, 40, pr.WHITE)
                
        
            if group != -1:
        
                preset = self.preset.load("preset_4")
                if group == 0:
                    self.group_0_objects.extend(preset.planets)
                elif group == 1:
                    self.group_1_objects.extend(preset.planets)
        
        else:
            pr.draw_rectangle(70,745,420,75,pr.GRAY)
            pr.draw_text("preset 4", 90, 765, 40, pr.WHITE)



