import pyray as pr 
import math
from vector.vector import *

class Player():

    def __init__(self,speed):
        self.pos = Vector3(
                            0,
                            300,
                            300
                            )
        self.TotalChangeX = 0
        self.TotalChangeY = 0
        self.sensitiviy  = 0.002
        self.direction = Vector3(1,0,1)
        self.speed = speed
        
        
        



         

    def update(self):
        speed = pr.get_frame_time() * self.speed
        mouse_delta = pr.get_mouse_delta()

         # camera movement

        self.TotalChangeX += mouse_delta.x * self.sensitiviy
        self.TotalChangeY -= mouse_delta.y * self.sensitiviy

        max_pitch = math.radians(89)
        self.TotalChangeY = max(-max_pitch, min(max_pitch, self.TotalChangeY))

        direction_x = math.cos(self.TotalChangeY) * math.sin(self.TotalChangeX)

        direction_y = math.sin(self.TotalChangeY)

        direction_z = - math.cos(self.TotalChangeY) * math.cos(self.TotalChangeX)

        self.direction = Vector3(
            direction_x,
            direction_y,
            direction_z
        )

        # position movement

        forward = pr.is_key_down(pr.KEY_W) - pr.is_key_down(pr.KEY_S)
        strafe = pr.is_key_down(pr.KEY_D) - pr.is_key_down(pr.KEY_A)
        up = pr.is_key_down(pr.KEY_LEFT_SHIFT) - pr.is_key_down(pr.KEY_LEFT_CONTROL)

        if pr.is_key_pressed(pr.KEY_Q):
            self.speed *= 10
        elif pr.is_key_pressed(pr.KEY_E):
            self.speed /= 10
        

        movement_x = self.direction.x
        movement_z = self.direction.z
        movement_y = self.direction.y


        #forward/backwards
        self.pos.x += forward * movement_x * speed
        self.pos.z += forward * movement_z * speed 
        self.pos.y += forward * movement_y * speed
        #strafe
        self.pos.x += strafe * -movement_z * speed
        self.pos.z += strafe * + movement_x * speed 
        #up/down    
        self.pos.y += up * speed

    def camera_update(self,camera):

        camera.position = pr.Vector3(
                        self.pos.x,
                        self.pos.y,
                        self.pos.z
                        )
        camera.target = pr.Vector3(
                        self.pos.x + self.direction.x,
                        self.pos.y + self.direction.y,
                        self.pos.z + self.direction.z
                        )
        
