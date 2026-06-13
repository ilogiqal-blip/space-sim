import pyray as pr
import math
from Planet import *
from .get_input import *



class config_menu():

    def __init__(self):
        self.radius = 6
        self.density = 5
        self.position_x = 0
        self.position_y = 0
        self.position_z = 0
        self.speed = 0
        self.direction_degrees = pr.Vector2(0,0)
        self.planet_number = 0
        self.input = get_menu_option()
        self.x_start = 610 + 550
        self.y_start = 130

    def draw(self,mouse_pos,camera):

        pr.draw_text(f"Radius: {self.radius}", self.x_start, self.y_start, self.input.menu_size("r"), self.input.menu_colour("r"))
        pr.draw_text(f"Density: {self.density}", self.x_start, self.y_start + 50, self.input.menu_size("d"), self.input.menu_colour("d"))
        pr.draw_text(f"Position x: {self.position_x}", self.x_start, self.y_start + 100, self.input.menu_size("x"), self.input.menu_colour("x"))
        pr.draw_text(f"Position y: {self.position_y}", self.x_start, self.y_start + 150, self.input.menu_size("y"), self.input.menu_colour("y"))
        pr.draw_text(f"Position z: {self.position_z}", self.x_start, self.y_start + 200, self.input.menu_size("z"), self.input.menu_colour("z"))
        pr.draw_text(f"Speed: {self.speed}", self.x_start, self.y_start + 250, self.input.menu_size("speed"), self.input.menu_colour("speed"))
        pr.draw_text(f"Direction x: {self.direction_degrees.x}", self.x_start, self.y_start + 300, self.input.menu_size("direction_x"), self.input.menu_colour("direction_x"))
        pr.draw_text(f"Direction y: {self.direction_degrees.y}", self.x_start, self.y_start + 350, self.input.menu_size("direction_y"), self.input.menu_colour("direction_y"))
        pr.draw_text(f"Planet number: {self.planet_number}", self.x_start, self.y_start + 400, 20, pr.WHITE)
 
        pr.draw_rectangle(840, 150, 100, 100, pr.DARKGREEN)
        pr.draw_rectangle_lines(840, 150, 100, 100, pr.WHITE)
        pr.draw_text("GO!", 860, 180, 40, pr.WHITE)
############################################################################## confirm function

        if self.radius > 0 and self.density > 0:
            pr.begin_mode_3d(camera)

            pr.draw_sphere_wires((self.position_x, self.position_y, self.position_z), self.radius,50,25, pr.GREEN)

            pr.end_mode_3d()


            if (840 < mouse_pos.x < 940) and (150 < mouse_pos.y < 250):

                pr.draw_rectangle(840, 150, 100, 100, pr.WHITE)
                pr.draw_text("GO!", 860, 180, 40, pr.DARKGREEN)

                if pr.is_mouse_button_released(pr.MOUSE_BUTTON_LEFT):
                    planet_number += 1

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

                    
                    planet = Planet()