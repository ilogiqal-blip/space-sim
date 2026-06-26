import pyray as pr

class get_main_menu_option():

    def __init__(self):
        self.start = pr.Vector2(70,70)
        self.lenght= pr.Vector2(420,150)
        
    def get_option_hovered(self):
        mouse_pos = pr.get_mouse_position()

        if (self.start.x < mouse_pos.x < self.start.x + self.lenght.x) and (self.start.y < mouse_pos.y < self.start.y + self.lenght.y):
            return "create new planet"
        elif (self.start.x < mouse_pos.x < self.start.x + self.lenght.x) and (self.start.y +180 < mouse_pos.y < self.start.y + self.lenght.y +180):
            return "reset"
        elif (self.start.x < mouse_pos.x < self.start.x + self.lenght.x) and (self.start.y +360 < mouse_pos.y < self.start.y + self.lenght.y +360):
            return "preset"