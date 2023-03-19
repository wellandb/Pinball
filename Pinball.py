from settings import *
from ball import *
from paddle import *
from peg import *
from collisions import *
import math
from boardGeneration import *
import log_to_fractal

def redrawGameWindow():
    win.fill(BLACK)
    for i in pegs:
       i.draw()
    for i in balls:
        i.draw()
        i.move()
    pygame.display.update()

# Initialization

for i in pegs:
    i.draw()
    pygame.display.update()

def mouseClick():
    ballX = mouse[0]
    ballY = mouse[1]
    return ballX, ballY

# save parameters to file
f = open("parameter_log.txt", "a")

# First loop to get starting parameters
run = True
while run:

    clock.tick(30)

    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # if mous click then set ball start position
        elif event.type == pygame.MOUSEBUTTONDOWN:
            ballX, ballY = mouseClick()
            f.write(str(ballX) +  " "  + str(ballY))
            run = False
    
    pygame.display.update()


def mouseClick2():
    weight = 5/math.sqrt((mouse[0]-ballX)**2 + (mouse[1] - ballY)**2)
    ballXVel = (mouse[0]-ballX)*weight
    ballYVel = (mouse[1] - ballY)*weight
    return ballXVel, ballYVel
    
# second loop to get the ball velocity
while not run:
    clock.tick(30)

    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            ballXVel, ballYVel = mouseClick2()
            f.write(" " + str(ballXVel) + " " + str(ballYVel) + "\n")
            run = True

    win.fill(BLACK)
    for i in pegs:
        i.draw()
    pygame.draw.circle(win, WHITE, [ballX, ballY], 5)
    pygame.draw.line(win, WHITE, [ballX, ballY], mouse)
    
    pygame.display.update()

# close the file
f.close()

# create ball
balls = pygame.sprite.Group()
balls.add(ball(ballX, ballY, ballXVel, ballYVel)) # x, y, xVel, yVel: ALL NEED TO BE CHOSEN EACH RUN AT START

log = open("route_tracker.txt", "a")
#mainloop
run = True
while run:

    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    # COLLISION CHECK
    for i in balls:      
        log.write(ballPegCollision(i, pegs))
    if ballWallCollision(balls):
        run = False

    redrawGameWindow()


log.write("\n")
log.close()
log_to_fractal.main()
pygame.quit()