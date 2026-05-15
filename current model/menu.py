import pyray as pr 
import math
import time
from Planet import Planet


def draw_menu():
    pr.draw_rectangle(50,50,460,700,pr.Color(50,50,50,125))
    pr.draw_rectangle_lines(50,50,460,700,pr.DARKGRAY)

    mouse_pos = pr.get_mouse_position()
    #print(mouse_pos.x,mouse_pos.y)

    if (70 < mouse_pos.x < 270) and ( 70< mouse_pos.y <220):
        pr.draw_rectangle_lines(70,70,200,150,pr.WHITE)
        pr.draw_rectangle(70,70,200,150,pr.DARKGRAY)
        if pr.is_mouse_button_pressed(pr.MOUSE_BUTTON_LEFT):
            pr.draw_rectangle(70,70,200,150,pr.GRAY)
            print("Button_1 pressed")

    else:
        pr.draw_rectangle(70,70,200,150,pr.GRAY)


    if (290 < mouse_pos.x < 490) and ( 70< mouse_pos.y <220):
        pr.draw_rectangle_lines(290,70,200,150,pr.WHITE)
        pr.draw_rectangle(290,70,200,150,pr.DARKGRAY)
        if pr.is_mouse_button_pressed(pr.MOUSE_BUTTON_LEFT):
            pr.draw_rectangle(290,70,200,150,pr.GRAY)
            print("Button_2 pressed")
    else:
        pr.draw_rectangle(290,70,200,150,pr.GRAY)

    
    if (70 < mouse_pos.x < 270) and ( 240< mouse_pos.y <490):
        pr.draw_rectangle_lines(70,240,200,150,pr.WHITE)
        pr.draw_rectangle(70,240,200,150,pr.DARKGRAY)
        if pr.is_mouse_button_pressed(pr.MOUSE_BUTTON_LEFT):
            pr.draw_rectangle(70,240,200,150,pr.GRAY)
            print("Button_3 pressed")
    else:
        pr.draw_rectangle(70,240,200,150,pr.GRAY)

    if (290 < mouse_pos.x < 490) and ( 240< mouse_pos.y <490):
        pr.draw_rectangle_lines(290,240,200,150,pr.WHITE)
        pr.draw_rectangle(290,240,200,150,pr.DARKGRAY)
        if pr.is_mouse_button_pressed(pr.MOUSE_BUTTON_LEFT):
            pr.draw_rectangle(290,240,200,150,pr.GRAY)
            print("Button_4 pressed")
    else:
        pr.draw_rectangle(290,240,200,150,pr.GRAY)
    