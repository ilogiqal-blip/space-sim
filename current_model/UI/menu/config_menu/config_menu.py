import pyray as pr
import math
from entities.Planet import *
from .input import *



class config_menu():

    def __init__(self,objects):
        self.radius = 6
        self.density = 5
        self.position_x = 0
        self.position_y = 0
        self.position_z = 0
        self.speed = 0
        self.direction_degrees = pr.Vector2(0,0)
        self.planet_id = 0
        self.input = get_menu_option()
        self.x_start = 610 + 550
        self.y_start = 130
        self.objects = objects
    
    def draw(self,mouse_pos,camera):

        pr.draw_text(f"Radius: {self.radius}", self.x_start, self.y_start, self.input.menu_size("r"), self.input.menu_colour("r"))
        pr.draw_text(f"Density: {self.density}", self.x_start, self.y_start + 50, self.input.menu_size("d"), self.input.menu_colour("d"))
        pr.draw_text(f"Position x: {self.position_x}", self.x_start, self.y_start + 100, self.input.menu_size("x"), self.input.menu_colour("x"))
        pr.draw_text(f"Position y: {self.position_y}", self.x_start, self.y_start + 150, self.input.menu_size("y"), self.input.menu_colour("y"))
        pr.draw_text(f"Position z: {self.position_z}", self.x_start, self.y_start + 200, self.input.menu_size("z"), self.input.menu_colour("z"))
        pr.draw_text(f"Speed: {self.speed}", self.x_start, self.y_start + 250, self.input.menu_size("speed"), self.input.menu_colour("speed"))
        pr.draw_text(f"Direction x: {self.direction_degrees.x}", self.x_start, self.y_start + 300, self.input.menu_size("direction_x"), self.input.menu_colour("direction_x"))
        pr.draw_text(f"Direction y: {self.direction_degrees.y}", self.x_start, self.y_start + 350, self.input.menu_size("direction_y"), self.input.menu_colour("direction_y"))
        pr.draw_text(f"Planet ID: {self.planet_id}", self.x_start, self.y_start + 400, 20, pr.WHITE)
 
        
##############################################################################
        self.radius += self.input.add_input("r")
        self.density += self.input.add_input("d")
        self.position_x += self.input.add_input("x")
        self.position_y += self.input.add_input("y")
        self.position_z += self.input.add_input("z")
        self.speed += self.input.add_input("speed")
        self.direction_degrees.x += self.input.add_input("direction_x")
        self.direction_degrees.y += self.input.add_input("direction_y")

        if self.radius > 0 and self.density > 0:
            pr.begin_mode_3d(camera)
            pr.draw_sphere_wires((self.position_x, self.position_y, self.position_z), self.radius,50,25, pr.GREEN)
            pr.end_mode_3d()
############################################################################## confirm function

            if (1440 < mouse_pos.x < 1540) and (150 < mouse_pos.y < 250):
                
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

        mass = 4/3 * math.pi * math.pow(self.radius,3) * self.density *1000000000
        yaw = math.radians(self.direction_degrees.x)
        pitch = math.radians(self.direction_degrees.y)
        direction_x = math.cos(pitch) * math.sin(yaw)
        direction_y = math.sin(pitch)
        direction_z = - math.cos(pitch) * math.cos(yaw)

        velocity = pr.Vector3(
                        direction_x * self.speed,
                        direction_y * self.speed,
                        direction_z * self.speed
                    )
        
        return self.radius, pr.Vector3(self.position_x,self.position_y,self.position_z), pr.WHITE, mass, velocity, self.planet_id
     
    def reset(self):
        self.radius = 6
        self.density = 5
        self.position_x = 0
        self.position_y = 0
        self.position_z = 0
        self.speed = 0
        self.direction_degrees = pr.Vector2(0,0)
        self.planet_id = 0
        self.input = get_menu_option()
        