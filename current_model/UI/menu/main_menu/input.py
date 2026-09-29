import pyray as pr

class get_main_menu_option():

    def __init__(self):
        self.start = pr.Vector2(70,70)
        self.lenght= pr.Vector2(420,150)
        
    def get_option_hovered(self):
        mouse_pos = pr.get_mouse_position()

        if (self.start.x < mouse_pos.x < self.start.x + self.lenght.x) and (70 < mouse_pos.y < 220):
            return "create new planet"
        elif (self.start.x < mouse_pos.x < self.start.x + self.lenght.x) and (250 < mouse_pos.y < 400):
            return "reset"
        elif (self.start.x < mouse_pos.x < self.start.x + self.lenght.x) and (430 < mouse_pos.y < 505):
            return "preset_1"
        elif (self.start.x < mouse_pos.x < self.start.x + self.lenght.x) and (535 < mouse_pos.y < 610):
            return "preset_2"
        elif (self.start.x < mouse_pos.x < self.start.x + self.lenght.x) and (640 < mouse_pos.y < 715):
            return "preset_3"
        elif (self.start.x < mouse_pos.x < self.start.x + self.lenght.x) and (745 < mouse_pos.y < 820):
            return "preset_4"