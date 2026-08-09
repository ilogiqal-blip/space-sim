import pyray as pr
#from entities.Planet import *





def apply_a(planet,other,dt):
    acceleration,target,r = planet.calc_a(other)

    if r == None:
            return

    acceleration_v = pr.Vector3(
                                            acceleration * target.x / r,
                                            acceleration * target.y / r,
                                            acceleration * target.z / r
                                            )

    planet.velocity.x += acceleration_v.x * dt 
    planet.velocity.y += acceleration_v.y * dt 
    planet.velocity.z += acceleration_v.z * dt 


def update(planet,dt):
        planet.position.x += planet.velocity.x * dt
        planet.position.y += planet.velocity.y * dt
        planet.position.z += planet.velocity.z * dt

def eular_integrate(objects,sim_settings):
        dt = (pr.get_frame_time() * sim_settings.time_scale / sim_settings.substeps) 
        
            
        for i in range(sim_settings.substeps):  #iterate for the amount of substeps per frame
            for planet in objects:              #this for loop updates every planets acceleration
        
                for other_planet in objects:
                                
                    if planet.id != other_planet.id: # checks that the planet its applying gravity to is not itself
        
                            apply_a(planet,other_planet,dt)
                                                    
                    else:
                            continue
        
        
                        
            for planet in objects:             #this for loop updates all of the planets position after all of
                update(planet,dt)              #the planets seperate accelerations have been calculated 