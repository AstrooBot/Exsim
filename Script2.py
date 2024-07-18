#Example of use: rectilienar motion

import Simulator

sim = Simulator.simulator()
sim.generate_space(500,500)
bodies = []
angle = 90
pos_x = 225
pos_y = 225
for body in range(1, 17):
    bodies.append('body' + str(body))

for body in bodies :
    sim.add_body(body, 50 , 50)
    sim.set_speed(body, 50)

for body in range(1, 17): 
    angle += 22.5
    sim.set_angle(bodies[body- 1],angle)
    sim.set_position(bodies[body -1 ], pos_x, pos_y)

sim.running()