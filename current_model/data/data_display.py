import pyray as pr



def draw_graph(x_label,y_label,data,graph_texture):

    
    

    pr.begin_texture_mode(graph_texture)

    pr.clear_background(pr.LIGHTGRAY)

    screen_pos_x = 00
    screen_pos_y = 00

    width = 900
    height = 600


    



    line_height = height - 40
    line_width = width - 80
    line_pos_x = screen_pos_x + 50
    line_pos_y = screen_pos_y + height - 30
    
    

    pr.draw_rectangle(screen_pos_x,screen_pos_y,width,height,pr.WHITE)

    pr.draw_line(line_pos_x, line_pos_y, line_pos_x + line_width, line_pos_y,pr.BLACK) # x axis
    pr.draw_line(line_pos_x, line_pos_y, line_pos_x, line_pos_y - line_height, pr.BLACK ) # y axis

    pr.draw_text(x_label, screen_pos_x +(width//2) - (len(x_label) * 6) ,screen_pos_y + height - 25, 20,pr.BLACK)
    pr.draw_text(y_label,screen_pos_x + 5,screen_pos_y + (height//2), 20,pr.BLACK)

    pr.draw_text(f"{data.data[len(data.data)//2][0]}", screen_pos_x +(width//2) - (len(x_label) * 6) ,screen_pos_y + height - 25, 20,pr.BLACK)
    pr.draw_text(f"{data.data[len(data.data)//2][1]}",screen_pos_x + 5,screen_pos_y + (height//2), 20,pr.BLACK)
    unit_x = line_width / data.data[len(data.data)-1][0]

    if data.data[len(data.data)-1][1] == 0:
        unit_y = 1
    else:
        unit_y = line_height / data.data[len(data.data)-1][1]

    for i in range(1,len(data.data)):
        pr.draw_line(line_pos_x + int(data.data[i][0]*unit_x) ,line_pos_y - int(data.data[i][1]*unit_y), line_pos_x + int(data.data[i-1][0]*unit_x) ,line_pos_y - int(data.data[i-1][1]*unit_y),pr.BLUE)
            
            
    pr.end_texture_mode()