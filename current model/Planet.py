import pyray as pr 
import math
import time
from gravitational_pull import *

Planet_version = "0.0.8"

class Planet():

    def __init__(self,r,D,position,velocity,yaw,pitch):
        self.version = Planet_version
        self.radius = r
        self.density = D
        self.velocity = velocity
        self.colour = pr.DARKGREEN
        self.position = position
        self.yaw = yaw
        self.pitch = pitch

        #print(f" \n Radius inputted: {r}   Density inputted: {D}  Initialised planet mass: {self.mass:25}")

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
        
    def simulate(self,objects,yaw,pitch):
        velocity = self.velocity
        direction = pr.Vector3(0, 0, 0)

        direction.x = math.cos(pitch) * math.sin(yaw)
        direction.y = math.sin(pitch)
        direction.z = -math.cos(pitch) * math.cos(yaw)
        

        force = gravitational_pull(objects,direction,velocity)
            
        self.position.x += velocity * direction.x * pr.get_frame_time()
        self.position.y += velocity * direction.y * pr.get_frame_time()
        self.position.z += velocity * direction.z * pr.get_frame_time()

        
            



print(f"Planet version {Planet_version}")