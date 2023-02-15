from settings import *

class trail():
    
    def __init__(self, colour, startpos, endpos):
        self.colour = colour
        self.startpos = startpos
        self.endpos = endpos

    def draw(self):
        pygame.draw.line(win, self.colour, self.startpos, self.endpos)

x = [(1,2)]
points = []
for i in x:
    a = i[0] *2
    b = i[1] *2
    points.append((a,b))

print(points)