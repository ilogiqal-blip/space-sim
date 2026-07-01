import pyray as pr
timescale = 10000
substeps = 20

def simulate(objects):
    dt = (pr.get_frame_time() * timescale / substeps) # we want it to apply the gravity 20 times so the "frame time " 
                                                        # is now divided by 20 as its 20 times per frame


    for i in range(substeps):
        for planet in objects:

            for other_planet in objects:
                        
                if planet.id != other_planet.id:

                        planet.apply_a(other_planet,dt)
                                            
                else:
                    continue


                
        for planet in objects:
            planet.update(dt)