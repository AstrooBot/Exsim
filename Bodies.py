import pygame

class body:

    def __init__(self, width, height, color, surface) :
        self.surface = surface
        self.form = None
        self.rect = None

        #attributes physics 
        self.width = width
        self.height = height
        self.color = color
        self.x_position = None
        self.y_position = None
        self.speed = None

    def set_position(self, x_position, y_position):

        self.x_position = x_position
        self.y_position = y_position
        self.form = pygame.draw.rect(self.surface, self.color , (self.x_position, self.y_position, self.width, self.height), 0)
        self.rect = pygame.rect.Rect(self.form)
    
    def set_speed(self, speed):
        self.speed = speed 
    
    def get_speed(self):
        return self.speed

    def update(self, time):
        self.rect.x += self.speed
        self.set_position(self.rect.x, self.rect.y)
