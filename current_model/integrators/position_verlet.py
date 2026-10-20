import pyray as pr
from vector.vector import Vector3

def position_verlet_integrate(objects, sim_settings):
    dt = (pr.get_frame_time() * sim_settings.time_scale / sim_settings.substeps)

    for i in range(sim_settings.substeps): 
        
        for planet in objects:
            planet.position.x += 0.5 * planet.velocity.x * dt
            planet.position.y += 0.5 * planet.velocity.y * dt
            planet.position.z += 0.5 * planet.velocity.z * dt

        for planet in objects:
            planet.acceleration = calc_total_a(planet, objects)

        for planet in objects:
            planet.velocity.x += planet.acceleration.x * dt
            planet.velocity.y += planet.acceleration.y * dt
            planet.velocity.z += planet.acceleration.z * dt

        for planet in objects:
            planet.position.x += 0.5 * planet.velocity.x * dt
            planet.position.y += 0.5 * planet.velocity.y * dt
            planet.position.z += 0.5 * planet.velocity.z * dt




def calc_total_a(planet,objects):
        

        acceleration_v = Vector3(0, 0, 0)

        for other in objects:

            if planet.id == other.id:
                continue

            
            acceleration,target,r = planet.calc_a(other)
                         
            if r == None:
                continue
                         
                         
            acceleration_v.x += acceleration * target.x / r
            acceleration_v.y += acceleration * target.y / r
            acceleration_v.z += acceleration * target.z / r

        return acceleration_v