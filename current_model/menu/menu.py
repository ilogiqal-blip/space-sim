import pyray as pr 
from .config_menu.config_menu import * 
from .state import *
from .config_menu.get_input import *



class menu():
    def __init__(self,camera,objects):
        self.config_menu_open = menu_state()
        self.config_menu = config_menu(objects)
        self.objects = objects
        self.camera = camera
        self.input = get_menu_option()
        self.start_x = 600 + 550
        self.start_y = 70

    
     

    def draw_menu(self):
    
        pr.draw_rectangle(50,50,460,700,pr.Color(50,50,50,125))
        pr.draw_rectangle_lines(50,50,460,700,pr.DARKGRAY)

        mouse_pos = pr.get_mouse_position()
    
        if (70 < mouse_pos.x < 490) and ( 70< mouse_pos.y <220):
            pr.draw_rectangle(70,70,420,150,pr.DARKGRAY)
            pr.draw_rectangle_lines(70,70,420,150,pr.GRAY)
            pr.draw_text("create new planet", 90, 100, 40, pr.WHITE)
        
            if pr.is_mouse_button_released(pr.MOUSE_BUTTON_LEFT):
                self.config_menu_open.toggle_side_menu()
        else:
            pr.draw_rectangle(70,70,420,150,pr.GRAY)
            pr.draw_text("create new planet", 90, 100, 40, pr.WHITE)
    

        if self.config_menu_open.menu_open:
            pr.draw_rectangle(self.start_x,self.start_y,420,600,pr.Color(50,50,50,200))
            pr.draw_rectangle_lines(self.start_x,self.start_y,420,600,pr.GRAY)
            pr.draw_text("Input Planet Parameters", self.start_x + 10, 80, 20, pr.WHITE)

            self.config_menu.draw(mouse_pos,self.camera,)
            #check_mouse_input()
            #check_button_input()


            pr.draw_rectangle(70,70,420,150,pr.DARKGRAY)
            pr.draw_text("create new planet", 90, 100, 40, pr.WHITE)
    

    

########################################################################## reset button
        if (70 < mouse_pos.x < 490) and ( 250< mouse_pos.y <400):

            pr.draw_rectangle(70,250,420,150,pr.DARKGRAY)
            pr.draw_rectangle_lines(70,250,420,150,pr.GRAY)
            pr.draw_text("reset simulation", 90, 280, 40, pr.WHITE)
        

            if pr.is_mouse_button_released(pr.MOUSE_BUTTON_LEFT):

                self.objects.clear()

        else:
            pr.draw_rectangle(70,250,420,150,pr.GRAY)
            pr.draw_text("reset simulation", 90, 280, 40, pr.WHITE)




