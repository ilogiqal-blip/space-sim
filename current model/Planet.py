import pyray as pr 
import math
import time

Planet_version = "0.0.7"
target_direction = pr.Vector3(0, 0, 0)
class Planet():

    def __init__(self,planets):
        self.radius = planets[0]
        self.density = planets[1]
        self.position = planets[2]
        self.speed = planets[3]
        self.color = planets[4]
        self.yaw = planets[5]
        self.pitch = planets[6]
        self.mass = planets[7]
        

    

    def draw(self,color):
        pr.draw_sphere((self.position.x,
                        self.position.y,
                        self.position.z),

                        self.radius,
                        color)
        
        pr.draw_sphere_wires((self.position.x,
                            self.position.y,
                            self.position.z),
                              
                            self.radius + 0.002,
                            25,
                            50,
                            pr.Color(55,55,55,55))
        
    def simulate(self,objects):
        for obj in objects:
            if obj != self:
                direction = pr.Vector3(
                    obj[2].x - self.position.x,
                    obj[2].y - self.position.y,
                    obj[2].z - self.position.z
                )



#radius     [0]
#density    [1]
#position   [2]
#velocity   [3]
#color      [4]
#yaw        [5]
#pitch      [6]
        

        
        
        
            



print(f"Planet version {Planet_version}")