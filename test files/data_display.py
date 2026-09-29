import pyray as pr



def draw_graph(x_label,y_label,data,graph_texture,unit_y_division):

    pr.begin_texture_mode(graph_texture)
    pr.clear_background(pr.WHITE)


    #################################################### screen and starting position adjustments
    screen_pos_x = 00
    screen_pos_y = 00

    width = 1200
    height = 800

    line_height = height - 40
    line_width = width - 150
    line_pos_x = screen_pos_x + 50
    line_pos_y = screen_pos_y + height - 30
    #unit_y_division = 0

    ####################################################### drawing of the graph and labels
    

    pr.draw_rectangle(screen_pos_x,screen_pos_y,width,height,pr.WHITE)

    ############################################################## calculating maximum change and therefore the graph heigh and
                                                                 # pixel value
    
    unit_x = line_width / data.data[len(data.data)-1][0]     ## calculating pixel value x
    
    
    #for i in range(len(data.data)):
     #   if abs(data.data[i][1]) > abs(unit_y_division):      ## calulating maximum % energy change
      #      unit_y_division = data.data[i][1]

    #unit_y_division = 0.001
    
    if unit_y_division == 0:                  ## base case for no values
            unit_y = 1
    else:
        unit_y = (line_height // 2) / abs(unit_y_division)  ## calculating y pixel value based of of maximum change 

    
    
    ############################################################### ploting data on graph
    for i in range(1,len(data.data)):
        pr.draw_line(line_pos_x + int(data.data[i][0]*unit_x) ,line_pos_y - int(data.data[i][1]*unit_y) - (line_height//2), line_pos_x + int(data.data[i-1][0]*unit_x) ,line_pos_y - int(data.data[i-1][1]*unit_y) - (line_height//2) ,pr.BLUE)
    

    pr.draw_line(line_pos_x, line_pos_y - (line_height//2), line_pos_x + line_width, line_pos_y - (line_height//2),pr.BLACK) # x axis
    pr.draw_line(line_pos_x, line_pos_y, line_pos_x, line_pos_y - line_height, pr.BLACK ) # y axis

    pr.draw_text(x_label, screen_pos_x + (width//2) - (len(x_label) * 6) ,screen_pos_y + height - 25, 20,pr.BLACK)
    pr.draw_text(y_label, screen_pos_x + 5,screen_pos_y + (height//2), 20,pr.BLACK)

    pr.draw_text(f"{data.data[len(data.data) - 1][0]}",screen_pos_x + line_width - 100,line_pos_y - 150, 20,pr.BLACK)



    pr.draw_text(f"{abs(unit_y_division)}",screen_pos_x + 20,screen_pos_y, 20,pr.BLACK)
            
    pr.end_texture_mode()
    