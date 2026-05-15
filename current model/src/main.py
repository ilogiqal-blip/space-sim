import pyray as pr 
import math
import time
#print(dir(pr))
from Player import Player

def main():
    pr.init_window(1400,900,"window")
    pr.set_target_fps(60)
    pr.rl_set_line_width(3)
    camera = pr.Camera3D(
                        (2,1,2),              #position(x,y,z)
                        (0,0,0),                #target(x,y,z)       
                        (0,1,0),                #up(x,y,z)
                         60,                    #fov
                        pr.CAMERA_PERSPECTIVE)  #projection
    map_size = 5
    player = Player(10)


    #planets = [planet1,planet2]
    planet1 = Planet(2,2,pr.Vector3(0,0,0))
    planet2 = Planet(5,2,pr.Vector3(5,0,5))
    planet3 = Planet(5,2,pr.Vector3(-15,0,-15))
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
            planet2.simulate()
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


        planet1.draw(pr.RED)
        planet2.draw(pr.BLUE)
        planet3.draw(pr.BLACK)
            
        


        #pr.disable_cursor()
        pr.end_mode_3d()
        if menu_open:
            draw_menu()
        pr.end_drawing()
        
         
class Planet():

    def __init__(self,r,D,position):
        self.radius = r
        self.density = D
        self.colour = pr.DARKGREEN
        self.mass = (4/3)*math.pi*math.pow(self.radius,3)
        self.position = pr.Vector3(position.x,
                                   position.y,
                                   position.z)

        print(f" \n Radius inputted: {r}   Density inputted: {D}  Initialised planet mass: {self.mass:25}")

    def draw(self,color):
        pr.draw_sphere((self.position.x,
                        self.position.y,
                        self.position.z),

                        self.radius,
                        color)
        
        pr.draw_sphere_wires((self.position.x,
                            self.position.y,
                            self.position.z),
                              
                            self.radius + 0.002,
                            25,
                            50,
                            pr.Color(55,55,55,55))
        
    def simulate(self):
        self.position.x += 0.01

def draw_menu():
    pr.draw_rectangle(50,50,460,700,pr.Color(50,50,50,125))
    pr.draw_rectangle(70,70,200,150,pr.GRAY)
    pr.draw_rectangle(290,70,200,150,pr.GRAY)
    pr.draw_rectangle(70,240,200,150,pr.GRAY)
    pr.draw_rectangle(290,240,200,150,pr.GRAY)
    

#def create_grid(mass,position):


    

        

        


       
        

     
main()

