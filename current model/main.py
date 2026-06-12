import pyray as pr 
from menu.menu import *
from menu.menu_state import *
from grid.grid import *
from Player import *
from Planet import *
#print(dir(pr))



def main():

    pr.init_window(1600,900,"Simple Game Engine")
    pr.set_target_fps(60)
    pr.rl_set_line_width(3)

    camera = pr.Camera3D(
                        (2,1,2),                #position(x,y,z)
                        (0,0,0),                #target(x,y,z)       
                        (0,1,0),                #up(x,y,z)
                        60,                     #fov
                        pr.CAMERA_PERSPECTIVE)  #projection
    
    player = Player(500)
    menu = menu_state()
    objects = []
    

    while not pr.window_should_close():
        if pr.is_key_pressed(pr.KEY_O):
            menu.toggle_menu()
                

        if not menu.menu_open: 
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
        grid(objects)

################################################### Drawing all of the planets in objects[]

        if len(objects) > 0:
            for planet in objects:
                planet = Planet(planet)
                planet.draw(planet.color)

########################################################################################### 
       
        pr.end_mode_3d()

        if menu.menu_open:
            draw_menu(objects,camera)
            
        pr.end_drawing()



#radius     [0]
#density    [1]
#position   [2]
#speed      [3]
#color      [4]
#yaw        [5]
#pitch      [6]
#mass       [7]
    
         


main()
