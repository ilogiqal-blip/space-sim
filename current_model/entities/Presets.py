from .Planet import *

class Preset():

    def __init__(self,objects):
        self.preset_1 = (
                        20,
                         pr.Vector3(0,0,0),
                         pr.BLUE,
                         4/3 * math.pi * math.pow(20,3) * 5 *1000000000,
                         0,
                         "preset"
                        )
        self.planets = []
        self.objects = objects



    def get_preset_vaiables():
        direction_degrees = pr.Vector3(0,0)
        radius = 20
        density = 5
        position = pr.Vector3(0,0,0)
        speed = 0
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

        return radius, pr.Vector3(position.x,position.y,position.z), pr.WHITE, mass, velocity, planet_id
    
    def get_preset(self):
        self.planets = [self.preset_1]
        # write preset selection script
        


    def create_planets(self):
        self.get_preset()
        for planet in self.planets:
            preset_planet = Planet(*planet)
        self.objects.append(preset_planet)
        print(self.objects)


