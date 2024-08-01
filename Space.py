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
        self.GRAVITY = 9.81
    
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
            print(self.bodies['lol'].get_y_current_speed(((self.time - self.bodies['lol'].time_started_movement  ) /1000)) )
            print( self.bodies['lol'].maximus_elevation)
        self.time_passed = self.time

    def update(self):

        self.surface.fill('Black')
        self.print_time()
        self.update_for_bodies()

    def update_for_bodies(self):

        for body in self.bodies:

            self.restriction_for_movement(body)
            self.bodies[body].update(self.time)

    def elastic_border_collision(self, body, time):
        speed = []
        time = time / 1000 
        speed.append(self.bodies[body].get_x_current_speed(time))
        speed.append( self.bodies[body].y_speed + self.bodies[body].y_acceleration * time - math.sqrt(2 * self.GRAVITY * self.bodies[body].maximus_elevation))
        return speed
    
    def elastic_border_collision_gravity(self, body, time):
         pass        
    
    def restriction_for_movement(self, body):

        if self.bodies[body].x_position + self.bodies[body].width > self.surface_x_length:  
                self.bodies[body].x_position_initial = self.surface_x_length - self.bodies[body].width 
                self.bodies[body].y_position_initial = self.bodies[body].y_position
                self.bodies[body].set_time_started_movement(self.time)
                self.bodies[body].x_speed *= - 1 
                self.bodies[body].x_acceleration *= - 1
                self.bodies[body].x_speed += self.elastic_border_collision(body, self.time)[0]

        if self.bodies[body].x_position < 0 :
                self.bodies[body].x_position_initial = 0
                self.bodies[body].y_position_initial = self.bodies[body].y_position
                self.bodies[body].set_time_started_movement(self.time)
                self.bodies[body].x_speed *= - 1
                self.bodies[body].x_acceleration *= - 1
                self.bodies[body].x_speed += self.elastic_border_collision(body, self.time)[0]

        if self.bodies[body].y_position + self.bodies[body].height > self.surface_y_length:  
                self.bodies[body].y_position_initial = self.surface_y_length - self.bodies[body].height
                self.bodies[body].x_position_initial = self.bodies[body].x_position 
                self.bodies[body].set_time_started_movement(self.time)
                self.bodies[body].y_speed *= - 1
                self.bodies[body].y_acceleration *= - 1
                self.bodies[body].y_speed += self.elastic_border_collision(body, self.time)[1]

        if self.bodies[body].y_position  < 0 :
                self.bodies[body].y_position_initial = 0
                self.bodies[body].x_position_initial = self.bodies[body].x_position 
                self.bodies[body].set_time_started_movement(self.time)
                self.bodies[body].y_speed *= - 1
                self.bodies[body].y_acceleration *= - 1
                self.bodies[body].y_speed += self.elastic_border_collision(body, self.time)[1]

    def get_x_length(self):
        return self.x_length

    def get_y_length(self):
        return self.y_length
    
    def get_body_position(self, body):
        pass

    def get_body_position_respect_to(self, body1, body2):
        pass
    
