import pyray as pr 
from menu.menu import *
from menu.state import *
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
    objects = []
    player = Player(500)
    main_menu_state = menu_state()
    main_menu = menu(camera)


    start_game_loop(main_menu_state,player,objects,camera,main_menu)

def start_game_loop(main_menu_state,player,objects,camera,main_menu):

    while not pr.window_should_close():

        if pr.is_key_pressed(pr.KEY_O):
            main_menu_state.toggle_menu()


        if not main_menu_state.menu_open: 
            player.update()

#############################################################################simulate here
            for planet in objects:
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
                planet.draw(planet.color)

########################################################################################### 
       
        pr.end_mode_3d()

        if main_menu_state.menu_open:
            main_menu.draw_menu()
            
        pr.end_drawing()

def render():
    return 
main()
