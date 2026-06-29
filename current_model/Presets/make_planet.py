import pyray as pr
import math
from entities.Planet import Planet

def make_planet(radius, position, yaw_deg, pitch_deg, density, speed, colour, planet_id):
        mass = 4/3 * math.pi * math.pow(radius, 3) * density * 1000000000

        yaw   = math.radians(yaw_deg)
        pitch = math.radians(pitch_deg)

        direction_x = math.cos(pitch) * math.sin(yaw)
        direction_y = math.sin(pitch)
        direction_z = -math.cos(pitch) * math.cos(yaw)

        velocity = pr.Vector3(
            direction_x * speed,
            direction_y * speed,
            direction_z * speed
        )

        return Planet(radius, position, colour, mass, velocity, planet_id)    