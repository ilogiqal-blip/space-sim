import pyray as pr 
import math
import time

def draw_menu():
    pr.draw_rectangle(50,50,460,700,pr.Color(50,50,50,125))
    pr.draw_rectangle(70,70,200,150,pr.GRAY)
    pr.draw_rectangle(290,70,200,150,pr.GRAY)
    pr.draw_rectangle(70,240,200,150,pr.GRAY)
    pr.draw_rectangle(290,240,200,150,pr.GRAY)