#Example of use: rectilienar motion

import Simulator

sim = Simulator.simulator()
sim.generate_space(500,500)

sim.add_body('0', 50 ,50)
sim.set_position('0', 175, 175)
sim.set_speed('0', 70.71)
sim.set_angle('0', -135) 

sim.add_body('1', 50 ,50)
sim.set_position('1', 225, 175) 
sim.set_speed('1', 50)
sim.set_angle('1', -90) 

sim.add_body('2', 50 ,50)
sim.set_position('2', 275, 175)
sim.set_speed('2',  70.71)
sim.set_angle('2', -45) 

sim.add_body('3', 50 ,50)
sim.set_position('3', 275, 225) 
sim.set_speed('3', 50)
sim.set_angle('3', 0) 

sim.add_body('4', 50 ,50)
sim.set_position('4', 275, 275)
sim.set_speed('4',  70.71)
sim.set_angle('4', 45) 

sim.add_body('5', 50 ,50)
sim.set_position('5', 225, 275)
sim.set_speed('5', 50)
sim.set_angle('5', 90) 

sim.add_body('6', 50 ,50)
sim.set_position('6', 175, 275)
sim.set_speed('6',  70.71)
sim.set_angle('6', 135) 

sim.add_body('7', 50 ,50)
sim.set_position('7', 175, 225) 
sim.set_speed('7', 50)
sim.set_angle('7', 180) 

sim.running()