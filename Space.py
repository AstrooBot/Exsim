import pygame

"""this class emulates the behavour of space based on classic physics. For that reasons, it has only two attributes: dimensions (x, y) and time"""
class space :

    def __init__(self, width, height) :
        self.width = width
        self.height = height
        self.size = (self.width, self.height)
        self.surface = pygame.display.set_mode(self.size)
        self.time_unid = 1000 #the unid for time is second
        self.distance_unid = 0.2645833333 #the unid for distance is mm
        self.time_passed = 0
    
    def set_time(self):
        self.time_passed += 1
        pygame.time.delay(self.time_unid)
    
    def get_time(self):
        return self.time_passed
    
    """Define how it has to be the space""" 
    def setting(self):
        self.set_time()

        