from settings import *
import fractals
import chatgpt_query

# Works out the mean angle out of a list of angles
def mean_angle(angles):
    return math.degrees(cmath.phase(sum(cmath.rect(1, math.radians(a)) for a in angles)/len(angles)))

def main(line = -1):
    # Route tracker is a text file that stores all the peg locations and ball velocity of every ball and peg collision
    file = open("route_tracker.txt", "r")
    # split into all the different routes
    lines = file.read().splitlines()
    # choose the line to create the fractal with, set as the last line
    fractal_line = lines[line].split()
    file.close()

    # stores the positions of all the collided pegs
    pegs = []
    # stores the velocity of the ball
    vels = []

    # split the stored values into pegs and velocity
    for i in range(len(fractal_line)):
        if i%4 == 0:
            pegs.append([float(fractal_line[i]),float(fractal_line[i+1])])
        if i%4 == 2:
            vels.append([float(fractal_line[i]),float(fractal_line[i+1])])

    # if no collisions made
    if len(pegs) == 0 or len(vels) == 0:
        fractals.main(False, 1, 25, True, 19, 1.2, RED, 'uuu', 10)
        return
    # Fractal inputs

    # could make multiple shapes
    # could make syymetric shapes

    # SHAPE
    # needs number of shapes, then

    #for i in range(len(shapes)):
    #    if pegs % len(shapes) == i:
    #        shape = i

    # regular = True, means that the shape created will be a equillateral polygon
    # regular = False, means that the shape will be chosen from the irregular shapes list
    if len(pegs) % 2 == 1:
        regular = False
    else:
        regular = True
    # either the sides of the polygon or the number modulo length of list for irregular shapes
    shape = 3 + len(pegs) % 10
    

    # ANGLE
    # work out average angle of ball and use that, bearing from positive x & y which in pygame is right and down respecively, then taken counter clockwise as y has been switched so should bearing rotation
    angles = []
    for x,y in vels:
        temp_angle = math.degrees(math.atan(float(x)/float(y)))
        if temp_angle < 0:
            temp_angle  = 360 + temp_angle
        angles.append(temp_angle)
    angle = mean_angle(angles)

    # CLockwise
    # if average angle of ball is from 180 to 360 degrees then counter-clk otherwise clk from 0-180
    if angle < 180:
        clockwise = True

    x_avg = 0
    y_avg = 0
    for x,y in pegs:
        x_avg += x
        y_avg += y
    x_avg = x_avg/len(pegs)
    y_avg = y_avg/len(pegs)

    # COLOUR
    # need to choose 3 numbers from 0-255
    r = (int(x_avg)^2) % 256
    g = (int(y_avg)^2) % 256
    b = (int((x_avg+y_avg)/2)^2) % 256

    colour = (r, g, b)
        
    # depth
    # need number from 5 to 20
    
    depth = 5 + len(pegs) % 15

    # scale
    # need numnber from 1.05 to 2
    # also needs to be related to depth so large depth has small scale and vice versa
    scale = 1 + 1/(depth/4)

    state = int(math.sqrt(x_avg**2 + y_avg**2)) % 8
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

    # change needs to be from 4-60
    change = 10 + int(x_avg**2 * y_avg**2) % 50
    
    fractals.main(regular, shape, angle, clockwise, depth, scale, colour, state, change)

    # Create the call to chat gpt to create a fractal
    chatgpt = open("to_chat.txt", 'a')

    if regular:
        reg = "using equillateral polygons with sides greater than 2 "
    else:
        reg = "using irregular shapes "
    if clockwise:
        clk = "rotating " + str(angle) + " clockwise "
    else:
        clk = "rotating " + str(angle) + " anticlockwise "
    
    d = " with depth " + str(depth)
    s = " with scale " + str(scale)
    cl = " using the colour " + str(colour) + " and changing the colour values by " + str(change)
    question = "Create a fractal in pygame " + reg + clk + d + s + cl + '\n'
    chatgpt.write(question)
    chatgpt.close()
    chat = False
    if chat:
        chatgpt_query.main(question)


