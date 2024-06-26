import pygame, Space , Bodies

class simulator:

    def __init__(self) -> None:
        
        self.is_running = None
        self.user_events_list = None

        self.surface = None
        self.space = None


    def generate_space(self, x_lenght, y_length):

        self.space = Space.space(x_lenght, y_length)
        self.surface = pygame.display.set_mode(self.space.size)
        pygame.display.set_caption('Space')
                                   
        print('Space has been created successfully')
    
    def add_body(self, name, width, height, color):
        body = Bodies.body(width, height, color, self.surface)
        self.space.bodies[name] = body

        print('Body called ', name, ' has successfully added' )
    
    def running(self):

        print('Simulation has started')
        
        pygame.init()
        self.is_running = True
        while self.is_running :
            self.surface.fill('Black')
            self.space.update()

            print('Time of execution :', self.space.time_passed, ' Seconds')

            self.user_events_list = pygame.event.get()
            for user_event in self.user_events_list:

                if user_event.type == pygame.QUIT :
                    self.is_running = False
                    print('Simulation has ended')

            pygame.display.update()

        