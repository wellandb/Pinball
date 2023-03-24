# Import necessary modules and classes
from settings import * # creates the window and initialises needed variables
from shape import *

# change's the x,y coordinates to pixel position
def to_pixels(x,y):
    return(screenWidth/2 + screenWidth * x/20, screenHeight/2 - screenHeight * y/20)

# Function to convert pixel values to coordinates
def from_pixels(x, y):
    return(20*x/screenWidth - 10, 10 - 20 * y/screenHeight)

# draws a grid to be able to tell x,y location from eye
def draw_grid(win):
    for x in range(-9,10):
        draw_segment(win, (x,-10), (x,10), LIGHT_GRAY)
    for y in range(-9,10):
        draw_segment(win, (-10,y), (10,y), LIGHT_GRAY)
    

    draw_segment(win, (-10,0), (10,0), DARK_GRAY)
    draw_segment(win, (0,-10), (0,10), DARK_GRAY)
    
# creates a random state
def random_state():
    s = ""
    for i in range(3):
        if random.randint(0,1) == 0:
            s += "u"
        else:
            s += "d"
    return s

# draws a polygon given pixel points of verticies
def draw_poly(win, pp, colour, state=random_state()):
    pixel_points = [to_pixels(x,y) for x,y in pp]
    pygame.draw.polygon(win, colour, pixel_points)
    return [colour, pp, state]

# draws a line segment 
def draw_segment(win, v1, v2, colour):
    pygame.draw.line(win, colour, to_pixels(*v1), to_pixels(*v2), 2)
    return [colour, v1, v2]

# creates a random colour
def random_colour():
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))

# updates the r,g,b values of the colour depending on state, u = up, d = down 
def update_colour(colour, change, state):
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
    
    return (r, g, b)
    

# gets area of polygon
def Area(poly):
    corners = poly[1]
    n = len(corners) # of corners
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += corners[i][0] * corners[j][1]
        area -= corners[j][0] * corners[i][1]
    area = abs(area) / 2.0
    return area

# creates the fractal for a given shape
def create_fractal(shape, angle, clockwise, depth, scale, colour, state, change):
    fractal = [] # fractal list
    regular, frac_shape, sides = shape[0], shape[1], shape[2] # get the shape
    clr = colour
    scl = scale
    clk = True
    xMove = 0
    yMove = 0
    for i in range(0,depth): # self repeating function
        delete = False
        x = frac_shape(clr, sides) # creeate shape
        x.rotate_poly(angle, clockwise) # rotate shape
        x.reflect_poly(45) # reflect it in the x,y line
        x.translate_poly(xMove, yMove) # move shape by x, y
        if x.scale_poly(scale): # scale the poly and return true if the shape is so big that it should be deleted
            delete = True
        x.set_state(state) # set the state of the shape
        x.set_clockwise(clk) # set the rotation of the shape
        if not delete: # if the shape is small enough
            fractal.append(x) # add shape to fractal
        scale *= scl # increase the scale of the next fractal
        clr = update_colour(clr, change, state) # update the colour of the next fractal by change
        clk = not(clk) # flip direction of rotation for the next shape
        # if i < depth/4:
        #     xMove = (xMove + 0.01) % 1
        #     yMove = (yMove + 0.01) % 1
        # elif i < depth*3/4:
        #     xMove = (xMove - 0.01) 
        #     yMove = (yMove - 0.01)
        # else:
        #     xMove = (xMove + 0.01) 
        #     yMove = (yMove + 0.01) 

    return fractal

# Function to redraw the game window
def redrawGameWindow(polys, segments, shapes):
    # fills the background with white
    win.fill(WHITE)
    draw_grid(win) # draw the grid
    for segment in segments: # draw the segments
        draw_segment(win, segment[1], segment[2], segment[0])
    polys.sort(reverse = True, key=Area) # sort the shapes so the largest are drawn first so that you can see the smaller shapes
    for poly in polys:
        draw_poly(win, poly[1], poly[0])
    # To make it look better
    win.fill(BLACK) # fill the background black for a better look
    shapes.sort(reverse= True, key=lambda x: x.get_area()) # sort the shapes so the largest are drawn first so that you can see the smaller shapes
    for shape in shapes: # draw the shapes
        shape.draw(win)
    pygame.display.update()

# main function called, takes in all the parameters for the fractal creation
def main(regular, sides, angle, clockwise, depth, scale, clr, state, change):
    # initialize lists to store the segments
    segments = []
    # initialize lists to store the polygons
    polys = []
     # initialize lists to store the shapes
    shapes = []

    # triangle = Triangle
    # square = Square
    # star = Star
    # polygon = Polygon
    # list that stores the possible irregular classes
    irregular_shapes = [Star, Irregular, Irregular2, Irregular3]
    # shape = pos_shapes[shape % len(pos_shapes)]
    # regular class is made of polygons of different shapes
    regular_shape = Polygon
    # creates the shape of the fractal to be repeated
    if regular:
        shape = (True, regular_shape, 3+sides%7)
    else:
        shape = (False, irregular_shapes[sides%len(irregular_shapes)], sides)
        # if irregular_shapes[sides%len(irregular_shapes)] == Irregular3:
        #     depth = depth % 11
    # creates the fractal and stores it in shapes
    shapes = create_fractal(shape, angle, clockwise, depth, scale, clr, state, change)
    # shapes = create_fractal(star, 20, True, 10, 1.2, (146, 231, 56), 'udu', 3)

    # stores the roation of the fractal each frame
    rotation = 1

    # loop to display and interact with fractal
    done = False
    while not done:
        # frame rate
        clock.tick(30)

        # event checker to see whether or not to quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        
        # Interaction with fractal
        # gets the state of all the keys on the keyboard
        keys = pygame.key.get_pressed()

        # if pressing up then scale all the shapes down
        if keys[pygame.K_UP]:
            scale = 0.95
        # if pressing down then scale all the shapes up
        elif keys[pygame.K_DOWN]:
            scale = 1.05
        # otherwise don't change the size of the shapes
        else:
            scale = 1

        # Create changes to the fractal
        # for i in range(len(polys)):
        #     # change colour based on what is stored by that shape
        #     new_colour, new_state = update_colour(polys[i][0], 1, polys[i][2])
        #     # rotate and scale new points
        #     new_points = scale_poly(rotate_poly(polys[i][1], 5, True), scale)
        #     # update polygons
        #     polys[i] = [new_colour, new_points, new_state]

        # loops through the shapes 
        for s in shapes:
            s.rotate_poly(rotation, s.get_clockwise()) # rotates the shape in the direction it wants with a set rotation per frame
            s.update_colour(3) # update the colour the shape by it's state
            s.scale_poly(scale) # scale the shape by the scale given through the interaction of the user

        
        # check that shapes aren't too small/big and then remove all that are too big/small to improve performance
        # polys = check_polys(polys, star(1))
        # redraw the window
        redrawGameWindow(polys, segments, shapes)
# main(False, 5, 20, False, 14, 1.3, BLUE, 'udu', 15)