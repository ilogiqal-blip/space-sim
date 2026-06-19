import pyray as pr 
from UI.menu.main_menu.menu import *
from UI.menu.state import *
from grid.grid import *
from entities.Player import *
from entities.Planet import *
from physics.simulate import *
from physics.collisions import *
from UI.main_UI import *
from update_event import *

class Game():

    def __init__(self):

        self.camera = pr.Camera3D(
                        (2,1,2),                #position(x,y,z)
                        (0,0,0),                #target(x,y,z)       
                        (0,1,0),                #up(x,y,z)
                        60,                     #fov
                        pr.CAMERA_PERSPECTIVE)  #projection
        
        self.objects = []
        self.player = Player(500)
        self.ui = UI(self.camera,self.objects)
        pr.disable_cursor()

    def start_game_loop(self):

        while not pr.window_should_close():

            update_event_menu(self.ui)


            if not self.ui.main_menu.state.menu_open: 
                self.player.update()
                simulate(self.objects)
                self.player.camera_update(self.camera)
            
        

            pr.begin_drawing()
            pr.clear_background(pr.BLACK)
            pr.begin_mode_3d(self.camera)


            grid(self.objects)


            if len(self.objects) > 0:
                for planet in self.objects:
                    planet.draw()


       
            pr.end_mode_3d()

            self.ui.draw_UI()
                
            pr.end_drawing()
