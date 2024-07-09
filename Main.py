import Simulator

exsim = Simulator.simulator()
exsim.generate_space(1000,1000)
exsim.add_body('lol2', 100,100)
exsim.set_position('lol2', 700, 500)
exsim.set_speed('lol2', -200)
exsim.running()