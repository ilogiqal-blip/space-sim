import pyray as pr

def grid(planets):

    size = 200
    distance = 10
    #x = 0 - size/2
    y = 0
    #z = 0 - size/2

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