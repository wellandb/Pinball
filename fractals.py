from settings import *


"""
import turtle

TK_SILENCE_DEPRECATION=1
min_branch_lenght = 5

wn = turtle.Screen()
wn.setup(width = 1200, height = 600)

def build_tree(t, branch_length, shorten_by, angle):
    if branch_length > min_branch_lenght:
        t.forward(branch_length)
        new_length = branch_length - shorten_by

        t.left(angle)
        build_tree(t, new_length, shorten_by, angle)

        t.right(angle*2)
        build_tree(t, new_length, shorten_by, angle)

        t.left(angle)
        t.backwards(branch_length)
        print("bye")
def setUp():
    
    tree = turtle.Turtle()

    tree.setheading(90)
    tree.color('green')
    tree.speed(100)
    tree.goto(0,0)
    tree.pendown()
    tree.forward(100)
    print("hey")

    build_tree(tree, 50, 5, 30)

setUp()
while True:
    wn.update()

"""
def to_pixels(x,y):
    return(screenWidth/2 + screenWidth * x/20, screenHeight/2 - screenHeight * y/20)

def draw_grid(win, segments):
    for x in range(-9,10):
        draw_segment(win, (x,-10), (x,10), LIGHT_GRAY, segments)
    for y in range(-9,10):
        draw_segment(win, (-10,y), (10,y), LIGHT_GRAY, segments)
    

    draw_segment(win, (-10,0), (10,0), DARK_GRAY, segments)
    draw_segment(win, (0,-10), (0,10), DARK_GRAY, segments)
    

def draw_poly(win, pp, colour, polys):
    pixel_points = [to_pixels(x,y) for x,y in pp]
    pygame.draw.polygon(win, colour, pixel_points)
    polys.append([colour, pp])

def redraw_poly(win, pp, colour):
    pixel_points = [to_pixels(x,y) for x,y in pp]
    pygame.draw.polygon(win, colour, pixel_points)

def draw_segment(win, v1, v2, colour, segments):
    pygame.draw.line(win, colour, to_pixels(*v1), to_pixels(*v2), 2)
    segments.append([colour, v1, v2])

def redraw_segment(win, v1, v2, colour):
    pygame.draw.line(win, colour, to_pixels(*v1), to_pixels(*v2), 2)

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

def update_colour(colour, state = "uuu", change = 20):
    # make sure no number goes out of index
    for i in range(3):
        if colour[i] + change >= 255 and state[i] == "u":
            state = state[:i] + "d" + state[i+1:]
        elif colour[i] - change <= 0 and state[i] == "d":
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
    

# also could add symetry
def fractal_poly(angle, clockwise, depth, scale, random):
    # recreate poly at an angle
    for i in range(depth):
        # Update colour, scale poly by 2, rotate poly by angle
        #polys.append([update_colour(polys[-1][0]),scale_poly(rotate_poly(polys[-1][1], angle, clockwise),2)])
        # Random Colour
        if random:
            polys.append([random_colour(),scale_poly(rotate_poly(polys[-1][1], angle, clockwise),scale)])
        else:
            polys.append([update_colour(polys[-1][0]),scale_poly(rotate_poly(polys[-1][1], angle, clockwise),scale)])


def redrawGameWindow(polys, segments):
    win.fill(WHITE)
    for segment in segments:
        redraw_segment(win, segment[1], segment[2], segment[0])
    for poly in reversed(polys):
        redraw_poly(win, poly[1], poly[0])
    pygame.display.update()

segments = []
polys = []

# draw triangle in middle of screen
triangle = [(1,1), (-1,1), (-1,-1)]
square = [(1,1), (1,-1), (-1,-1), (-1,1)]
def star(r):
    pp = []
    for k in range(5):
        print(((r*math.cos(2*math.pi*k/5+math.pi/2)),𝑟*(math.sin(2*math.pi*k/5+math.pi/2))))
        pp.append(((r*math.cos(2*math.pi*k/5+math.pi/2)),𝑟*(math.sin(2*math.pi*k/5+math.pi/2))))
        pp.append(((r/2*math.cos(2*math.pi*k/5+math.pi/2)),𝑟/2*(math.sin(2*math.pi*k/5+math.pi/2))))
    return pp

draw_grid(win, segments)
draw_poly(win, square, BLUE, polys)
# Fractal
fractal_poly(35, True, 10, 1.5, False)

done = False
while not done:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    keys = pygame.key.get_pressed()

    redrawGameWindow(polys, segments)

pygame.quit()
