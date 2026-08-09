import pyray as pr
import math

def calc_total_energy(objects):
    G = 6.674e-29  # Mm^3 * kg^-1 * s^-2
    potential = 0
    kinetic = 0

    for planet in objects:
        speed = math.sqrt( planet.velocity.x**2 + planet.velocity.y**2 + planet.velocity.z**2)

        kinetic += 1/2 * planet.mass * speed**2

    
    for i in range(len(objects)):
        
        for j in range(i+1,len(objects)):

            planet = objects[i]
            other = objects[j]
                
                

                
            target = pr.Vector3(
                                                    other.position.x - planet.position.x,
                                                    other.position.y - planet.position.y,
                                                    other.position.z - planet.position.z 
                                                    )


            r = math.sqrt(target.x**2 + target.y**2 + target.z**2)
            potential += -(G*planet.mass*other.mass)/r

    total_energy = kinetic + potential
    
    return total_energy