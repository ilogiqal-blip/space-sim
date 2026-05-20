import pyray as pr 
import math
import time
from Planet import *
from menu import *
#f = G*M*m/r^2

#objects
#radius     [0]
#density    [1]
#position   [2]
#velocity   [3]
#color      [4]
#yaw        [5]
#pitch      [6]


def gravitational_pull(objects,direction,velocity):
    force = 0
    
    if 1 < len(objects) < 2:
        G = 6.67430 * math.pow(10,-11)
        M = 4/3 * math.pi * math.pow(objects[0][0],3)
        m = 4/3 * math.pi * math.pow(objects[1][0],3)
        r = math.sqrt(math.pow(objects[0][2].x - objects[1][2].x,2) + math.pow(objects[0][2].y - objects[1][2].y,2) + math.pow(objects[0][2].z - objects[1][2].z,2))

        force = G * ((M * m) / math.pow(r,2))

    return(force)

    