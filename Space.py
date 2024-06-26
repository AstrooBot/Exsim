import pygame, Bodies

class space:

    def __init__(self, x_length, y_length) :
        
        self.x_length = x_length
        self.y_length = y_length
        self.size = (self.x_length, self.y_length)
        self.time_unid = 1000 
        self.time_passed = 0
        self.bodies = {}
    
    def update(self):
    
        self.time_passed += 1

        for i in self.bodies:
            self.restriction_for_movement(self.bodies[i])
            self.bodies[i].update(self.time_passed)

          
        pygame.time.delay(self.time_unid)

    def restriction_for_movement(self, body):
                
        if body.rect.right < 0:  
                body.rect.left = self.x_length 
        if body.rect.left > self.x_length:  
                body.rect.right = 0 
    
