from settings import *

# Paddle class
class paddle(pygame.sprite.Sprite):
    
    def __init__(self, x, y, xVel, yVel, maxX, maxY, width, height):
        super().__init__()
        self.xVel = xVel
        self.yVel = yVel
        self.maxX = maxX #Max movement in x value
        self.maxY = maxY #Max movement in y value
        self.xMove = 0
        self.yMove = 0
        self.xDir = 1
        self.yDir = 1
        
        self.rect = pygame.Rect(x,y,width,height)

    def draw(self):
        pygame.draw.rect(win, RED, self.rect)

    def move(self):
        if self.xMove >= self.maxX:
            self.xDir = -1
        elif self.xMove <= 0:
            self.xDir = 1

        if self.yMove >= self.maxY:
            self.yDir = -1
        elif self.yMove <= 0:
            self.yDir = 1
            