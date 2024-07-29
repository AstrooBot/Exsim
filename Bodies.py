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
        self.acceleration = 0
        self.x_acceleration = 0
        self.y_acceleration = 0
        self.time_started_movement = None
        self.gravity = 0
    
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

    def set_angle(self, angle):
        self.angle = angle
        self.set_speed(self.speed)
        
    def set_speed(self, speed):
        self.x_speed = speed * math.cos(self.angle)
        self.y_speed = speed * math.sin(self.angle)
        self.speed = speed

    def set_acceleration(self, acceleration):

        self.acceleration = acceleration
        self.x_acceleration = acceleration * math.cos(self.angle)
        self.y_acceleration = acceleration * math.sin(self.angle)

    def set_gravity(self, time):
        self.gravity = - 1/2 * (9.81 * (time ** 2))

        return self.gravity
        

    def mru_sim_x(self, time):
        time = ((time - self.time_started_movement) /1000)
        self.x_position = self.x_position_initial + self.x_speed * time + 1/2 * (self.x_acceleration * time ** 2)

    def mru_sim_y(self, time):   
        time = ((time - self.time_started_movement) /1000)
        self.y_position = self.y_position_initial + self.y_speed * time + 1/2 * (self.y_acceleration * time ** 2) + self.set_gravity(time)
        if self.y_speed * time + 1/2 * (self.y_acceleration * time ** 2) + self.set_gravity(time) == 0:
            extra_time = time
        else: 
            extra_time = 0
        if self.y_position < 0 and extra_time != 0:
            self.y_speed += 9.81 * extra_time
        elif self.y_position < 0:
            self.y_speed += 9.81 * time

    def get_speed(self):
        return self.speed

    def update(self, time):

        self.mru_sim_x(time)
        self.mru_sim_y(time)
        self.set_position(self.x_position, self.y_position)
