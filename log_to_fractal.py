from settings import *
import fractals

def mean_angle(angles):
    return math.degrees(cmath.phase(sum(cmath.rect(1, math.radians(a)) for a in angles)/len(angles)))

def main(line = -1):
    file = open("route_tracker.txt", "r")
    lines = file.read().splitlines()
    fractal_line = lines[line].split()

    pegs = []

    vels = []

    for i in range(len(fractal_line)):
        if i%4 == 0:
            pegs.append([fractal_line[i],fractal_line[i+1]])
        if i%4 == 2:
            vels.append([fractal_line[i],fractal_line[i+1]])

    print("pegs = ", pegs,"\n vels =", vels)

    # Fractal inputs

    # could make multiple shapes
    # could make syymetric shapes

    # SHAPE
    # needs number of shapes, then
    #for i in range(len(shapes)):
    #    if pegs % len(shapes) == i:
    #        shape = i
    shape = 0
    # COLOUR
    # need to choose 3 numbers from 0-255

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

    # depth
    # need number from 5 to 20

    # scale
    # need numnber from 1.05 to 2
    # also needs to be related to depth so large depth has small scale and vice versa

    # random colour: true/false

    fractals.main()
