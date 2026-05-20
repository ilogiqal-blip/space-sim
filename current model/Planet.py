import pyray as pr 
import math
import time
Planet_version = "0.0.8"

class Planet():

    def __init__(self,r,D,position,velocity,direction):
        self.version = Planet_version
        self.radius = r
        self.density = D
        self.velocity = velocity
        self.colour = pr.DARKGREEN
        self.vol = (4/3)*math.pi*math.pow(self.radius,3)
        self.mass = self.vol * self.density
        self.position = position
        self.direction = direction

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
        
    def simulate(self,objects):
        velocity = self.velocity
        force = 0
        direction = self.direction
        mass = self.mass
        self.position.x += velocity * pr.get_frame_time()

        
            



print(f"Planet version {Planet_version}")