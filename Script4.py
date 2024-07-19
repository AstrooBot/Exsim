#Example of use: rectlinear motion
import Simulator 

sim = Simulator.simulator()

sim.generate_space(500,500)

sim.add_body('1', 50 ,50)
sim.set_position('1', 225, 0)
sim.set_speed('1', 50)
sim.set_angle('1', 90)


sim.running()