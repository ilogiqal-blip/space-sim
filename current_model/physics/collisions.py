import pyray as pr
import math


def check_collision(objects):
    for i in range(len(objects)):
        planet = objects[i]
        
        for j in range(i+1,len(objects)):
            other = objects[j]
             
            if planet.id != other.id:

                target = pr.Vector3(
                                    other.position.x - planet.position.x,
                                    other.position.y - planet.position.y,
                                    other.position.z - planet.position.z 
                                    )
                
                r = math.sqrt(target.x**2 + target.y**2 + target.z**2)

                if r <= planet.radius + other.radius:
                    return True
                else:
                    return False
             

def merge_planets(p1,p2):
        
        merged_mass = p1.mass + p2.mass

        merged_radius = (p1.radius**3 + p2.radius**3) ** (1/3)

        merged_position = pr.Vector3(
                                    (p1.position.x * p1.mass + p2.position.x * p2.mass) / merged_mass,
                                    (p1.position.y * p1.mass + p2.position.y * p2.mass) / merged_mass,
                                    (p1.position.z * p1.mass + p2.position.z * p2.mass) / merged_mass
                                    )
        merged_colour = pr.WHITE
        
        merged_velocity = pr.Vector3((p1.velocity.x * p1.mass + p2.velocity.x * p2.mass) / merged_mass,
                                     (p1.velocity.y * p1.mass + p2.velocity.y * p2.mass) / merged_mass,
                                     (p1.velocity.z * p1.mass + p2.velocity.z * p2.mass) / merged_mass
                                    )
                                      
        planet_id = f"merged{p1.id},{p2.id}"
        
        return merged_radius, merged_position, merged_colour, merged_mass, merged_velocity, planet_id