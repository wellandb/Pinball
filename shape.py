from settings import *

# Use these for pixel and location definition
def to_pixels(x,y):
    return(screenWidth/2 + screenWidth * x/20, screenHeight/2 - screenHeight * y/20)

def from_pixels(x, y):
    return(20*x/screenWidth - 10, 10 - 20 * y/screenHeight)

class shape(pygame.sprite.Sprite):
    
    def __init__(self, x, y, colour):
        super().__init__()
        self.x = x
        self.y = y
        self.colour = colour
        self.points = []
        self.state = self.random_state()
    
    def get_points(self):
        return self.points
    
    def get_colour(self):
        return self.colour
    
    def get_state(self):
        return self.state

    def set_points(self, new_points):
        self.points = new_points
    
    def set_colour(self, new_colour):
        self.colour = new_colour
    
    def set_state(self, new_state):
        self.state = new_state

    def rotate_poly(self, angle, clockwise):
        points = []
        for i in self.points:
            if clockwise:
                x = math.cos(math.radians(angle))*i[0] - math.sin(math.radians(angle)) * i[1]
                y = math.sin(math.radians(angle))*i[0] + math.cos(math.radians(angle))*i[1]
            else:
                x = math.cos(math.radians(angle))*i[0] + math.sin(math.radians(angle)) * i[1]
                y = - math.sin(math.radians(angle))*i[0] + math.cos(math.radians(angle))*i[1]
            points.append((x,y))
        self.points = points

    def scale_poly(self, scale):
        points = []
        for i in self.points:
            x = scale * i[0]
            y = scale * i[1]
            points.append((x,y))
        self.points = points

    def translate_poly(self, xMove, yMove):
        points = []
        for i in self.points:
            x = i[0] + xMove
            y = i[1] + yMove
            points.append((x,y))
        self.points = points

    def random_state(self):
        s = ""
        for i in range(3):
            if random.randint(0,1) == 0:
                s += "u"
            else:
                s += "d"
        return s


    def random_colour(self):
        return (random.randint(0,255),random.randint(0,255),random.randint(0,255))

    def update_colour(self, colour, change = 20, state = random_state()):
        # make sure no number goes out of index
        for i in range(3):
            if colour[i] + change > 255 and state[i] == "u":
                state = state[:i] + "d" + state[i+1:]
            elif colour[i] - change < 0 and state[i] == "d":
                state = state[:i] + "u" + state[i+1:]

        # update colour
        if state[0] == "u":
            r = colour[0] + change
        else:
            r = colour[0] - change
        if state[1] == "u":
            g = colour[1] + change
        else:
            g = colour[1] - change
        if state[2] == "u":
            b = colour[2] + change
        else:
            b = colour[2] - change
        
        return (r, g, b), state

    def get_area(self):
        corners = self.points
        n = len(corners) # of corners
        area = 0.0
        for i in range(n):
            j = (i + 1) % n
            area += corners[i][0] * corners[j][1]
            area -= corners[j][0] * corners[i][1]
        area = abs(area) / 2.0
        return area

    def draw(self, win):
        pass
        

class triangle(shape):

    def __init__(self):
        super().__init__()
        self.points = [(1,1), (-1,1), (-1,-1)]

class square(shape):

    def __init__(self):
        super().__init__()
        self.points = [(1,1), (1,-1), (-1,-1), (-1,1)]

class star(shape):

    def __init__(self):
        super().__init__()
        self.points = self.base(1)

    def base(self, r):
        pp = []
        for k in range(5):
            pp.append(((r*math.cos(2*math.pi*k/5+math.pi/2)),𝑟*(math.sin(2*math.pi*k/5+math.pi/2))))
            pp.append(((r/2*math.cos(2*math.pi*k/5+math.pi/2)),𝑟/2*(math.sin(2*math.pi*k/5+math.pi/2))))
        return pp