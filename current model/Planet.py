import pyray as pr 
import math
import time

Planet_version = "0.0.7"

class Planet():

    def __init__(self,planet):
        #print(f"creating planet with radius {planet[0]} density {planet[1]} position {planet[2]} speed {planet[3]} color {planet[4]} yaw {planet[5]} pitch {planet[6]} mass {planet[7]}")
        
        
        self.radius = planet[0]
        self.density = planet[1]
        self.position = planet[2]
        self.speed = planet[3]
        self.color = planet[4]
        self.yaw = planet[5]
        self.pitch = planet[6]
        self.mass = planet[7]
        self.velocity = planet[8]
        self.acceleration = pr.Vector3(-5,0,0)


        
        

    

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
        
    def simulate(self,planet,planets):

        self.velocity.x += self.acceleration.x
        self.velocity.y += self.acceleration.y
        self.velocity.z += self.acceleration.z
        
        self.position.x += self.velocity.x * pr.get_frame_time()
        self.position.y += self.velocity.y * pr.get_frame_time()
        self.position.z += self.velocity.z * pr.get_frame_time()





        



#radius     [0]
#density    [1]
#position   [2]
#speed      [3]
#color      [4]
#yaw        [5]
#pitch      [6]
#mass       [7]
        

        
        
        
            



print(f"Planet version {Planet_version}")