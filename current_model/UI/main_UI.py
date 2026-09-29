from .menu.state import *
from .menu.main_menu.menu import *
from .menu.config_menu.config_menu import *
from .menu.collisions_menu.collision_menu import *


class UI():
    
    def __init__(self,camera,group_0_objects,group_1_objects):
        
        self.main_menu = menu(group_0_objects,group_1_objects)
        self.collision_menu = collision_menu()
        self.config_menu = config_menu(group_0_objects,self.collision_menu)
        
        self.camera = camera
        


    def draw_UI(self,sim_settings,player):

        pr.draw_text(f"fps = {pr.get_fps()}", 1010, 10, 20, sim_settings.Get_colour("time_scale"))
        

        pr.draw_text(f"time scale = x{sim_settings.time_scale}", 10, 10, 20, sim_settings.Get_colour("time_scale"))
        pr.draw_text(f"substeps = {sim_settings.substeps}", 10, 40, 20, sim_settings.Get_colour("substeps"))
        pr.draw_text(f"display scale = x{sim_settings.display_scale}", 10, 70, 20, sim_settings.Get_colour("display_scale"))
        pr.draw_text(f"target frames = {sim_settings.target_frames}", 10, 100 , 20, sim_settings.Get_colour("target_frames"))
        pr.draw_text(f"player speed x{player.speed}", 10, 130 , 20, sim_settings.Get_colour("player speed"))
        pr.draw_text(f"group 0 integrator = {sim_settings.get_integrator("0")}", 10, 160 , 20 ,sim_settings.Get_colour("group 0 integrator"))
        pr.draw_text(f"group 1 integrator = {sim_settings.get_integrator("1")}", 10, 190 , 20 ,sim_settings.Get_colour("group 1 integrator"))
        pr.draw_text(f"start = {sim_settings.start}", 10, 220 , 20 ,sim_settings.Get_colour("start"))
        pr.draw_text(f"test start = {sim_settings.test_start}", 10, 250 , 20 ,sim_settings.Get_colour("test start"))
        pr.draw_text(f"elasped time = {sim_settings.elapsed_time:.5f}", 10, 280 , 20 ,sim_settings.Get_colour("elapsed time"))
        pr.draw_text(f"target time = {sim_settings.simulation_duration}", 10, 310 , 20 ,sim_settings.Get_colour("sim duratiion"))



        if self.main_menu.state.menu_open:
            self.main_menu.draw_menu(self.config_menu,sim_settings)

        if self.config_menu.state.menu_open:
            pr.draw_rectangle(1160,70,420,600,pr.Color(50,50,50,200))    
            pr.draw_rectangle_lines(1160,70,420,600,pr.GRAY)
            pr.draw_text("Input Planet Parameters", 1160 + 10, 80, 20, pr.WHITE)

            self.config_menu.draw(self.camera)

            pr.draw_rectangle(70,70,420,150,pr.DARKGRAY)
            pr.draw_text("create new planet", 90, 100, 40, pr.WHITE)
        
        if self.collision_menu.state.menu_open:
            self.collision_menu.draw_menu(sim_settings)