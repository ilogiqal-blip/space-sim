import pyray as pr 
import math
import time
Planet_version = "0.0.2"

class Planet():

    def __init__(self,r,D,position):
        self.radius = r
        self.density = D
        self.colour = pr.DARKGREEN
        self.vol = (4/3)*math.pi*math.pow(self.radius,3)
        self.mass = self.vol * self.density
        self.position = pr.Vector3(position.x,
                                   position.y,
                                   position.z)

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
        
    def simulate(self):
        force = 0
        mass = self.mass
        #print(force,mass)
print(f"Planet version {Planet_version}")