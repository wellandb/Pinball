# Importing necessary modules
from settings import *
from trail import *
import math

# Ball class
class ball(pygame.sprite.Sprite):
    
    # Intialize the intance of the object
    def __init__(self, x, y, xVel, yVel):
        super().__init__()
        self.rect = pygame.Rect(x, y, 10, 10)
        self.xVel = xVel
        self.yVel = yVel
        self.colour = WHITE
        self.radius = 5
        self.tick = 0
        self.trails = []

    # draw the ball onto the screen
    def draw(self, win):
        pygame.draw.circle(win, self.colour ,[self.rect.x + self.rect.width/2, self.rect.y+ self.rect.height/2], self.radius)
        # pygame.draw.rect(win, BLUE, self.rect)
        self.tick += 1 # draw the trail after 3 frames have passed
        if self.tick == 3:
            self.trail() # create the trail for the ball in the line it has travelled
            self.tick = 0
        for i in self.trails:
            i.draw(win) # draw the trail of the route of the ball

    # move the ball by the velocity
    def move(self):
        self.rect.x += self.xVel
        self.rect.y += self.yVel
        if self.yVel < 10:
            self.yVel += 0.2 # gravity Based off of tick rate

    # change the velocity of the ball
    def changeDirection(self, newX, newY):
        self.xVel = newX
        self.yVel = newY
    
    # get the direction of the ball
    def getDirection(self):
        return math.tan(self.rect.y/self.rect.x) # Doesn't return Angle

    # method to create the trail in the direction the ball has moved
    def trail(self):
        self.trails.append(trail(self.colour, [self.rect.x-(self.xVel*2), self.rect.y-(self.yVel*2)], [self.rect.x, self.rect.y]))
