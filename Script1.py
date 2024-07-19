#Example of use: DVD locker screen emulation

import Simulator

sim = Simulator.simulator()
sim.generate_space(1920,1080)
sim.add_body('dvd', 70, 70)
sim.set_position('dvd', 0,100)
sim.set_speed('dvd', 200)
sim.set_angle('dvd', 45)
sim.running()