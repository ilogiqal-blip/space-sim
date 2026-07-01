import pyray as pr


def simulate(objects,sim_settings):
    dt = (pr.get_frame_time() * sim_settings.time_scale / sim_settings.substeps) 

    
    for i in range(sim_settings.substeps):
        for planet in objects:

            for other_planet in objects:
                        
                if planet.id != other_planet.id:

                        planet.apply_a(other_planet,dt)
                                            
                else:
                    continue


                
        for planet in objects:
            planet.update(dt)