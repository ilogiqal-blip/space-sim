import pyray as pr
import math
from Planet import *


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

    def draw(self,mouse_pos,camera):

    ############################################################################# Radius
        if (610 < mouse_pos.x < 710) and ( 130 < mouse_pos.y < 150):
            active_field = "r"              
            pr.draw_text(f"Radius: {self.radius}", 610, 130, 30, pr.LIGHTGRAY)
            pr.draw_text(f"Density: {self.density}", 610, 180, 20, pr.WHITE)
            pr.draw_text(f"Position x: {self.position_x}", 610, 230, 20, pr.WHITE)
            pr.draw_text(f"Position y: {self.position_y}", 610, 280, 20, pr.WHITE)
            pr.draw_text(f"Position z: {self.position_z}", 610, 330, 20, pr.WHITE)
            pr.draw_text(f"Speed: {self.speed}", 610, 380, 20, pr.WHITE)
            pr.draw_text(f"Direction x: {self.direction_degrees.x}", 610, 430, 20, pr.WHITE)
            pr.draw_text(f"Direction y: {self.direction_degrees.y}", 610, 480, 20, pr.WHITE)
            pr.draw_text(f"Planet number: {self.planet_number}", 610, 530, 20, pr.WHITE)
    ############################################################################# Density
        elif (610 < mouse_pos.x < 710) and ( 180 < mouse_pos.y < 200):              
            active_field = "d"
            pr.draw_text(f"Density: {self.density}", 610, 180, 30, pr.LIGHTGRAY)
            pr.draw_text(f"Radius: {self.radius}", 610, 130, 20, pr.WHITE)
            pr.draw_text(f"Position x: {self.position_x}", 610, 230, 20, pr.WHITE)
            pr.draw_text(f"Position y: {self.position_y}", 610, 280, 20, pr.WHITE)
            pr.draw_text(f"Position z: {self.position_z}", 610, 330, 20, pr.WHITE)
            pr.draw_text(f"Speed: {self.speed}", 610, 380, 20, pr.WHITE)
            pr.draw_text(f"Direction x: {self.direction_degrees.x}", 610, 430, 20, pr.WHITE)
            pr.draw_text(f"Direction y: {self.direction_degrees.y}", 610, 480, 20, pr.WHITE)
            pr.draw_text(f"Planet number: {self.planet_number}", 610, 530, 20, pr.WHITE)
    ############################################################################# Position X
        elif (610 < mouse_pos.x < 730) and ( 230 < mouse_pos.y < 250):              
            active_field = "x"
            pr.draw_text(f"Position x: {self.position_x}", 610, 230, 30, pr.LIGHTGRAY)
            pr.draw_text(f"Radius: {self.radius}", 610, 130, 20, pr.WHITE)
            pr.draw_text(f"Density: {self.density}", 610, 180, 20, pr.WHITE)
            pr.draw_text(f"Position y: {self.position_y}", 610, 280, 20, pr.WHITE)
            pr.draw_text(f"Position z: {self.position_z}", 610, 330, 20, pr.WHITE)
            pr.draw_text(f"Speed: {self.speed}", 610, 380, 20, pr.WHITE)
            pr.draw_text(f"Direction x: {self.direction_degrees.x}", 610, 430, 20, pr.WHITE)
            pr.draw_text(f"Direction y: {self.direction_degrees.y}", 610, 480, 20, pr.WHITE)
            pr.draw_text(f"Planet number: {self.planet_number}", 610, 530, 20, pr.WHITE)
    ############################################################################# Position Y
        elif (610 < mouse_pos.x < 730) and ( 280 < mouse_pos.y < 300):              
            active_field = "y"
            pr.draw_text(f"Position y: {self.position_y}", 610, 280, 30, pr.LIGHTGRAY)
            pr.draw_text(f"Radius: {self.radius}", 610, 130, 20, pr.WHITE)
            pr.draw_text(f"Density: {self.density}", 610, 180, 20, pr.WHITE)
            pr.draw_text(f"Position x: {self.position_x}", 610, 230, 20, pr.WHITE)
            pr.draw_text(f"Position z: {self.position_z}", 610, 330, 20, pr.WHITE)
            pr.draw_text(f"Speed: {self.speed}", 610, 380, 20, pr.WHITE)
            pr.draw_text(f"Direction x: {self.direction_degrees.x}", 610, 430, 20, pr.WHITE)
            pr.draw_text(f"Direction y: {self.direction_degrees.y}", 610, 480, 20, pr.WHITE)
            pr.draw_text(f"Planet number: {self.planet_number}", 610, 530, 20, pr.WHITE)
    ############################################################################## Position Z
        elif (610 < mouse_pos.x < 730) and ( 330 < mouse_pos.y < 350):              
            active_field = "z"
            pr.draw_text(f"Position z: {self.position_z}", 610, 330, 30, pr.LIGHTGRAY)
            pr.draw_text(f"Radius: {self.radius}", 610, 130, 20, pr.WHITE)
            pr.draw_text(f"Density: {self.density}", 610, 180, 20, pr.WHITE)
            pr.draw_text(f"Position x: {self.position_x}", 610, 230, 20, pr.WHITE)
            pr.draw_text(f"Position y: {self.position_y}", 610, 280, 20, pr.WHITE)
            pr.draw_text(f"Speed: {self.speed}", 610, 380, 20, pr.WHITE)
            pr.draw_text(f"Direction x: {self.direction_degrees.x}", 610, 430, 20, pr.WHITE)
            pr.draw_text(f"Direction y: {self.direction_degrees.y}", 610, 480, 20, pr.WHITE)
            pr.draw_text(f"Planet number: {self.planet_number}", 610, 530, 20, pr.WHITE)
    ############################################################################## speed input
        elif (610 < mouse_pos.x < 730) and ( 380 < mouse_pos.y < 400):              
            active_field = "speed"
            pr.draw_text(f"Speed: {self.speed}", 610, 380, 30, pr.LIGHTGRAY)
            pr.draw_text(f"Radius: {self.radius}", 610, 130, 20, pr.WHITE)
            pr.draw_text(f"Density: {self.density}", 610, 180, 20, pr.WHITE)
            pr.draw_text(f"Position x: {self.position_x}", 610, 230, 20, pr.WHITE)
            pr.draw_text(f"Position y: {self.position_y}", 610, 280, 20, pr.WHITE)
            pr.draw_text(f"Position z: {self.position_z}", 610, 330, 20, pr.WHITE)
            pr.draw_text(f"Direction x: {self.direction_degrees.x}", 610, 430, 20, pr.WHITE)
            pr.draw_text(f"Direction y: {self.direction_degrees.y}", 610, 480, 20, pr.WHITE)
            pr.draw_text(f"Planet number: {self.planet_number}", 610, 530, 20, pr.WHITE)
    ############################################################################## direction x input
        elif (610 < mouse_pos.x < 730) and ( 430 < mouse_pos.y < 450):              
            active_field = "direction_x"
            pr.draw_text(f"Direction x: {self.direction_degrees.x}", 610, 430, 30, pr.LIGHTGRAY)
            pr.draw_text(f"Radius: {self.radius}", 610, 130, 20, pr.WHITE)
            pr.draw_text(f"Density: {self.density}", 610, 180, 20, pr.WHITE)
            pr.draw_text(f"Position x: {self.position_x}", 610, 230, 20, pr.WHITE)
            pr.draw_text(f"Position y: {self.position_y}", 610, 280, 20, pr.WHITE)
            pr.draw_text(f"Position z: {self.position_z}", 610, 330, 20, pr.WHITE)
            pr.draw_text(f"Speed: {self.speed}", 610, 380, 20, pr.WHITE)
            pr.draw_text(f"Direction y: {self.direction_degrees.y}", 610, 480, 20, pr.WHITE)
            pr.draw_text(f"Planet number: {self.planet_number}", 610, 530, 20, pr.WHITE)
    ############################################################################## direction y input
        elif (610 < mouse_pos.x < 730) and ( 480 < mouse_pos.y < 500):
            active_field = "direction_y"
            pr.draw_text(f"Direction y: {self.direction_degrees.y}", 610, 480, 30, pr.LIGHTGRAY)
            pr.draw_text(f"Radius: {self.radius}", 610, 130, 20, pr.WHITE)
            pr.draw_text(f"Density: {self.density}", 610, 180, 20, pr.WHITE)
            pr.draw_text(f"Position x: {self.position_x}", 610, 230, 20, pr.WHITE)
            pr.draw_text(f"Position y: {self.position_y}", 610, 280, 20, pr.WHITE)
            pr.draw_text(f"Position z: {self.position_z}", 610, 330, 20, pr.WHITE)
            pr.draw_text(f"Speed: {self.speed}", 610, 380, 20, pr.WHITE)
            pr.draw_text(f"Direction x: {self.direction_degrees.x}", 610, 430, 20, pr.WHITE)
            pr.draw_text(f"Planet number: {self.planet_number}", 610, 530, 20, pr.WHITE)
    ############################################################################## else
        else:
            pr.draw_text(f"Radius: {self.radius}", 610, 130, 20, pr.WHITE)
            pr.draw_text(f"Density: {self.density}", 610, 180, 20, pr.WHITE)
            pr.draw_text(f"Position x: {self.position_x}", 610, 230, 20, pr.WHITE)
            pr.draw_text(f"Position y: {self.position_y}", 610, 280, 20, pr.WHITE)
            pr.draw_text(f"Position z: {self.position_z}", 610, 330, 20, pr.WHITE)
            pr.draw_text(f"Speed: {self.speed}", 610, 380, 20, pr.WHITE)
            pr.draw_text(f"Direction x: {self.direction_degrees.x}", 610, 430, 20, pr.WHITE)
            pr.draw_text(f"Direction y: {self.direction_degrees.y}", 610, 480, 20, pr.WHITE)
            pr.draw_text(f"Planet number: {self.planet_number}", 610, 530, 20, pr.WHITE)
            active_field = ""
############################################################################## direction vecter calculation
        yaw = math.radians(self.direction_degrees.x)
        pitch = math.radians(self.direction_degrees.y)

        
############################################################################## confirm button
    
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
                    direction_x = math.cos(pitch) * math.sin(yaw)
                    direction_y = math.sin(pitch)
                    direction_z = - math.cos(pitch) * math.cos(yaw)

                    velocity = pr.Vector3(
                        direction_x * self.speed,
                        direction_y * self.speed,
                        direction_z * self.speed
                    )

                    
                    planet = Planet()