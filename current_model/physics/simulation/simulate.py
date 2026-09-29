from integrators.euler import *
from integrators.RK4 import *
from integrators.velocity_verlet import *


def simulate(objects,sim_settings,group):

    integrator = sim_settings.get_integrator(group)
    print("fetched integrator",group)

    if integrator == "euler":
        euler_integrate(objects,sim_settings)
        print("using integrator: euler",group)


    elif integrator == "RK4":
        RK4_integrate(objects,sim_settings)
        print("using integrator: RK4",group)
        
        
    elif integrator =="velocity verlet":
        velocity_verlet_integrate(objects,sim_settings)
        print("using integrator: velocity verlet",group)