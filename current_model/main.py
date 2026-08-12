import pyray as pr
from loop import *
#print(dir(pr))




def main():

    pr.set_config_flags(pr.FLAG_WINDOW_RESIZABLE)
    pr.init_window(1400,900,"Space sim engine")
    pr.rl_set_line_width(3)
    graph_texture = pr.load_render_texture(900,600)

    
    
    game = Game()
    
    game.start_game_loop(graph_texture)



main()
