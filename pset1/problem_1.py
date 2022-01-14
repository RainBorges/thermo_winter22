# import the code for the simulation
from simulator import Simulation

# create a new class for the simulation with some randomish variable choices
sim = Simulation(N=100, E=10, size=750, radius=3, mass=1, delay=2)

# run the simulation
sim.run_simulation(steps=10000)
