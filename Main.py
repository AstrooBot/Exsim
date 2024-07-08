import Simulator

exsim = Simulator.simulator()
exsim.generate_space(1000,1000)
exsim.add_body('lol2', 50,50)
exsim.space.bodies['lol2'].set_position(50,500)
exsim.space.bodies['lol2'].set_speed(50)
exsim.running()