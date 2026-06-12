import pyray as pr 
import math
import time

Planet_version = "0.0.10"

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
        self.acceleration = pr.Vector3(0,0,0)
        self.target = pr.Vector3(0,0,0)
        self.planet_No = planet[9]


        
        

    

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
        a = 0
        G = 6.4730 * (10 **-11)
        

        for object in planets: #for each planet in planets[] 

            if object[9] != self.planet_No:
 
                other =   object
                self.target = pr.Vector3(
                                    other[2].x - self.position.x,
                                    other[2].y - self.position.y,
                                    other[2].z - self.position.z 
                                    )
            
                r = math.sqrt(self.target.x**2 + self.target.y**2 + self.target.z**2)

                if r == 0:
                    return
        
                a = (G*other[7])/(r**2)


                self.acceleration = pr.Vector3(
                                            a * self.target.x / r,
                                            a * self.target.y / r,
                                            a * self.target.z / r
                                            )

                self.velocity.x += self.acceleration.x #* pr.get_frame_time()
                self.velocity.y += self.acceleration.y #* pr.get_frame_time()
                self.velocity.z += self.acceleration.z #* pr.get_frame_time()

                print(f"planet {self.planet_No} compared planet {other[9]} acceleration {a}")    

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