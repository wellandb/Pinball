# Importing necessary modules
from settings import *

# Use these for pixel and location definition
def to_pixels(x,y):
    return(screenWidth/2 + screenWidth * x/20, screenHeight/2 - screenHeight * y/20)

# Function to convert pixel values to coordinates
def from_pixels(x, y):
    return(20*x/screenWidth - 10, 10 - 20 * y/screenHeight)

# Function that creates a random state of change for the r.g.b values of the colour of a shape
# It creates a 3 bit binary number with 1="u" or up and 0 ="d" or down
def random_state():
    s = ""
    for i in range(3):
        if random.randint(0,1) == 0:
            s += "u"
        else:
            s += "d"
    return s

# Class that creates a Shape
class Shape(pygame.sprite.Sprite):
    
    def __init__(self,colour):
        super().__init__() # each shape is a sprite
        # self.x = x
        # self.y = y
        self.colour = colour
        self.points = []
        self.state = random_state()
        self.clockwise = True
    
    def get_points(self): # return the verticies of the shape
        return self.points
    
    def get_colour(self): # returns the colour of the shape
        return self.colour
    
    def get_state(self): # returns the state of the shape
        return self.state

    def set_points(self, new_points): # Method to set the list of verticies to a new set of verticies
        self.points = new_points
    
    # Method to set the colour of a shape
    def set_colour(self, new_colour):
        self.colour = new_colour
    
    # Method that sets the state of a shape
    def set_state(self, new_state):
        self.state = new_state
    
    # Method to get the rotation direction of the shape: True = clockwise, False = anticlockwise
    def get_clockwise(self):
        return self.clockwise

    # Method to set the rotation direction of the shape: True = clockwise, False = anticlockwise
    def set_clockwise(self, bool_val):
        self.clockwise = bool_val

    # MEthod to rotate the shape by a certain angle in a certain direction
    def rotate_poly(self, angle, clockwise):
        points = [] # all the verticies change so we store them in a new list of the "points"
        for i in self.points:
            # This is the matrix equation for rotating a point around 0,0
            if clockwise:
                x = math.cos(math.radians(angle))*i[0] - math.sin(math.radians(angle)) * i[1] 
                y = math.sin(math.radians(angle))*i[0] + math.cos(math.radians(angle)) * i[1]
            else:
                x = math.cos(math.radians(angle))*i[0] + math.sin(math.radians(angle)) * i[1]
                y = - math.sin(math.radians(angle))*i[0] + math.cos(math.radians(angle))* i[1]
            points.append((x,y))
        self.points = points

    # Change the size of the shape
    def scale_poly(self, scale):
        points = [] # new points list needed as all points change when changing the size
        # Matrix equation for scaling the shape from 0,0
        for i in self.points:
            x = scale * i[0]
            y = scale * i[1]
            points.append((x,y))
        self.set_points(points)
        # If the new area of the shape is so great that it is much greater than the size of the window
        # then return True as to delete the shape as it will slow the program down massively or could just crash
        if self.get_area() > 1000:
            return True
        return False

    # Move the shape coordinates by x,y 
    def translate_poly(self, xMove, yMove):
        points = []
        for i in self.points:
            x = i[0] + xMove
            y = i[1] + yMove
            points.append((x,y))
        self.points = points
    
    # Reflection or symmetry of the shape by a certain angle (angle is the bearing from y=0 line)
    def reflect_poly(self, angle):
        points = []
        for i in self.points:
            x = math.cos(math.radians(2*angle))*i[0] + math.sin(math.radians(2*angle)) * i[1]
            y = math.sin(math.radians(2*angle))*i[0] - math.cos(math.radians(2*angle)) * i[1]
            points.append((x,y))
        self.points = points
        return points

    # Method to get a random colour
    def random_colour(self):
        return (random.randint(0,255),random.randint(0,255),random.randint(0,255))

    # Method to update the colour of the shape by the state, with a certain change of value for the r,g,b values
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
        
    # Method to get the area of the shape
    def get_area(self):
        corners = self.points
        n = len(corners) # of corners
        area = 0.0
        # Formula to work out the area of a shape given the verticies
        for i in range(n):
            j = (i + 1) % n
            area += corners[i][0] * corners[j][1]
            area -= corners[j][0] * corners[i][1]
        area = abs(area) / 2.0
        return area

    # Draw the shape onto the window specified
    def draw(self, win):
        pixel_points = [to_pixels(x,y) for x,y in self.points]
        pygame.draw.polygon(win, self.colour, pixel_points)
        
# A Triangle class, child of Shape
class Triangle(Shape):

    # Initialize the triangle
    def __init__(self, colour):
        super().__init__(colour) # It is a shape so get all the methods and attributes from shape
        self.points = [(1,1), (-1,1), (0,-1)] # set of verticies for a triangele 
        self.base_points = self.points # set the base of the triangle so it can be refrenced later if any transformations occur on that shape

# Square Class, child of Shape
class Square(Shape):

    def __init__(self, colour):
        super().__init__(colour)
        self.points = [(1,1), (1,-1), (-1,-1), (-1,1)]
        self.base_points = self.points

# star class, child of shape
class Star(Shape):

    def __init__(self, colour, sides):
        super().__init__(colour)
        self.points = self.base(1)
        self.base_points = self.base(1)

    # function to create a star shape and returns the verticies
    def base(self, r):
        pp = []
        for k in range(5):
            pp.append(((r*math.cos(2*math.pi*k/5+math.pi/2)),𝑟*(math.sin(2*math.pi*k/5+math.pi/2))))
            pp.append(((r/2*math.cos(2*math.pi*k/5+math.pi/2)),𝑟/2*(math.sin(2*math.pi*k/5+math.pi/2))))
        return pp

# Irregular shape class
class Irregular(Shape):
    def __init__(self, colour, sides):
        super().__init__(colour)
        # don't set sides too high or it lags
        if sides < 3 or sides > 13:
            sides = 3 + sides % 10
        self.sides = sides
        self.points = self.base(1)
        self.base_points = self.base(1)
        points = self.points # save initial points
        # reflect the intial shape to all 4 quartes of the screen to create a more full shape
        self.reflect_poly(90)
        for i in self.points:
            points.append(i)
        self.reflect_poly(180)
        for i in self.points:
            points.append(i)
        self.reflect_poly(270)
        for i in points:
            self.points.append(i)
        
    # Function to create a irregular shape 
    def base(self, r):
        pp = []
        for k in range(self.sides):
            pp.append((math.sqrt(r*math.cos(2*math.pi*k/5+math.pi/2)**2),math.sqrt(𝑟*(math.sin(2*math.pi*k/5+math.pi/2))**2)))
            pp.append((math.sqrt(r/2*math.cos(2*math.pi*k/5+math.pi/2)**2),math.sqrt(𝑟/2*(math.sin(2*math.pi*k/5+math.pi/2))**2)))
        return pp

# class to create an equilateral polygon, child of shape
class Polygon(Shape):

    # rotate around 0,0 with a radius and angle to work out the next point
    def rotate(self, radius, angle):
        # points is a tuple
        new_points = (radius*math.cos(angle), radius*math.sin(angle))
        return new_points

    # intialize object with sides to decide the number of sides that the equillateral polygon has
    def __init__(self, colour, sides):
        super().__init__(colour)
        org_angle = 2*math.pi/sides # original angle
        radius = 1 # intial radiuse
        for i in range(sides): # create a verticie of the polygon for each side
            angle = org_angle*i # work out angle of verticie from 0,0
            self.points.append(self.rotate(radius, angle)) # add verticie to points
            
# Irregular2 shape class
class Irregular2(Shape):
    def __init__(self, colour, sides):
        super().__init__(colour)
        # don't set sides too high or it lags
        if sides < 3 or sides > 13:
            sides = 3 + sides % 10
        self.sides = sides
        self.points = self.base(1)
        self.base_points = self.base(1)
        points = self.points # save initial points
        # reflect the intial shape to all 4 quartes of the screen to create a more full shape
        self.reflect_poly(90)
        for i in self.points:
            points.append(i)
        self.reflect_poly(180)
        for i in self.points:
            points.append(i)
        self.reflect_poly(270)
        for i in points:
            self.points.append(i)
        

    # intialize object with sides to decide the number of sides that the equillateral polygon has
    def base(self, r):
        pp = []
        for k in range(self.sides):
            pp.append((math.sqrt(r*math.sin(2*math.pi*k/10+math.pi/2)**2),math.sqrt(𝑟*(math.cos(2*math.pi*k/10+math.pi/2))**2)))
            pp.append((math.sqrt(r/2*math.sin(2*math.pi*k/5+math.pi/2)**2),math.sqrt(𝑟/2*(math.cos(2*math.pi*k/5+math.pi/2))**2)))
            pp.append((math.sqrt(r/4*math.sin(2*math.pi*k/5+math.pi/2)**2),math.sqrt(𝑟/4*(math.cos(2*math.pi*k/5+math.pi/2))**2)))
        return pp


# Irregular3 shape class
class Irregular3(Shape):
    def __init__(self, colour, sides):
        super().__init__(colour)
        # don't set sides too high or it lags
        if sides < 3 or sides > 13:
            sides = 3 + sides % 10
        self.sides = sides
        self.points = self.base(1)
        self.base_points = self.base(1)
        points = self.points # save initial points
        # reflect the intial shape to all 4 quartes of the screen to create a more full shape
        self.reflect_poly(90)
        for i in self.points:
            points.append(i)
        self.reflect_poly(180)
        for i in self.points:
            points.append(i)
        self.reflect_poly(270)
        for i in points:
            self.points.append(i)
        

    # intialize object with sides to decide the number of sides that the equillateral polygon has
    def base(self, r):
        pp = []
        for k in range(self.sides):
            pp.append((r*math.sin(2*math.pi*k/10+math.pi/2),𝑟*(math.cos(2*math.pi*k/10+math.pi/2))))
            pp.append((r/2*math.sin(2*math.pi*k/10+math.pi/2),𝑟/2*(math.cos(2*math.pi*k/10+math.pi/2))))
        return pp