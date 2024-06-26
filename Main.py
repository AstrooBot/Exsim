import Simulator

exsim = Simulator.simulator()
exsim.generate_space(500,500)
exsim.add_body('lol', 30, 30, 'White')
exsim.space.bodies['lol'].set_position(0,30)
exsim.space.bodies['lol'].set_speed(10)
exsim.running()