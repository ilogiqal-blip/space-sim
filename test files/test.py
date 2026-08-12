import pyray as pr
from test_data_class import *



running = True


def draw_graph(position,x_label,y_label,data):

    screen_pos_x = 10
    screen_pos_y = 10

    screen_width = pr.get_screen_width()
    screen_height = pr.get_screen_height()

    height = (screen_height - 40) // 3
    width = screen_width - 20


    if position == 1:
        screen_pos_y = 10
    elif position == 2:
        screen_pos_y = 20 + height
    elif position == 3:
        screen_pos_y = 30 + height + height
    else:
        print(f"graph position '{position}' doesn't exist \n please select from positions 1-3")
    
    
    
    #print(f"height: {height} width: {width}")
    pr.draw_rectangle(screen_pos_x,screen_pos_y,width,height,pr.WHITE)
    pr.draw_line(screen_pos_x + 50,screen_pos_y +height - 30, screen_pos_x + width - 20, screen_pos_y + height - 30,pr.BLACK)
    pr.draw_line(screen_pos_x + 50,screen_pos_y +height - 30, screen_pos_x + 50, screen_pos_y  + 20, pr.BLACK )
    pr.draw_text(x_label, screen_pos_x +(width//2) - (len(x_label) * 6) ,screen_pos_y + height - 25, 20,pr.BLACK)
    pr.draw_text(y_label,screen_pos_x + 5,screen_pos_y + (height//2), 20,pr.BLACK)

    

    
    
    

def main(running):



    pr.set_config_flags(pr.FLAG_WINDOW_RESIZABLE)
    pr.init_window(450,940,"Simulation Data")
    pr.rl_set_line_width(3)
    pr.set_target_fps(60)
    

    while running:
        if pr.is_key_pressed(pr.KEY_I):
            running = not running

        pr.begin_drawing()
        pr.clear_background(pr.BLACK)

        
        for i in range(3):
            draw_graph(i+1,f"elapsed time", f"% \nloss",f"%loss")
    
        pr.end_drawing()

main(running)

pr.LIGHTGRAY