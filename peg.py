# Import necessary modules
from settings import *

# Peg class
class peg(pygame.sprite.Sprite):
    
    # Intialize objects
    def __init__(self, x, y, radius, colour):
        super().__init__()
        self.rect = pygame.Rect(x,y, 7, 7)
        self.radius = radius
        self.colour = colour
        # Calculate the side length of the hexagon
        s = min(self.rect.width, self.rect.height)/2
        
        # Calculate the vertices of the hexagon
        self.points = []
        org_angle = 2*math.pi/6
        radius = 7
        for i in range(6):
            angle = org_angle*i
            self.points.append((self.rect.x + radius*math.cos(angle), self.rect.y + radius*math.sin(angle)))

        x, y = self.rect.center
        self.vertices = [
            (x - s*math.cos(math.pi/6), y - s*math.sin(math.pi/6)),
            (x + s*math.cos(math.pi/6), y - s*math.sin(math.pi/6)),
            (x + s, y),
            (x + s*math.cos(math.pi/6), y + s*math.sin(math.pi/6)),
            (x - s*math.cos(math.pi/6), y + s*math.sin(math.pi/6)),
            (x - s, y)
        ]
        
        # Calculate the normal vector for each side
        self.normals = []
        for i in range(6):
            v1 = self.vertices[i]
            v2 = self.vertices[(i+1) % 6]
            vector = (v2[0] - v1[0], v2[1] - v1[1])
            normal = (-vector[1], vector[0])
            length = math.sqrt(normal[0]**2 + normal[1]**2)
            normal = (normal[0]/length, normal[1]/length)
            self.normals.append(normal)

    # draw the peg on the window
    def draw(self, win):
        pygame.draw.circle(win, self.colour ,[self.rect.x + self.radius/2,self.rect.y+ self.radius/2], self.radius)