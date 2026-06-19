


def simulate(objects):

    for planet in objects:

        for other_planet in objects:
                    
            if planet.id != other_planet.id:

                    planet.apply_a(other_planet)
                                         
            else:
                continue


                
        planet.update()