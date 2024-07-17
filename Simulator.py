import pygame, math, Space, Bodies

class simulator:

    def __init__(self) -> None:
        
        self.is_running = None
        self.user_events_list = None
        self.space = None
        self.bodies = {}
    
    def rad_to_deg(self, rad):
         deg = rad * 180 / math.pi
         return deg 
    
    def deg_to_rad(self, deg):
        rad = deg * (math.pi / 180)
        return rad 
    
    def generate_space(self, x_length, y_length):

        self.space = Space.space(x_length, y_length, self.bodies)

        print('A space has been created')
    
    def add_body(self, name, width, height):
        body = Bodies.body(width, height, self.space.surface)
        self.space.bodies[name] = body

        print('Body called ', name, ' has successfully added' )
    
    def set_position(self, body_name, x_position, y_position):
        self.space.bodies[body_name].set_position(x_position, y_position)
    
    def set_angle(self, body_name, body_angle):
         body_angle = self.deg_to_rad(body_angle)
         self.space.bodies[body_name].set_angle(body_angle, self.space.time)

    def set_speed(self, body_name, body_speed):
         self.space.bodies[body_name].set_speed(body_speed, self.space.time)

    def running(self):

        print('Simulation has started')
        pygame.init()
        self.is_running = True
        while self.is_running :
  
            self.space.update()

            self.user_events_list = pygame.event.get()
            for user_event in self.user_events_list:

                if user_event.type == pygame.QUIT :
                    self.is_running = False
                    print('Simulation has ended')

            pygame.display.update()        