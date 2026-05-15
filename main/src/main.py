import pyray as pr 
import math
import time
#print(dir(pr))


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


        planet1.draw()
        planet2.draw()
        planet3.draw()
            
        


        #pr.disable_cursor()
        pr.end_mode_3d()
        if menu_open:
            draw_menu()
        pr.end_drawing()
        

class Player():

    def __init__(self,speed):
        self.pos = pr.Vector3(
                            0,
                            0.5,
                            0
                            )
        self.TotalChangeX = 0
        self.TotalChangeY = 0
        self.sensitiviy  = 0.002
        self.direction = pr.Vector3(1,0,1)
        self.speed = speed
        
        print(f"sensitivity set to:{self.sensitiviy}")



         

    def update(self):
        speed = pr.get_frame_time() * self.speed
        mouse_delta = pr.get_mouse_delta()
        #print(mouse_delta.x, mouse_delta.y)

         # camera movement

        self.TotalChangeX += mouse_delta.x * self.sensitiviy
        self.TotalChangeY -= mouse_delta.y * self.sensitiviy
        #print(f"\n Total axis change x:y  {self.TotalChangeX,self.TotalChangeY} \n")

        max_pitch = math.radians(89)
        self.TotalChangeY = max(-max_pitch, min(max_pitch, self.TotalChangeY))

        direction_x = math.cos(self.TotalChangeY) * math.sin(self.TotalChangeX)
        #print(f"direction x: {self.direction.x:25}     position x: {self.pos.x}")

        direction_y = math.sin(self.TotalChangeY)
        #print(f"direction y: {self.direction.y:25}     position y: {self.pos.y}")

        direction_z = - math.cos(self.TotalChangeY) * math.cos(self.TotalChangeX)
        #print(f"direction z: {self.direction.z:25}     position z: {self.pos.z}")

        self.direction = pr.Vector3(
            direction_x,
            direction_y,
            direction_z
        )

        # position movement

        forward = pr.is_key_down(pr.KEY_W) - pr.is_key_down(pr.KEY_S)
        strafe = pr.is_key_down(pr.KEY_D) - pr.is_key_down(pr.KEY_A)
        up = pr.is_key_down(pr.KEY_Q) - pr.is_key_down(pr.KEY_E)
        

        movement_x = self.direction.x
        movement_z = self.direction.z
        movement_y = self.direction.y

        #print(f"movement x: {movement_x:25}")
        #print(f"movement z: {movement_z:25}")

        #forward/backwards
        self.pos.x += forward * movement_x * speed
        self.pos.z += forward * movement_z * speed 
        self.pos.y += forward * movement_y * speed
        #strafe
        self.pos.x += strafe * -movement_z * speed
        self.pos.z += strafe * + movement_x * speed 
        #up/down    
        self.pos.y += up * speed
         
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

    def draw(self):
        pr.draw_sphere((self.position.x,
                        self.position.y,
                        self.position.z),

                        self.radius,
                        self.colour)
        
        pr.draw_sphere_wires((self.position.x,
                            self.position.y,
                            self.position.z),
                              
                            self.radius + 0.002,
                            25,
                            50,
                            pr.BLUE)
        
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

