import pyray as pr
import math
from entities.Planet import Planet

def make_planet(radius, position, yaw_deg, pitch_deg, density, speed, colour, planet_id):
        
        s = speed / 1000 #km/s to Mm/s
        r = radius #Mm


        mass = 4/3 * math.pi * math.pow(r, 3) * density * 1e21 # convert to kg 

        yaw   = math.radians(yaw_deg)
        pitch = math.radians(pitch_deg)

        direction_x = math.cos(pitch) * math.sin(yaw)
        direction_y = math.sin(pitch)
        direction_z = -math.cos(pitch) * math.cos(yaw)

        velocity = pr.Vector3(
            direction_x * s,
            direction_y * s,
            direction_z * s
        ) 

        return Planet(r, position, colour, mass, velocity, planet_id)    