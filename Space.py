import pygame, math


class space:

    def __init__(self, x_length, y_length, bodies) :
        
        self.time = 0
        self.time_passed = 0
        self.time_frame_delay = 0
        self.time_clock = pygame.time.Clock()
        self.time_clock_started_ticks = pygame.time.get_ticks()
        self.surface_x_length = x_length
        self.surface_y_length = y_length
        self.surface_size = (x_length, y_length)
        self.surface = pygame.display.set_mode(self.surface_size)
        self.bodies = bodies
    
    def get_time(self):
        return self.time
    
    """def set_time(self, time):
            self.time = time"""
    
    def print_time(self):

        self.time = pygame.time.get_ticks() - self.time_clock_started_ticks
        self.time_frame_delay = self.time_clock.get_time()
        self.time -= self.time_frame_delay 

        if self.time % 1000 == 0 and self.time != self.time_passed:
            print('Time of execution :', int(self.time/1000), ' Seconds')

        self.time_passed = self.time

    def update(self):

        self.surface.fill('Black')
        self.print_time()
        self.update_for_bodies()

    def update_for_bodies(self):

        for body in self.bodies:
            self.bodies[body].update(self.time)
            self.restriction_for_movement(body)

    def restriction_for_movement(self, body):

        if self.bodies[body].x_position + self.bodies[body].width > self.surface_x_length:  
                self.bodies[body].x_position_initial = self.surface_x_length - self.bodies[body].width 
                self.bodies[body].y_position_initial = self.bodies[body].y_position
                self.bodies[body].set_time_started_movement(self.time)
                self.bodies[body].x_speed *= - 1           

        if self.bodies[body].x_position < 0 :
                self.bodies[body].x_position_initial = 0
                self.bodies[body].y_position_initial = self.bodies[body].y_position
                self.bodies[body].set_time_started_movement(self.time)
                self.bodies[body].x_speed *= - 1

        if self.bodies[body].y_position + self.bodies[body].height > self.surface_y_length:  
                self.bodies[body].y_position_initial = self.surface_y_length - self.bodies[body].height
                self.bodies[body].x_position_initial = self.bodies[body].x_position 
                self.bodies[body].set_time_started_movement(self.time)
                self.bodies[body].y_speed *= - 1
        if self.bodies[body].y_position  < 0 :
                self.bodies[body].y_position_initial = 0
                self.bodies[body].x_position_initial = self.bodies[body].x_position 
                self.bodies[body].set_time_started_movement(self.time)
                self.bodies[body].y_speed *= - 1
                
    def get_x_length(self):
        return self.x_length

    def get_y_length(self):
        return self.y_length
    
    def get_body_position(self, body):
        pass

    def get_body_position_respect_to(self, body1, body2):
        pass
    
