from integrators.euler import *
from integrators.RK4 import *
from integrators.velocity_verlet import *


def simulate(objects,sim_settings,group):

    integrator = sim_settings.get_integrator(group)
    #print("fetched integrator",group)

    if integrator == "euler":
        #print("using integrator: euler",group)
        euler_integrate(objects,sim_settings)
        

    elif integrator == "RK4":
        #print("using integrator: RK4",group)
        RK4_integrate(objects,sim_settings)
        
        
        
    elif integrator =="velocity verlet":
        #print("using integrator: velocity verlet",group)
        velocity_verlet_integrate(objects,sim_settings)
        