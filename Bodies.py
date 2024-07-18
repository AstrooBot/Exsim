import pygame, math

class body:

    def __init__(self, width, height, surface) :
        self.surface = surface
        self.form = None
        self.rect = None

        #attributes physics 
        self.width = width
        self.height = height
        self.color = 'White'
        self.angle = 0
        self.x_position = None
        self.x_position_initial = None
        self.y_position = None
        self.y_position_initial = None
        self.x_speed = 0
        self.y_speed = 0
        self.speed = 0
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

    def set_time_started_movement(self, time):
        self.time_started_movement = time

    def set_angle(self, angle, time):
        self.angle = angle
        self.set_speed(self.speed, time)
        
    def set_speed(self, speed, time):
        self.x_speed = speed * math.cos(self.angle)
        self.y_speed = speed * math.sin(self.angle)
        self.speed = speed
        self.set_time_started_movement(time)
        
    def mru_sim_x(self, time):

        self.x_position = self.x_position_initial + self.x_speed * ((time - self.time_started_movement) /1000)

    def mru_sim_y(self, time):   

        self.y_position = self.y_position_initial + self.y_speed * ((time - self.time_started_movement) /1000)

    def get_speed(self):
        return self.speed

    def update(self, time):

        self.mru_sim_x(time)
        self.mru_sim_y(time)
        self.set_position(self.x_position, self.y_position)
