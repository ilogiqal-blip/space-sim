from ..state import * 
import pyray as pr

class collision_menu():

    
    def __init__(self):
        self.height = pr.get_screen_height()
        self.width = pr.get_screen_width()
        self.menu_open = menu_state()
        self.screen_size = pr.Vector2(self.width, self.height)
        self.menu_size = pr.Vector2(400, 400)
        self.state = menu_state()

    def draw_menu(self):
        pr.draw_rectangle(
            int((self.screen_size.x - self.menu_size.x) / 2),
            int((self.screen_size.y - self.menu_size.y) / 2),
            int(self.menu_size.x),
            int(self.menu_size.y),
            pr.WHITE
        )