import pyray as pr 
import math



class Planet():

    def __init__(self,radius,position,colour,mass,velocity,planet_id):
               
        self.radius = radius   #Mm
        self.position = position #Mm
        self.colour = colour 
        self.mass = mass #kg
        self.velocity = velocity #Mm/s
        self.acceleration = 0 
        self.id = planet_id
        


        
        

    

    def draw(self,sim_settings):
        scaled_pos = pr.Vector3(
                        self.position.x / sim_settings.display_scale,
                        self.position.y / sim_settings.display_scale,
                        self.position.z / sim_settings.display_scale
                        )
        
        pr.draw_sphere(
                        (
                            scaled_pos.x,
                            scaled_pos.y,
                            scaled_pos.z
                            ),

                        self.radius / sim_settings.display_scale,
                        self.colour)
        
        pr.draw_sphere_wires(
                            (
                                scaled_pos.x,
                                scaled_pos.y,
                                scaled_pos.z
                                ),
                              
                            (self.radius / sim_settings.display_scale) + 0.002,
                            25,
                            50,
                            pr.Color(55,55,55,55))
        
    def draw_label(self,camera,sim_settings):
        scaled_pos = pr.Vector3(
                        self.position.x / sim_settings.display_scale,
                        self.position.y / sim_settings.display_scale,
                        self.position.z / sim_settings.display_scale
                        )
        
        screen_pos = pr.get_world_to_screen(scaled_pos,camera)
        pr.draw_text(str(self.id), int(screen_pos.x) , int(screen_pos.y) , 40, pr.GREEN)
        
    def calc_a(self,other):

        G = 6.674e-29  # Mm^3 * kg^-1 * s^-2
        target = pr.Vector3(
                                    other.position.x - self.position.x,
                                    other.position.y - self.position.y,
                                    other.position.z - self.position.z 
                                    )
            
        r = math.sqrt(target.x**2 + target.y**2 + target.z**2) #km

        if r <= 0:
            return None, None, None
        
        acceleration = (G*other.mass)/(r**2)

        return acceleration,target,r

        
