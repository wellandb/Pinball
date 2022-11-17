from settings import *

# Peg class
class peg(pygame.sprite.Sprite):
    
    def __init__(self, x, y, radius, colour):
        super().__init__()
        self.rect = pygame.Rect(x,y, 7, 7)
        self.radius = radius
        self.colour = colour

    def draw(self):
        pygame.draw.circle(win, self.colour ,[self.rect.x, self.rect.y], self.radius)