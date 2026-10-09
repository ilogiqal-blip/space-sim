import pyray as pr
from vector.vector import Vector3

def velocity_verlet_integrate(objects,sim_settings):

    dt = (pr.get_frame_time() * sim_settings.time_scale / sim_settings.substeps)
    for planet in objects:
        planet.acceleration = calc_total_a(planet,objects)

    for i in range(sim_settings.substeps): 
        for planet in objects:

            planet.position.x += (planet.velocity.x * dt) + (0.5 * planet.acceleration.x * (dt**2))
            planet.position.y += (planet.velocity.y * dt) + (0.5 * planet.acceleration.y * (dt**2))
            planet.position.z += (planet.velocity.z * dt) + (0.5 * planet.acceleration.z * (dt**2))

        for planet in objects:
            planet.temp_planet_acceleration = calc_total_a(planet,objects)

        for planet in objects:

            planet.velocity.x += 0.5 * (planet.acceleration.x + planet.temp_planet_acceleration.x) * dt
            planet.velocity.y += 0.5 * (planet.acceleration.y + planet.temp_planet_acceleration.y) * dt
            planet.velocity.z += 0.5 * (planet.acceleration.z + planet.temp_planet_acceleration.z) * dt

            planet.acceleration = planet.temp_planet_acceleration
            

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