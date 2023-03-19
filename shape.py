from settings import *

# Use these for pixel and location definition
def to_pixels(x,y):
    return(screenWidth/2 + screenWidth * x/20, screenHeight/2 - screenHeight * y/20)

def from_pixels(x, y):
    return(20*x/screenWidth - 10, 10 - 20 * y/screenHeight)

def random_state():
    s = ""
    for i in range(3):
        if random.randint(0,1) == 0:
            s += "u"
        else:
            s += "d"
    return s

class Shape(pygame.sprite.Sprite):
    
    def __init__(self,colour):
        super().__init__()
        # self.x = x
        # self.y = y
        self.colour = colour
        self.points = []
        self.state = random_state()
        self.clockwise = True
    
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
    
    def get_clockwise(self):
        return self.clockwise

    def set_clockwise(self, bool_val):
        self.clockwise = bool_val

    def rotate_poly(self, angle, clockwise):
        points = []
        for i in self.points:
            if clockwise:
                x = math.cos(math.radians(angle))*i[0] - math.sin(math.radians(angle)) * i[1]
                y = math.sin(math.radians(angle))*i[0] + math.cos(math.radians(angle)) * i[1]
            else:
                x = math.cos(math.radians(angle))*i[0] + math.sin(math.radians(angle)) * i[1]
                y = - math.sin(math.radians(angle))*i[0] + math.cos(math.radians(angle))* i[1]
            points.append((x,y))
        self.points = points

    def scale_poly(self, scale):
        points = []
        for i in self.points:
            x = scale * i[0]
            y = scale * i[1]
            points.append((x,y))
        self.set_points(points)
        print(self.get_area(), 20*20, self.points)
        if self.get_area() > 20*20:
            print('too big')
            return True
        return False

    def translate_poly(self, xMove, yMove):
        points = []
        for i in self.points:
            x = i[0] + xMove
            y = i[1] + yMove
            points.append((x,y))
        self.points = points


    def random_colour(self):
        return (random.randint(0,255),random.randint(0,255),random.randint(0,255))

    def update_colour(self, change = 20):
        # make sure no number goes out of index
        for i in range(3):
            if self.colour[i] + change > 255 and self.state[i] == "u":
                self.state = self.state[:i] + "d" + self.state[i+1:]
            elif self.colour[i] - change < 0 and self.state[i] == "d":
                self.state = self.state[:i] + "u" + self.state[i+1:]

        # update colour
        if self.state[0] == "u":
            r = self.colour[0] + change
        else:
            r = self.colour[0] - change
        if self.state[1] == "u":
            g = self.colour[1] + change
        else:
            g = self.colour[1] - change
        if self.state[2] == "u":
            b = self.colour[2] + change
        else:
            b = self.colour[2] - change
        
        self.colour = (r, g, b)
        

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
        print('drawing', self.points)
        pixel_points = [to_pixels(x,y) for x,y in self.points]
        pygame.draw.polygon(win, self.colour, pixel_points)
        

class Triangle(Shape):

    def __init__(self, colour):
        super().__init__(colour)
        self.points = [(1,1), (-1,1), (0,-1)]
        self.base_points = self.points

class Square(Shape):

    def __init__(self, colour):
        super().__init__(colour)
        self.points = [(1,1), (1,-1), (-1,-1), (-1,1)]
        self.base_points = self.points

class Star(Shape):

    def __init__(self, colour):
        super().__init__(colour)
        self.points = self.base(1)
        self.base_points = self.base(1)

    def base(self, r):
        pp = []
        for k in range(5):
            pp.append(((r*math.cos(2*math.pi*k/5+math.pi/2)),𝑟*(math.sin(2*math.pi*k/5+math.pi/2))))
            pp.append(((r/2*math.cos(2*math.pi*k/5+math.pi/2)),𝑟/2*(math.sin(2*math.pi*k/5+math.pi/2))))
        return pp
    
class Polygon(Shape):

    def rotate(self, radius, angle):
        # points is a tuple
        new_points = (radius*math.cos(angle), radius*math.sin(angle))
        return new_points


    def __init__(self, colour, sides):
        super().__init__(colour)
        org_angle = 2*math.pi/sides
        radius = 1
        for i in range(sides):
            angle = org_angle*i
            self.points.append(self.rotate(radius, angle))
            print(self.points)
            