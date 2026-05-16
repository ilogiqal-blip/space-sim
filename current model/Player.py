import pyray as pr 
import math
import time

Player_version = "0.0.1"

class Player():

    def __init__(self,speed):
        print(f"Player version {Player_version}")
        self.pos = pr.Vector3(
                            0,
                            0.5,
                            0
                            )
        self.TotalChangeX = 0
        self.TotalChangeY = 0
        self.sensitiviy  = 0.002
        self.direction = pr.Vector3(1,0,1)
        self.speed = speed
        
        print(f"sensitivity set to:{self.sensitiviy}")



         

    def update(self):
        speed = pr.get_frame_time() * self.speed
        mouse_delta = pr.get_mouse_delta()
        #print(mouse_delta.x, mouse_delta.y)

         # camera movement

        self.TotalChangeX += mouse_delta.x * self.sensitiviy
        self.TotalChangeY -= mouse_delta.y * self.sensitiviy
        #print(f"\n Total axis change x:y  {self.TotalChangeX,self.TotalChangeY} \n")

        max_pitch = math.radians(89)
        self.TotalChangeY = max(-max_pitch, min(max_pitch, self.TotalChangeY))

        direction_x = math.cos(self.TotalChangeY) * math.sin(self.TotalChangeX)
        #print(f"direction x: {self.direction.x:25}     position x: {self.pos.x}")

        direction_y = math.sin(self.TotalChangeY)
        #print(f"direction y: {self.direction.y:25}     position y: {self.pos.y}")

        direction_z = - math.cos(self.TotalChangeY) * math.cos(self.TotalChangeX)
        #print(f"direction z: {self.direction.z:25}     position z: {self.pos.z}")

        self.direction = pr.Vector3(
            direction_x,
            direction_y,
            direction_z
        )

        # position movement

        forward = pr.is_key_down(pr.KEY_W) - pr.is_key_down(pr.KEY_S)
        strafe = pr.is_key_down(pr.KEY_D) - pr.is_key_down(pr.KEY_A)
        up = pr.is_key_down(pr.KEY_Q) - pr.is_key_down(pr.KEY_E)
        

        movement_x = self.direction.x
        movement_z = self.direction.z
        movement_y = self.direction.y

        #print(f"movement x: {movement_x:25}")
        #print(f"movement z: {movement_z:25}")

        #forward/backwards
        self.pos.x += forward * movement_x * speed
        self.pos.z += forward * movement_z * speed 
        self.pos.y += forward * movement_y * speed
        #strafe
        self.pos.x += strafe * -movement_z * speed
        self.pos.z += strafe * + movement_x * speed 
        #up/down    
        self.pos.y += up * speed
print(f"Player version {Player_version}")