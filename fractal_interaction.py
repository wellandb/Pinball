# Importing necessary modules
from settings import *
from shape import *
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox

# Function to convert the coordinates to pixel values
def to_pixels(x,y):
    return(screenWidth/2 + screenWidth * x/20, screenHeight/2 - screenHeight * y/20)

# Function to convert the pixel values to coordinates
def from_pixels(x, y):
    return(20*x/screenWidth - 10, 10 - 20 * y/screenHeight)

# draw the grid on the window
def draw_grid(win):
    for x in range(-9,10):
        draw_segment(win, (x,-10), (x,10), LIGHT_GRAY)
    for y in range(-9,10):
        draw_segment(win, (-10,y), (10,y), LIGHT_GRAY)
    

    draw_segment(win, (-10,0), (10,0), DARK_GRAY)
    draw_segment(win, (0,-10), (0,10), DARK_GRAY)
    
# Function to create a random state for the colour update values
# binary 3 bit number where 1="u" or up and 0="d" or down, the location of the state is equal to the r,g,b value change direction
def random_state():
    s = ""
    for i in range(3):
        if random.randint(0,1) == 0:
            s += "u"
        else:
            s += "d"
    return s

# draw a polygon given a list of verticies
def draw_poly(win, pp, colour, state=random_state()):
    pixel_points = [to_pixels(x,y) for x,y in pp]
    pygame.draw.polygon(win, colour, pixel_points)
    return [colour, pp, state]

# draw a line segment
def draw_segment(win, v1, v2, colour):
    pygame.draw.line(win, colour, to_pixels(*v1), to_pixels(*v2), 2)
    return [colour, v1, v2]

# create a random colour
def random_colour():
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))

# update colour values based off of state
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
    

# get area of a polygon
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

# create a fractal out of a shape with the given parameters
def create_fractal(shape, angle, clockwise, depth, scale, colour, state, change):
    fractal = []
    regular, frac_shape, sides = shape[0], shape[1], shape[2]
    clr = colour
    scl = scale
    clk = True
    xMove = 0
    yMove = 0
    for i in range(0,depth):
        delete = False
        if regular:
            x = frac_shape(clr, sides)
        else:
            x = frac_shape(clr, sides)
        x.rotate_poly(angle, clockwise)
        x.reflect_poly(45)
        x.translate_poly(xMove, yMove)
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

# redraw the game window and update the screen
def redrawGameWindow(polys, segments, shapes, sliders, outputs, labels):
    win.fill(WHITE)
    draw_grid(win)
    for segment in segments:
        draw_segment(win, segment[1], segment[2], segment[0])
    polys.sort(reverse = True, key=Area)
    for poly in polys:
        draw_poly(win, poly[1], poly[0])
    # To make it look better
    win.fill(BLACK)
    # sort the shapes by area with largest drawn first so you can see the smaller shapes
    shapes.sort(reverse= True, key=lambda x: x.get_area())
    for shape in shapes:
        shape.draw(win)
    for s in sliders:
        s.draw()
    for o in outputs:
        o.draw()
    for l in labels:
        l.draw()
    pygame_widgets.update(pygame.event.get())
    pygame.display.update()

# main function that creates the fractal interaction
def main(regular, sides, angle, clockwise, depth, scale, clr, state, change):
    segments = []
    polys = []
    shapes = []
    # slider and textbox intialises 
    # sliders equate to the parameters of the create fractal function
    # outputs are the current value of the sliders
    # labels are the names of the parameters that the sliders are changing
    reg_slider = Slider(win, screenWidth-100, 0, 100, 40, min=0, max=1, step=1)
    reg_output = TextBox(win, screenWidth-150, 0, 50, 40, fontSize=30, textColour=BLACK)
    reg_label = TextBox(win, screenWidth-300, 0, 150, 40, fontSize=30, textColour=BLACK)
    reg_label.disable() # disable so it only acts as a label rather than something to type text into
    reg_label.setText("Equillateral:") # set label of slider

    sides_slider = Slider(win, screenWidth-100, 50, 100, 40, min=0, max=20, step=1)
    sides_output = TextBox(win, screenWidth-150, 50, 50, 40, fontSize=30, textColour=BLACK)
    sides_label = TextBox(win, screenWidth-300, 50, 150, 40, fontSize=30, textColour=BLACK)
    sides_label.disable()
    sides_label.setText("Sides:")

    angle_slider = Slider(win, screenWidth-100, 100, 100, 40, min=0, max=360, step=1)
    angle_output = TextBox(win, screenWidth-150, 100, 50, 40, fontSize=30, textColour=BLACK)
    angle_label = TextBox(win, screenWidth-300, 100, 150, 40, fontSize=30, textColour=BLACK)
    angle_label.disable()
    angle_label.setText("Angle:")

    clockwise_slider = Slider(win, screenWidth-100,150, 100, 40, min=0, max=1, step=1)
    clockwise_output = TextBox(win, screenWidth-150, 150, 50, 40, fontSize=30, textColour=BLACK)
    clockwise_label = TextBox(win, screenWidth-300, 150, 150, 40, fontSize=30, textColour=BLACK)
    clockwise_label.disable()
    clockwise_label.setText("Clockwise:")

    depth_slider = Slider(win, screenWidth-100, 200, 100, 40, min=1, max=20, step=1)
    depth_output = TextBox(win, screenWidth-150, 200, 50, 40, fontSize=30, textColour=BLACK)
    depth_label = TextBox(win, screenWidth-300, 200, 150, 40, fontSize=30, textColour=BLACK)
    depth_label.disable()
    depth_label.setText("Depth:")

    # scale_slider = Slider(win, screenWidth-100, 250, 100, 40, min=1, max=2, step=0.1)
    # scale_output = TextBox(win, screenWidth-150, 250, 50, 40, fontSize=30, textColour=BLACK)
    # scale_label = TextBox(win, screenWidth-300, 250, 150, 40, fontSize=30, textColour=BLACK)
    # scale_label.disable()
    # scale_label.setText("Scale:")

    clr_slider = Slider(win, screenWidth-100, 250, 100, 40, min=0, max=255, step=1)
    clr_output = TextBox(win, screenWidth-150, 250, 50, 40, fontSize=10, textColour=BLACK)
    clr_label = TextBox(win, screenWidth-300, 250, 150, 40, fontSize=30, textColour=BLACK)
    clr_label.disable()
    clr_label.setText("Colour:")

    state_slider = Slider(win, screenWidth-100, 300, 100, 40, min=0, max=7, step=1)
    state_output = TextBox(win, screenWidth-150, 300, 50, 40, fontSize=30, textColour=BLACK)
    state_label = TextBox(win, screenWidth-300, 300, 150, 40, fontSize=30, textColour=BLACK)
    state_label.disable()
    state_label.setText("RGB Change:")

    change_slider = Slider(win, screenWidth-100, 350, 100, 40, min=1, max=99, step=1)
    change_output = TextBox(win, screenWidth-150, 350, 50, 40, fontSize=30, textColour=BLACK)
    change_label = TextBox(win, screenWidth-300, 350, 150, 40, fontSize=30, textColour=BLACK)
    change_label.disable()
    change_label.setText("Gradient:")

    # create the lists to store the sliders, outputs and labels
    sliders = [reg_slider, sides_slider, angle_slider, clockwise_slider, depth_slider,  clr_slider, state_slider, change_slider] # scale_slider,
    outputs = [reg_output, sides_output, angle_output, clockwise_output, depth_output,  clr_output, state_output, change_output] #scale_output,
    for i in range(len(outputs)):
        outputs[i].disable()
        outputs[i].setText(sliders[i].getValue())
        
    labels = [reg_label, sides_label, angle_label, clockwise_label, depth_label,  clr_label, state_label, change_label] # scale_label,
    # shape lists store the possible shapes to be drawn
    irregular_shapes = [Star, Irregular, Irregular2, Irregular3]
    # irregular_shapes = [Irregular3]
    regular_shape = Polygon
    if regular:
        shape = (True, regular_shape, 3+sides%12)
    else:
        shape = (False, irregular_shapes[sides%len(irregular_shapes)], sides)


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
            scale_frac = 0.95
        elif keys[pygame.K_DOWN]:
            scale_frac = 1.05
        else:
            scale_frac = 1

        regular = reg_slider.getValue()
        reg_output.setText(regular)

        sides = sides_slider.getValue()
        sides_output.setText(sides)

        angle = angle_slider.getValue()
        angle_output.setText(angle)

        clockwise = clockwise_slider.getValue()
        clockwise_output.setText(clockwise)

        depth = depth_slider.getValue()
        depth_output.setText(depth)

        # scale = scale_slider.getValue()
        # scale_output.setText(scale)

        clr = (clr_slider.getValue(),clr_slider.getValue(),clr_slider.getValue())
        clr_output.setText(clr)

        state = state_slider.getValue()
        if state == 0:
            state = "ddd"
        elif state == 1:
            state = "ddu"
        elif state == 2:
            state = "dud"
        elif state == 3:
            state = "duu"
        elif state == 4:
            state = "udd"
        elif state == 5:
            state = "udu"
        elif state == 6:
            state = "uud"
        else:
            state = "uuu"
        state_output.setText(state)

        change = change_slider.getValue()
        change_output.setText(change)

        if regular == 1:
            shape = (True, regular_shape, 3+sides%12)
        else:
            shape = (False, irregular_shapes[sides%len(irregular_shapes)], sides)

        rotation = 1
        for s in sliders:
            s.listen(pygame.event.get())
        

        if keys[pygame.K_SPACE]:
            scale = 1 + 1/(depth/4)
            shapes = create_fractal(shape, angle, clockwise, depth, scale, clr, state, change)

        for s in shapes:
            s.rotate_poly(rotation, s.get_clockwise())
            s.update_colour(3)
            s.scale_poly(scale_frac)

        redrawGameWindow(polys, segments, shapes, sliders, outputs, labels)