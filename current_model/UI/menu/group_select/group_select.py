import pyray as pr

def get_group(x,y):
    x += 600
    pr.draw_rectangle(x,y,500,40,pr.DARKGRAY)
    pr.draw_text("press k for group 0 and l for group 1",x+5,y+5,20,pr.WHITE)
    if pr.is_key_pressed(pr.KEY_K):
        return 0
    elif pr.is_key_pressed(pr.KEY_L):
        return 1
    else:
        return -1