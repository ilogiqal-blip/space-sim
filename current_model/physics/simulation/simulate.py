import pyray as pr
from integrators.eular import *
from integrators.RK4 import *
from integrators.velocity_verlet import *


def simulate(objects,sim_settings):

    integrator = sim_settings.get_integrator()

    if integrator == "eular":
        eular_integrate(objects,sim_settings)
    elif integrator == "RK4":
        RK4_integrate()
    elif integrator =="velocity verlet":
        velocity_verlet_integrate()