from settings import *
from trail import *
import math

# Ball class
class ball(pygame.sprite.Sprite):
    
    def __init__(self, x, y, xVel, yVel):
        super().__init__()
        self.rect = pygame.Rect(x, y, 10, 10)
        self.xVel = xVel
        self.yVel = yVel
        self.colour = WHITE
        self.radius = 5
        self.tick = 0
        self.trails = []

    def draw(self):
        pygame.draw.circle(win, self.colour ,[self.rect.x + self.rect.width/2, self.rect.y+ self.rect.height/2], self.radius)
        # pygame.draw.rect(win, BLUE, self.rect)
        self.tick += 1
        if self.tick == 3:
            self.trail()
            self.tick = 0
        for i in self.trails:
            i.draw()


    def move(self):
        self.rect.x += self.xVel
        self.rect.y += self.yVel
        if self.yVel < 10:
            self.yVel += 0.2 # gravity Based off of tick rate

    def changeDirection(self, newX, newY):
        self.xVel = newX
        self.yVel = newY
    
    def getDirection(self):
        return math.tan(self.rect.y/self.rect.x) # Doesn't return Angle

    def trail(self):
        self.trails.append(trail(self.colour, [self.rect.x-(self.xVel*2), self.rect.y-(self.yVel*2)], [self.rect.x, self.rect.y]))
