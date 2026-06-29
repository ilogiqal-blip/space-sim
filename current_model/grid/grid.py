import pyray as pr

def grid(planets):
    count = 0

    size = 200 #km
    distance = 20 #km
    
    y = 0
    

    for x in range(-size,size,distance):
        for z in range(-size,size,distance):
            pr.draw_line_3d(
                        (x,y,z),
                        (x,y,z + distance),
                        pr.WHITE
                        )
            
    for x in range(-size,size,distance):
        for z in range(-size,size,distance):
            pr.draw_line_3d(
                        (x,y,z),
                        (x + distance,y,z),
                        pr.WHITE
                        )