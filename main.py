import pyray as pr 
import math
import time
#print(dir(pr))




def main():
    pr.init_window(800,600,"window")
    pr.rl_set_line_width(3)
    camera = pr.Camera3D(
                        (2,1,2),              #position(x,y,z)
                        (0,0,0),                #target(x,y,z)       
                        (0,1,0),                #up(x,y,z)
                         60,                    #fov
                        pr.CAMERA_PERSPECTIVE)  #projection
    map_size = 2
    player = Player()
    pr.get_mouse_delta()
    
    


    while not pr.window_should_close():
        player.update()
        mouse_delta = pr.get_mouse_delta()

        camera.position = player.pos
        camera.target = pr.Vector3(
            player.direction.x,
            player.direction.y,
            player.direction.z
                                    )
        

        pr.begin_drawing()
        pr.clear_background(pr.SKYBLUE)
        pr.begin_mode_3d(camera)
        pr.draw_grid(map_size * 10, 0.2 )
        pr.draw_plane(
                    (2,-0.01,0),                #plane position(x,y,z)
                    (map_size*2, map_size*2),   #plane size
                    pr.WHITE)                   #plane colour

        pr.end_mode_3d()
        pr.end_drawing()
        

class Player():

    def __init__(self):
        self.pos = pr.Vector3(
                            2,
                            0.5,
                            2
                            )
        self.TotalChangeX = 0
        self.TotalChangeY = 0
        self.sensitiviy  = 0.002
        self.direction = pr.Vector3(1,0,1)
        self.speed = 2
        pr.disable_cursor()
        print(f"sensitivity set to:{self.sensitiviy}")


    #def get_movement_vector():


         

    def update(self):
        speed = pr.get_frame_time() * self.speed
        mouse_delta = pr.get_mouse_delta()

        # position movement

        forward = pr.is_key_down(pr.KEY_W) - pr.is_key_down(pr.KEY_S)
        strafe = pr.is_key_down(pr.KEY_D) - pr.is_key_down(pr.KEY_A)
        
        self.pos.x = self.pos.x + forward * speed
        self.pos.z = self.pos.z + strafe * speed

        movement_x = self.direction.x - self.pos.x
        print(f"movement x: {movement_x:25}")
        movement_z = self.direction.z - self.pos.z
        print(f"movement z: {movement_z:25}")

        

        


        # camera movement

        self.TotalChangeX += mouse_delta.x * self.sensitiviy
        self.TotalChangeY -= mouse_delta.y * self.sensitiviy
        #print(f"\n Total axis change x:y  {self.TotalChangeX,self.TotalChangeY} \n")

        max_pitch = math.radians(89)
        self.TotalChangeY = max(-max_pitch, min(max_pitch, self.TotalChangeY))

        direction_x = math.cos(self.TotalChangeY) * math.sin(self.TotalChangeX)
        print(f"direction x: {self.direction.x:25}     position x: {self.pos.x}")

        direction_y = math.sin(self.TotalChangeY)
        print(f"direction y: {self.direction.y:25}     position y: {self.pos.y}")

        direction_z = - math.cos(self.TotalChangeY) * math.cos(self.TotalChangeX)
        print(f"direction z: {self.direction.z:25}     position z: {self.pos.z}")

        self.direction = pr.Vector3(direction_x + self.pos.x, direction_y + self.pos.y, direction_z + self.pos.z)
        print(forward)
        print(strafe)
        

     
main()
