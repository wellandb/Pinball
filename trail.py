from settings import *

class trail():
    
    def __init__(self, colour, startpos, endpos):
        self.colour = colour
        self.startpos = startpos
        self.endpos = endpos

    def draw(self):
        pygame.draw.line(win, self.colour, self.startpos, self.endpos)