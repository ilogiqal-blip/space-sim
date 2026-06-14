import pyray as pr

class menu_state():

    def __init__(self):
        self.menu_open = False

    def toggle_menu(self):
        self.menu_open  = not self.menu_open

    def toggle_side_menu(self):
        self.menu_open = not self.menu_open

    
    
