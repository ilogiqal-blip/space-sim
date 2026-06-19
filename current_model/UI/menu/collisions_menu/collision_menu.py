from ..state import * 
import pyray as pr

class collision_menu():

    def __init__(self):
        self.menu_open = menu_state()
        self.screen_size = pr.Vector2(pr.get_screen_height,pr.get_screen_width)
        self.menu_size = pr.Vector2(100,100)

    def draw_menu(self):
        pr.draw_rectangle((self.screen_size.x/2) - (self.menu_size.x),(self.screen_size.y/2)-(self.menu_size.y))
