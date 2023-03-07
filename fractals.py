from settings import *

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

def rotate_poly(poly, angle, clockwise):
    points = []
    for i in poly:
        if clockwise:
            x = math.cos(math.radians(angle))*i[0] - math.sin(math.radians(angle)) * i[1]
            y = math.sin(math.radians(angle))*i[0] + math.cos(math.radians(angle))*i[1]
        else:
            x = math.cos(math.radians(angle))*i[0] + math.sin(math.radians(angle)) * i[1]
            y = - math.sin(math.radians(angle))*i[0] + math.cos(math.radians(angle))*i[1]
        points.append((x,y))
    return points

def scale_poly(poly, scale):
    points = []
    for i in poly:
        x = scale * i[0]
        y = scale * i[1]
        points.append((x,y))
    return points

def translate_poly(poly, xMove, yMove):
    points = []
    for i in poly:
        x = i[0] + xMove
        y = i[1] + yMove
        points.append((x,y))
    return points


def random_colour():
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))

def update_colour(colour, change = 20, state = random_state()):
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

# check if shapes are not needed to be shown and then removes them to speed up frctal and stop choppy effect
def check_polys(polys, shape):
    screenArea = Area([0,[from_pixels(0,0), from_pixels(0,screenHeight), from_pixels(screenWidth,screenHeight), from_pixels(screenWidth,0)]])
    for i in range(len(polys)):
        if Area(polys[i]) > 1600:
            polys.append(draw_poly(win, shape, polys[i][0], polys[i][2]))
            polys.remove(polys[i])
        if Area(polys[i]) < Area([0, shape]) * 0.75:
            polys.append(draw_poly(win, scale_poly(shape, math.sqrt(screenArea / Area([0, shape]))), polys[i][0]))
            polys.remove(polys[i])
    return polys

# checks that all veticies are offscreen
def offscreen(points):
    off = True
    for a,b in points:
        x, y = to_pixels(a,b)
        if  x > 0 and y > 0 and x < screenWidth and y < screenHeight:
            off = False
    return off

# also could add symetry
def fractal_poly(angle, clockwise, depth, scale, random, poly, poly_list):
    # recreate poly at an angle
    # Update colour, scale poly by 2, rotate poly by angle
    #polys.append([update_colour(polys[-1][0]),scale_poly(rotate_poly(polys[-1][1], angle, clockwise),2)])
    # Random Colour
    if random:
        p = [random_colour(),scale_poly(rotate_poly(poly[1], angle, clockwise),scale), random_state()]
    else:
        p = [update_colour(poly[0], 5, poly[2])[0], scale_poly(rotate_poly(poly[1], angle, clockwise),scale), poly[2]]

    poly_list.append(p)
    if depth == 1 or Area(poly) > 1600:
        return
    else:
        fractal_poly(angle, clockwise, depth - 1, scale, random, p, poly_list)




def redrawGameWindow(polys, segments):
    win.fill(WHITE)
    draw_grid(win)
    for segment in segments:
        draw_segment(win, segment[1], segment[2], segment[0])
    polys.sort(reverse = True, key=Area)
    for poly in polys:
        draw_poly(win, poly[1], poly[0])
    pygame.display.update()

def main():
    segments = []
    polys = []

    # draw triangle in middle of screen
    triangle = [(1,1), (-1,1), (-1,-1)]
    square = [(1,1), (1,-1), (-1,-1), (-1,1)]

    def star(r):
        pp = []
        for k in range(5):
            pp.append(((r*math.cos(2*math.pi*k/5+math.pi/2)),𝑟*(math.sin(2*math.pi*k/5+math.pi/2))))
            pp.append(((r/2*math.cos(2*math.pi*k/5+math.pi/2)),𝑟/2*(math.sin(2*math.pi*k/5+math.pi/2))))
        return pp

    # shapes
    shapes = [triangle, square, star(1)]


    #polys.append(draw_poly(win, star(1), BLACK))
    polys.append(draw_poly(win, square, BLUE))
    #polys.append(draw_poly(win, triangle, RED))

    # Fractal
    #fractal_poly(50, True, 15, 1.33, True, [BLACK, star(1)])
    fractal_poly(35, True, 15, 1.2, False, [BLUE, square, random_state()], polys)
    #fractal_poly(26, True, 4, 5, True, [RED, triangle])


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
        for i in range(len(polys)):
            # change colour based on what is stored by that shape
            new_colour, new_state = update_colour(polys[i][0], 1, polys[i][2])
            # rotate and scale new points
            new_points = scale_poly(rotate_poly(polys[i][1], 5, True), scale)
            # update polygons
            polys[i] = [new_colour, new_points, new_state]

        
        # check that shapes aren't too small/big and then remove all that are too big/small to improve performance
        polys = check_polys(polys, square)
        # redraw the window
        redrawGameWindow(polys, segments)

main()
pygame.quit()