import pyray as pr 
import math



class Planet():

    def __init__(self,radius,position,colour,mass,velocity,planet_id):
               
        self.radius = radius
        self.position = position
        self.colour = colour
        self.mass = mass
        self.velocity = velocity
        self.acceleration = 0
        self.id = planet_id


        
        

    

    def draw(self):
        pr.draw_sphere((self.position.x,
                        self.position.y,
                        self.position.z),

                        self.radius,
                        self.colour)
        
        pr.draw_sphere_wires((self.position.x,
                            self.position.y,
                            self.position.z),
                              
                            self.radius + 0.002,
                            25,
                            50,
                            pr.Color(55,55,55,55))
        
    def calc_a(self,other):
        
        G = 6.67430e-11
        target = pr.Vector3(
                                    other.position.x - self.position.x,
                                    other.position.y - self.position.y,
                                    other.position.z - self.position.z 
                                    )
            
        r = math.sqrt(target.x**2 + target.y**2 + target.z**2)

        if r <= 0:
            return None, None, None
        
        acceleration = (G*other.mass)/(r**2)

        return acceleration,target,r



    def apply_a(self,other):
        dt = pr.get_frame_time()
        acceleration,target,r = self.calc_a(other)

        if r == None:
            return

        acceleration_v = pr.Vector3(
                                            acceleration * target.x / r,
                                            acceleration * target.y / r,
                                            acceleration * target.z / r
                                            )

        self.velocity.x += acceleration_v.x * dt 
        self.velocity.y += acceleration_v.y * dt 
        self.velocity.z += acceleration_v.z * dt 


    def update(self):
        dt = pr.get_frame_time()
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt
        self.position.z += self.velocity.z * dt

        
