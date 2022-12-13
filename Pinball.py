from settings import *
from ball import *
from paddle import *
from peg import *
from collisions import *
import math
from boardGeneration import *

def redrawGameWindow():
    win.fill(black)
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

run = True
while run:

    clock.tick(30)

    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            ballX, ballY = mouseClick()
            run = False
    
    pygame.display.update()


def mouseClick2():
    weight = 5/math.sqrt((mouse[0]-ballX)**2 + (mouse[1] - ballY)**2)
    ballXVel = (mouse[0]-ballX)*weight
    ballYVel = (mouse[1] - ballY)*weight
    return ballXVel, ballYVel
    

while not run:
    clock.tick(30)

    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            ballXVel, ballYVel = mouseClick2()
            run = True

    win.fill(black)
    for i in pegs:
        i.draw()
    pygame.draw.circle(win, white, [ballX, ballY], 5)
    pygame.draw.line(win, white, [ballX, ballY], mouse)
    
    pygame.display.update()

balls = pygame.sprite.Group()
balls.add(ball(ballX, ballY, ballXVel, ballYVel)) # x, y, xVel, yVel: ALL NEED TO BE CHOSEN EACH RUN AT START

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
        ballPegCollision(i, pegs)
    ballWallCollision(balls)

    redrawGameWindow()

pygame.quit()