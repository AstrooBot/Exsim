import pygame

class body:

    def __init__(self, width, height, surface) :
        self.surface = surface
        self.form = None
        self.rect = None

        #attributes physics 
        self.width = width
        self.height = height
        self.color = 'White'
        self.x_position = None
        self.x_position_initial = None
        self.y_position = None
        self.y_position_initial = None
        self.speed = (0,0)
        self.time_started_movement = 0
    
    def initial_positions(self, x_position, y_position):

        if self.x_position == None :
            self.x_position_initial = x_position
        if self.y_position == None:
            self.y_position_initial = y_position
            
    def set_position(self, x_position, y_position):
        self.initial_positions(x_position, y_position)        
        self.x_position = x_position
        self.y_position = y_position
        self.form = pygame.draw.rect(self.surface, self.color , (self.x_position, self.y_position, self.width, self.height), 0)
        self.rect = pygame.rect.Rect(self.form)

    def mru_sim_x(self, time):

        self.x_position = self.x_position_initial + self.speed[0] * ((time - self.time_started_movement) /1000)

    def mru_sim_y(self, time):   
        self.y_position = self.y_position_initial + self.speed[1] * ((time - self.time_started_movement) /1000)

    def set_speed(self, speed_x, speed_y, time):
        self.speed = (speed_x, speed_y)
        self.time_started_movement = time

    def get_speed(self):
        return self.speed

    def update(self, time):

        self.mru_sim_x(time)
        self.mru_sim_y(time)
        self.set_position(self.x_position, self.y_position)
