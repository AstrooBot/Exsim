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
        self.maximus_elevation = None
        self.counter = 0
        self.GRAVITY = 9.81
    
    def initial_positions(self, x_position, y_position):

        if self.x_position == None :
            self.x_position_initial = x_position
        if self.y_position == None:
            self.y_position_initial = y_position
        if self.maximus_elevation == None:
            self.maximus_elevation = y_position
            
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

    def mru_sim_x(self, time):
        time = ((time - self.time_started_movement) /1000)
        self.x_position = self.x_position_initial + 1/2 * (self.get_x_current_speed(time) + self.x_speed) * time
    
    def mru_sim_y(self, time):   
        time = ((time - self.time_started_movement ) /1000)
        #self.get_maximus_elevation(time)
        self.y_position = self.y_position_initial + 1/2 * (self.get_y_current_speed(time) + self.y_speed) * time
    
    def get_x_current_speed(self, time):
        x_current_speed = self.x_speed + self.x_acceleration * time
        return x_current_speed
    
    def get_y_current_speed(self, time):
        y_current_speed = self.y_speed + self.y_acceleration * time - self.get_gravity_action(time)
        return y_current_speed
    
    def get_gravity_action(self, time):
        gravity_acceleration = - self.GRAVITY * time
        return gravity_acceleration

    def get_maximus_elevation(self, time):
        if int(self.get_y_current_speed(time)) == 0 :
            self.maximus_elevation = self.y_position
            print('lol')
            


    def update(self, time):

        self.mru_sim_x(time)
        self.mru_sim_y(time)
        self.set_position(self.x_position, self.y_position)
