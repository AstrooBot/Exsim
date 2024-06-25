import pygame
 
class screen:

    def __init__(self, space) :
        self.space = space
        self.surface = space.surface
        self.user_events_list = None
        self.is_running = None
    
    def update(self):

        self.surface.fill('Black')
        self.space.update()
    
    def running(self):
        pygame.init()
        self.is_running = True
        while self.is_running == True :
            self.space.setting()
            self.user_events_list = pygame.event.get()
            for user_event in self.user_events_list:
                if user_event.type == pygame.QUIT:
                    self.is_running = False
        
            pygame.display.update()
        