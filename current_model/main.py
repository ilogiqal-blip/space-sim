import pyray as pr
from game import *
#print(dir(pr))




def main():

    pr.set_config_flags(pr.FLAG_WINDOW_RESIZABLE)
    pr.init_window(1600,900,"Space sim engine")
    pr.set_target_fps(60)
    pr.rl_set_line_width(3)

    
    
    game = Game()
    
    game.start_game_loop()



main()
