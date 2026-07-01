import pyray as pr
import math
from entities.Planet import *
from .input import *
from ..state import *



class config_menu():

    def __init__(self,objects,collision_menu):
        self.radius_Mm = 6
        self.density_g_cm3 = 5
        self.position_x = 0
        self.position_y = 0
        self.position_z = 0
        self.speed_km_s = 0
        self.direction_degrees = pr.Vector2(0,0)
        self.planet_id = 0
        self.input = get_config_menu_option()
        self.x_start = 610 + 550
        self.y_start = 130
        self.objects = objects
        self.state = menu_state()
        self.collision_menu = collision_menu
    
    def draw(self,camera):

        pr.draw_text(f"Radius:      {self.radius_Mm}",                 self.x_start, self.y_start,       self.input.menu_size("r"), self.input.menu_colour("r")) #Mm
        pr.draw_text(f"Density:     {self.density_g_cm3}",                self.x_start, self.y_start + 50,  self.input.menu_size("d"), self.input.menu_colour("d")) #g/cm3
        pr.draw_text(f"Position x:  {self.position_x}",             self.x_start, self.y_start + 100, self.input.menu_size("x"), self.input.menu_colour("x")) 
        pr.draw_text(f"Position y:  {self.position_y}",             self.x_start, self.y_start + 150, self.input.menu_size("y"), self.input.menu_colour("y"))
        pr.draw_text(f"Position z:  {self.position_z}",             self.x_start, self.y_start + 200, self.input.menu_size("z"), self.input.menu_colour("z"))
        pr.draw_text(f"Speed:       {self.speed_km_s}",                  self.x_start, self.y_start + 250, self.input.menu_size("speed"), self.input.menu_colour("speed")) #km/s
        pr.draw_text(f"Direction x: {self.direction_degrees.x}",    self.x_start, self.y_start + 300, self.input.menu_size("direction_x"), self.input.menu_colour("direction_x"))
        pr.draw_text(f"Direction y: {self.direction_degrees.y}",    self.x_start, self.y_start + 350, self.input.menu_size("direction_y"), self.input.menu_colour("direction_y"))
        pr.draw_text(f"Planet ID:   {self.planet_id}",              self.x_start, self.y_start + 400, 20, pr.WHITE)
 
        
##############################################################################
        self.radius_Mm +=      self.input.add_input("r")
        self.density_g_cm3 +=     self.input.add_input("d")
        self.position_x +=  self.input.add_input("x")
        self.position_y +=  self.input.add_input("y")
        self.position_z +=  self.input.add_input("z")
        self.speed_km_s +=       self.input.add_input("speed")
        self.direction_degrees.x += self.input.add_input("direction_x")
        self.direction_degrees.y += self.input.add_input("direction_y")

        if self.radius_Mm > 0 and self.density_g_cm3 > 0:
            pr.begin_mode_3d(camera)
            pr.draw_sphere_wires((self.position_x, self.position_y, self.position_z), self.radius_Mm,50,25, pr.GREEN)
            pr.end_mode_3d()
############################################################################## confirm function

            if self.input.get_option_hovered() == "GO":
                
                pr.draw_rectangle(1440, 150, 100, 100, pr.WHITE)
                pr.draw_text("GO!", 1460, 180, 40, pr.DARKGREEN)

                if pr.is_mouse_button_released(pr.MOUSE_BUTTON_LEFT):
                    self.planet_id += 1

                    planet = Planet(*self.create_planet())
                    self.objects.append(planet)
            else:
                pr.draw_rectangle(1440, 150, 100, 100, pr.DARKGREEN)
                pr.draw_rectangle_lines(1440, 150, 100, 100, pr.WHITE)
                pr.draw_text("GO!", 1460, 180, 40, pr.WHITE)

    def create_planet(self):
        
        speed = self.speed_km_s /1000
        
        mass = 4/3 * math.pi * math.pow(self.radius_Mm,3) * self.density_g_cm3 * 1e21 # vonvert to kg 
        yaw = math.radians(self.direction_degrees.x)
        pitch = math.radians(self.direction_degrees.y)
        direction_x = math.cos(pitch) * math.sin(yaw)
        direction_y = math.sin(pitch)
        direction_z = - math.cos(pitch) * math.cos(yaw)

        velocity = pr.Vector3(
                        direction_x * speed,
                        direction_y * speed,
                        direction_z * speed
                    )
        
        return self.radius_Mm, pr.Vector3(self.position_x,self.position_y,self.position_z), pr.WHITE, mass, velocity, self.planet_id
     
    def config_reset(self):
        self.radius_Mm = 6
        self.density_g_cm3 = 5
        self.position_x = 0
        self.position_y = 0
        self.position_z = 0
        self.speed_km_s = 0
        self.direction_degrees = pr.Vector2(0,0)
        self.planet_id = 0
        self.input = get_config_menu_option()
        self.collision_menu.state.toggle_state()
        
        