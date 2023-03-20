from settings import *
from shape import *

def to_pixels(x,y):
    return(screenWidth/2 + screenWidth * x/20, screenHeight/2 - screenHeight * y/20)

def from_pixels(x, y):
    return(20*x/screenWidth - 10, 10 - 20 * y/screenHeight)

def draw_grid(win):
    for x in range(-9,10):
        draw_segment(win, (x,-10), (x,10), LIGHT_GRAY)
    for y in range(-9,10):
        draw_segment(win, (-10,y), (10,y), LIGHT_GRAY)
    

    draw_segment(win, (-10,0), (10,0), DARK_GRAY)
    draw_segment(win, (0,-10), (0,10), DARK_GRAY)
    
def random_state():
    s = ""
    for i in range(3):
        if random.randint(0,1) == 0:
            s += "u"
        else:
            s += "d"
    return s

def draw_poly(win, pp, colour, state=random_state()):
    pixel_points = [to_pixels(x,y) for x,y in pp]
    pygame.draw.polygon(win, colour, pixel_points)
    return [colour, pp, state]

def draw_segment(win, v1, v2, colour):
    pygame.draw.line(win, colour, to_pixels(*v1), to_pixels(*v2), 2)
    return [colour, v1, v2]

def random_colour():
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))

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

def create_fractal(shape, angle, clockwise, depth, scale, colour, state, change):
    fractal = []
    if shape[0]:
        regular, frac_shape, sides = True, shape[1], shape[2]
    else:
        regular, frac_shape = False, shape[1]
    clr = colour
    scl = scale
    clk = True
    for i in range(0,depth):
        delete = False
        if regular:
            x = frac_shape(clr, sides)
        else:
            x = frac_shape(clr)
        x.rotate_poly(angle, clockwise)
        if x.scale_poly(scale):
            delete = True
        x.set_state(state)
        x.set_clockwise(clk)
        if not delete:
            fractal.append(x)
        scale *= scl
        clr = update_colour(clr, change, state)
        clk = not(clk)
    return fractal


def redrawGameWindow(polys, segments, shapes):
    win.fill(WHITE)
    draw_grid(win)
    for segment in segments:
        draw_segment(win, segment[1], segment[2], segment[0])
    polys.sort(reverse = True, key=Area)
    for poly in polys:
        draw_poly(win, poly[1], poly[0])
    # To make it look better
    win.fill(BLACK)
    shapes.sort(reverse= True, key=lambda x: x.get_area())
    for shape in shapes:
        shape.draw(win)
    pygame.display.update()

def main(regular, sides, angle, clockwise, depth, scale, clr, state, change):
    segments = []
    polys = []
    shapes = []

    # triangle = Triangle
    # square = Square
    # star = Star
    # polygon = Polygon
    irregular_shapes = [Star]
    # shape = pos_shapes[shape % len(pos_shapes)]
    regular_shape = Polygon
    if regular:
        shape = (True, Polygon, 3+sides%13)
    else:
        shape = (False, irregular_shapes[sides%len(irregular_shapes)])

    angle = 20
    clockwise = True
    rotation = 1

    shapes = create_fractal(shape, angle, clockwise, depth, scale, clr, state, change)
    # shapes = create_fractal(star, 20, True, 10, 1.2, (146, 231, 56), 'udu', 3)


    done = False
    while not done:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        
        # Interaction with fractal
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            scale = 0.95
        elif keys[pygame.K_DOWN]:
            scale = 1.05
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

        for s in shapes:
            s.rotate_poly(rotation, s.get_clockwise())
            s.update_colour(3)
            s.scale_poly(scale)

        
        # check that shapes aren't too small/big and then remove all that are too big/small to improve performance
        # polys = check_polys(polys, star(1))
        # redraw the window
        redrawGameWindow(polys, segments, shapes)
