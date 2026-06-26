from .Planet import *

class Preset():

    def __init__(self,objects):
        self.preset_1_input_data = [20,0,0,5,50,"preset 1"] #radius,yaw,pitch,density,speed,planet_id)
        self.planets = []
        self.objects = objects

    def add_preset_objects(self):
        preset = self.get_preset()
        for planet in preset:

            # start coding here again 
    def get_preset_vaiables(self):
        direction_degrees = pr.Vector3(0,0)
        radius = 20
        density = 5
        speed = 50
        planet_id = "preset 1"

        mass = 4/3 * math.pi * math.pow(radius,3) * density *1000000000
        yaw = math.radians(direction_degrees.x)
        pitch = math.radians(direction_degrees.y)

        direction_x = math.cos(pitch) * math.sin(yaw)
        direction_y = math.sin(pitch)
        direction_z = - math.cos(pitch) * math.cos(yaw)

        velocity = pr.Vector3(
                        direction_x * speed,
                        direction_y * speed,
                        direction_z * speed
                    )
        
        return radius, pr.Vector3(0,0,0), pr.BLUE, mass, velocity, "preset 1"
    ##########radius , position         , colour , mass , velocity , id
    
    def get_preset(self):
        self.planets = [self.preset_1]
        # write preset selection script
        


    def create_planets(self):


        for planet in self.planets:
            preset_planet = Planet(*planet)
        self.objects.append(preset_planet)
        print(self.objects)


