import pyray as pr 
from UI.menu.main_menu.menu import *
from UI.menu.state import *
from grid.grid import *
from entities.Player import *
from entities.Planet import *
from physics.simulation.simulate import *
from physics.collisions import *
from physics.total_energy import calc_total_energy
from UI.main_UI import *
from update_event import *
from physics.simulation.simulate_settings import *
from data.gathered_data import *
from data.calculate_percentage_loss import *


class Game():

    def __init__(self):

        self.camera = pr.Camera3D(
                        (2,1,2),                #position(x,y,z)
                        (0,0,0),                #target(x,y,z)       
                        (0,1,0),                #up(x,y,z)
                        60,                     #fov
                        pr.CAMERA_PERSPECTIVE)  #projection
        
        self.group_0_objects = []
        self.group_1_objects = []
        self.player = Player(500)
        self.sim_settings = Sim_settings()
        self.ui = UI(self.camera,self.group_0_objects,self.group_1_objects)
        self.temp_fps = 0
        pr.disable_cursor()
        
        

    def start_game_loop(self):
        

        while not pr.window_should_close():
            
            if self.sim_settings.target_frames != self.temp_fps:
                pr.set_target_fps(self.sim_settings.target_frames)
                self.temp_fps = self.sim_settings.target_frames

            update_event_menu(self.ui)

            
            
            if not self.ui.main_menu.state.menu_open and not self.ui.collision_menu.state.menu_open:

                update_event_sim_settings(self.sim_settings,self.group_0_objects,self.group_1_objects)

                self.player.update()



                if self.sim_settings.start:

                    if len(self.group_0_objects) > 0:
                        simulate(self.group_0_objects,self.sim_settings,"0")

                    if len(self.group_1_objects) > 0:
                        simulate(self.group_1_objects,self.sim_settings,"1")
    


                    if self.sim_settings.test_start:
                        self.sim_settings.elapsed_time += pr.get_frame_time()

                        if len(self.group_0_objects) > 0:
                            self.sim_settings.group_0_current_total_system_energy = calc_total_energy(self.group_0_objects)
                            group_0_percentage_loss = calc_percentage_loss(self.group_0_objects,self.sim_settings,"0")
                            self.sim_settings.group_0_gathered_data.add_data(group_0_percentage_loss,self.sim_settings.elapsed_time)

                        if len(self.group_1_objects) > 0:
                            self.sim_settings.group_1_current_total_system_energy = calc_total_energy(self.group_1_objects)
                            group_1_percentage_loss = calc_percentage_loss(self.group_1_objects,self.sim_settings,"1")
                            self.sim_settings.group_1_gathered_data.add_data(group_1_percentage_loss,self.sim_settings.elapsed_time)

                    
                self.player.camera_update(self.camera)
            
        

            pr.begin_drawing()
            pr.clear_background(pr.BLACK)
            pr.begin_mode_3d(self.camera)


            grid()


            if len(self.group_0_objects) > 0:
                for planet in self.group_0_objects:
                    planet.draw(self.sim_settings,"0")

            if len(self.group_1_objects) > 0:
                            for planet in self.group_1_objects:
                                planet.draw(self.sim_settings,"1")
                    


       
            pr.end_mode_3d()

            if len(self.group_0_objects) > 0:
                for planet in self.group_0_objects:
                    planet.draw_label(self.camera,self.sim_settings)

            if len(self.group_1_objects) > 0:
                            for planet in self.group_1_objects:
                                planet.draw_label(self.camera,self.sim_settings)
            

            self.ui.draw_UI(self.sim_settings,self.player)

                                
                
            pr.end_drawing()
