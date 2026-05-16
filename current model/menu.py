import pyray as pr 
import math
import time
from Planet import Planet

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
    
    if (70 < mouse_pos.x < 270) and ( 70< mouse_pos.y <220):
        pr.draw_rectangle_lines(70,70,200,150,pr.WHITE)
        pr.draw_rectangle(70,70,200,150,pr.DARKGRAY)
        
        if pr.is_mouse_button_released(pr.MOUSE_BUTTON_LEFT):
            side_menu = not side_menu
    if side_menu:
        pr.draw_rectangle(600,70,400,300,pr.GRAY)
        pr.draw_rectangle_lines(600,70,400,300,pr.WHITE)
        pr.draw_text("Input Planet Parameters", 610, 80, 20, pr.WHITE)

        draw_side_menu(mouse_pos)
        check_mouse_input()
        check_button_input()

        
        pr.draw_rectangle(70,70,200,150,pr.GRAY)

        #print("Button_1 pressed")
        #new_planet = [r,d,
                    #pr.Vector3(x,y,z),
                    #255,0,255,255]
            
        #planets.append(new_planet)
        #planet = Planet(new_planet[0], new_planet[1], new_planet[2])

        #print(f" \n Radius inputted: {new_planet[0]}   Density inputted: {new_planet[1]}  Initialised planet mass: {planet.mass:25}")

    else:
        pr.draw_rectangle(70,70,200,150,pr.GRAY)


def draw_side_menu(mouse_pos):
        global r 
        global d
        global x
        global y
        global z
        global active_field
    ############################################################################# Radius
        if (610 < mouse_pos.x < 700) and ( 130 < mouse_pos.y < 150):
            active_field = "r"              
            pr.draw_text(f"Radius: {r}", 610, 130, 20, pr.LIGHTGRAY)
        else:
            pr.draw_text(f"Radius: {r}", 610, 130, 20, pr.WHITE)
############################################################################# Density
        if (610 < mouse_pos.x < 700) and ( 180 < mouse_pos.y < 200):              
            active_field = "d"
            pr.draw_text(f"Density: {d}", 610, 180, 20, pr.LIGHTGRAY)
        else:
            pr.draw_text(f"Density: {d}", 610, 180, 20, pr.WHITE)
############################################################################# Position X
        if (610 < mouse_pos.x < 700) and ( 230 < mouse_pos.y < 250):              
            active_field = "x"
            pr.draw_text(f"position x: {x}", 610, 230, 20, pr.LIGHTGRAY)
        else:
            pr.draw_text(f"position x: {x}", 610, 230, 20, pr.WHITE)
############################################################################# Position Y
        if (610 < mouse_pos.x < 700) and ( 280 < mouse_pos.y < 300):              
            active_field = "y"
            pr.draw_text(f"position y: {y}", 610, 280, 20, pr.LIGHTGRAY)
        else:
            pr.draw_text(f"position y: {y}", 610, 280, 20, pr.WHITE)
############################################################################## Position Z
        if (610 < mouse_pos.x < 700) and ( 330 < mouse_pos.y < 350):              
            active_field = "z"
            pr.draw_text(f"position z: {z}", 610, 330, 20, pr.LIGHTGRAY)
        else:
            pr.draw_text(f"position z: {z}", 610, 330, 20, pr.WHITE)

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
    