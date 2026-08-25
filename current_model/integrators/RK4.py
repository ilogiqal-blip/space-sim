import pyray as pr
from entities.Planet import *

def RK4_integrate(objects,sim_settings):

    dt = (pr.get_frame_time() * sim_settings.time_scale / sim_settings.substeps)


    for i in range(sim_settings.substeps):
#######################################################################k1
        # k1_v is just the initial velocity
        # so no k1 is needed to be calculated


        for planet in objects:
             
             planet.k1_a = calc_total_a(planet,objects,"std")
#######################################################################k2
        for planet in objects:

             
             planet.temp_planet_pos.x = planet.position.x + planet.velocity.x * dt/2
             planet.temp_planet_pos.y = planet.position.y + planet.velocity.y * dt/2
             planet.temp_planet_pos.z = planet.position.z + planet.velocity.z * dt/2
             

             
             planet.k2_v.x = planet.velocity.x + planet.k1_a.x * dt/2
             planet.k2_v.y = planet.velocity.y + planet.k1_a.y * dt/2
             planet.k2_v.z = planet.velocity.z + planet.k1_a.z * dt/2
             

        for planet in objects:

             planet.k2_a = calc_total_a(planet,objects,"temp")

#######################################################################k3

        for planet in objects:

             planet.temp_planet_pos.x = planet.position.x + planet.k2_v.x * dt/2
             planet.temp_planet_pos.y = planet.position.y + planet.k2_v.y * dt/2
             planet.temp_planet_pos.z = planet.position.z + planet.k2_v.z * dt/2

             planet.k3_v.x = planet.velocity.x + planet.k2_a.x * dt/2
             planet.k3_v.y = planet.velocity.y + planet.k2_a.y * dt/2
             planet.k3_v.z = planet.velocity.z + planet.k2_a.z * dt/2

        for planet in objects:

             planet.k3_a = calc_total_a(planet,objects,"temp")

#######################################################################k4
        
        for planet in objects:

             planet.temp_planet_pos.x = planet.position.x + planet.k3_v.x * dt
             planet.temp_planet_pos.y = planet.position.y + planet.k3_v.y * dt
             planet.temp_planet_pos.z = planet.position.z + planet.k3_v.z * dt

             planet.k4_v.x = planet.velocity.x + planet.k3_a.x * dt
             planet.k4_v.y = planet.velocity.y + planet.k3_a.y * dt
             planet.k4_v.z = planet.velocity.z + planet.k3_a.z * dt

        for planet in objects:

             planet.k4_a = calc_total_a(planet,objects,"temp")

#######################################################################final update

        for planet in objects:

             planet.position.x += dt/6 * (planet.velocity.x + (planet.k2_v.x * 2) + (planet.k3_v.x * 2) + planet.k4_v.x)
             planet.position.y += dt/6 * (planet.velocity.y + (planet.k2_v.y * 2) + (planet.k3_v.y * 2) + planet.k4_v.y)
             planet.position.z += dt/6 * (planet.velocity.z + (planet.k2_v.z * 2) + (planet.k3_v.z * 2) + planet.k4_v.z)

             planet.velocity.x += dt/6 * (planet.k1_a.x + (planet.k2_a.x * 2) + (planet.k3_a.x * 2) + planet.k4_a.x)
             planet.velocity.y += dt/6 * (planet.k1_a.y + (planet.k2_a.y * 2) + (planet.k3_a.y * 2) + planet.k4_a.y)
             planet.velocity.z += dt/6 * (planet.k1_a.z + (planet.k2_a.z * 2) + (planet.k3_a.z * 2) + planet.k4_a.z)




    
def calc_total_a(planet,objects,type):
        

        acceleration_v = pr.Vector3(0, 0, 0)

        for other in objects:

            if planet.id == other.id:
                continue

            if type == "temp":
                acceleration,target,r = planet.calc_a_temp_pos(other)
            if type == "std":
                 acceleration,target,r = planet.calc_a(other)
                         
            if r == None:
                continue
                         
                         
            acceleration_v.x += acceleration * target.x / r
            acceleration_v.y += acceleration * target.y / r
            acceleration_v.z += acceleration * target.z / r

        return acceleration_v



                                                            

