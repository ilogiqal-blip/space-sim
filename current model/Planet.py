import pyray as pr 
import math
import time

Planet_version = "0.0.7"
target_direction = pr.Vector3(0, 0, 0)
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
        self.acceleration = 0
        self.mass = 4/3 * math.pi * math.pow(self.radius,3) * self.density
        

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
        force = 0
        

        #force = gravitational_pull(objects,direction,velocity)
        #objects
#radius     [0]
#density    [1]
#position   [2]
#velocity   [3]
#color      [4]
#yaw        [5]
#pitch      [6]
        

        if 1 < len(objects) < 3:
            global target_direction

            if objects[1][2].x -self.position.x == 0:
                target_direction.x = objects[0][2].x -self.position.x
            else:
                target_direction.x = objects[1][2].x -self.position.x

            if objects[1][2].y -self.position.y == 0:
                target_direction.y = objects[0][2].y -self.position.y
            else:
                target_direction.y = objects[1][2].y -self.position.y

            if objects[1][2].z -self.position.z == 0:
                target_direction.z = objects[0][2].z -self.position.z
            else:
                target_direction.z = objects[1][2].z -self.position.z

            G = 6.67430 * math.pow(10,-11)
            M = 4/3 * math.pi * math.pow(objects[0][0],3) * objects[0][1] * 1000000
            m = 4/3 * math.pi * math.pow(objects[1][0],3) * objects[1][1] * 1000000
            r = math.sqrt(math.pow(objects[0][2].x - objects[1][2].x,2) + math.pow(objects[0][2].y - objects[1][2].y,2) + math.pow(objects[0][2].z - objects[1][2].z,2))

            force = G * ((M * m) / math.pow(r,2))
            
            self.acceleration = force / self.mass
            

            print(f"force: {force:25}     velocity: {velocity:5}     direction: {target_direction.x:25} {target_direction.y:25} {target_direction.z:25} acceleration: {self.acceleration:25} mass: {self.mass:25}")
            
        self.position.x += ((direction.x * velocity)+ (self.acceleration * target_direction.x)) * pr.get_frame_time()
        self.position.y += ((direction.y * velocity)+ (self.acceleration * target_direction.y)) * pr.get_frame_time()
        self.position.z += ((direction.z * velocity)+ (self.acceleration * target_direction.z)) * pr.get_frame_time()

        
            



print(f"Planet version {Planet_version}")