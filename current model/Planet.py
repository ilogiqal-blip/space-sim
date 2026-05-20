import pyray as pr 
import math
import time
Planet_version = "0.0.8"

class Planet():

    def __init__(self,r,D,position,velocity,yaw,pitch):
        self.version = Planet_version
        self.radius = r
        self.density = D
        self.velocity = velocity
        self.colour = pr.DARKGREEN
        self.vol = (4/3)*math.pi*math.pow(self.radius,3)
        self.mass = self.vol * self.density
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
        force = 0
        direction = pr.Vector3(0, 0, 0)
        mass = self.mass
        direction.x = math.cos(pitch) * math.sin(yaw)
        print(f"direction.x: {direction.x}")

        direction.y = math.sin(pitch)
        print(f"direction.y: {direction.y}")

        direction.z = -math.cos(pitch) * math.cos(yaw)
        print(f"direction.z: {direction.z}")
##############################################
 #       for obj in objects:
 #           if obj[2] != self.position:
  #              other_mass = (4/3)*math.pi*math.pow(obj[0],3) * obj[1]
  #              distance_vector = pr.Vector3(obj[2].x - self.position.x,
  #                                          obj[2].y - self.position.y,
   #                                         obj[2].z - self.position.z)
  #              distance = math.sqrt(distance_vector.x**2 + distance_vector.y**2 + distance_vector.z**2) 
#
  #              if distance > self.radius + obj[0]: # only calculate if not colliding
   #                 force += (6.67430e-11 * mass * other_mass) / (distance ** 2)
   #                 direction.x += distance_vector.x / distance
    #                direction.y += distance_vector.y / distance
    #                direction.z += distance_vector.z / distance
        
        self.position.x += velocity * direction.x * pr.get_frame_time()
        self.position.y += velocity * direction.y * pr.get_frame_time()
        self.position.z += velocity * direction.z * pr.get_frame_time()

        
            



print(f"Planet version {Planet_version}")