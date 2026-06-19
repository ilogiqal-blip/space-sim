import pyray as pr


class get_menu_option():

    def __init__(self):
        self.start_x = 610 + 550
        self.start_y = 130
        self.cooldown = 0
        

    def get_option_hovered(self):
        self.mouse_pos = pr.get_mouse_position()

        if (self.start_x < self.mouse_pos.x < self.start_x + 100) and (self.start_y < self.mouse_pos.y < self.start_y + 20):
            return "r"
        elif (self.start_x < self.mouse_pos.x < self.start_x + 100) and (self.start_y + 50 < self.mouse_pos.y < self.start_y + 70):              
            return "d"
        elif (self.start_x < self.mouse_pos.x < self.start_x + 120) and (self.start_y + 100 < self.mouse_pos.y < self.start_y + 120):              
            return "x"
        elif (self.start_x < self.mouse_pos.x < self.start_x + 120) and (self.start_y + 150 < self.mouse_pos.y < self.start_y + 170):              
            return "y"
        elif (self.start_x < self.mouse_pos.x < self.start_x + 120) and (self.start_y + 200 < self.mouse_pos.y < self.start_y + 220):              
            return "z"
        elif (self.start_x < self.mouse_pos.x < self.start_x + 120) and (self.start_y + 250 < self.mouse_pos.y < self.start_y + 270):              
            return "speed"
        elif (self.start_x < self.mouse_pos.x < self.start_x + 120) and (self.start_y + 300 < self.mouse_pos.y < self.start_y + 320):              
            return "direction_x"
        elif (self.start_x < self.mouse_pos.x < self.start_x + 120) and (self.start_y + 350 < self.mouse_pos.y < self.start_y + 370):
            return "direction_y"
        elif (70 < self.mouse_pos.x < 490) and ( 70< self.mouse_pos.y <220):
            return "create new planet"
        

    def menu_colour(self,menu_option):
        if menu_option is None:
            return
        elif menu_option == self.get_option_hovered():
            return pr.WHITE
        else:
            return pr.WHITE
        
    def menu_size(self,menu_option):
        big = 40
        small = 20
        if menu_option is None:
            return
        elif menu_option == self.get_option_hovered():
            return big

        else:
            return small     
        
    def add_input(self,check):

        if pr.is_key_pressed(pr.KEY_EQUAL):
            if check == self.get_option_hovered():
                return int(1)
        elif pr.is_key_pressed(pr.KEY_MINUS):
            if check == self.get_option_hovered():
                return int(-1)
            

        elif pr.is_mouse_button_down(pr.MOUSE_BUTTON_RIGHT):
            if check == self.get_option_hovered():
                if self.cooldown <= 0:
                    self.cooldown = 0.005
                    return int(-1)
                else:
                    self.cooldown -= pr.get_frame_time()
                    return 0
                
        elif pr.is_mouse_button_down(pr.MOUSE_BUTTON_LEFT):
            if check == self.get_option_hovered():
                if self.cooldown <= 0:
                    self.cooldown = 0.005
                    return int(1)
                else:
                    self.cooldown -= pr.get_frame_time()
                    return 0
        return 0

        

