import pyray as pr 
import math
import time
from menu import *
from Planet import *
#print(dir(pr))


main_version = "0.0.9"
from Player import Player
from Planet import Planet
from menu import *
    
def main():
    pr.init_window(2000,1200,"Simple Game Engine")
    pr.set_target_fps(60)
    pr.rl_set_line_width(3)
    camera = pr.Camera3D(
                        (2,1,2),               #position(x,y,z)
                        (0,0,0),                #target(x,y,z)       
                        (0,1,0),                #up(x,y,z)
                         60,                    #fov
                        pr.CAMERA_PERSPECTIVE)  #projection
    player = Player(500)


    objects = []

    menu_open = False

    while not pr.window_should_close():
        if pr.is_key_pressed(pr.KEY_O):
            menu_open = not menu_open

            if menu_open:
                pr.enable_cursor()
            else:
                pr.disable_cursor()
                

        



        if not menu_open: 
            player.update()

#############################################################################simulate here
            for planet in objects:
                planet = Planet(planet)
                planet.simulate(planet,objects)

                
#########################################################################################

            pr.disable_cursor()
        

            camera.position = pr.Vector3(
                player.pos.x,
                player.pos.y,
                player.pos.z
                )
            camera.target = pr.Vector3(
                player.pos.x + player.direction.x,
                player.pos.y + player.direction.y,
                player.pos.z + player.direction.z
                )
        

        pr.begin_drawing()
        pr.clear_background(pr.BLACK)
        pr.begin_mode_3d(camera)
        #pr.draw_grid(map_size * 5,20)
        grid(objects)
################################################### Drawing all of the planets in objects[]
        if len(objects) > 0:
            for planet in objects:
                planet = Planet(planet)
                planet.draw(planet.color)
###########################################################################################        
        pr.end_mode_3d()
        if menu_open:
            draw_menu(objects,camera)
            
        pr.end_drawing()


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
            
         


main()

print(f"main version   {main_version:5}")
