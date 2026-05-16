import pyray as pr 
import math
import time
from Planet import Planet
from Player import Player

version = "0.0.8"
side_menu = False
r = 0
d = 0
x = 0
y = 0
z = 0
active_field = ""


def draw_menu(planets):
    global side_menu
    global r 
    global d
    global x
    global y
    global z
    global active_field
    pr.draw_rectangle(50,50,460,700,pr.Color(50,50,50,125))
    pr.draw_rectangle_lines(50,50,460,700,pr.DARKGRAY)

    mouse_pos = pr.get_mouse_position()
    
    if (70 < mouse_pos.x < 490) and ( 70< mouse_pos.y <220):
        pr.draw_rectangle_lines(70,70,420,150,pr.WHITE)
        pr.draw_text("create new planet", 90, 100, 40, pr.WHITE)
        
        if pr.is_mouse_button_released(pr.MOUSE_BUTTON_LEFT):
            side_menu = not side_menu
    if side_menu:
        pr.draw_rectangle(600,70,420,300,pr.GRAY)
        pr.draw_rectangle_lines(600,70,420,300,pr.WHITE)
        pr.draw_text("Input Planet Parameters", 610, 80, 20, pr.WHITE)

        draw_side_menu(mouse_pos, planets)
        check_mouse_input()
        check_button_input()


        pr.draw_rectangle(70,70,420,150,pr.DARKGRAY)
        pr.draw_text("create new planet", 90, 100, 40, pr.WHITE)

    else:
        pr.draw_rectangle(70,70,420,150,pr.GRAY)
        pr.draw_text("create new planet", 90, 100, 40, pr.WHITE)


def draw_side_menu(mouse_pos,planets):
        global r 
        global d
        global x
        global y
        global z
        global active_field
    ############################################################################# Radius
        if (610 < mouse_pos.x < 710) and ( 130 < mouse_pos.y < 150):
            active_field = "r"              
            pr.draw_text(f"Radius: {r}", 610, 130, 30, pr.LIGHTGRAY)
            pr.draw_text(f"Density: {d}", 610, 180, 20, pr.WHITE)
            pr.draw_text(f"Position x: {x}", 610, 230, 20, pr.WHITE)
            pr.draw_text(f"Position y: {y}", 610, 280, 20, pr.WHITE)
            pr.draw_text(f"Position z: {z}", 610, 330, 20, pr.WHITE)
    ############################################################################# Density
        elif (610 < mouse_pos.x < 710) and ( 180 < mouse_pos.y < 200):              
            active_field = "d"
            pr.draw_text(f"Density: {d}", 610, 180, 30, pr.LIGHTGRAY)
            pr.draw_text(f"Radius: {r}", 610, 130, 20, pr.WHITE)
            pr.draw_text(f"Position x: {x}", 610, 230, 20, pr.WHITE)
            pr.draw_text(f"Position y: {y}", 610, 280, 20, pr.WHITE)
            pr.draw_text(f"Position z: {z}", 610, 330, 20, pr.WHITE)
    ############################################################################# Position X
        elif (610 < mouse_pos.x < 730) and ( 230 < mouse_pos.y < 250):              
            active_field = "x"
            pr.draw_text(f"Position x: {x}", 610, 230, 30, pr.LIGHTGRAY)
            pr.draw_text(f"Radius: {r}", 610, 130, 20, pr.WHITE)
            pr.draw_text(f"Density: {d}", 610, 180, 20, pr.WHITE)
            pr.draw_text(f"Position y: {y}", 610, 280, 20, pr.WHITE)
            pr.draw_text(f"Position z: {z}", 610, 330, 20, pr.WHITE)  
    ############################################################################# Position Y
        elif (610 < mouse_pos.x < 730) and ( 280 < mouse_pos.y < 300):              
            active_field = "y"
            pr.draw_text(f"Position y: {y}", 610, 280, 30, pr.LIGHTGRAY)
            pr.draw_text(f"Radius: {r}", 610, 130, 20, pr.WHITE)
            pr.draw_text(f"Density: {d}", 610, 180, 20, pr.WHITE)
            pr.draw_text(f"Position x: {x}", 610, 230, 20, pr.WHITE)
            pr.draw_text(f"Position z: {z}", 610, 330, 20, pr.WHITE)
    ############################################################################## Position Z
        elif (610 < mouse_pos.x < 730) and ( 330 < mouse_pos.y < 350):              
            active_field = "z"
            pr.draw_text(f"Position z: {z}", 610, 330, 30, pr.LIGHTGRAY)
            pr.draw_text(f"Radius: {r}", 610, 130, 20, pr.WHITE)
            pr.draw_text(f"Density: {d}", 610, 180, 20, pr.WHITE)
            pr.draw_text(f"Position x: {x}", 610, 230, 20, pr.WHITE)
            pr.draw_text(f"Position y: {y}", 610, 280, 20, pr.WHITE)

        else:
            pr.draw_text(f"Radius: {r}", 610, 130, 20, pr.WHITE)
            pr.draw_text(f"Density: {d}", 610, 180, 20, pr.WHITE)
            pr.draw_text(f"Position x: {x}", 610, 230, 20, pr.WHITE)
            pr.draw_text(f"Position y: {y}", 610, 280, 20, pr.WHITE)
            pr.draw_text(f"Position z: {z}", 610, 330, 20, pr.WHITE)
            active_field = ""
############################################################################## confirm button
    
        pr.draw_rectangle(840, 150, 100, 100, pr.DARKGREEN)
        pr.draw_rectangle_lines(840, 150, 100, 100, pr.WHITE)
        pr.draw_text("GO!", 860, 180, 40, pr.WHITE)
        if (840 < mouse_pos.x < 940) and (150 < mouse_pos.y < 250):
            pr.draw_rectangle(840, 150, 100, 100, pr.WHITE)
            pr.draw_text("GO!", 860, 180, 40, pr.DARKGREEN)
            if pr.is_mouse_button_released(pr.MOUSE_BUTTON_LEFT):
                new_planet = [r,d,
                    pr.Vector3(x,y,z),
                    255,0,255,255]
            
                planets.append(new_planet)
                planet = Planet(new_planet[0], new_planet[1], new_planet[2])

                #print(f"Radius inputted: {new_planet[0]}   Density inputted: {new_planet[1]}  Initialised volume: {planet.vol:25}  initialised mass: {planet.mass:25}")
                print(f"Planet version {planet.version:5}")
                print(f"menu version   {version:5}")
            
def check_mouse_input():
    global r 
    global d
    global x
    global y
    global z
    global active_field
    if active_field == "r" and pr.is_mouse_button_down(pr.MOUSE_BUTTON_LEFT):
        r += 1
        time.sleep(0.05)
    elif active_field == "r" and pr.is_mouse_button_down(pr.MOUSE_BUTTON_RIGHT):
        r -= 1
        time.sleep(0.05)
        if r < 0:
            r = 0

    if active_field == "d" and pr.is_mouse_button_down(pr.MOUSE_BUTTON_LEFT):
        d += 1
        time.sleep(0.05)
    elif active_field == "d" and pr.is_mouse_button_down(pr.MOUSE_BUTTON_RIGHT):
        d -= 1
        time.sleep(0.05)
        if d < 0:
            d = 0  

    if active_field == "x" and pr.is_mouse_button_down(pr.MOUSE_BUTTON_LEFT):
        x += 1
        time.sleep(0.05)
    elif active_field == "x" and pr.is_mouse_button_down(pr.MOUSE_BUTTON_RIGHT):
        x -= 1
        time.sleep(0.05)
        if x < 0:
            x = 0

    if active_field == "y" and pr.is_mouse_button_down(pr.MOUSE_BUTTON_LEFT):
        y += 1
        time.sleep(0.05)
    elif active_field == "y" and pr.is_mouse_button_down(pr.MOUSE_BUTTON_RIGHT):
        y -= 1
        time.sleep(0.05)
        if y < 0:
            y = 0

    if active_field == "z" and pr.is_mouse_button_down(pr.MOUSE_BUTTON_LEFT):
        z += 1
        time.sleep(0.05)
    elif active_field == "z" and pr.is_mouse_button_down(pr.MOUSE_BUTTON_RIGHT):
        z -= 1
        time.sleep(0.05)
        if z < 0:
            z = 0

def check_button_input():
    global r 
    global d
    global x
    global y
    global z
    global active_field
    if active_field == "r" and pr.is_key_pressed(pr.KEY_EQUAL):
        r += 1
        time.sleep(0.05)
    elif active_field == "r" and pr.is_key_pressed(pr.KEY_MINUS):
        r -= 1
        time.sleep(0.05)
        if r < 0:
            r = 0

    if active_field == "d" and pr.is_key_pressed(pr.KEY_EQUAL):
        d += 1
        time.sleep(0.05)
    elif active_field == "d" and pr.is_key_pressed(pr.KEY_MINUS):
        d -= 1
        time.sleep(0.05)
        if d < 0:
            d = 0  

    if active_field == "x" and pr.is_key_pressed(pr.KEY_EQUAL):
        x += 1
        time.sleep(0.05)
    elif active_field == "x" and pr.is_key_pressed(pr.KEY_MINUS):
        x -= 1
        time.sleep(0.05)
        if x < 0:
            x = 0

    if active_field == "y" and pr.is_key_pressed(pr.KEY_EQUAL):
        y += 1
        time.sleep(0.05)
    elif active_field == "y" and pr.is_key_pressed(pr.KEY_MINUS):
        y -= 1
        time.sleep(0.05)
        if y < 0:
            y = 0

    if active_field == "z" and pr.is_key_pressed(pr.KEY_EQUAL):
        z += 1
        time.sleep(0.05)
    elif active_field == "z" and pr.is_key_pressed(pr.KEY_MINUS):
        z -= 1
        time.sleep(0.05)
        if z < 0:
            z = 0

print(f"menu version   {version:5}")