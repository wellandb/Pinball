# Import necessary modules
from settings import *

# trail class
class trail():
    # Intialize object
    def __init__(self, colour, startpos, endpos):
        self.colour = colour
        self.startpos = startpos
        self.endpos = endpos
    # draw the trail on the window
    def draw(self, win):
        pygame.draw.line(win, self.colour, self.startpos, self.endpos)

