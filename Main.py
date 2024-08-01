import Simulator

exsim = Simulator.simulator()
exsim.generate_space(1000,1000)
exsim.add_body('lol', 70,70)
exsim.set_position('lol', 500, 500)
exsim.set_angle('lol', -90)



"""exsim.add_body('lol2', 100,100)
exsim.set_position('lol2', 1000, 0)
exsim.set_speed('lol2', - 200, - 200)

exsim.add_body('lol3', 100,100)
exsim.set_position('lol3', 0, 1000)
exsim.set_speed('lol3', 200,  200)

exsim.add_body('lol4', 100,100)
exsim.set_position('lol4', 1000, 1000)
exsim.set_speed('lol4', - 200, - 200)

exsim.add_body('lol5', 100,100)
exsim.set_position('lol5', 0, 450)
exsim.set_speed('lol5', 200, 0)

exsim.add_body('lol6', 100,100)
exsim.set_position('lol6', 450, 0)
exsim.set_speed('lol6', 0, -200)

exsim.add_body('lol7', 100,100)
exsim.set_position('lol7', 1000, 450)
exsim.set_speed('lol7', -200, 0)

exsim.add_body('lol8', 100,100)
exsim.set_position('lol8', 450, 1000)
exsim.set_speed('lol8', 0, 200)"""

exsim.running()