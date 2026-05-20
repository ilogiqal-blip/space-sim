import pyray as pr 
import math
import time
from menu import *
#print(dir(pr))


main_version = "0.0.8"
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
    map_size = 5
    player = Player(10)


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
            for obj in objects:
                planet = Planet(obj[0],obj[1],obj[2],obj[3],obj[5])
                planet.simulate()
                #print(obj)
                obj[2] = planet.position
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
        pr.draw_grid(map_size * 20,1)

################################################### Drawing all of the planets in objects[]
        if len(objects) > 0:
            for obj in objects:
                planet = Planet(obj[0],obj[1],obj[2],obj[3],obj[5])
                planet.draw(obj[4])
###########################################################################################        
        pr.end_mode_3d()
        if menu_open:
            draw_menu(objects)
            
        pr.end_drawing()
            
main()

print(f"main version   {main_version:5}")